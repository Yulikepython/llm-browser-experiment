# llm-browser-experiment

このプロジェクトは、LLM（Large Language Model）とブラウザオートメーションの組み合わせを学習・試用するためのサンプルプロジェクトです。  
リポジトリ([browser-use](https://github.com/browser-use/browser-use))をもとに、**私的な実験目的で一部のコードや構成を改変**して利用しています。

> **※本リポジトリの内容は、「browser-use」のオリジナル機能を上回ることを保証するものではありません。  
> あくまで個人的にカスタマイズ・実験を行っているものです。**

---

## 何ができるか

1. **LLM × ブラウザ操作の自動化**  
   - このプロジェクトでは、OpenAI や Anthropic といった LLM API を用いて「ブラウザを自動操作するエージェント」を実行できます。  
   - 具体的には、あるサイトにアクセスして情報を取得したり、テキストを入力したり、検索操作を行うといった流れを自動化できます。

2. **プロンプトは `.py` ファイルで管理**  
   - `prompts/` ディレクトリにあるサンプルファイル（例: `sample_prompt1.py`）や、  
     個人用の `my_prompts/` ディレクトリに作成した `.py` ファイルに `task_prompt` 変数を定義します。  
   - 実行時に `python main.py <prompt_file_name>` とするだけで、その `task_prompt` を使ってエージェントが動作する仕組みです。

3. **実行結果は `outputs/` ディレクトリに日時付きファイル名で保存**  
   - エージェントの実行が終わると、指定したフォーマット（デフォルトでは `.md`）で結果ファイルが作成されます。  
   - 例: `20250205-153001-output.md` のように、タイムスタンプを含む名前で保存されるため、同じスクリプトを何度走らせても上書きされず別ファイルとして記録が残せます。  
   - コンソールにも出力されますが、後から見返す場合は `outputs/` にあるファイルをチェックしてください。

4. **個人用のプロンプトは `my_prompts/` に置く**  
   - ログイン情報や機密内容を含むプロンプトは、`my_prompts/` 直下にファイルを作り、バージョン管理 (`.gitignore`) から外して利用することが推奨です。  
   - サンプルは `prompts/` にあるので参考にしてみてください。

---

## 機能概要

- `ChatOpenAI`（OpenAI APIを用いたチャットモデル）と、自作(または外部ライブラリの) `Agent`（ブラウザ操作を行うエージェント）を利用しています。
- `.env` で管理されるAPIキーなどの環境変数を使い、LLMとやり取りを行います。
- **`main.py` を実行すると、指定された `.py` ファイル（例: `sample_prompt1.py`）に含まれる `task_prompt` 変数を読み込み、エージェントが動作して結果をコンソールに表示し、`outputs/` フォルダにファイルを保存します。**

---

## セットアップ方法

### 1. リポジトリのクローン

```bash
git clone https://github.com/Yulikepython/llm-browser-experiment.git
cd llm-browser-experiment
```

### 2. Python仮想環境の作成（推奨）

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

### 3. 必要パッケージのインストール

```bash
pip install -r requirements.txt
```

```bash
pip install langchain_openai browser_use
```

### 4. 環境変数ファイルの設定

`.env.sample` を参考に、プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の項目を設定します。

```
OPENAI_API_KEY=あなたのOpenAIのAPIキー
ANTHROPIC_API_KEY=あなたのAnthropicのAPIキー
```

必要に応じて環境変数を追加設定してください。

### 5. 実行

```bash
python main.py <prompt_file_name>
```

例:

```bash
python main.py sample_prompt1
```

実行すると、対応する `task_prompt` が読み込まれ、ブラウザを制御するエージェントが動作して結果がコンソールに出力されます。  
同時に、`outputs/` ディレクトリに `YYYYMMDD-HHMMSS-output.md` の形式でログが保存されます。

---

## サンプルプロンプトについて

- `prompts/` ディレクトリには、動作確認や機能テスト用の**サンプルプロンプト**を3つ配置しています。  
- **これらのサンプルプロンプトはあくまで参考例であり、内容の正確性や最終的な出力品質を保証するものではありません。**  
- 実行タイミングやWebサイトの変更などにより、同じプロンプトでも出力結果が変化する可能性があり、過去の出力例と同じ結果を得られるとは限りません。  
- 出力ファイルには実行日時が記録されますが、これはあくまでその時点での結果であり、常に最新・最適な情報を保証するものではありません。

---

## 注意事項・免責事項

1. **API利用料について**  
   - 本プロジェクトは OpenAI などの外部 API を利用し、**API の呼び出しコストが発生する場合があります**。  
   - 各 API プロバイダの料金体系に従うため、実行する際は **ご自身のアカウントでの課金** や **無料枠の範囲** に十分ご注意ください。  
   - 当方では、API使用料や利用過程で発生した費用について、一切の責任を負いかねます。

2. **結果の品質・正確性について**  
   - LLM を用いた出力は状況や入力次第で変動し、誤情報を含む可能性があります。  
   - サンプルコード・サンプルプロンプトで得られた結果は、常に正確・最新であることを保証しません。

3. **プロジェクト仕様・動作**  
   - 本プロジェクトは実験用であり、**完全な動作やバグのない状態を保証するものではありません**。  
   - 動作環境やバージョン差異により挙動が変わる可能性があります。

4. **責任の限定**  
   - 本プロジェクトを利用したことによって生じたいかなる損害や障害についても、**作者は一切の責任を負いません**。  
   - **すべて自己責任** でご利用ください。

5. **第三者サイトへのアクセス**  
   - プロンプトによりアクセスする外部サイトの利用規約やプライバシーポリシーを遵守してください。  
   - 自動化ツールやスクレイピングの規約が定められている場合には、そちらに反しないようご注意ください。

6. **プライベートプロンプトの管理**  
   - 個人的に使用する機密情報を含むプロンプト（ログイン情報など）は `my_prompts/` ディレクトリに置くなど、**バージョン管理から除外** してください。  
   - 誤って公開しないよう、セキュリティに十分配慮してください。

---

## ディレクトリ・ファイル構成

```
.
├── main.py
├── prompt_manager.py
├── result_handler.py
├── prompts/
│   ├── sample_prompt1.py
│   ├── sample_prompt2.py
│   └── sample_prompt3.py
├── my_prompts/  (個人用。gitignore推奨)
├── outputs/     (生成された出力ファイルが保存される)
├── LICENSE.md
└── README.md
```

> `my_prompts/` は個人用のプロンプトファイルを置く想定で `.gitignore` されています。

## 参考にしたもの・改変内容

- [browser-use](https://github.com/browser-use/browser-use) という「LLM + ブラウザ自動化」のオープンソースリポジトリを参考にしています。
- 個人的な実験のため、一部コードやタスクPromptの扱いを変更し、ローカルで使いやすいように構成を調整しました（セキュリティ面でAPIキーを環境変数管理にする等）。

---

## ライセンス

- このリポジトリは [MIT License](./LICENSE.md) に準拠して公開しています。  
  - オリジナルの [browser-use](https://github.com/browser-use/browser-use) も MIT ライセンスで公開されています。  
  - MIT のライセンス文書は、本プロジェクトの `LICENSE.md` に記載しています。
- 本リポジトリのコードを利用・再配布される場合は、**必ず MIT ライセンスの条件を満たした上でご利用ください**。

> **Citation（引用）について**  
> 本プロジェクトの元となる [browser-use](https://github.com/browser-use/browser-use) の作者様は、研究やプロジェクトで使用する場合に以下の形式での引用を推奨されています。（あくまでオリジナル作者からのリクエストであり、私個人からのお願いではありません。）

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

研究論文等で本プロジェクトを利用される際は、上記のスタイルで元プロジェクトを引用することをご検討ください。

---

何か不明点がありましたら、IssuesやPull Requestなどでフィードバックをお寄せください。  
※このリポジトリは個人的な実験用に整備しているため、大幅なサポートはお約束できません。ご了承ください。