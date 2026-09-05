"""
Numerical examples for Table 1 in the paper.

Functional forms:
  g(e) = beta * log(1 + e)        =>  g'(e) = beta / (1+e)
  K(e) = kappa * e^2 / 2          =>  K'(e) = kappa * e

Nash equilibrium FOC (s=0):
  kappa * e^N = (1-rho)/3 * beta/(1+e^N)
  => kappa * e^N * (1+e^N) = (1-rho)*beta/3

Social optimum FOC:
  kappa * e^S = alpha*(1+rho)/2 * beta/(1+e^S)
  => kappa * e^S * (1+e^S) = alpha*(1+rho)*beta/2

Both are quadratic in e: kappa*e^2 + kappa*e - C = 0
  => e = [-kappa + sqrt(kappa^2 + 4*kappa*C)] / (2*kappa)
     = [-1 + sqrt(1 + 4*C/kappa)] / 2

Implementation:
  s* = 1 - bar_alpha(rho)/alpha
  bar_alpha(rho) = 2*(1-rho)/(3*(1+rho))

Welfare:
  W^soc(e) = alpha*(1+rho)*g(e) - 2*K(e) + const
           = alpha*(1+rho)*beta*log(1+e) - kappa*e^2 + const
  (the const = -t/4 - c doesn't affect comparisons)
  
  Welfare loss from decentralization:
  DeltaW = W^soc(e^S) - W^soc(e^N(0))
"""
import math

def solve_e(C, kappa):
    """Solve kappa*e*(1+e) = C  =>  e = [-1 + sqrt(1 + 4C/kappa)] / 2"""
    disc = 1 + 4*C/kappa
    if disc < 0:
        return None
    return (-1 + math.sqrt(disc)) / 2

def compute_example(alpha, rho, beta, kappa, t):
    """Compute all quantities for a single parameter set."""
    # Nash FOC coefficient
    C_N = (1 - rho) * beta / 3
    e_N = solve_e(C_N, kappa)
    
    # Social optimum FOC coefficient
    C_S = alpha * (1 + rho) * beta / 2
    e_S = solve_e(C_S, kappa)
    
    # Threshold
    bar_alpha = 2*(1-rho) / (3*(1+rho))
    
    # Optimal matching rate
    s_star = 1 - bar_alpha / alpha
    
    # Welfare (drop constant)
    def W(e):
        return alpha*(1+rho)*beta*math.log(1+e) - kappa*e**2
    
    W_S = W(e_S)
    W_N = W(e_N)
    DeltaW = W_S - W_N  # welfare loss from decentralization (positive = decentralization is worse)
    
    # Relative welfare loss (% of planner's welfare)
    if abs(W_S) > 1e-10:
        pct_loss = DeltaW / abs(W_S) * 100
    else:
        pct_loss = float('nan')
    
    # Over or underinvestment
    if alpha < bar_alpha:
        regime = "OVER"
    elif alpha > bar_alpha:
        regime = "UNDER"
    else:
        regime = "EXACT"
    
    return {
        'alpha': alpha, 'rho': rho, 'beta': beta, 'kappa': kappa, 't': t,
        'bar_alpha': bar_alpha,
        'e_N': e_N, 'e_S': e_S,
        'g_N': beta*math.log(1+e_N), 'g_S': beta*math.log(1+e_S),
        's_star': s_star,
        'W_N': W_N, 'W_S': W_S, 'DeltaW': DeltaW, 'pct_loss': pct_loss,
        'regime': regime
    }

# Fixed parameters
beta = 1.0
kappa = 1.0
t = 1.0

print("=" * 90)
print("TABLE 1: Sensitivity analysis for the baseline model")
print(f"  g(e) = {beta}*log(1+e),  K(e) = {kappa}*e^2/2,  t = {t}")
print("=" * 90)

# Panel A: Varying alpha for fixed rho
print("\nPanel A: Varying alpha (rho = 0.3)")
print(f"  bar_alpha(0.3) = {2*(1-0.3)/(3*(1+0.3)):.4f}")
print()
header = f"{'alpha':>6} {'rho':>5} | {'e^N':>8} {'e^S':>8} | {'bar_a':>7} {'s*':>8} | {'regime':>6} | {'DW':>8} {'%loss':>7}"
print(header)
print("-" * 82)

