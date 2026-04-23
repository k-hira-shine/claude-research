# 他社AI比較・Claude の立ち位置

> 🔴 比較情報は1ヶ月で古くなりうる。updates/ の ⚡ フラグ確認後、必ずここを更新すること。
> 最終更新: 2026-04-23（対象: Claude Sonnet 4.5〜Opus 4.7 / GPT-4o・GPT-5.4 / Gemini 1.5 Pro）

## 主張（有効）

### コーディング性能：Claude Opus 4.7 が GPT-5.4 を約10ポイント上回る（2026-04時点） `c033`
SWE-bench Verified（実際の GitHub バグ修正タスク）で Claude Opus 4.7 が 87.6%、GPT-5.4 が約 77%。Mythos Preview は 93.9% という歴史的スコアを記録（訓練データ汚染なし確認済み）。Claude Code は 1M トークンでコードベース全体を把握できる点も優位性。

- **発言者**: Anthropic・独立ベンチマーク機関
- **掲載**: Anthropic 公式・playcode.io・AI Weekly
- **種別**: 公式発表
- **発信日**: 2026-04-16
- **信憑性**: ★★★★☆
- **鮮度**: 🔴 要更新
- **一次ソース**: https://www.anthropic.com/news/claude-opus-4-7
- **補足ソース**: https://playcode.io/blog/chatgpt-vs-claude-vs-gemini-coding-2026, https://aiweekly.co/learning-ai/generative-ai/chatgpt-vs-claude-vs-gemini
- **比較対象**: Claude Opus 4.7 vs GPT-5.4（2026-04時点）
- **関連トピック**: practical
- **動画フレーズ**: 「コードを書かせたら、2026年は Claude の独り勝ちです」

---

### 長文ライティング・指示追従：Claude が評価トップ（2026-04時点） `c034`
長文コンテンツ・ブランドボイス維持・ニュアンス表現で複数比較メディアの評価トップ。「箇条書きは使わない」「必ず日本語で」など細かい制約を最後まで守る能力が ChatGPT より高いとされる。理由は Constitutional AI が「指示を守っているか？」を自己チェックするステップを含むため。

- **発言者**: 複数メディア・ユーザーコミュニティ
- **掲載**: AI Weekly・MindStudio・playcode.io
- **種別**: 記者要約
- **発信日**: 2026-04-??
- **信憑性**: ★★★★☆
- **鮮度**: 🔴 要更新
- **一次ソース**: https://aiweekly.co/learning-ai/generative-ai/chatgpt-vs-claude-vs-gemini
- **補足ソース**: https://www.mindstudio.ai/blog/chatgpt-vs-claude-vs-gemini-2026/
- **比較対象**: Claude Sonnet 4.5 vs GPT-4o vs Gemini 1.5 Pro（2026-04時点）
- **関連トピック**: practical
- **動画フレーズ**: 「「言われた通りに動く AI」——これが Claude の最大の強みです」

---

### 画像生成：Claude のみ不可（2026-04時点） `c035`
Claude 単体では画像を生成できない。ChatGPT は DALL-E 3 内蔵、Gemini は Imagen 内蔵。Anthropic が「テキストの品質と安全性」に集中投資してきた結果。外部ツール連携は可能。

- **発言者**: 各社公式 UI
- **掲載**: 各社公式
- **種別**: 公式発表
- **発信日**: 2026-04-??
- **信憑性**: ★★★★★
- **鮮度**: 🔴 要更新
- **一次ソース**: https://claude.ai
- **補足ソース**: 
- **比較対象**: Claude vs ChatGPT vs Gemini（2026-04時点）
- **関連トピック**: 
- **動画フレーズ**: 「Claude だけできないこと——それは画像生成です」

---

### コンテキストウィンドウ：Claude 1M・Gemini 1M超・ChatGPT 12.8万（2026-04時点） `c036`
Claude 4.6+ は 1M トークン（文庫本 約 100 冊分）。Gemini は 1M 超。ChatGPT（GPT-4o）は 12.8万トークンで最も短い。コードベース全体・長大な法律文書を一括処理できる点で Claude と Gemini が優位。

- **発言者**: 各社公式仕様
- **掲載**: 各社公式ドキュメント
- **種別**: 公式発表
- **発信日**: 2026-02-??
- **信憑性**: ★★★★★
- **鮮度**: 🔴 要更新
- **一次ソース**: https://www.anthropic.com/claude/opus
- **補足ソース**: 
- **比較対象**: Claude Opus 4.7 vs GPT-4o vs Gemini 1.5 Pro（2026-04時点）
- **関連トピック**: practical
- **動画フレーズ**: 「文庫本 100冊分を一度に読める AI——それが今の Claude です」

---

### 数学・純粋ロジック推論：ChatGPT o3 が推論特化設計で優位（2026-04時点） `c037`
ChatGPT o シリーズは「答える前にじっくり考える（Chain of Thought）」に特化した専門モデル。数学証明・科学推論では o3 が Claude を上回ることが多い。Claude は「速く・幅広く・高品質に」の汎用設計であり、得意な戦場が異なる。

- **発言者**: 複数比較メディア
- **掲載**: AI Weekly・playcode.io
- **種別**: 記者要約
- **発信日**: 2026-04-??
- **信憑性**: ★★★★☆
- **鮮度**: 🔴 要更新
- **一次ソース**: https://aiweekly.co/learning-ai/generative-ai/chatgpt-vs-claude-vs-gemini
- **補足ソース**: 
- **比較対象**: Claude Sonnet 4.5 vs GPT-o3（2026-04時点）
- **関連トピック**: 
- **動画フレーズ**: 「Claude は万能選手型、ChatGPT の o シリーズは数学・理系の専門家型」

---

### 無料プランとリアルタイム検索：Gemini が最も寛大（2026-04時点） `c038`
無料で使える量は Gemini が最も多い（Google 広告収益基盤）。Claude は制限が早く来る傾向。リアルタイム検索はデフォルトで Gemini（Google 検索直結）と ChatGPT が優位。Claude は設定が必要。

- **発言者**: 複数比較メディア
- **掲載**: AI Weekly・Medium・複数比較記事
- **種別**: 記者要約
- **発信日**: 2026-04-??
- **信憑性**: ★★★★☆
- **鮮度**: 🔴 要更新
- **一次ソース**: https://aiweekly.co/learning-ai/generative-ai/chatgpt-vs-claude-vs-gemini
- **補足ソース**: 
- **比較対象**: Claude vs ChatGPT vs Gemini（2026-04時点）
- **関連トピック**: 
- **動画フレーズ**: 「無料でとにかく使いたいなら Gemini、信頼性・安全性なら Claude」

---

## 上書き済み

<!-- なし -->
