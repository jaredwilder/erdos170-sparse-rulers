# Erdős 170: the constant is 1.5603, not √2

Erdős 170 asks for the asymptotics of `F(N)` — the least number of marks on `[0, N]` whose
pairwise differences cover every distance `1..N` (a sparse ruler, or difference basis). The
question the campaign actually froze is the **value of `lim F(N)/√N`**, and the frozen definition
of the governing constant reads

```
c₀ = √( sup { 2(1 − sin θ / θ) : θ ∈ ℝ, θ ≠ 0 } )
```

Three separate objects in the corpus evaluate that supremum as **2**, giving `c₀ = √2 ≈ 1.414214`.

**That is wrong, and the error is a one-liner.** `sin θ / θ` goes negative. Taking `θ → ∞` gives
the limit 2, not the supremum. The supremum is attained where `sin θ / θ` is *minimized*, at the
first positive root of `tan θ = θ`:

```
θ*            = 4.493409457909064175307880927...
sin θ* / θ*   = −0.217233628211221657408279326...
sup           = 2(1 + 0.2172336282...) = 2.434467256422443314816558651...
c₀            = √2.4344672564...        = 1.560277942041879702102077382...
```

A scan of `sin θ / θ` over `θ ∈ (0, 60)` at step `10⁻³` confirms `θ*` is the global minimum.

**`c₀ = 1.5603`, not `1.4142`.** The difference is 0.1461 — about 10%. This is the
Rédei–Rényi / Leech constant, and it is strictly stronger than the trivial pair-counting bound
√2 that the corpus collapsed it onto.

## The small-value table, computed exhaustively

Complete enumeration over all mark sets containing 0 and N, smallest size first.

| N | F(N) | witnesses of that size | lexicographically first |
|---|---|---|---|
| 1 | 2 | 1 | `{0,1}` |
| 2 | 3 | 1 | `{0,1,2}` |
| 3 | 3 | 2 | `{0,1,3}` |
| 4 | 4 | 3 | `{0,1,2,4}` |
| 5 | 4 | 4 | `{0,1,2,5}` |
| 6 | 4 | 2 | `{0,1,4,6}` |
| 7 | 5 | 12 | `{0,1,2,3,7}` |
| 8 | 5 | 8 | `{0,1,2,5,8}` |
| 9 | 5 | 4 | `{0,1,2,6,9}` |
| 10 | **6** | 38 | `{0,1,2,3,6,10}` |
| 11 | 6 | 30 | `{0,1,2,3,7,11}` |
| 12 | 6 | 14 | `{0,1,2,3,8,12}` |
| 13 | 6 | 6 | `{0,1,2,6,10,13}` |
| 14 | 7 | 130 | `{0,1,2,3,4,9,14}` |
| 15 | 7 | 80 | `{0,1,2,3,4,10,15}` |
| 16 | 7 | 32 | `{0,1,2,3,8,12,16}` |
| 17 | 7 | 12 | `{0,1,2,3,8,13,17}` |
| 18 | 8 | 500 | `{0,1,2,3,4,5,12,18}` |
| 19 | 8 | 326 | `{0,1,2,3,4,9,14,19}` |
| 20 | 8 | 150 | `{0,1,2,3,4,10,15,20}` |

```
F(1..20) = 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8
```

Extended by the same exhaustive method to N = 48:

```
F(1..48) = 2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,
           10,10,10,10,10,10,10,11,11,11,11,11,11,11,12,12,12,12,12
```

with `F(N) <= F(N+1) <= F(N)+1` throughout the range. Witnesses at the top:
`F(43)=11` via `{0,1,3,6,13,20,27,34,38,42,43}` and `F(48)=12` via
`{0,1,2,3,13,26,29,33,39,43,47,48}`.

## Two shipped witnesses do not work

| N | shipped witness | result |
|---|---|---|
| 7 | `{0,1,3,4,7}` | **fails — distance 5 is not covered** |
| 8 | `{0,1,3,6,8}` | **fails — distance 4 is not covered** |

Correct witnesses of the same size:

```
N = 7 :  {0, 1, 2, 3, 7}
N = 8 :  {0, 1, 2, 5, 8}
```

## F(10) = 6

The corpus carries both F(10)=5 and F(10)=6 in different routes. **It is 6**, with 38 distinct
6-mark witnesses. No 5-mark ruler of length 10 exists.

## Where the counting bound is actually tight

`F(N) ≥ ⌈(1 + √(1+8N))/2⌉` comes from needing `C(m,2) ≥ N` distinct positive differences.

For the real bound, exhaustively:

| | N |
|---|---|
| **tight** | 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 16, 17, 22, 23, 29 |
| **not tight** | everything else through N = 48 |

Thus:

```
tight through N = 9
first short by 1 at N = 10   (bound 5, truth 6)
first short by 2 at N = 44   (bound 10, truth 12)
```

## The parity obstruction, and its generalization

Ten distinct differences in `[1,10]` must sum to 55, odd. Any 5-mark ruler's gap-weighted sum is
`4d₁ + 6d₂ + 6d₃ + 4d₄`, even. So no perfect 5-mark ruler of length 10 exists.

More generally,

```
Σ_{i<j} (a_j − a_i) = Σ_i (2i − k + 1) a_i
```

is even whenever `k` is odd, while a perfect `k`-mark ruler requires the differences to be
`1..C(k,2)`. The obstruction therefore fires for every odd `k` for which
`C(k,2)(C(k,2)+1)/2` is odd, including `k=5,7,13,...`.

## The definition is load-bearing from N = 18

Restricted and unrestricted variants agree through N=17 and first diverge at N=18. The 7-mark set

```
{0, 2, 7, 14, 15, 18, 24}
```

has diameter 24 and covers `1..18`, while no 7-mark subset of `{0,...,18}` does. Thus restricted
`F(18)=8` and unrestricted `F(18)=7`.

## Reproduce

`ruler.py` recomputes the small exact table and witness audit. `c0.py` computes the constant.
