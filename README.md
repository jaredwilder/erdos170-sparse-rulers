# Erdős #170 — sparse rulers and difference bases

For `N>=1`, let `F(N)` be the least number of marks in `[0,N]` whose positive pairwise differences cover every integer `1,...,N`.

This repository contains exact small values, corrected witnesses, a parity obstruction, and an evaluation of the associated asymptotic constant.

## Results

- The constant

  \[
  c_0=\sqrt{\sup_{t\ne0}2\left(1-\frac{\sin t}{t}\right)}
  \]

  equals **1.5602779420418797...**, not `sqrt(2)`. The supremum occurs at the first positive root of `tan(t)=t`.
- Exact exhaustive values of `F(N)` are recorded through **`N=48`**.
- Corrected witnesses are supplied for `N=7` and `N=8`.
- **`F(10)=6`**; no five-mark ruler of length 10 exists.
- The elementary pair-counting lower bound first misses by one at `N=10` and by two at `N=44` within the computed range.
- A parity identity rules out perfect odd-mark rulers in the relevant congruence classes.
- Restricted and unrestricted difference-basis variants first diverge at **`N=18`**: the unrestricted problem has a seven-mark witness of diameter 24, while the restricted value is `F(18)=8`.

## Files

- [`ERDOS-170-SETTLED.md`](ERDOS-170-SETTLED.md) — mathematical write-up and corrected table.
- [`ruler.py`](ruler.py) — exact small-`N` search and witness checker.
- [`c0.py`](c0.py) — high-precision evaluation of `c_0`.
- [`PROVENANCE.md`](PROVENANCE.md) — source history.

## Reproduce

```bash
python ruler.py
python c0.py
```

`c0.py` requires `mpmath`.

The exhaustive statements are finite through the ranges stated above; the repository does not assert a complete solution of every asymptotic form of Erdős #170.

Author: Jared Wilder.
