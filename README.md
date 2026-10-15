# cp-library

手持ちの競プロコードを整理するライブラリ。Notionのコードを起点に、普段の名前・マクロ・書き方を保って整備しました。

## 現在の内容

- [template.cpp](template.cpp): 「儀式」のC++コードをそのまま移行。
- [snippets/](snippets/README.md): 「後付け型テンプレ」の5つのコード断片をそのまま分割。
- [vscode/cpp.code-snippets](vscode/cpp.code-snippets): 原本から生成するVS Code用スニペット。

## VS Codeで使う

編集するのは `template.cpp` と `snippets/*.inc` です。変更後、次のコマンドでJSONを作り直します。Python 3の標準ライブラリだけで動き、リポジトリのルートで実行してください。別のディレクトリからはスクリプトの絶対パスを指定できます。

```sh
python3 tools/generate_snippets.py
```

このコマンドは、生成した6個をmacOSの `~/Library/Application Support/Code/User/snippets/cpp.json` に直接反映します。既存の `kyopro`・`outof`・`dxdy4`・`dxdy8` は引き継いで置き換え、ほかのスニペットは保持します。更新前には同じフォルダに日時付き `.bak` を作成します。変更がない場合は書き換えもバックアップ作成もしません。

呼び出し名は `kyopro`、`dxdy4`、`dxdy8`、`outof`、`digits`、`rnum`。`kyopro` は展開後にカーソルが `solve()` 内へ移動します。C++ファイルの `Insert Snippet` から選択でき、設定の `"editor.tabCompletion": "on"` で呼び出し名＋Tabでも展開できます。

リポジトリ内のJSONだけを生成する場合は `--generate-only`、別の登録先を使う場合は `--target /path/to/cpp.json` を付けます。登録先は通常のJSONを前提とし、コメント・末尾カンマなどで解析できない場合は上書きせず停止します。

編集は原本側で行い、このコマンドで再反映してください。スニペットの前提条件は [snippets/README.md](snippets/README.md) を参照してください。

## コンテストで使う前に

[AtCoder生成AI対策ルール（2026-10-14版）](https://info.atcoder.jp/entry/llm-rules-ja)では、事前に生成AIで作成したコードはコンテスト開始前のWeb公開と、コピー時の参照URL添付が必要です。

公開リポジトリ: https://github.com/tuttu630tttu/cp-library

使う版の公開済みコミットを開き、ファイルの固定URLを提出コードのコメントに添付してください。更新版も使用するコンテストの開始前に公開します。

```cpp
// Source: https://github.com/tuttu630tttu/cp-library/blob/<公開済みコミットSHA>/template.cpp
```

上は書式例です。実在する公開済みコミットのURLに置き換えてください。開催中のABC・ARC・AGCでは、AIへのコード修正・デバッグ依頼も禁止されています。

## 整備方針

そのままコピーして使えるテンプレート・関数・コード断片だけを置きます。`template.cpp` の型エイリアス・マクロや、貼り付け先の変数を前提にする断片は、必要な条件を明記します。問題固有の実装例、未完成コード、学習メモは含めません。

出典は各ファイルまたはREADMEに残します。

## 動作確認

GCC 16 / C++17でテンプレートの構文確認済み。4方向・8方向それぞれとスニペットを組み合わせてコンパイルし、digits・rnumの0と通常値、outofの境界と内側を確認済み。
