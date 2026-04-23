# Claude リサーチ

台本執筆のためのネタ・主張（claim）を蓄積するリポジトリ。

## トピック一覧

| ファイル | 内容 |
|---------|------|
| [drama.md](topics/drama.md) | 創業ドラマ・人間ストーリー |
| [emotions.md](topics/emotions.md) | 感情・意識・解釈可能性研究 |
| [safety.md](topics/safety.md) | AI 安全性・アライメント |
| [vs-others.md](topics/vs-others.md) | 他社AI比較・Claude の立ち位置 🔴 毎月更新 |
| [practical.md](topics/practical.md) | 実用・Projects・職種別ビフォーアフター |
| [authority.md](topics/authority.md) | 権威性・投資・導入事例 |
| [future.md](topics/future.md) | AGI・未来予測・Claude の進化 |
| [updates/](updates/) | AI ニュース自動取り込み（未審査）|

## 索引

`claims/index.jsonl` — sync.py が自動生成。手動編集禁止。フィルタ・重複確認はここで。

```bash
# 例：freshness=red の claim を一覧表示
python3 -c "
import json
for line in open('claims/index.jsonl'):
    c = json.loads(line)
    if c['freshness'] == 'red':
        print(c['id'], c['title'])
"
```

## Claim フォーマット

各 claim に必須のフィールド：

```
発言者 / 掲載 / 種別（公式発表|本人発言|記者要約|コミュニティ報告）
発信日（YYYY-MM-DD）/ 信憑性（★1〜5）/ 鮮度（🟢常緑 / 🟡要確認 / 🔴要更新）
一次ソース（URL）/ 補足ソース / 関連トピック / 動画フレーズ
```

ID（`c001` など）は sync.py が自動採番する。新規追加時は ID なしで書いてよい。

## スクリプト

```bash
# topics/ を編集したあとに実行 → ID 採番 + index.jsonl 再生成
python scripts/sync.py

# updates/ の未審査 claim を topics/ に昇格させる対話 UI
python scripts/promote.py
```

## 鮮度の目安

| 記号 | 対象 | 確認頻度 |
|------|------|---------|
| 🟢 常緑 | 歴史的事実・逸話・設計思想 | 不要 |
| 🟡 要確認 | 機能仕様・市場動向 | 3ヶ月ごと |
| 🔴 要更新 | 比較・ランキング・料金・新モデル情報 | 毎月 |
