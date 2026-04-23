#!/usr/bin/env python3
"""
promote.py — updates/*.md の pending claim を topics/ に昇格させる対話スクリプト。

使い方:
  python scripts/promote.py
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

UPDATES_DIR = Path(__file__).parent.parent / "updates"
TOPICS_DIR = Path(__file__).parent.parent / "topics"
SYNC_SCRIPT = Path(__file__).parent / "sync.py"

VALID_TOPICS = {"drama", "emotions", "safety", "vs-others", "practical", "authority", "future"}
STATUS_PENDING = re.compile(r"<!--\s*status:\s*pending\s*-->")
STATUS_LINE = re.compile(r"<!--\s*status:\s*\S+.*?-->")


def split_claims(text: str) -> list[str]:
    """
    `### 見出し` から次の `### 見出し` または `---` までを1 claim として分割する。
    claim 先頭の `<!-- status: ... -->` タグを含む。
    """
    # `---` または次の `###` の手前で切る
    parts = re.split(r"(?=^###\s)", text, flags=re.MULTILINE)
    claims = []
    for part in parts:
        part = part.strip()
        if not part or part.startswith("#") and not part.startswith("###"):
            continue
        # `---` の手前で切る（末尾の区切り線を除去）
        part = re.sub(r"\n---\s*$", "", part).strip()
        if part:
            claims.append(part)
    return claims


def get_status(claim: str) -> str:
    """claim 文字列から status を返す。"""
    m = STATUS_LINE.search(claim)
    if not m:
        return "pending"
    content = m.group(0)
    if "promoted" in content:
        return "promoted"
    if "rejected" in content:
        return "rejected"
    return "pending"


def get_title(claim: str) -> str:
    m = re.search(r"^###\s+(.+)", claim, re.MULTILINE)
    return m.group(1).strip() if m else "(タイトルなし)"


def validate_claim(claim: str) -> list[str]:
    """sync.py と同じ必須フィールドチェックを簡易実行する。"""
    required = ["発言者", "掲載", "種別", "発信日", "信憑性", "鮮度", "一次ソース"]
    errors = []
    for field in required:
        pattern = re.compile(rf"\*\*{field}\*\*\s*[:：]\s*(\S)")
        if not pattern.search(claim):
            errors.append(f"必須フィールド欠落または空: {field}")
    return errors


def update_status_in_file(path: Path, old_claim: str, new_status: str, reason: str = "") -> None:
    """updates/*.md 内の該当 claim の status タグを書き換える。"""
    text = path.read_text(encoding="utf-8")
    reason_str = f' reason="{reason}"' if reason else ""
    new_tag = f"<!-- status: {new_status}{reason_str} -->"

    if STATUS_LINE.search(old_claim):
        new_claim = STATUS_LINE.sub(new_tag, old_claim, count=1)
    else:
        # status タグがない場合は ### 行の前に挿入
        new_claim = re.sub(r"(^###\s)", f"{new_tag}\n\\1", old_claim, count=1)

    text = text.replace(old_claim, new_claim, 1)
    path.write_text(text, encoding="utf-8")


def append_to_topic(topic: str, claim_body: str) -> None:
    """topics/[topic].md の ## 主張（有効） セクション末尾に claim を追記する。"""
    topic_path = TOPICS_DIR / f"{topic}.md"
    text = topic_path.read_text(encoding="utf-8")

    # status タグを除去してから追記
    body = STATUS_LINE.sub("", claim_body).strip()

    active_marker = "## 主張（有効）"
    superseded_marker = "## 上書き済み"

    if superseded_marker in text:
        insert_pos = text.index(superseded_marker)
        text = text[:insert_pos].rstrip() + "\n\n" + body + "\n\n---\n\n" + text[insert_pos:]
    elif active_marker in text:
        text = text.rstrip() + "\n\n" + body + "\n\n---\n"
    else:
        text = text.rstrip() + "\n\n## 主張（有効）\n\n" + body + "\n\n---\n"

    topic_path.write_text(text, encoding="utf-8")


def run_sync_strict() -> bool:
    """sync.py を --strict モードで実行。成功なら True を返す。"""
    result = subprocess.run(
        [sys.executable, str(SYNC_SCRIPT), "--strict"],
        capture_output=True,
        text=True,
    )
    sys.stderr.write(result.stderr)
    return result.returncode == 0


def main() -> None:
    pending: list[tuple[Path, str]] = []

    for md_path in sorted(UPDATES_DIR.glob("*.md")):
        if md_path.name == "unknown-date.md":
            continue
        text = md_path.read_text(encoding="utf-8")
        for claim in split_claims(text):
            if get_status(claim) == "pending":
                pending.append((md_path, claim))

    # unknown-date.md も対象に（発信日=unknown は昇格不可だが表示はする）
    unknown_path = UPDATES_DIR / "unknown-date.md"
    if unknown_path.exists():
        for claim in split_claims(unknown_path.read_text(encoding="utf-8")):
            if get_status(claim) == "pending":
                pending.append((unknown_path, claim))

    if not pending:
        print("pending の claim はありません。")
        return

    print(f"\n{len(pending)} 件の pending claim があります。\n")

    for i, (src_path, claim) in enumerate(pending, 1):
        title = get_title(claim)
        is_comparison = "⚡" in claim
        is_unknown_date = src_path.name == "unknown-date.md"

        print(f"{'─'*60}")
        print(f"[{i}/{len(pending)}] {title}")
        print(f"  ファイル: {src_path.name}")
        if is_comparison:
            print("  ⚡ 比較フラグあり")
        if is_unknown_date:
            print("  ⚠️  発信日不明 → 昇格不可（rejected のみ選択可）")
        print()
        print(claim[:500] + ("..." if len(claim) > 500 else ""))
        print()

        while True:
            if is_unknown_date:
                choice = input("操作: [r]eject / [s]kip > ").strip().lower()
            else:
                choice = input("操作: [p]romote / [r]eject / [s]kip > ").strip().lower()

            if choice == "s":
                print("  → スキップ（pending のまま）\n")
                break

            if choice == "r":
                reason = input("  却下理由を入力（省略可）: ").strip()
                update_status_in_file(src_path, claim, "rejected", reason)
                print("  → rejected に更新しました\n")
                break

            if choice == "p" and not is_unknown_date:
                errors = validate_claim(claim)
                if errors:
                    print("  ⚠️  バリデーションエラーがあります:")
                    for e in errors:
                        print(f"     - {e}")
                    print("  updates/ のファイルを手動修正してから再実行してください。")
                    break

                print(f"  移動先トピック: {', '.join(sorted(VALID_TOPICS))}")
                topic = input("  トピック名を入力 > ").strip()
                if topic not in VALID_TOPICS:
                    print(f"  ⚠️  無効なトピック名です: {topic}")
                    continue

                # topics/ への追記前にバックアップ
                topic_path = TOPICS_DIR / f"{topic}.md"
                backup_path = topic_path.with_suffix(".md.bak")
                shutil.copy2(topic_path, backup_path)

                try:
                    append_to_topic(topic, claim)
                    ok = run_sync_strict()
                    if not ok:
                        print("  ⚠️  sync.py がエラーを返しました。topics/ への追記を取り消します。")
                        shutil.move(str(backup_path), str(topic_path))
                        break
                    backup_path.unlink(missing_ok=True)
                    update_status_in_file(src_path, claim, "promoted")
                    print(f"  → {topic}.md に追記し、promoted に更新しました\n")
                except Exception as e:
                    print(f"  ⚠️  エラー発生: {e}。topics/ への追記を取り消します。")
                    shutil.move(str(backup_path), str(topic_path))
                break

            print("  無効な入力です。")


if __name__ == "__main__":
    main()
