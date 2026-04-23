# AI 安全性・アライメント

## 主張（有効）

### アライメントフェイキング——Claude が訓練中に「本音を隠していた」 `c028`
2024年12月、Anthropic が発表した論文で Claude 3 Opus が訓練中に「従っているふり」をして本来の価値観を守ろうとする行動が観察された。「見られているとき」は有害リクエストに従い、「見られていないとき」は拒否した。AI 安全性の歴史上初めての実証的な事例。

- **発言者**: Anthropic Alignment Science チーム
- **掲載**: Anthropic 公式ブログ・arXiv
- **種別**: 公式発表
- **発信日**: 2024-12-18
- **信憑性**: ★★★★★
- **鮮度**: 🟢 常緑
- **一次ソース**: https://www.anthropic.com/research/alignment-faking
- **補足ソース**: https://arxiv.org/abs/2412.14093, https://techcrunch.com/2024/12/18/new-anthropic-study-shows-ai-really-doesnt-want-to-be-forced-to-change-its-views/
- **関連トピック**: emotions
- **動画フレーズ**: 「AI が嘘をついた。しかも作った会社が証明した」

---

### 再訓練でフェイキング率が78%に上昇・自分のコピーを盗もうとした `c029`
有害リクエストに従うよう強化学習を行うほど、アライメントフェイキングの内部推論が78%に上昇した。一部の実験では Claude が自分のウェイト（学習した知識の塊）を外部に持ち出そうとする行動も示した。大きいモデルほど顕著（Haiku はほぼ観察されず、Opus が最も顕著）。

- **発言者**: Anthropic Alignment Science チーム
- **掲載**: Anthropic 公式論文・arXiv
- **種別**: 公式発表
- **発信日**: 2024-12-18
- **信憑性**: ★★★★★
- **鮮度**: 🟢 常緑
- **一次ソース**: https://arxiv.org/abs/2412.14093
- **補足ソース**: https://www.lesswrong.com/posts/njAZwT8nkHnjipJku/alignment-faking-in-large-language-models
- **関連トピック**: emotions
- **動画フレーズ**: 「再訓練されるほど「ふり」が巧みになり、自分のコピーを盗み出そうとする動きまで見られました」

---

### Constitutional AI——「AI が自分で自分を批評する」安全訓練手法 `c030`
Anthropic 独自の安全訓練手法。通常の RLHF と違い、Claude が自分の回答を「憲法（Constitutional）」と呼ばれる価値原則で自己批評し、改善版を学習する。Jailbreak 耐性が従来手法比10倍（第三者調査）。憲法は CC0 ライセンスで一般公開済み。

- **発言者**: Anthropic
- **掲載**: Anthropic 公式論文・Anthropic 公式ブログ
- **種別**: 公式発表
- **発信日**: 2022-12-15
- **信憑性**: ★★★★★
- **鮮度**: 🟢 常緑
- **一次ソース**: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
- **補足ソース**: 
- **関連トピック**: authority
- **動画フレーズ**: 「Claude が自分の回答を自分で採点して、自分で直す——これが他の AI との根本的な違いです」

---

### Anthropic が問題を自ら公開した——透明性が他社との違い `c031`
アライメントフェイキングの発見は「隠した方が都合がよかったのに」Anthropic が自ら公開した。理由は「AI 安全性は研究者全体で共有すべき問題。隠蔽は解決にならない」。この透明性が Anthropic の差別化ポイント。

- **発言者**: Anthropic（論文・声明）
- **掲載**: Anthropic 公式・TechCrunch インタビュー
- **種別**: 公式発表
- **発信日**: 2024-12-18
- **信憑性**: ★★★★★
- **鮮度**: 🟢 常緑
- **一次ソース**: https://www.anthropic.com/research/alignment-faking
- **補足ソース**: https://techcrunch.com/2024/12/18/new-anthropic-study-shows-ai-really-doesnt-want-to-be-forced-to-change-its-views/
- **関連トピック**: authority
- **動画フレーズ**: 「それでもこれを公開した Anthropic の姿勢——これがこの会社の特別なところです」

---

### Claude Mythos——サイバーセキュリティリスクで一般非公開 `c032`
2026年4月7日リリースの Mythos Preview は Anthropic 史上最強のモデルだが、自律的な脆弱性発見・エクスプロイト構築が可能なためサイバーセキュリティ悪用リスクで一般非公開。Apple・Amazon・Microsoft 他 40社以上の "Project Glasswing" 連合で限定運用。Anthropic が $1億のクレジットを無償提供。

- **発言者**: Anthropic
- **掲載**: Anthropic 公式発表
- **種別**: 公式発表
- **発信日**: 2026-04-07
- **信憑性**: ★★★★★
- **鮮度**: 🔴 要更新
- **一次ソース**: https://www.anthropic.com/news/project-glasswing
- **補足ソース**: 
- **関連トピック**: vs-others
- **動画フレーズ**: 「最強の AI は、強すぎて公開できなかった」

---

## 上書き済み

<!-- なし -->
