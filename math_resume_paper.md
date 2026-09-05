# 論文の数学的構造と証明の完全解説レジュメ（詳細版・式番号対応表付き）

本資料では、対象論文において用いられているすべての数式（式番号1〜20等）について、論文中の式番号と対応させつつ、その導出過程や Appendix の証明を「計算の途中式を一切省かず」、大学1年生でも確実に追えるように詳細に解説します。

---

## 1. モデルの基本設定 (Model Setup)

### 1-1. 消費者と効用

論文中の **式 (1)** は消費者の効用関数を表します。
$$ U_f(x) = V + \bar{q} + q_f - p_f - t \, d_f(x) \quad \text{--- (1)} $$
（$f \in \{A, B\}$、$d_A(x)=x, d_B(x)=1-x$）

### 1-2. 知覚品質の分解（真の品質 vs 説得的要素）

論文中の **式 (2)** は、需要をシフトさせる「知覚品質 $q_f$」を、社会厚生に寄与する「真の品質 $r_f$」と「説得的要素」に分解する式です。
$$ r_f \equiv \alpha q_f, \quad q_f - r_f = (1-\alpha) q_f \quad \text{--- (2)} $$
ここで、$\alpha \in [0,1]$ は**厚生関連シェア（welfare-relevant share）**を表します。

### 1-3. R&Dとスピルオーバー（知覚品質の生産）

論文中の **式 (3)** は、両自治体の投資 $e_1, e_2$ が知覚品質をどう生み出すかを示しています。
$$ q_A = g(e_1) + \rho g(e_2), \quad q_B = g(e_2) + \rho g(e_1) \quad \text{--- (3)} $$

- $\rho \in [0, 1)$: **知識のスピルオーバー（Knowledge spillovers）**。

### 1-4. 自治体の目的関数（局所的な社会厚生）と社会厚生関数

論文中の **式 (4)** は、各自治体が最大化する局所的な目的関数です。企業利益から（補助金を加味した）R&Dコストを引いたものです。
$$ W_i^{\mathrm{loc}} = \pi_{f(i)}(p_A, p_B; q_A, q_B) - (1-s)K(e_i) \quad \text{--- (4)} $$

論文中の **式 (5)** は、マッチング補助率 $s$ が取り得る値の範囲（自治体の負担が非負）を示しています。
$$ s \le 1 \quad \text{--- (5)} $$

論文中の **式 (6)** は、中央の計画者が考える「全体としての社会厚生」です。説得成分は除外し、真の品質 $r$ のみをカウントし、そこからすべての輸送コストと全地域のR&Dコストを引きます。
$$ W^{\mathrm{soc}} = \int_0^1 r_{\sigma(x)} \,dx - \int_0^1 t \, d_{\sigma(x)}(x) \,dx - c - K(e_1) - K(e_2) \quad \text{--- (6)} $$
（ここで $\sigma(x)$ は消費者 $x$ が購入する企業）

---

## 2. 第2段階：価格競争 (Stage 2: Price Competition)

### 2-1. 無差別な消費者（市場の境界 $x^*$）: 式 (7) の導出

消費者にとって企業AとBの効用が等しくなる点 $x^*$ を求めます。式 (1) を用いて $U_A(x^*) = U_B(x^*)$ とします。
$$ V + \bar{q} + q_A - p_A - t x^* = V + \bar{q} + q_B - p_B - t (1-x^*) $$
両辺から $V + \bar{q}$ を消去します。
$$ q_A - p_A - t x^* = q_B - p_B - t + t x^* $$
$t x^*$ を右辺に、残りを左辺に移行してまとめます。
$$ q_A - q_B - p_A + p_B + t = 2t x^* $$
これを $2t$ で割ると、論文の **式 (7)** が得られます。
$$ x^*(p_A, p_B; q_A, q_B) = \frac{q_A - q_B - p_A + p_B + t}{2t} \quad \text{--- (7)} $$

論文中の **式 (8)** は、内部解の十分条件です。投資 $e_i \in [0, \bar{e}]$ の最大変動幅が $3t$ 未満なら、境界が $(0,1)$ の内側に収まることを示しています。
$$ (1-\rho)\{g(\bar{e}) - g(0)\} < 3t \quad \text{--- (8)} $$

