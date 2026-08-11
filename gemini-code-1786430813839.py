from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
    background-color: #0b0f19;
    @bottom-right {
      content: counter(page) " / " counter(pages);
      font-family: 'Space Grotesk', 'Noto Sans JP', sans-serif;
      font-size: 8.5pt;
      color: #64748b;
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Outfit', 'Hiragino Sans', 'Meiryo', sans-serif;
    color: #e2e8f0;
    line-height: 1.5;
    margin: 0;
    padding: 0;
    font-size: 9.5pt;
    background-color: #0b0f19;
  }

  /* Header Section */
  .header-container {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 18px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  }

  .header-badge {
    display: inline-block;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    color: #ffffff;
    font-size: 8pt;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
  }

  .header-title {
    font-size: 18pt;
    font-weight: 900;
    margin: 0 0 6px 0;
    color: #ffffff;
    letter-spacing: -0.01em;
  }

  .header-subtitle {
    font-size: 9.5pt;
    color: #94a3b8;
    margin: 0;
    line-height: 1.4;
  }

  /* Concept Box */
  .intro-box {
    background: rgba(15, 23, 42, 0.8);
    border-left: 4px solid #38bdf8;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding: 12px 16px;
    border-radius: 0 10px 10px 0;
    margin-bottom: 18px;
  }

  .intro-box p {
    margin: 0;
    color: #cbd5e1;
    font-size: 9.5pt;
  }

  /* Section Headings */
  h2 {
    color: #f8fafc;
    font-size: 12pt;
    font-weight: 800;
    border-bottom: 1px solid #1e293b;
    padding-bottom: 5px;
    margin-top: 18px;
    margin-bottom: 10px;
    page-break-after: avoid;
    display: flex;
    align-items: center;
  }

  h2::before {
    content: "■";
    color: #818cf8;
    font-size: 10pt;
    margin-right: 8px;
  }

  /* Feature Grid Table */
  .feature-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 8px;
    margin-left: -8px;
    margin-right: -8px;
    margin-bottom: 8px;
  }

  .feature-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 12px;
    vertical-align: top;
    width: 50%;
  }

  .feature-title {
    font-weight: 800;
    font-size: 10pt;
    color: #38bdf8;
    margin-bottom: 4px;
  }

  .feature-desc {
    font-size: 8.5pt;
    color: #94a3b8;
    margin: 0;
    line-height: 1.4;
  }

  /* Shortcut Table */
  .key-table {
    width: 100%;
    border-collapse: collapse;
    background: #0f172a;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #1e293b;
    margin-bottom: 15px;
  }

  .key-table th, .key-table td {
    padding: 7px 12px;
    text-align: left;
    border-bottom: 1px solid #1e293b;
    font-size: 8.5pt;
  }

  .key-table th {
    background-color: #1e293b;
    color: #38bdf8;
    font-weight: 700;
  }

  .kbd {
    display: inline-block;
    background-color: #334155;
    color: #f8fafc;
    border: 1px solid #475569;
    border-radius: 4px;
    padding: 1px 6px;
    font-family: monospace;
    font-weight: bold;
    font-size: 8pt;
  }

  /* Modes Section */
  .mode-box {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 10px;
    page-break-inside: avoid;
  }

  .mode-header {
    font-weight: 800;
    font-size: 10pt;
    color: #a855f7;
    margin-bottom: 4px;
  }

  .mode-desc {
    font-size: 8.5pt;
    color: #cbd5e1;
    margin: 0 0 6px 0;
  }

  .mode-tips {
    font-size: 8pt;
    color: #34d399;
    margin: 0;
  }

  /* Strategy Box */
  .strategy-box {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(6, 182, 212, 0.1) 100%);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 10px;
    padding: 12px 16px;
    margin-top: 12px;
    page-break-inside: avoid;
  }

  .strategy-title {
    color: #34d399;
    font-weight: 800;
    font-size: 10pt;
    margin-bottom: 6px;
  }

  .strategy-box ul {
    margin: 0;
    padding-left: 16px;
    color: #cbd5e1;
    font-size: 8.5pt;
  }

  .strategy-box li {
    margin-bottom: 4px;
  }

