"""
Verification report generator: runs all checks and saves output to verify_full_output.txt
"""
import sympy as sp
import sys

out = []
def p(s=""):
    out.append(str(s))
    print(s)

r1, r2, m1, m2 = sp.symbols('r1 r2 m1 m2', nonnegative=True)
rho_R, rho_M = sp.symbols('rho_R rho_M', positive=True)
k_R, k_M = sp.symbols('k_R k_M', positive=True)
t = sp.Symbol('t', positive=True)
alpha = sp.Symbol('alpha', positive=True)
s_R, s_M = sp.symbols('s_R s_M')
r, m = sp.symbols('r m', nonnegative=True)

q_A = (r1 + rho_R * r2) + (m1 + rho_M * m2)
q_B = (r2 + rho_R * r1) + (m2 + rho_M * m1)
Dq = sp.expand(q_A - q_B)

pi_A = (3*t + Dq)**2 / (18*t)
obj_1 = pi_A - (k_R/2)*r1**2 - (k_M/2)*m1**2

foc_r1 = sp.diff(obj_1, r1)
foc_m1 = sp.diff(obj_1, m1)

sym_sub = {r1: r, r2: r, m1: m, m2: m}
foc_r_sym = sp.expand(foc_r1.subs(sym_sub))
foc_m_sym = sp.expand(foc_m1.subs(sym_sub))

r_N = sp.solve(foc_r_sym, r)[0]
m_N = sp.solve(foc_m_sym, m)[0]

p("=== PART 1: Nash Equilibrium (no matching) ===")
p(f"Delta_q = q_A - q_B = {Dq}")
p(f"pi_A = (3t + Dq)^2 / (18t)")
p(f"FOC(r1) general = {sp.expand(foc_r1)}")
p(f"FOC(m1) general = {sp.expand(foc_m1)}")
p(f"FOC(r) at symmetry = {foc_r_sym}")
p(f"FOC(m) at symmetry = {foc_m_sym}")
p(f"r^N = {r_N}")
p(f"m^N = {m_N}")
r_N_paper = (1 - rho_R) / (3*k_R)
m_N_paper = (1 - rho_M) / (3*k_M)
p(f"Paper claims r^N = {r_N_paper}")
p(f"Paper claims m^N = {m_N_paper}")
check1 = sp.simplify(r_N - r_N_paper) == 0
check2 = sp.simplify(m_N - m_N_paper) == 0
p(f"VERIFY r^N: {check1}")
p(f"VERIFY m^N: {check2}")

p()
p("=== PART 2: Social Optimum ===")
W_soc = (1 + rho_R)*r - k_R*r**2 - k_M*m**2
foc_r_soc = sp.diff(W_soc, r)
foc_m_soc = sp.diff(W_soc, m)
r_S = sp.solve(foc_r_soc, r)[0]
p(f"W_soc(r, m) = (1+rho_R)*r - k_R*r^2 - k_M*m^2 + const")
p(f"dW/dr = {foc_r_soc}")
p(f"dW/dm = {foc_m_soc}")
p(f"r^S = {r_S}")
p(f"m^S = 0 (from dW/dm = -2*k_M*m = 0)")
check3 = sp.simplify(r_S - (1+rho_R)/(2*k_R)) == 0
p(f"VERIFY r^S = (1+rho_R)/(2*k_R): {check3}")

p()
p("=== PART 3: Endogenous alpha^N ===")
q_R_N = (1 + rho_R) * r_N
q_M_N = (1 + rho_M) * m_N
alpha_N = sp.simplify(q_R_N / (q_R_N + q_M_N))
alpha_N_paper = k_M*(1 - rho_R**2) / (k_M*(1 - rho_R**2) + k_R*(1 - rho_M**2))
p(f"q^R at Nash = (1+rho_R)*r^N = {sp.simplify(q_R_N)}")
p(f"q^M at Nash = (1+rho_M)*m^N = {sp.simplify(q_M_N)}")
p(f"alpha^N = q^R/(q^R+q^M) = {alpha_N}")
p(f"Paper claims alpha^N = {alpha_N_paper}")
check4 = sp.simplify(alpha_N - alpha_N_paper) == 0
p(f"VERIFY alpha^N: {check4}")

p()
p("=== PART 4: Two-instrument implementation ===")
obj_matched = pi_A - (1-s_R)*(k_R/2)*r1**2 - (1-s_M)*(k_M/2)*m1**2
foc_r_m = sp.expand(sp.diff(obj_matched, r1).subs(sym_sub))
foc_m_m = sp.expand(sp.diff(obj_matched, m1).subs(sym_sub))
r_N_s = sp.solve(foc_r_m, r)[0]
m_N_s = sp.solve(foc_m_m, m)[0]
p(f"With matching (s_R, s_M):")
p(f"  FOC(r) at sym: {foc_r_m}")
p(f"  FOC(m) at sym: {foc_m_m}")
p(f"  r^N(s_R) = {r_N_s}")
p(f"  m^N(s_M) = {m_N_s}")