### 2-2. 企業の均衡価格と需要 : 式 (9)〜(11) の導出（Proposition 1）

企業Aの利潤 $\pi_A$ の最大化を行います。需要は $D_A = x^*$ です。
$$ \pi_A = (p_A - c) \left( \frac{q_A - q_B - p_A + p_B + t}{2t} \right) $$
これを $p_A$ について積の微分（前微分$\times$後 ＋ 前$\times$後微分）します。
$$ \frac{\partial \pi_A}{\partial p_A} = 1 \cdot \left( \frac{q_A - q_B - p_A + p_B + t}{2t} \right) + (p_A - c) \cdot \left( \frac{-1}{2t} \right) = 0 $$
両辺に $2t$ を掛けます。
$$ q_A - q_B - p_A + p_B + t - p_A + c = 0 \implies q_A - q_B - 2p_A + p_B + t + c = 0 \quad (\text{企業A条件}) $$

企業Bについても同様に $\pi_B = (p_B - c)(1-x^*)$ を $p_B$ で微分して解くと、
$$ q_B - q_A - 2p_B + p_A + t + c = 0 \quad (\text{企業B条件}) $$

企業A条件と企業B条件の連立方程式を解きます。
引くと：$2(q_A - q_B) - 3(p_A - p_B) = 0 \implies p_A - p_B = \frac{2}{3}(q_A - q_B)$
足すと：$2t + 2c - (p_A + p_B) = 0 \implies p_A + p_B = 2t + 2c$
これらを足し引きして2で割ると、論文の均衡価格 **式 (9), (10)** を得ます。
$$ p_A^* = c + t + \frac{q_A - q_B}{3} \quad \text{--- (9)} $$
$$ p_B^* = c + t - \frac{q_A - q_B}{3} \quad \text{--- (10)} $$

これを式 (7) に代入すると、均衡需要 **式 (11)** が得られます。
$$ D_A^* = x^* = \frac{1}{2} + \frac{q_A - q_B}{6t}, \quad D_B^* = 1 - x^* = \frac{1}{2} - \frac{q_A - q_B}{6t} \quad \text{--- (11)} $$

### 2-3. 縮約形利潤 : 式 (12) の計算

知覚品質の差 $\Delta q \equiv q_A - q_B$ を導入し、利益率 $p_A^* - c$ と需要 $D_A^*$ を掛け算します。
$$ p_A^* - c = t + \frac{\Delta q}{3} = \frac{3t + \Delta q}{3} $$
$$ D_A^* = \frac{1}{2} + \frac{\Delta q}{6t} = \frac{3t + \Delta q}{6t} $$
$$ \pi_A^*(\Delta q) = (p_A^* - c) \cdot D_A^* = \left( \frac{3t + \Delta q}{3} \right) \cdot \left( \frac{3t + \Delta q}{6t} \right) = \frac{(3t + \Delta q)^2}{18t} $$
企業Bも同様に計算され、**式 (12)** が得られます。
$$ \pi_A^* = \frac{(3t + q_A - q_B)^2}{18t}, \quad \pi_B^* = \frac{(3t - q_A + q_B)^2}{18t} \quad \text{--- (12)} $$

---

## 3. 第1段階：分権的R&D競争 (Stage 1: Decentralized R&D)

### 3-1. 品質差分の式と1階条件 : 式 (13), (14) の導出

式 (3) から品質差を計算すると、論文の **式 (13)** になります。
$$ \Delta q \equiv q_A - q_B = (1-\rho)(g(e_1) - g(e_2)) \quad \text{--- (13)} $$

式 (4) の局所的厚生 $W_1^{\mathrm{loc}} = \pi_A^*(\Delta q) - (1-s)K(e_1)$ を $e_1$ で微分します。
チェインルール（合成関数の微分）を用います。
$$ \frac{\partial W_1^{\mathrm{loc}}}{\partial e_1} = \frac{\partial \pi_A^*}{\partial \Delta q} \cdot \frac{\partial \Delta q}{\partial e_1} - (1-s)K'(e_1) = 0 $$

