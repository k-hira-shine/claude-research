#!/usr/bin/env python3
"""
sync.py — topics/*.md を解析して claims/index.jsonl を再生成する。

使い方:
  python scripts/sync.py           # 通常モード（警告のみ、exit 0）
  python scripts/sync.py --strict  # strict モード（エラーがあれば exit 1）
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

TOPICS_DIR = Path(__file__).parent.parent / "topics"
CLAIMS_DIR = Path(__file__).parent.parent / "claims"
INDEX_FILE = CLAIMS_DIR / "index.jsonl"

REQUIRED_FIELDS = ["発言者", "掲載", "種別", "発信日", "信憑性", "鮮度", "一次ソース"]
VALID_CLAIM_TYPES = {"公式発表", "本人発言", "記者要約", "コミュニティ報告"}
VALID_FRESHNESS = {"🟢", "🟡", "🔴"}
DATE_PATTERN = re.compile(r"^\d{4}-(\d{2}|\?\?)- (\d{2}|\?\?)$|^unknown$|^\d{4}-\d{2}-\d{2}$|^\d{4}-\d{2}-\?\?$|^\d{4}-\?\?-\?\?$")
SUPERSEDED_PATTERN = re.compile(r"<!--\s*superseded_by:\s*(c\d+)\s*-->")


def normalize_title(title: str) -> str:
    """タイトルを小文字化・記号除去・空白正規化して dedupe_key 用に正規化する。"""
    title = unicodedata.normalize("NFKC", title).lower()
    title = re.sub(r"[^\w\s]", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def parse_field(line: str) -> tuple[str, str]:
    """「- **フィールド名**: 値」形式の行を (field, value) に分解する。"""
    m = re.match(r"[-*]\s*\*{0,2}([^*:：]+)\*{0,2}\s*[:：]\s*(.*)", line)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", ""


def stars_to_int(value: str) -> int | None:
    count = value.count("★")
    if 1 <= count <= 5:
        return count
    return None


def freshness_to_key(value: str) -> str | None:
    if "🟢" in value:
        return "green"
    if "🟡" in value:
        return "yellow"
    if "🔴" in value:
        return "red"
    return None


def load_existing_ids() -> set[int]:
    """index.jsonl と topics/*.md の両方から既存 ID を収集する。"""
    ids: set[int] = set()

    if INDEX_FILE.exists():
        for line in INDEX_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                m = re.match(r"c(\d+)", obj.get("id", ""))
                if m:
                    ids.add(int(m.group(1)))
            except json.JSONDecodeError:
                pass

    for md in TOPICS_DIR.glob("*.md"):
        for line in md.read_text(encoding="utf-8").splitlines():
            m = re.search(r"`c(\d+)`", line)
            if m:
                ids.add(int(m.group(1)))

    return ids


def next_id(existing_ids: set[int]) -> str:
    n = max(existing_ids, default=0) + 1
    return f"c{n:03d}"


def parse_topic_file(path: Path) -> list[dict]:
    """topics/*.md を解析して claim の dict リストを返す。"""
    text = path.read_text(encoding="utf-8")
    topic = path.stem
    claims = []

    current_section = "active"
    current_title = None
    current_id = None
    current_lines: list[str] = []
    current_superseded_by = None

    def flush(title, cid, lines, status, superseded_by):
        if title is None:
            return None
        fields: dict[str, str] = {}
        for l in lines:
            k, v = parse_field(l)
            if k:
                fields[k] = v
            m = SUPERSEDED_PATTERN.search(l)
            if m:
                superseded_by = m.group(1)
        return {
            "title": title,
            "id": cid,
            "status": status,
            "superseded_by": superseded_by,
            "fields": fields,
            "topic": topic,
        }

    for line in text.splitlines():
        if line.strip() == "## 主張（有効）":
            current_section = "active"
            continue
        if line.strip() == "## 上書き済み":
            current_section = "superseded"
            continue

        heading_match = re.match(r"^###\s+(.+?)(?:\s+`(c\d+)`)?$", line)
        if heading_match:
            result = flush(current_title, current_id, current_lines,
                           "active" if current_section == "active" else "superseded",
                           current_superseded_by)
            if result:
                claims.append(result)
            raw_title = heading_match.group(1)
            current_title = re.sub(r"~~(.+?)~~", r"\1", raw_title).strip()
            current_id = heading_match.group(2)
            current_lines = []
            current_superseded_by = None
            continue

        if current_title is not None:
            current_lines.append(line)

    result = flush(current_title, current_id, current_lines,
                   "active" if current_section == "active" else "superseded",
                   current_superseded_by)
    if result:
        claims.append(result)

    return claims


def validate(claim: dict) -> list[str]:
    errors = []
    f = claim["fields"]
    for req in REQUIRED_FIELDS:
        if req not in f or not f[req].strip():
            errors.append(f"必須フィールド欠落: {req}")

    if "種別" in f and f["種別"] not in VALID_CLAIM_TYPES:
        errors.append(f"種別が不正: {f['種別']}")
    if "発信日" in f and not DATE_PATTERN.match(f["発信日"]):
        errors.append(f"発信日フォーマット不正: {f['発信日']}")
    if "信憑性" in f and stars_to_int(f["信憑性"]) is None:
        errors.append(f"信憑性フォーマット不正: {f['信憑性']}")
    if "鮮度" in f and freshness_to_key(f["鮮度"]) is None:
        errors.append(f"鮮度フォーマット不正: {f['鮮度']}")
    if "一次ソース" in f and f["一次ソース"] and not f["一次ソース"].startswith("http"):
        errors.append(f"一次ソースが URL でない: {f['一次ソース']}")
    if "上書き先" in f and f["上書き先"] and not re.match(r"^c\d+$", f["上書き先"]):
        errors.append(f"上書き先フォーマット不正（cXXX 形式でない）: {f['上書き先']}")

    return errors


def build_jsonl_record(claim: dict, assigned_id: str) -> dict:
    f = claim["fields"]
    record = {
        "id": assigned_id,
        "topic": claim["topic"],
        "related_topics": [t.strip() for t in f.get("関連トピック", "").split(",") if t.strip()],
        "title": claim["title"],
        "speaker": f.get("発言者", ""),
        "publication": f.get("掲載", ""),
        "claim_type": f.get("種別", ""),
        "issued_at": f.get("発信日", ""),
        "credibility": stars_to_int(f.get("信憑性", "")) or 0,
        "freshness": freshness_to_key(f.get("鮮度", "")) or "",
        "status": claim["status"],
        "primary_source": f.get("一次ソース", ""),
        "supporting_sources": f.get("補足ソース", ""),
        "compare_models": f.get("比較対象", ""),
        "superseded_by": claim.get("superseded_by") or f.get("上書き先", ""),
        "video_phrase": f.get("動画フレーズ", "").strip("「」"),
        "dedupe_key": f"{f.get('発言者', '')}::{normalize_title(claim['title'])}::{f.get('発信日', '')}",
    }
    return record


def write_id_back(path: Path, title_without_id: str, assigned_id: str) -> None:
    """MD ファイルの ### タイトル 行に ID を書き戻す（既存 ID がない場合のみ）。"""
    text = path.read_text(encoding="utf-8")
    escaped = re.escape(title_without_id)
    pattern = re.compile(rf"^(###\s+{escaped})\s*$", re.MULTILINE)
    new_text = pattern.sub(rf"\1 `{assigned_id}`", text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")


def main(strict: bool = False) -> int:
    CLAIMS_DIR.mkdir(parents=True, exist_ok=True)
    existing_ids = load_existing_ids()
    all_records = []
    error_count = 0

    for md_path in sorted(TOPICS_DIR.glob("*.md")):
        raw_claims = parse_topic_file(md_path)
        for claim in raw_claims:
            errors = validate(claim)
            if errors:
                for e in errors:
                    print(f"[WARNING] {md_path.name} / {claim['title']}: {e}", file=sys.stderr)
                error_count += 1
                if strict:
                    continue  # strict モードではエラー claim をスキップして index に入れない

            if claim["id"] is None:
                cid = next_id(existing_ids)
                existing_ids.add(int(cid[1:]))
                claim["id"] = cid
                write_id_back(md_path, claim["title"], cid)
            else:
                n = int(claim["id"][1:])
                existing_ids.add(n)

            record = build_jsonl_record(claim, claim["id"])
            all_records.append(record)

    INDEX_FILE.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in all_records) + ("\n" if all_records else ""),
        encoding="utf-8",
    )

    print(f"[sync.py] {len(all_records)} claims を index.jsonl に書き込みました。", file=sys.stderr)
    if error_count:
        print(f"[sync.py] バリデーションエラー: {error_count} 件", file=sys.stderr)
        if strict:
            return 1
    return 0


if __name__ == "__main__":
    strict_mode = "--strict" in sys.argv
    sys.exit(main(strict=strict_mode))
