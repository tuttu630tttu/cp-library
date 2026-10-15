# cp-library

競技プログラミング用のC++テンプレートと、コピーして使えるコード断片をまとめたライブラリです。

## 現在の内容

- [template.cpp](template.cpp): 入出力設定・型エイリアス・マクロ・main関数を含む基本テンプレート。
- [snippets/](snippets/README.md): 4方向・8方向の移動配列、範囲外判定、桁の分解・反転。
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

## テンプレートの参考資料

テンプレートの作成時に参考にした資料です。一部は記憶に基づくため、確認できた対応関係を以下に記載しています。

- [APG4b — C++入門](https://atcoder.jp/contests/APG4b)
- [sorachandu: 自分が競プロで使っているテンプレートの解説](https://qiita.com/sorachandu/items/041169d34b9f9b99bcf7) — Init（出力精度設定を含む）、型エイリアス、各種マクロ、inf、4方向・8方向の配列に同じ記述または共通点があります。範囲外判定は、記事の符号なし整数版に対し本リポジトリでは符号付き整数で負の座標も判定します。
- [【競技プログラミング】真似するだけでコーディングが爆速になるマクロ27選【ゆっくり解説】（Frest）](https://www.youtube.com/watch?v=d8fk8psRMeU) — 概要欄では、2026年10月15日の追記で「この動画を含め、このチャンネルの動画等で公開しているコードはご自由に使っていただいて構いません。」と利用許可が明記されています。概要欄には、動画のマクロの半分程度はsnukeさんに由来する旨も記載されています。動画内コードとの個別の対応や、元の提供者による利用条件は未確認です。
- [drken: 動的計画法超入門！ Educational DP Contest の A ～ E 問題の解説と類題集](https://qiita.com/drken/items/dc53c683d6de8aeacf5a) — chmin・chmaxに同じ実装があります。
- [drken: BFS (幅優先探索) 超入門！](https://qiita.com/drken/items/996d80bcae64649a6580) — Graphの型エイリアスの参考元。記事中にも同じ定義があります。

### コードの由来

自作の部分、参考資料をもとにした部分、AIで作成・修正した部分をまとめています。

| 対象 | 由来・変更内容 |
| --- | --- |
| `digits`・`rnum` | 自作後、AIでリファクタリング |
| `outof` | sorachandu氏の記事のuint版をもとに、AIと相談してll型の上下限比較へ変更。引数名は行・列に合わせてii・jjに変更 |
| `Field`・`Board`・`min_pq` | 基本は自作。命名などをAIと相談 |
| `Graph` | drken氏の上記BFS解説を参考に採用。記事中に `using Graph = vector<vector<int>>;` あり |
| `pb`・`unless`・`until` | 自作 |
| `rrep` | Frest氏の上記動画を参考に作成 |
| `idx` | [ABC450 Cの公式解説一覧](https://atcoder.jp/contests/abc450/tasks/abc450_c/editorial)を参考に採用。[公式解説のC++例](https://atcoder.jp/contests/abc450/editorial/17745)に同じマクロあり |
| `MOD1`・`MOD9` | 剰余計算用の定数として追加 |
| `SIGMA` | [ABC449 C — Comfortable Distance](https://atcoder.jp/contests/abc449/tasks/abc449_c)の学習時に使っていた定数。[公式解説](https://atcoder.jp/contests/abc449/editorial/17269)は文字の種類数をσと表記。公式コードでは `cnt(26)` のため、`SIGMA` という定数名を導入した直接の由来は未確定 |
| `sub()`・`solve()`・`main()` | AIと相談して作成。`sub`は補助関数用の空枠、`solve`は問題の実装、`main`は複数テストケースに対応するループ（初期設定は1ケース） |
| `tools/generate_snippets.py` | 本リポジトリの整備時にAIで作成 |
| `vscode/cpp.code-snippets` | `template.cpp`・`snippets/*.inc`から上記スクリプトで生成。由来は各原本と同じ |

`SIGMA` の定数名を導入したきっかけは不明です。そのほかも、参考資料に同じ記述や類似した記述があっても、採用した経緯を断定できない部分があります。

参考資料の記載だけで、元コードの再ライセンス許可を得たことにはなりません。リポジトリ全体へのライセンス付与は保留しています。

## AtCoder Library (ACL)

ACLを使う場合は、[AtCoder公式の公開案内](https://atcoder.jp/posts/517)と[公式リポジトリ](https://github.com/atcoder/ac-library)を参照してください。利用条件は[ACLのLICENSE](https://github.com/atcoder/ac-library/blob/master/LICENSE)で確認できます。

基本テンプレートの `#include<atcoder/all>` と `using namespace atcoder;` はコメントアウトしてあります。使用時に有効にし、ローカル環境にはACLを別途導入してください。このリポジトリにはACL本体を同梱していません。

## 動作確認

GCC 16 / C++17でテンプレートの構文確認済み。4方向・8方向それぞれとスニペットを組み合わせてコンパイルし、digits・rnumの0と通常値、outofの境界と内側を確認済み。