</style>
</head>
<body>

  <div class="header-container">
    <span class="header-badge">Leap Vocab Master Pro v2.5</span>
    <h1 class="header-title">Leap Vocab Master Pro 活用・学習ガイド</h1>
    <p class="header-subtitle">アクティブリコールと分散学習を極める、次世代型英単語フラッシュカードツールの完全攻略マニュアル</p>
  </div>

  <div class="intro-box">
    <p><strong>「Leap Vocab Master Pro」</strong>は、最新のWebテクノロジーを活用したハイテク英単語カードアプリです。3Dカードフリップ、音声合成（TTS）、4択テスト、自動分析などの機能を駆使し、英単語の「思い出す力（アクティブリコール）」と「定着率」を劇的に向上させます。</p>
  </div>

  <h2>アプリの主要機能と特徴</h2>
  <table class="feature-table">
    <tr>
      <td class="feature-card">
        <div class="feature-title">🎴 3Dインタラクティブ・カード</div>
        <div class="feature-desc">表裏を瞬時に反転。日→英モードでは頭文字ヒント（例：A _ _ _ _）が自動生成され、スペル想起をサポート。</div>
      </td>
      <td class="feature-card">
        <div class="feature-title">🔊 米国英語リアル音声 (TTS)</div>
        <div class="feature-desc">ワンクリックまたはショートカットキーでネイティブ発音を再生。再生速度（0.8x〜1.2x）の調整にも対応。</div>
      </td>
    </tr>
    <tr>
      <td class="feature-card">
        <div class="feature-title">📊 習得度＆要復習フィルタ</div>
        <div class="feature-desc">「要復習（スター）」と「習得済み」を個別に管理。未修得の単語のみを抽出して効率的に演習可能。</div>
      </td>
      <td class="feature-card">
        <div class="feature-title">📂 Custom Data (Excel/JSON)</div>
        <div class="feature-desc">外部のExcel (.xlsx) や JSON ファイルをドラッグ＆ドロップするだけで、自作単語帳を瞬時に読み込み可能。</div>
      </td>
    </tr>
  </table>

  <h2>効率を高めるキーボードショートカット一覧</h2>
  <table class="key-table">
    <thead>
      <tr>
        <th style="width: 25%;">キー操作</th>
        <th style="width: 30%;">対象画面</th>
        <th>機能・アクション</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="kbd">Space</span></td>
        <td>カード学習</td>
        <td>カードを裏返して「意味 / 単語」を表示（音効付き）</td>
      </tr>
      <tr>
        <td><span class="kbd">←</span> / <span class="kbd">→</span></td>
        <td>カード学習</td>
        <td>前後の単語カードへ移動</td>
      </tr>
      <tr>
        <td><span class="kbd">S</span></td>
        <td>全画面共通</td>
        <td>現在の英単語のネイティブ発音を再生 (Speak)</td>
      </tr>
      <tr>
        <td><span class="kbd">B</span></td>
        <td>カード学習 / 一覧</td>
        <td>「要復習リスト（スター）」への追加・解除 (Bookmark)</td>
      </tr>
      <tr>
        <td><span class="kbd">M</span></td>
        <td>カード学習</td>
        <td>「習得済み（Mastered）」ステータスの切り替え</td>
      </tr>
    </tbody>
  </table>

  <h2>4つの学習モードと活用法</h2>

  <div class="mode-box">
    <div class="mode-header">1. カード学習（メインモード）</div>
    <div class="mode-desc">反復暗記の核となるモード。「英→日」で意味を確認するだけでなく、「日→英」モード＋頭文字ヒントを使ってアウトプット力を鍛えます。</div>
    <div class="mode-tips">💡 コツ: 「自動再生 ON」にして速度を調整すれば、ハンズフリーの音読暗記ツールとして活用できます。</div>
  </div>

  <div class="mode-box">
    <div class="mode-header">2. 4択テスト (Quiz Challenge)</div>
    <div class="mode-desc">選択肢の中から正しい意味・単語を選ぶ実践モード。連続正解数（STREAK）が記録され、ゲーム感覚で定着度を測定できます。</div>
    <div class="mode-tips">💡 コツ: 正解・不正解時に独自のSFX（効果音）が鳴るため、テンポよくテンションを維持しながら解けます。</div>
  </div>

  <div class="mode-box">
    <div class="mode-header">3. 単語一覧 ＆ 検索</div>
    <div class="mode-desc">指定範囲内の全単語をリスト表示。リアルタイム検索で気になる単語を即座に探せます。</div>
  </div>

  <div class="mode-box">
    <div class="mode-header">4. 進捗分析 (Analytics)</div>
    <div class="mode-desc">「習得率（％）」や「要復習数」をグラフと数値で可視化。達成感を感じながら学習を継続できます。</div>
  </div>

  <div class="strategy-box">
    <div class="strategy-title">🚀 記憶定着率を爆発的に高める「3ステップ攻略法」</div>
    <ul>
      <li><strong>Step 1【全範囲を英→日で一巡】:</strong> 範囲を指定（例: 1〜100）し、カード学習でサクサク確認。あやふやな単語は <span class="kbd">B</span> キーで要復習へ。</li>
      <li><strong>Step 2【日→英 ＋ 4択テスト】:</strong> 「出題方向切り替え」で日→英にし、頭文字ヒントから単語を思い出す訓練を実施。その後4択テストで総仕上げ。</li>
      <li><strong>Step 3【未修得・要復習フィルタで絞り込み】:</strong> 覚えた単語は <span class="kbd">M</span> キーで「習得済み」へ。最後に「未修得のみ」フィルタをオンにして、苦手な単語だけを全滅させます。</li>
    </ul>
  </div>

</body>
</html>
"""

# Convert to PDF
input_html_path = 'leap_master_guide.html'
output_pdf_path = 'leap_vocab_master_guide.pdf'

with open(input_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

HTML(filename=input_html_path).write_pdf(output_pdf_path)
print(f"PDF generated: {output_pdf_path}")