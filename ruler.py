"""Exhaustively compute F(N): the least number of marks on [0,N] whose pairwise
differences cover every distance 1..N. Sparse-ruler / difference-basis numbers.

Settles the Erdos 170 table and checks the witnesses reported in the ore corpus.
"""
from itertools import combinations

REPORTED = {
    1: [0, 1], 2: [0, 1, 2], 3: [0, 1, 3], 4: [0, 1, 3, 4],
    5: [0, 1, 3, 5], 6: [0, 1, 4, 6], 7: [0, 1, 3, 4, 7], 8: [0, 1, 3, 6, 8],
}


def covers(marks, N):
    d = set()
    for a, b in combinations(marks, 2):
        d.add(abs(a - b))
    return all(x in d for x in range(1, N + 1))


def F(N):
    """least k and ALL witnesses of that size containing 0 and N."""
    for k in range(2, N + 3):
        found = []
        for mid in combinations(range(1, N), k - 2):
            m = (0,) + mid + (N,)
            if covers(m, N):
                found.append(list(m))
        if found:
            return k, found
    return None, []


print("%-4s %-5s %-9s %s" % ("N", "F(N)", "#witness", "lexicographically first witness"))
print("-" * 72)
table = {}
for N in range(1, 21):
    k, w = F(N)
    table[N] = k
    print("%-4d %-5d %-9d %s" % (N, k, len(w), w[0]))

print()
print("sequence F(1..20):", [table[n] for n in range(1, 21)])

print()
print("=" * 72)
print("CHECK OF THE WITNESSES REPORTED IN THE ORE CORPUS")
print()
for N, w in REPORTED.items():
    ok = covers(w, N)
    k, good = F(N)
    d = set()
    for a, b in combinations(w, 2):
        d.add(abs(a - b))
    missing = [x for x in range(1, N + 1) if x not in d]
    status = "OK" if ok else "FAILS - missing %s" % missing
    print("  N=%-2d size %d  %-18s %s" % (N, len(w), w, status))
    if not ok:
        same = [g for g in good if len(g) == len(w)]
        print("       a correct witness of the same size: %s" % (same[0] if same else "none"))

print()
print("=" * 72)
print("COUNTING LOWER BOUND  ceil((1+sqrt(1+8N))/2)  vs exact F(N)")
from math import ceil, sqrt
print("%-4s %-6s %-8s %s" % ("N", "F(N)", "bound", "tight?"))
for N in range(1, 21):
    b = ceil((1 + sqrt(1 + 8 * N)) / 2)
    print("%-4d %-6d %-8d %s" % (N, table[N], b, "TIGHT" if table[N] == b else ""))
