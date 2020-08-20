.. _section-1:

Roadmap
~~~~~~~

**Up until now**

-  Consumer choice

-  Price and income effects

-  Measuring welfare and well-being

-  Risk and intertemporal choices

-  Exchange economies

**This class:**

-  Production economy

**Coming up**

-  Strategic behaviour of firms

-  Auctions

Overview **Objective**

-  Introducing firms and production in an exchange economy

**Main takeaway**

-  A production economy is very similar to an exchange economy

-  Firms are agents, just like consumers

**Methodology**

-  Calculating the firms’ demand

-  Calculating the firms’ supply

-  Calculating the consumers’ demand

-  The price is determined at equilibrium

   .. math:: total \;\; demand  = total \;\; supply

The Firm’s Decisions
====================

A Firm’s Decisons

**Inputs and outputs**

-  A firm is caracterized by the production function :math:`F`

-  Given the inputs, :math:`F` determines the output

**Example: an input and an output**

-  e.g. An iron mine — input: labor :math:`L`, output: iron
   :math:`Y = F(L) = \sqrt{L}`

-  The firm’s constraint: given an input, it can only produce a certain
   level of output

Example (cont.) **Two inputs, one output**

-  Inputs: Iron Ore (:math:`I`), Coal (:math:`C`) — Output: Steel
   (:math:`S`)

-  :math:`S(I,C)  = I^{\alpha}C^{\beta}\quad \quad` (with
   :math:`\alpha + \beta <1`)

Production Functions: MRTS

Consider the production function :math:`Y = F(X,Z)`. Take the total
differential:

.. math:: dY = F'_X(X,Z)dX + F'_Z(X,Z)dZ

Set :math:`dY = 0`, We obtain the Marginal Rate of Technical
Substitution:

.. math:: MRTS = \frac{dZ}{dX} = -\frac{F'_X(X,Z)}{F'_Z(X,Z)}

The slopes are isoquant in the space :math:`(X,Z)`.

**Exercise A**: Find the MRTS for :math:`Y=X^{\alpha} Z^{\beta}`

Production Functions: Returns to Scale

A production function has returns to scale that are :

-  constant: if :math:`F(X,Z)` is homogenous of degree 1

-  increasing: si :math:`F(X,Z)` is homogenous of a degree larger than 1

-  decreasing: si :math:`F(X,Z)` is homogenous of a degree smaller than
   1

**Exercise B**: Consider the function
:math:`Y=F(X,Z)=A X^\alpha Z^\beta`. What are the returns to scale of
that function?

Cost Minimization

Given a level of production :math:`Y`, what is the best choice of
inputs?

.. math:: \min_{X,Z} \{ p_X X + p_Z Z : F(X,Z) \ge Y \}

Set the lagrangian:

.. math:: L(X,Z,\mu) = p_X X + p_Z Z + \mu(Y - F(X,Z))

The FOC are:

.. math:: p_X - \mu F'_X(X,Z) = 0

.. math:: p_Z - \mu F'_Z(X,Z) = 0

.. math:: F(X,Z) = Y

Cost Minimization

We can simplify this:

.. math:: \frac{p_X}{p_Z} = \frac{F'_X(X,Z)}{F'_Z(X,Z)}

.. math:: F(X,Z) = Y

The first condition: :math:`MRTS =` Relative Price

**Exercise C**: Find the conditional demands for
:math:`Y=X^{1/2} Z^{1/4}`.

Conditional Demands

The solution gives the conditional demand functions for inputs:

.. math:: X^*(p_X,p_Z,Y),Z^*(p_X,p_Z,Y)

.

What are the properties of these functions?

-  Homogenous of degree zero in :math:`(p_X,p_Z)`

-  Symmetry:
   :math:`\frac{\partial X^*(p_X,p_Z,Y)}{\partial p_Z} = \frac{\partial Z^*(p_X,p_Z,Y)}{\partial p_X}`

-  Negativity: :math:`\frac{\partial X^*(p_X,p_Z,Y)}{\partial p_X}<0`.

Cost Functions

By substituting the conditional demands, we obtain the cost function:

.. math:: C(p_X,p_Z,Y) = p_X X^*(p_X,p_Z,Y) + p_Z Z^*(p_X,p_Z,Y)

Properties:

-  Non-decreasing in :math:`(Y,p_X,p_Z)`

-  Homogenous of degree 1 in :math:`(p_X,p_Z)`