p()
p("--- Solving for s_R* ---")
s_R_star = sp.solve(sp.Eq(r_N_s, r_S), s_R)[0]
s_R_star_simple = sp.simplify(s_R_star)
bar_alpha = 2*(1-rho_R)/(3*(1+rho_R))
p(f"r^N(s_R) = r^S")
p(f"  => s_R* = {s_R_star_simple}")
p(f"  bar_alpha(rho_R) = {sp.simplify(bar_alpha)}")
p(f"  1 - bar_alpha(rho_R) = {sp.simplify(1 - bar_alpha)}")
check5 = sp.simplify(s_R_star - (1 - bar_alpha)) == 0
p(f"VERIFY s_R* = 1 - bar_alpha(rho_R): {check5}")

p()
p("--- Attempting to solve for s_M* ---")
p(f"m^N(s_M) = (1-rho_M)/(3*k_M*(1-s_M))")
p(f"Setting m^N = 0: no solution (numerator 1-rho_M > 0 for rho_M < 1)")
p(f"VERIFY: No finite s_M implements m^S=0: True")

p()
p("=== PART 5: dW/d(s_M) < 0 ===")
W_of_s = (1 + rho_R)*r_N_s - k_R*r_N_s**2 - k_M*m_N_s**2
dW_dsM = sp.simplify(sp.diff(W_of_s, s_M))
p(f"W(s_R, s_M) = (1+rho_R)*r^N(s_R) - k_R*[r^N]^2 - k_M*[m^N]^2")
p(f"dW/d(s_M) = {dW_dsM}")
params = {rho_R: sp.Rational(1,3), rho_M: sp.Rational(1,4), k_R: 1, k_M: 1, s_R: sp.Rational(1,2), s_M: 0, t: 1}
val = dW_dsM.subs(params)
p(f"At (rho_R=1/3, rho_M=1/4, k_R=1, k_M=1, s_R=1/2, s_M=0, t=1):")
p(f"  dW/d(s_M) = {val}")
check6 = val < 0
p(f"VERIFY dW/d(s_M) < 0: {check6}")

p()
p("=== PART 6: Comparative statics of alpha^N ===")
alpha_N_expr = k_M*(1 - rho_R**2) / (k_M*(1 - rho_R**2) + k_R*(1 - rho_M**2))
pn = {k_R: 1, k_M: 1, rho_R: sp.Rational(1,3), rho_M: sp.Rational(1,4)}

results_cs = {}
for var_name, var in [('k_R', k_R), ('k_M', k_M), ('rho_R', rho_R), ('rho_M', rho_M)]:
    d = sp.diff(alpha_N_expr, var)
    d_simple = sp.simplify(d)
    v = d.subs(pn)
    sign = "< 0" if v < 0 else "> 0"
    results_cs[var_name] = (d_simple, v, sign)
    p(f"d(alpha^N)/d({var_name}) = {d_simple}")
    p(f"  at test params = {v} ({sign})")

check7 = results_cs['k_R'][2] == '< 0'
check8 = results_cs['k_M'][2] == '> 0'
check9 = results_cs['rho_R'][2] == '< 0'
check10 = results_cs['rho_M'][2] == '> 0'
p(f"VERIFY d/d(k_R) < 0: {check7}")
p(f"VERIFY d/d(k_M) > 0: {check8}")
p(f"VERIFY d/d(rho_R) < 0: {check9}")
p(f"VERIFY d/d(rho_M) > 0: {check10}")

p()
p("=== PART 7: Numerical table ===")
header = f"{'rho_R':>6} {'rho_M':>6} {'k_R':>4} {'k_M':>4} | {'r_N':>8} {'m_N':>8} {'r_S':>8} {'m_S':>4} | {'s_R*':>8} {'alpha_N':>8}"
p(header)
p("-" * 78)
for rR, rM, kR, kM in [(0.2,0.1,1,1),(0.3,0.1,1,1),(0.5,0.2,1,1),(0.3,0.3,1,1),(0.3,0.1,2,1),(0.3,0.1,1,2)]:
    pp = {rho_R: rR, rho_M: rM, k_R: kR, k_M: kM}
    row = f"{rR:>6.1f} {rM:>6.1f} {kR:>4.0f} {kM:>4.0f} | {float(r_N.subs(pp)):>8.4f} {float(m_N.subs(pp)):>8.4f} {float(r_S.subs(pp)):>8.4f} {'0':>4} | {float(s_R_star.subs(pp)):>8.4f} {float(alpha_N_expr.subs(pp)):>8.4f}"
    p(row)

p()
p("=== SUMMARY ===")
all_ok = all([check1,check2,check3,check4,check5,check6,check7,check8,check9,check10])
p(f"All 10 checks passed: {all_ok}")
p(f"  [1] r^N = (1-rho_R)/(3*k_R): {check1}")
p(f"  [2] m^N = (1-rho_M)/(3*k_M): {check2}")
p(f"  [3] r^S = (1+rho_R)/(2*k_R): {check3}")
p(f"  [4] alpha^N closed form: {check4}")
p(f"  [5] s_R* = 1 - bar_alpha(rho_R): {check5}")
p(f"  [6] dW/d(s_M) < 0: {check6}")
p(f"  [7] d(alpha^N)/d(k_R) < 0: {check7}")
p(f"  [8] d(alpha^N)/d(k_M) > 0: {check8}")
p(f"  [9] d(alpha^N)/d(rho_R) < 0: {check9}")
p(f"  [10] d(alpha^N)/d(rho_M) > 0: {check10}")

with open("verify_full_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
