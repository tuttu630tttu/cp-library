# スニペット

`template.cpp` の型エイリアス・マクロを前提に、必要な箇所へコピーします。

| ファイル | 貼り付け位置 | 条件 |
| --- | --- | --- |
| grid4.inc | グローバルまたはsolve内 | grid8.incと同時に貼らない |
| grid8.inc | グローバルまたはsolve内 | grid4.incと同時に貼らない |
| outof.inc | solve内 | 事前にh, wを定義。引数順は行、列 |
| digits.inc | グローバル | n >= 0 |
| rnum.inc | グローバル | n >= 0、反転結果がlong longに収まること |

参考資料: [sorachandu: 自分が競プロで使っているテンプレートの解説](https://qiita.com/sorachandu/items/041169d34b9f9b99bcf7)。4方向・8方向の配列は同じ記述があります。`outof`は記事のuint版をもとに、AIと相談して符号付き整数の比較へ変更しました。`digits`・`rnum`は自作後にAIでリファクタリングしています。詳細は[コードの由来](../README.md#コードの由来)を参照してください。

`.inc` は貼り付け用の断片です。単独のプログラムとしてはコンパイルできません。
