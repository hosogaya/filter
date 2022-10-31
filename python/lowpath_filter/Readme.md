# sample_data.csv
* sampling period: 0.025 [s]

# reference
* [FIRフィルタの実装](https://qiita.com/Ginom/items/4e438121fc345c4efded)
* [Pythonのバターワース](https://mori-memo.hateblo.jp/entry/2022/04/30/235815)
* [Rustのフィルタ](https://sounds-so-good.com/article/8341537962530/)
* [双二次フィルタ](https://ufcpp.net/study/sp/digital_filter/biquad/)
* [双一次変換とプリワーピング](https://www.makeitconvenient72.com/686/)

# Low path filter
基準フィルタは以下のようになる．(カットオフ周波数は１)
```math
H(s) = \frac{1}{s^2 + \frac{1}{Q}s + 1}
```
ディジタルフィルタに変換するために双一次変換を用いる.
```math
s = \frac{2}{T}\frac{1-z^{-1}}{1 + z^{-1}}
```
連続時間領域でのカットオフ周波数$\omega_{ca}$は，$s=s/\omega_{ca}$とすることで実現できる．このときに，連続時間領域での周波数は$0\sim\infty$であるのに対して，離散時間領域での周波数は$0\sim ナイキスト周波数$になるので補正する必要がある．これをプリワーピングという．
連続時間での角周波数を$\omega_a$，離散時間での角周波数を$\omega_d$とすると双一次変換の式から以下のような関係式が導かれる．
```math
\omega_a = \frac{2}{T}\tan\left(\frac{\omega_dT}{2}\right)
```

以上のことから以下のような変換を用いることでデジタルフィルタを設計することができる．ただし$f_c$はカットオフ周波数，$f_s$はサンプリング周波数である
```math
s = \frac{\frac{1-z^{-1}}{1 + z^{-1}}}{\tan\left(\frac{2\pi f_c}{2f_s}\right)}
```
