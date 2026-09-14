# Erdős 170 — sparse rulers and difference bases

This repository is the focused home for the Erdős 170 sparse-ruler program recovered from the ore estate.

For `N >= 1`, let `F(N)` be the least number of marks in `[0,N]` whose positive pairwise differences cover every integer `1,...,N`.

## Recovered results

- The asymptotic constant in the frozen definition
  `c0 = sqrt(sup_{t != 0} 2(1 - sin(t)/t))`
  is **1.5602779420418797...**, not `sqrt(2)`. The supremum occurs at the first positive root of `tan(t)=t`, where `sin(t)/t` is minimized.
- Exact exhaustive values are recorded through `N=48`.
- Two shipped witnesses at `N=7` and `N=8` were wrong; corrected witnesses of the same size are supplied.
- `F(10)=6`; there is no 5-mark ruler of length 10.
- The pair-counting lower bound is first short by one at `N=10` and first short by two at `N=44` in the computed range.
- A parity identity gives a general obstruction to perfect odd-mark rulers in the relevant congruence classes.
- Restricted and unrestricted variants first diverge at `N=18`: unrestricted admits a 7-mark witness of diameter 24, while restricted `F(18)=8`.

## Files

- [`ERDOS-170-SETTLED.md`](ERDOS-170-SETTLED.md) — recovered mathematical write-up and correction ledger.
- [`ruler.py`](ruler.py) — exact exhaustive sparse-ruler search for the small table and witness audit.
- [`c0.py`](c0.py) — high-precision computation of the asymptotic constant.
- [`PROVENANCE.md`](PROVENANCE.md) — source hashes and authority notes.

## Reproduce

```bash
python ruler.py
python c0.py
```

`c0.py` requires `mpmath`.

The computations establish the finite statements they explicitly enumerate. The asymptotic constant evaluation is analytic; this repository does not claim that every broader historical statement attached to Erdős 170 has been solved here.

Author: Jared Wilder