-  Concave in :math:`(p_X,p_Z)`

**Exercise D**: Find the cost function for :math:`Y=X^{1/2} Z^{1/4}`.

Relation Between Costs and Demands

An interesting result is Sheppard’s Lemma:

.. math:: \frac{\partial C(p_X,p_Z,Y)}{\partial p_X} = X^*(p_X,p_Z,Y)

**Exercise E**: Show that this works for finding :math:`X^*` for the
production function :math:`Y=X^{1/2} Z^{1/4}`.

Relation Between Costs and Demands

By using the envelope theorem, we can also see that

.. math:: \frac{\partial C(p_X,p_Y,Y)}{\partial Y} = \mu

:math:`\mu` is therefore the marginal cost at the optimum.

**Exercise F**: Find marginal cost for :math:`Y=X^{1/2} Z^{1/4}`.

If the production function has returns to scale that are:

-  Constant: :math:`C(p_X,p_Z,Y)` is linear in :math:`Y`

-  Increasing: :math:`C(p_X,p_Z,Y)` is concave in :math:`Y`

-  Decreasing: :math:`C(p_X,p_Z,Y)` is convex in :math:`Y`

The Firm as an Agent **Profit maximization**

-  Objective function: Profits = Value of outputs - costs of inputs

   .. math:: \Pi = V - C

-  Decision: The firm must choose its inputs to maximize profits

**Example**

-  e.g. Given an input :math:`X` and an output :math:`Y = F(X)`

   .. math::

      C(X) = p_X X\;;\quad V(Y) = p_Y
      Y\;;\quad \Pi(X) = p_Y F(X) - p_XX

**Exercise G** Suppose :math:`F(X) = \sqrt X`, find the demand for
:math:`X`

Supply and Demand of a Price-Taking Firm (I) **One input, one output**

-  Input :math:`X`, output :math:`Y =
   F(X)`

-  Profit :math:`\Pi(X) = p_Y F(X) -
   p_XX`.

-  Suppose that the firm wishes to produce

-  At the optimum the FOC is respected

   .. math::

      p_Y F'(X) - p_X = 0 \iff F'(X) =
      \frac{p_X}{p_Y}

-  The equation that allows us to find the demand :math:`X^*` gives the
   supply :math:`Y^* = F(X^*)`

**Exercise H** Suppose :math:`F(X) = \sqrt X`, find the supply function
of :math:`Y`.

Cost-minimization and Profit maximization

Multiple inputs, Two-step approach:

-  Minimize cost for choice of :math:`(X,Z)`.

-  Maximize profits over :math:`Y` using cost function (function of
   :math:`Y`).

**Exercise I** For :math:`Y=X^{1/2} Z^{1/4}`, find the supply function
of :math:`Y`.

Production Economy
==================

A Production Economy with a Firm and Two Goods (I)

**Context**

-  2 goods :math:`X` and :math:`Y`

-  Firm has a production function :math:`Y = F(X)`.

**Firm’s behaviour**

-  Given the prices :math:`p_Y` and :math:`p_X` the firm maximizes
   profits

   .. math:: \Pi(X) = p_Y F(X) - p_X X

-  Gives the firm’s demand :math:`X^{F,d}(p_X,p_Y)`;

   The firm’s supply :math:`Y^{F,s}(p_X,p_Y)`;

   ...and the profits :math:`\Pi`

A Production Economy with a Firm and Two Goods (II)

**The consumer’s behaviour**

-  2 consumers C1 et C2

-  The consumers have preferences represented by :math:`U_1(X, Y)` and
   :math:`U_2(X,Y)`

-  | Consumer 1 has an endowment :math:`X^{C1,e},
     Y^{C1,e}`
   | Consumer 2 has an endowment :math:`X^{C2,e}, Y^{C2,e}`

-  Both consumers have stocks :math:`\rho_{1}` and
   :math:`\rho_2 = 1- \rho_1` in the firm.

A Production Economy with a Firm and Two Goods (III) **The consumer’s
behaviour**

-  Consumer 1 must solve

   .. math::

      \begin{aligned}
       &&\max_{X,Y} U_1(X,Y) \\ &\textrm{s.t.} &\textrm{Cost of consumption} = \textrm{Total wealth} \\ &&  p_{X} X +  p_{Y}Y = p_{X}
      X^{C1,e}+ p_{Y}Y^{C1,e} + \rho_{1}\Pi\end{aligned}

