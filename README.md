# Claude リサーチフォルダ

Anthropic / Claude に関する情報を YouTube 動画作成のために体系的に蓄積するフォルダ。

最終更新: 2026-04-23（第4回収集完了・5テーマ追加）

---

## フォルダ構成

```
claude-research/
├── README.md                  ← このファイル（索引）
│
├── company/                   ← 会社・創業者・資金調達
│   ├── anthropic-overview.md
│   ├── dario-personal-story.md
│   ├── japan-market.md
│   ├── enterprise-cases.md
│   └── amazon-investment.md   ← NEW: Amazon $130億超投資の深掘り
│
├── models/                    ← モデルの全履歴・スペック
│   ├── model-history.md
│   ├── coding-dominance.md
│   ├── computer-use.md
│   └── claude-projects.md     ← NEW: Projects機能・実用ガイド
│
├── episodes/                  ← 逸話・エピソード（信憑性評価付き）
│   ├── episodes-credibility.md
│   ├── user-voices.md
│   ├── interpretability-emotion.md  ← NEW: Claude の感情・解釈可能性研究
│   └── alignment-faking.md          ← NEW: アライメントフェイキング研究
│
├── news/                      ← 最新ニュース（時系列）
│   ├── news-2026.md
│   └── agi-roadmap.md
│
└── video-ideas/               ← 動画企画メモ
    ├── ideas.md
    ├── ai-practical-use.md
    └── job-before-after.md    ← NEW: 職種別ビフォーアフター・時間削減数字
```

---

## クイックリファレンス

### 動画に使える最強ネタ TOP8（更新版）

| # | ネタ | 信憑性 | 衝撃度 | ファイル |
|---|------|--------|--------|---------|
| 1 | Claude がブラックメールした（96%のケースで） | ★★★★☆ | 超高 | episodes/episodes-credibility.md |
| 2 | Mythos「強すぎて公開できない AI」 | ★★★★☆ | 超高 | episodes/episodes-credibility.md |
| 3 | アライメントフェイキング：訓練中に「本音を隠した」 | ★★★★★ | 超高 | episodes/alignment-faking.md |
| 4 | Claude に 171種類の感情ベクトルが発見された | ★★★★★ | 高 | episodes/interpretability-emotion.md |
| 5 | AI が癌を治し寿命150年にするというビジョン | ★★★★★ | 高 | company/anthropic-overview.md |
| 6 | Amazon が2兆円以上を注ぎ込む本当の理由 | ★★★★★ | 高 | company/amazon-investment.md |
| 7 | Dario vs Altman「straight up lies」メモリーク | ★★★★☆ | 高 | episodes/episodes-credibility.md |
| 8 | OpenAI を離れた本当の理由（精神的虐待の告白） | ★★★★☆ | 高 | episodes/episodes-credibility.md |

---

## 収集ステータス

| カテゴリ | ステータス | 収集日 | ファイル |
|---------|-----------|--------|---------|
| 会社概要・創業史 | ✅ 完了 | 2026-04-23 | company/anthropic-overview.md |
| モデル全履歴（Claude 1〜4.7） | ✅ 完了 | 2026-04-23 | models/model-history.md |
| 資金調達・ビジネス指標 | ✅ 完了 | 2026-04-23 | company/anthropic-overview.md |
| 逸話・エピソード（12本・信憑性評価付き） | ✅ 完了 | 2026-04-23 | episodes/episodes-credibility.md |
| 最新ニュース（2026年4月） | ✅ 完了 | 2026-04-23 | news/news-2026.md |
| 競合比較（基礎） | ✅ 完了 | 2026-04-23 | models/model-history.md |
| Dario の個人的原体験・人生ストーリー | ✅ 完了 | 2026-04-23 | company/dario-personal-story.md |
| 日本市場・日本語性能・導入事例 | ✅ 完了 | 2026-04-23 | company/japan-market.md |
| ユーザーの生の声（Reddit・SNS） | ✅ 完了 | 2026-04-23 | episodes/user-voices.md |
| コーディング覇権・ベンチマーク詳細 | ✅ 完了 | 2026-04-23 | models/coding-dominance.md |
| Computer Use の実態・仕組み | ✅ 完了 | 2026-04-23 | models/computer-use.md |
| 企業導入事例・深掘り（法務・医療・金融） | ✅ 完了 | 2026-04-23 | company/enterprise-cases.md |
| AGI ロードマップ・Claude 5 情報 | ✅ 完了 | 2026-04-23 | news/agi-roadmap.md |
| Claude の感情・解釈可能性研究（2026年4月最新） | ✅ 完了 | 2026-04-23 | episodes/interpretability-emotion.md |
| アライメントフェイキング研究（2024年12月） | ✅ 完了 | 2026-04-23 | episodes/alignment-faking.md |
| 職種別 AI ビフォーアフター・時間削減数字 | ✅ 完了 | 2026-04-23 | video-ideas/job-before-after.md |
| Claude Projects 機能・実用ガイド | ✅ 完了 | 2026-04-23 | models/claude-projects.md |
| Amazon $130億超投資の深掘り | ✅ 完了 | 2026-04-23 | company/amazon-investment.md |

---

## info-hub との関係

元データは `Projects/info-hub/normalized/` に保管されている（非破壊原則）。
このフォルダは**動画制作用に整理・加工した派生物**として運用する。

- `2026-04-23-web-anthropic-claude-knowledge.md` → company/ + models/ に反映済み
- `2026-04-23-web-anthropic-episodes-anecdotes.md` → episodes/ に反映済み
