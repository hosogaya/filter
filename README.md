# filter

## Moving Average Filter
* $k$ : step
* $n$ : filter size
* $x(k)$ : observed value at $k$ step

### Simple moving average $SMA (k)$
```math
SMA(k) = \frac{1}{n}\sum_{i=0}^{n-1}x(k-i)
```

### Cumulative Average
```math
CA(k) = \frac{1}{k}\sum_{i=1}^{k}x(k) \\
CA(k+1) =  \frac{x(k+1) + k\cdot CA(k)}{k + 1}
```

### Weighted Moving Average
```math
WMA(k) = \frac{2}{n(n+1)}\sum_{i=0}^{n-1}(n-i)x(k - i)
```