-  Gives consumer :math:`1`\ ’s demand: :math:`X^{C1,d}(p_X,p_Y)` and
   :math:`Y^{C1,d}(p_X,p_Y)` (same idea for 2)

A Production Economy with a Firm and Two Goods (IV)

**Market equilibrium**

-  Numéraire: normalize :math:`p_{X} = 1` and :math:`p_{Y} = p`.

-  Given :math:`p`, we can find the demand :math:`X` and :math:`Y` for
   each consumer, the demand of :math:`X` for the firm and the supply of
   :math:`Y` by the firm.

-  The market for the good :math:`X` is at equilibrium at price
   :math:`p` if and only if

   .. math::

      \begin{aligned}
        \textrm{Total demand of } X &=&
      \textrm{Total supply of } X  \\ \iff X^{C1,d} + X^{C2,d} + X^{F,d} &=&
      X^{C1,e} + X^{C2,e}  \end{aligned}

-  The equilibrium prices are prices such that all markets are at
   equilibrium.

A Production Economy with a Firm and Two Goods (V) **Example**

-  :math:`F(X) =  \log(1+X)`

-  :math:`U_1(X,Y) =
   U_2(X,Y) = \log X + \alpha \log Y`

-  :math:`X^{C1,e} = 2` and :math:`X^{C2,e} =
   Y^{C1,e} = Y^{C2,e} = 0`

-  :math:`\rho_1 =0` and :math:`\rho_2 = 1`

-  price :math:`p_X = 1`, :math:`p_Y = p`

**Firm’s behaviour**

-  Profit maximization:

   .. math::

      \max_X p\log(1+X) - X\;\; \Rightarrow \;\; X^{F,d}
      = p- 1 \;\; et \;\; Y^{F,s} = \log p

-  Profit :math:`\Pi = p \log p - p
   +1`

A Production Economy with a Firm and Two Goods (VI) **Consumer’s
behaviour**

-  Given the income :math:`I`

   .. math::

      \max_{X,Y}
      \log X + \alpha \log Y \quad s.t.\;\; X + pY = I

-  | Income of consumer 1: :math:`I_1 = 2`
   | Income of consumer 2: :math:`I_2 = \Pi =  p \log
     p - p +1`

-  | Demand of consumer 1:

     .. math::

        X^{C1,d} = \frac{1}{1+\alpha}
        I_1 \;\; and \;\; Y^{C1,d} = \frac{\alpha}{1+\alpha} \frac{I_1}{p}
   | Demand of consumer 2:

     .. math::

        X^{C2,d} = \frac{1}{1+\alpha} I_2 \;\; and
        \;\; Y^{C2,d} = \frac{\alpha}{1+\alpha} \frac{I_2}{p}

A Production Economy with a Firm and Two Goods (VII) **Market
Equilibrium**

-  A market equilibrium for :math:`X`:

   .. math:: X^{F,d} + X^{C1,d} + X^{C2,d} = X^{C1,e} + X^{C2,e} = 2

-  gives

   .. math::

      \begin{aligned}
       & & p-1 + \frac{1}{1+\alpha}2 + \frac{1}{1+\alpha}(p\log p - p +1 ) = 2 \\
      &\iff& \alpha p +p\log p = 3 \alpha\end{aligned}

-  Equation describes the price :math:`p^*`.

-  Show that at :math:`p^*`, the market for :math:`Y` is also at
   equilibrium.

A Production Economy with a Firm and Multiple Goods **Methodology**

-  Given the prices, profit maximization gives firm demands and firm
   supply (profits)

-  Given the prices, endowments and stock (of the firms) distributions
   calculate the income and demand of consumers

-  For each good, maket equilibrium

   .. math::

      \textrm{total supply} =
      \textrm{total demand}

-  Given a system of equations: the solution gives us the equilibrium
   prices

See the Production Equilibrium Notebook for an example.

The Two Fundamental Theorems of Welfare Economics **Environment**

#. All agents are price-takers (firms and consumers; no monopoly)

#. Goods are homogeneous (uniform quality)

#. | Consumers’ preferences depend only on their own consumption
   | Firm decisions have no impact on other firms or consumers (no
     externalities)

**1st Theorem of Welfare Economics**

-  In a market equilibrium, the allocation of goods between consumers is
   Pareto-efficient.

**2nd Theorem of Welfare Economics**

-  Any Pareto-optimal allocation can be obtained as a market equilibrium
   with the use of endowment transfers.