rho_fixed = 0.3
for alpha in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    r = compute_example(alpha, rho_fixed, beta, kappa, t)
    print(f"{r['alpha']:>6.1f} {r['rho']:>5.1f} | {r['e_N']:>8.4f} {r['e_S']:>8.4f} | "
          f"{r['bar_alpha']:>7.4f} {r['s_star']:>8.4f} | {r['regime']:>6} | "
          f"{r['DeltaW']:>8.4f} {r['pct_loss']:>7.1f}%")

# Panel B: Varying rho for fixed alpha
print("\nPanel B: Varying rho (alpha = 0.6)")
print()
print(header)
print("-" * 82)

alpha_fixed = 0.6
for rho in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
    r = compute_example(alpha_fixed, rho, beta, kappa, t)
    print(f"{r['alpha']:>6.1f} {r['rho']:>5.1f} | {r['e_N']:>8.4f} {r['e_S']:>8.4f} | "
          f"{r['bar_alpha']:>7.4f} {r['s_star']:>8.4f} | {r['regime']:>6} | "
          f"{r['DeltaW']:>8.4f} {r['pct_loss']:>7.1f}%")

# Panel C: Selected parameter combinations for the paper
print("\n" + "=" * 90)
print("TABLE 1 (condensed for paper): Selected parameter combinations")
print("=" * 90)

scenarios = [
    # (alpha, rho, label)
    (0.2, 0.1, "Low alpha, low spillover (pure promotion)"),
    (0.2, 0.5, "Low alpha, high spillover"),
    (0.5, 0.3, "Moderate alpha and spillover"),
    (0.8, 0.1, "High alpha, low spillover"),
    (0.8, 0.5, "High alpha, high spillover (public research)"),
    (1.0, 0.3, "Fully real quality"),
    (1.0, 0.7, "Fully real quality, high spillover"),
]

print()
print(f"{'Scenario':>45} | {'alpha':>5} {'rho':>5} | {'e^N':>7} {'e^S':>7} {'ratio':>6} | {'s*':>7} | {'regime':>6} {'%loss':>6}")
print("-" * 110)

for alpha, rho, label in scenarios:
    r = compute_example(alpha, rho, beta, kappa, t)
    ratio = r['e_N'] / r['e_S'] if r['e_S'] > 0 else float('inf')
    print(f"{label:>45} | {r['alpha']:>5.1f} {r['rho']:>5.1f} | "
          f"{r['e_N']:>7.4f} {r['e_S']:>7.4f} {ratio:>6.2f} | "
          f"{r['s_star']:>7.4f} | {r['regime']:>6} {r['pct_loss']:>5.1f}%")

# Generate LaTeX table
print("\n\n% ========== LaTeX Table ==========")

latex = r"""
\begin{table}[tbp]
\centering
\caption{Numerical examples: decentralized investment, social optimum, and optimal matching rate.
  Functional forms: $g(e)=\log(1+e)$, $K(e)=e^2/2$, $t=1$.
  The threshold for overinvestment is $\bar\alpha(\rho)=2(1-\rho)/[3(1+\rho)]$.}
\label{tab:numerical}
\smallskip
\begin{tabular}{cccccccc}
\toprule
$\alpha$ & $\rho$ & $\bar\alpha(\rho)$ & $e^N$ & $e^S$ & $e^N/e^S$ & $s^*$ & Regime \\
\midrule
"""

for alpha, rho, label in scenarios:
    r = compute_example(alpha, rho, beta, kappa, t)
    ratio = r['e_N'] / r['e_S'] if r['e_S'] > 0 else float('inf')
    regime_str = r['regime'].lower()
    latex += (f"  {r['alpha']:.1f} & {r['rho']:.1f} & {r['bar_alpha']:.3f} & "
             f"{r['e_N']:.4f} & {r['e_S']:.4f} & {ratio:.2f} & "
             f"{r['s_star']:+.3f} & {regime_str} \\\\\n")

latex += r"""\bottomrule
\end{tabular}
\end{table}
"""

print(latex)

# Save LaTeX table separately
with open("table1_numerical.tex", "w", encoding="utf-8") as f:
    f.write(latex)
print("LaTeX table saved to table1_numerical.tex")
