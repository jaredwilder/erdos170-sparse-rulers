"""The Erdos 170 constant, computed at the right stationary point.

The frozen definition is  c0 = sqrt( sup { 2(1 - sin(t)/t) : t != 0 } ).
sin(t)/t goes NEGATIVE, so the sup is attained where sin(t)/t is MINIMIZED --
at the first positive root of tan(t) = t -- not in the limit t -> infinity.
Taking the limit gives 2, hence the (wrong) value sqrt(2).
"""
from mpmath import mp, findroot, sin, tan, sqrt, mpf

mp.dps = 30

t_star = findroot(lambda t: tan(t) - t, 4.5)
v = sin(t_star) / t_star
S = 2 * (1 - v)
c0 = sqrt(S)

print("first positive root of tan t = t")
print("  t*          =", t_star)
print("  sin(t*)/t*  =", v)
print()
print("  sup         =", S)
print("  c0 = sqrt   =", c0)
print()
print("  sqrt(2)     =", sqrt(2), "   <- the value the corpus filed")
print("  difference  =", c0 - sqrt(2))
print()

best = None
t = mpf("0.01")
while t < 60:
    x = sin(t) / t
    if best is None or x < best[1]:
        best = (t, x)
    t += mpf("0.001")
print("scan of sin(t)/t over (0,60), step 1e-3:")
print("  minimum", best[1], "at t =", best[0])
assert abs(best[0] - t_star) < mpf("0.002"), "scan disagrees with the root"
print("  agrees with t*  OK")