式 (12) を微分して、$\frac{\partial \pi_A^*}{\partial \Delta q} = \frac{2(3t + \Delta q)}{18t} = \frac{3t + \Delta q}{9t}$ 。
式 (13) を微分して、$\frac{\partial \Delta q}{\partial e_1} = (1-\rho)g'(e_1)$ 。
これらを代入します。
$$ \frac{3t + \Delta q}{9t} \cdot (1-\rho)g'(e_1) - (1-s)K'(e_1) = 0 $$

対称均衡解（$e_1 = e_2 = e^N$）を想定すると $\Delta q = 0$ になるため、第1項の係数は $\frac{3t}{9t} = \frac{1}{3}$ になります。
$$ \frac{1}{3} (1-\rho)g'(e^N) - (1-s)K'(e^N) = 0 $$
移項すると、論文の分権的均衡の1階条件 **式 (14)** になります。
$$ (1-s)K'(e^N(s)) = \frac{1-\rho}{3} g'(e^N(s)) \quad \text{--- (14)} $$

### 3-2. 強凹性（Strict Concavity）の条件（Appendix B）

Appendix Bで示される、局所的厚生が上に凸であることの条件です。
1階微分の式をさらに微分し、積の微分法则を適用します：
$$ \frac{\partial^2 W_1^{\mathrm{loc}}}{\partial e_1^2} = \left[ \frac{1}{9t} \cdot (1-\rho)g'(e_1) \right] (1-\rho)g'(e_1) + \left[ \frac{3t + \Delta q}{9t} \right] (1-\rho)g''(e_1) - (1-s)K''(e_1) $$
$$ = \frac{(1-\rho)^2}{9t}\{g'(e_1)\}^2 + \frac{(1-\rho)(3t+\Delta q)}{9t}g''(e_1) - (1-s)K''(e_1) $$
$g'' \le 0$ のため、第2項は負になります。そのため、これが全体として常に負（強凹関数）である十分条件として：
$$ (1-s)K''(e_1) > \frac{(1-\rho)^2}{9t}\{g'(e_1)\}^2 $$
がAppendix Bの冒頭に記述されています。

---

## 4. 社会的最適 (The Social Optimum)

計画者（Planner）の最適化です。市場のシェアや輸送コストの積分を計算します。
論文の **式 (15)** は、対称性がない場合の境界点と需要の再定義です（式(7), (11)と同じ）。
$$ x^* = \frac{1}{2} + \frac{\Delta q}{6t}, \quad D_A^* = x^*, \quad D_B^* = 1 - x^* \quad \text{--- (15)} $$

輸送コストの積分は以下のように計算され、論文の **式 (16)** を導きます。
$$ \int_0^{x^*} t \cdot x \, dx + \int_{x^*}^1 t \cdot (1-x) \, dx = \frac{t}{2}(x^*)^2 + t \left[ x - \frac{1}{2}x^2 \right]_{x^*}^1 $$
$$ = \frac{t}{2}(x^*)^2 + t \left( \frac{1}{2} - x^* + \frac{1}{2}(x^*)^2 \right) = t \left( (x^*)^2 - x^* + \frac{1}{2} \right) = t \left( (x^* - \frac{1}{2})^2 + \frac{1}{4} \right) $$
ここで式 (15) より $x^* - \frac{1}{2} = \frac{\Delta q}{6t}$ なので代入して二乗します。
$$ = t \left( \frac{(\Delta q)^2}{36t^2} + \frac{1}{4} \right) = \frac{t}{4} + \frac{(\Delta q)^2}{36t} \quad \text{--- (16)} $$

### 社会的最適の FOC 導出 : 式 (17)

対称状態（$e_1 = e_2 = e^S \implies \Delta q=0$）での社会厚生を計算します。式(6) に代入します。
式 (3) より $q_A = q_B = (1+\rho)g(e^S)$、真の品質は $r = \alpha(1+\rho)g(e^S)$ なので積分してもそのままです。
輸送コストは式(16)に $\Delta q=0$ を入れて $\frac{t}{4}$ です。
$$ W^{\mathrm{soc}}(e^S) = \alpha(1+\rho)g(e^S) - \frac{t}{4} - c - 2K(e^S) $$

これを $e^S$ で微分し $=0$ と置きます。
$$ \alpha(1+\rho)g'(e^S) - 2K'(e^S) = 0 $$
$$ K'(e^S(\alpha)) = \frac{\alpha(1+\rho)}{2} g'(e^S(\alpha)) \quad \text{--- (17)} $$
これが論文の **式 (17)** です。

---

## 5. 過剰/過少投資の閾値とマッチング率

### 式 (18), (19) の導出

分散的均衡（式 14）と社会的最適（式 17）の係数を等値化することで、$e^N$ と $e^S$ が等しくなる条件を求めます。
式 (14)（補助金なし $s=0$ のとき）：$K'(e^N) = \frac{1-\rho}{3}g'(e^N)$
式 (17)：$K'(e^S) = \frac{\alpha(1+\rho)}{2}g'(e^S)$

両者の係数が一致するような $\alpha$ の境界線 $\bar{\alpha}(\rho)$ を計算し、**式 (18)** を得ます。
$$ \frac{1-\rho}{3} = \frac{\alpha(1+\rho)}{2} \implies \bar{\alpha}(\rho) \equiv \frac{2(1-\rho)}{3(1+\rho)} \quad \text{--- (18)} $$

中央政府がこの最適解を誘導するための補助金率 $s^*$ を導出します。
式 (14) から：$K'(e^N) = \frac{1-\rho}{3(1-s)}g'(e^N)$。これを式(17)の係数と等値化します。
$$ \frac{1-\rho}{3(1-s)} = \frac{\alpha(1+\rho)}{2} $$
$(1-s)$ について解きます。
$$ 1-s = \frac{2(1-\rho)}{3\alpha(1+\rho)} $$
ここで分子のかたまりに 先ほどの 式(18) の $\bar{\alpha}(\rho)$ を代入できます。
$$ 1-s = \frac{\bar{\alpha}(\rho)}{\alpha} \implies s^* = 1 - \frac{\bar{\alpha}(\rho)}{\alpha} \quad \text{--- (19)} $$
これが論文の **式 (19)** です。

---

## 6. Appendix D：2つの投入要素への一般化（式 (20)）

Appendixの最後では、$\alpha$ を内生の割合として明示的にモデル化しています。

- 真の研究開発：$q_i^R = r_i + \rho_R r_j$
- 宣伝活動：$q_i^M = m_i + \rho_M m_j$
自治体はコスト $\frac{k_R}{2}r_i^2 + \frac{k_M}{2}m_i^2$ のもとで局所厚生を最大化します。
式 (13), (14) のときと同様のチェインルールで $r_i$ と $m_i$ について最適化を解くと、
$$ k_R r^N = \frac{1-\rho_R}{3} \implies r^N = \frac{1-\rho_R}{3k_R} $$
$$ k_M m^N = \frac{1-\rho_M}{3} \implies m^N = \frac{1-\rho_M}{3k_M} $$

このとき、生み出された知覚品質全体に対する、研究開発が産んだ知覚品質の割合を $\alpha^N$ と定義します。
$$ \alpha^N = \frac{q_i^R}{q_i^R + q_i^M} = \frac{(1+\rho_R)r^N}{(1+\rho_R)r^N + (1+\rho_M)m^N} $$
先ほどの $r^N, m^N$ を代入します。
$$ \alpha^N = \frac{(1+\rho_R) \frac{1-\rho_R}{3k_R}}{(1+\rho_R) \frac{1-\rho_R}{3k_R} + (1+\rho_M) \frac{1-\rho_M}{3k_M}} $$

$(1+x)(1-x) = 1-x^2$ にして、分母分子に $3 k_R k_M$ を掛けて整理すると、**式 (20) に相当する** 内生化された厚生産生割合 $\alpha^N$ が得られます。（※ 論文本文Corollary 1に記載の式）
$$ \alpha^N = \frac{k_M(1-\rho_R^2)}{k_M(1-\rho_R^2) + k_R(1-\rho_M^2)} $$

また、この構造のもとで中央政府が純粋な研究開発 $r$ に付与すべき補助金率を $s_R^*$ と置くと、式 (19) の $\alpha=1$ のパターンと完全に一致するため、**式 (20)** （Proposition 6）が得られます。
$$ s_R^* = 1 - \frac{2(1-\rho_R)}{3(1+\rho_R)} = 1 - \bar{\alpha}(\rho_R) \quad \text{--- (20)} $$

以上で、論文中のすべての式（式 (1) 〜 式 (20)）および Appendix の数学的構造の完全な導出・対応が完了しました。
