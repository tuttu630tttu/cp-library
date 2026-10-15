# スニペット

`template.cpp` の型エイリアス・マクロを前提に、必要な箇所へコピーします。元の名前と処理を維持しています。

| ファイル | 貼り付け位置 | 条件 |
| --- | --- | --- |
| grid4.inc | グローバルまたはsolve内 | grid8.incと同時に貼らない |
| grid8.inc | グローバルまたはsolve内 | grid4.incと同時に貼らない |
| outof.inc | solve内 | 事前にh, wを定義。引数順は行、列 |
| digits.inc | グローバル | n >= 0 |
| rnum.inc | グローバル | n >= 0、反転結果がlong longに収まること |

出典: https://app.notion.com/p/3bda262802fe80618ff2e6c7fbb4ca00

`.inc` は貼り付け用の断片です。単独のプログラムとしてはコンパイルできません。
