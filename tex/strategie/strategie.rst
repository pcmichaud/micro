Itinerary
~~~~~~~~~

**Until now**

-  Consumer choice

-  Risk and time

-  Measuring welfare

-  Exchange

-  Production

**This class: Strategic Behavior of Firms**

-  Monopoly

-  Cournot Oligopoly

-  Price Discrimination

Monopoly
========

Monopoly: Price Manipulation

**First Welfare Theorem**

-  The market is Pareto efficient.

-  Firms take the price as given: they do not internalize the impact of
   their choice of production on price (*price taker*).

-  Is this a good assumption?

**Perfect competition**

-  A large number of firms

-  All small in size

-  The production of each has a small effect on total production
   :math:`\Rightarrow` fixed price reasonable

-  e.g.: market for meat, cereals, coffee... But oil, diamonds?

Behavior of the Firm **Setup**

-  Good :math:`X` and the *numéraire* :math:`M`.

   Utility is quasi-linear :math:`U(X,M) = V(X) + M`,

   :math:`V(X)` concave, :math:`V'(0) = + \infty`

-  Endownment :math:`I_0` of :math:`M`, :math:`X` produced by a single
   firm, price :math:`p` (price of X since price of :math:`M` normalized
   to one).

-  The firm produces :math:`X` with a cost function :math:`C(X)`. Assume
   :math:`C'(0) = 0`

**Exercise A** Find the equilibrium price if the firm is a *price taker*
for :math:`V(X) = \sqrt{X}` and :math:`C(X) = X^2`

Strategic Price Manipulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The firm correctly anticipates that increasing its supply may lower
   the price on the market.

-  The firm picks :math:`X` so it maximizes

   .. math:: \Pi = p(X)X - C(X)

-  FOC yields

   .. math:: \frac{d\Pi}{dX} = 0 \iff p'(X)X + p(X) = C'(X)

-  Produces :math:`X_{PM}` such that
   :math:`p(X_{PM}) + p'(X_{PM}) X_{PM} = C'(X_{PM})`

-  marginal price-effect + infra-marginal price-effect = marginal cost.
   The infra marginal effect captures the impact of expanding production
   on the value from existing production.

Strategic Price Manipulation (II)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Exercise B** Find the equilibrium price if the firm is strategic for
:math:`V(X) = \sqrt{X}` and :math:`C(X) = X^2`. Compare graphically to
the case when the firm is price-taker.

**Exercise C** : In the exercise above, find an expression for the
equilibrium price as a function of the price elasticity of demand.

.. _monopoly-1:

Monopoly
~~~~~~~~

-  At optimal production :math:`X_{PM}`

   .. math:: p(X_{PM}) + p'(X_{PM})X_{PM} = C'(X_{PM})

   Given, :math:`p'(X_{PM})<0`, then :math:`p(X_{PM}) > C'(X_{PM})`.

-  The monopoly fixes production at a price higher than marginal cost.

-  If production of a firm has no impact on the price, it produces
   :math:`X_{PT}` s.t.

   .. math:: p(X_{PT}) = C'(X_{PT})

-  When the firm internalizes its effect on the price (has market
   power), it produces :math:`X_{PM}` such that

   .. math:: p(X_{PM}) + p'(X_{PM})X_{PM} > C'(X_{PM})

-  This implies :math:`X_{PM} < X_{PT}`.

.. _monopoly-2:

Monopoly
~~~~~~~~

A (artificial) monopoly is inefficient:

-  The monopoly makes profits. Those profits are given by:

   .. math:: \Pi_{PM} = (p(X_{PM}) - p(X_{PT}) X_{PM}

   . The price taker does not make profits.

-  Those profits reduce consumer surplus by the same amount. So no total
   welfare loss from this transfer.

-  The monopoly imposes a welfare loss because units
   :math:`X_{PT}>X_{PM}` have :math:`V'(X)-C'(X)>0`.

**Exercise D**: Show the profits and the rents in the graph done for
Exercise B.

Oligopoly
=========

.. _oligopoly-1:

Oligopoly
~~~~~~~~~

-  Oligopolies are markets where a (small) number of firms produce a
   good. Duopolies are a special case with two firms.

-  Duopoly: Two identical firms produce quantities :math:`X_A` and
   :math:`X_B`

-  Representative consumer with :math:`U(X,M) =V(X) + M` and

   .. math:: V(X) = D_0 X - \frac{\alpha}{2} X^2

-  Costs given by :math:`C_A(X) = C_B(X)= c \times X`

**Inverse demand**

-  :math:`P(X) = V'(X) = D_0 - \alpha X`

What should we compare with?

**Counterfactual is efficient production (Pareto sense)**

-  Pick :math:`X` such that marginal cost is equal to marginal valuation

   .. math::

      \begin{aligned}
       &\iff& c = D_0 - \alpha X \\ &\iff& X_{Pareto} = \frac{D_0 - c}{\alpha} \end{aligned}

**In comparison, the monopoly**

-  Maximizes

   .. math:: \Pi(X) =  P(X) X - c X = (D_0- \alpha X) X - c X

-  Produces

   .. math:: X_{Mon} = \frac{D_0 - c}{2\alpha} = \frac{1}{2} X_{Pareto}

Cournot Competition – Two firms **Best response curves (BR)**

-  Two identical firms

-  If firm :math:`B` produces :math:`X_B`, what is the optimal
   production :math:`X_A` of firm :math:`A`?

-  Profit

   .. math:: \Pi_A = P \times X_A - C(X_A) = [D_0 - \alpha(X_B + X_A)]X_A - C(X_A)

-  FOC is

   .. math:: D_0 -   \alpha(X_B + X_A) - \alpha X_A - c  = 0

-  Best response (BR) at :math:`X_B` is

   .. math:: X_A = \frac{D_0 -  c - \alpha X_B}{ 2 \alpha} = \frac{D_0 - c}{2\alpha} - \frac{1}{2}X_B

Cournot Competition – Duopoly

-  If firm :math:`A` produces :math:`X_A`, best response from :math:`B`
   is to pick

   .. math:: X_B =   \frac{D_0 -  c - \alpha X_A}{ 2 \alpha} = \frac{D_0 - c}{2\alpha} - \frac{1}{2}X_A

**Recall from Intro to Microeconomics principles of Game theory**

-  **Nash Equilibrium:** No firm can benefit from a unilateral change on
   her part.

-  If :math:`X^*_A` and :math:`X^*_B` are equilibrium quantities, we
   must have that :math:`A` best responds in an optimal way to
   :math:`X^*_B` and firm :math:`B` best responds in an optimal way to
   :math:`X^*_A`

Equilibrium We have the best response functions

-  

   .. math:: X^*_A =  \frac{D_0 - c - \alpha X_B^*}{ 2 \alpha} \quad and \quad  X^*_B = \frac{D_0 - c -  \alpha X_A^*}{2 \alpha}

-  Since symmetric firms: :math:`X^*_A = X^*_B = X^*` gives

   .. math:: X^*_A = X^*_B = X^* = \frac{D_0 - c}{3\alpha}

-  Total production

   .. math:: 2 X^* = \frac{2}{3} \frac{D_0 - c}{\alpha}

Some Exercises

| **Exercise E**: Plot the two best response functions in the space
  (:math:`X_A,X_B`). Plot the equilibrium outcome.
| **Exercise F**: Starting from :math:`X_A = \frac{D_0 - c}{2\alpha}`,
  :math:`D_0=10,c=1,\alpha=1`, show how applying the best response
  functions of each firm sequentially would eventually lead you to the
  equilibrium outcome.
| **Exercise G**: Assume firm A has marginal cost :math:`c_A` and firm
  B, :math:`c_B`, with :math:`c_A=2>c_B=1`. Also assume
  :math:`D_0=10,\alpha=1`. Find the equilibrium quantities of each firm.

Cournot Competition – Increasing Competition **With more firms**

-  N identical firms :math:`F_1,F_2,\cdots,F_N`

-  Given :math:`X_2, X_3, \cdots, X_N`, firm :math:`F_1` produces
   :math:`X_1` to maximize

   .. math:: \Pi_1 = [D_0 - \alpha(X_1 + X_2 + \cdots + X_N)]X_1 - c\times X_1

-  Best response is

   .. math:: X_1 = \frac{D_0 - c - \alpha[X_2 + X_3 + \cdots + X_N]}{ 2 \alpha}

**Exercise H**: Show how one obtains the best response function in the
example above.

Cournot competition

**Equilibrium with many firms**

-  :math:`X_1` optimal given :math:`X_2, X_3, \cdots, X_N`

-  :math:`X_2` optimal given :math:`X_1,X_3,X_4, \cdots, X_N`

-  :math:`\cdots`

-  :math:`X_N` optimal given :math:`X_1,X_2, \cdots, X_{N-1}`

-  :math:`N` equations, exploiting symmetry yields

   .. math:: X_1^* = X_2^* = \cdots = X_N^* = \frac{D_0 - c}{(N+1) \alpha}

-  Total production

   .. math:: \frac{N}{N+1} \frac{D_0 -c}{\alpha}

Competition

**Firm with no market power**

-  A firm with no market power picks :math:`X_0` such that price equals
   marginal cost :math:`p(X) = c`

**Competition**

-  If one firm acts as monopoly, total production is

   .. math:: X^{Tot}_1 = \frac{1}{2}\frac{D_0-c}{\alpha} \quad  and \quad \textrm{price } p_1 = \frac{1}{2} D_0  + \frac{1}{2} c

-  If two firms, total production

   .. math:: X^{Tot}_2 = \frac{2}{3}\frac{D_0-c}{\alpha} \quad  et \quad \textrm{price } p_2  = \frac{1}{3}D_0 +\frac{2}{3}c

-  If :math:`N` firms , total production

   .. math:: X^{Tot}_N = \frac{N}{N+1}\frac{D_0-c}{\alpha} \quad  and \quad  p_N = \frac{1}{N}D_0 +\frac{N}{N+1}c

Interesting Result **With many firms, cournot competition converges to
perfect competition (price taking behavior):**

-  When :math:`N` is large, :math:`p(X_N) \to c`,

   .. math:: \lim_{N \to \infty} \left( \frac{1}{N}D_0 +\frac{N}{N+1}c \right) = 0 + c = c

-  In other words, price equals marginal cost.

-  Firms cannot affect the price when too many firms in the market. They
   become price taker and the rents from strategic behavior are
   eliminated.

Bertrand Price Competition
==========================

Competing on Price

-  In some markets, capacity is illimited. Think of retail.

-  Firms compete on the price they post (think of a flea market).

-  Competition among a few sellers is best modelled using Bertrand price
   competition

-  Take :math:`N` identical firms with marginal cost
   :math:`c_i=c \quad \forall i=1,...,N`.

-  | First assume, :math:`p_i = c \quad \forall i`.

-  If one firm :math:`j` deviates and posts :math:`p_j>c`, she sells
   nothing (looses her market share). If she posts, :math:`p_j<c`, she
   makes a loss.

-  Equilibrium (nash) solution: :math:`p_i=c \quad \forall i`. As
   opposed to Cournot, Bertrand yields a competitive market outcome
   (Pareto optimal)!

-  Key assumption: Consumer can observe prices of all competitors
   without cost. Good homogeneous.

Bertrand Price Competition

-  Cournot better suited for things that take time to build, capacity
   (e.g. airplanes, etc).

-  In some markets, capacity is almost illimited and quantity adjusted
   very quickly. e.g. retail.

-  Firms compete on the price they post (think of a flea market with
   many kiosks close to each other selling the same thing).

-  Competition among a few sellers is best modelled using Bertrand price
   competition

Bertrand Price Competition

-  Take :math:`N` identical firms with marginal cost
   :math:`c_i=c \quad \forall i=1,...,N`.

-  | First assume, :math:`p_i = c \quad \forall i`.

-  If one firm :math:`j` deviates and posts :math:`p_j>c`, she sells
   nothing (looses her market share). If she posts, :math:`p_j<c`, she
   makes a loss.

-  Equilibrium (Nash) solution: :math:`p_i=c \quad \forall i`. As
   opposed to Cournot, Bertrand yields a competitive market outcome
   (Pareto optimal)!

-  Key assumption: Consumer can observe prices of all competitors
   without cost. Good homogeneous.

Other Important Topics The field of industrial organization deals with
strategic decisions of firms in different market settings.

Other topics of interest are:

-  Product differentiation (monopolistic competition)

-  Collusion

-  Price discrimination

These are covered in courses like *Comprendre la concurrence* (BAA) and
*Industrial Organization* (M.sc).
