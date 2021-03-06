.. raw:: latex

   \frame{\titlepage}

.. raw:: latex

   \frame{\tableofcontents}

.. _section-1:

Roadmap
~~~~~~~

**Up until now**

-  Consumer choice

-  Price and income effects

-  Risk and time

-  Measuring welfare and well-being

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**This class: Exchanges**

-  Market equilibrium in an exchange economy

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Coming up**

-  Production decisions in firms

-  Strategic behaviour of firms

-  Auctions

Market equilibrium
==================

Exchange Economy
~~~~~~~~~~~~~~~~

**Context**

-  Consider a situation with two consumers (1 and 2) and two goods
   (:math:`X` and :math:`Y`)

-  Utility fuctions :math:`U_1(X,Y)` and :math:`U_2(X,Y)`

-  Each consumer has an endowment of each good,
   :math:`B_1^e = (X_1^e,Y_1^e)` and :math:`B_2^e = (X_2^e,Y_2^e)`.

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Examples**

-  2 farmers, one has an endowment of potatoes and the other has an
   endowment of livestock.

-  Two countries: Country 1 has a petroleum endowment and Country 2 has
   a machinery endowment

-  Where do these endowments come from? Nature (resources) or production
   (consumer goods, machinery ...). We will talk about this further in
   the "Production" class.

.. _market-equilibrium-1:

Market Equilibrium
~~~~~~~~~~~~~~~~~~

**Individual demand**

-  Consumer 1 choses to consume :math:`(X_1^c, Y_1^c)`

-  Given the prices :math:`p_X` and :math:`p_Y`, the budget constraint
   is

   .. math:: p_X X_1^c + p_Y Y_1^c  =  p_X X_1^e + p_Y Y_1^e

-  Prices will be determined in equilibrium.

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Normalization**

-  Two unknown prices :math:`p_X` and :math:`p_Y`. Only relative price
   matters: the budget constraint can be written as follows :

   .. math:: X_1^c + \frac{p_Y}{p_X} Y_1^c  =   X_1^e + \frac{p_Y}{p_X} Y_1^e

-  Let’s define the relative price as :math:`p = p_Y/p_X`

Market Equilibrium – II
~~~~~~~~~~~~~~~~~~~~~~~

**Definition**

-  Individual demand: :math:`\max U_1` subject to
   :math:`X_1^c + p Y_1^c  =   X_1^e + p Y_1^e`

-  We obtain :math:`X_1^c(p)` and :math:`Y_1^c(p)`

-  :math:`p^*` is an equilibrium price only if at :math:`p^*` demand is
   equal to supply

   .. math::

      X_1^c(p^*)+X_2^c(p^*) = X_1^e + X_2^e \quad
      and \quad Y_1^c(p^*)+Y_2^c(p^*) = Y_1^e + Y_2^e

-  :math:`X_1^c(p^*) -
   X_1^e =X_2^e - X_2^c(p^*)  \;` is the amount of :math:`X` that is
   exchanged

-  si :math:`X_1^c - X_1^e < 0`, consumer 1 is a net supplier of
   :math:`X`.

Important Assumptions

-  Competitive market: consumers are **price takers**

-  All sold goods are homogeneous (identical) and percieved the same way
   by both the buyer and the seller

-  The utility of consumer 1 does not depend on the actions of the other
   consumer: **no externalities**

An Example
~~~~~~~~~~

**Context**

-  :math:`U_1(X,Y) =
   U_2(X,Y) = \log X + \alpha \log Y`

-  Price :math:`p_X= 1`, :math:`p_Y = p`.

-  Endowment :math:`X_1^e, Y_1^e, X_2^e, Y_2^e`

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Equilibrium**

-  Solution of individual demands:

   .. math::

      X_1^c =
      \frac{1}{1+\alpha}(X_1^e + p Y_1^e) \quad and \quad Y_1^c =
      \frac{\alpha}{1+\alpha}\frac{X_1^e + p Y_1^e}{p}

-  Market equilibrium for :math:`X`

   .. math::

      X_1^c(p) + X_2^c(p) = X_1^e + X_2^e
      \Rightarrow p = \alpha \frac{X_1^e + X_2^e}{Y_1^e + Y_2^e}

-  | Notice that the market for :math:`Y` has also reached an
     equilibrium at :math:`p`.
   | **Question:** only one unkown variable and two equations?

Walras’ Law
~~~~~~~~~~~

**One unkown variable but two equations**

-  No problem: equilibrium on one market implies equilibrium on the
   other

-  Budget constraint:

   .. math::

      X_1^c + p Y_1^c  =   X_1^e + p Y_1^e \quad and \quad
      X_2^c + p Y_2^c  =   X_2^e + p Y_2^e

   \ If we add one constraint to the other

   .. math::

      [X_1^c + X_2^c] + p [Y_1^c + Y_2^c] = [X_1^e + X_2^e] + p
      [Y_1^e + Y_2^e]

    An equilibrium in :math:`X` implies

   .. math::

      p
      [Y_1^c + Y_2^c]  = p [Y_1^e + Y_2^e] \Rightarrow  Y_1^c + Y_2^c = Y_1^e +
      Y_2^e

What determines the price?
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Compared static**

-  How :math:`p` varies with :math:`\alpha` (importance of the good
   :math:`Y`) and the aggregated quantities of :math:`X` and :math:`Y` ?

-  If :math:`\alpha` :math:`\nearrow` then :math:`p=p_Y`
   :math:`\nearrow`: since the total supply of :math:`Y` is fixed, when
   demand for :math:`Y` increases, the price must adjust to maintain the
   equilibrium.

-  If :math:`Y_1^e + Y_2^e
   \nearrow` then :math:`p=p_Y` :math:`\searrow`: the price must fall to
   sell the endowment.

-  If :math:`X_1^e + X_2^e \nearrow` then :math:`p = p_Y`
   :math:`\nearrow` since :math:`Y` has become rarer relative to
   :math:`X`

Pareto-efficient allocation
===========================

The Edgeworth Box
~~~~~~~~~~~~~~~~~

-  We draw the space of possible allocations in an Edgeworth box

-  The initial endowment is a point in this space

**Exercise A**: Show the endowment :math:`(x^e_1,y_1^e) = (50,20)` and
:math:`(x^e_2,y_2^e)=(20,50)` in an Edgeworth box.

.. _pareto-efficient-allocation-1:

Pareto-Efficient Allocation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  A point on the Edgeworth box where indifference curves cross is not
   Pareto-optimal.

-  We can define the core of this point as all the allocations that are
   a Pareto improvement.

-  When the core is empty, we get an allocation that is Pareto-efficient
   : this implies that the indifference curves are tangent.

-  The Pareto Frontier (or Pareto Front) is the curve that shows all the
   allocations that are Pareto-efficient.

Calculating an optimum

We can seek to maximize the welfare of an agent by keeping the other’s
fixed and respecting the resource constraints:

.. math::

   \begin{aligned}
   \max_{X_1,Y_1,X_2,Y_2} u(X_1,Y_1) \end{aligned}

 subject to:

.. math::

   \begin{aligned}
   u(X_2,Y_2)\ge \overline{u}_2 \\
   X_1 + X_2 \le X_e \\
   Y_1 + Y_2 \le Y_e\end{aligned}

A Few Exercises
~~~~~~~~~~~~~~~

**Exercise B**: Find the Pareto-optimal allocation for the utility
functions :math:`u_1` and :math:`u_2` strictly positive and concave,
:math:`u_j = \sqrt{x_j y_j}` for consumers :math:`j=1,2`, using the
Lagrangian method.

**Exercise C**: Find the Pareto-optimal allocation for the utility
functions :math:`u_j = \sqrt{x_j y_j}` for consumers :math:`j=1,2` with
the total endowments :math:`x_e = 128` and :math:`y_e=32` if
:math:`\overline{u}_2=48`.

**Exercise D**: In Exercise C, is the allocation :math:`(64,28,64,4)`
optimal? If it isn’t, find a Pareto improvement that can be made in the
core.

Market Equilibrium in an Edgeworth box

-  The budget constraint is given by the endowments and indicates which
   allocations are possible at price :math:`p`.

-  A market equilibrium implies that the :math:`MRS` are equal to the
   price ratio.

Exchange is Better Than Autarky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Property:**

-  Consider the equilibrium price: :math:`p^*` and the quantities
   consumed by consumer 1: :math:`X^c_1 = X^c_1(p^*)` and
   :math:`Y^c_1 = Y^c_1(p^*)`

-  We have :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Why?**

-  At :math:`p^*`, the basket :math:`B^e_1 = (X^e_1,Y^e_1)` is available
   and consumer 1 chooses :math:`B^c_1=(X^c_1, Y^c_1)`

-  This implies that :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`

-  Note: If :math:`U` concave and :math:`(X^c_1, Y^c_1) \neq (X^e_1,
   Y^e_1)` then :math:`U_1(X^c_1, Y^c_1) > U_1(X^e_1, Y^e_1)`

Welfare theorems
================

Propeties of a Market Equilibrium (I) – 1st Theorem of Welfare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1st theorem of welfare**

-  A market equilibrium is always Pareto-optimal.

-  In an allocation that is Pareto-efficient we cannot make a consumer
   better off without making another consumer worse off

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Why?**

-  At the equilibrium allocation
   :math:`X^c_1(p^*),Y^c_1(p^*),X^c_2(p^*),Y^c_1(p^*)` the indifference
   curve of consumer 1 is tangent to the budget constraint, and tangent
   to the indifference curve of consumer 2

-  This implies that the allocation is Pareto-efficient.

The 2nd Theorem
~~~~~~~~~~~~~~~

**The 2nd theorem of welfare**

-  We can achieve any Pareto-efficient allocation we desire through
   market equilibrium if we redistribute the initial endowments

-  This requires the ability to impose taxes (lump-sum payments)

-  Often called a decentralized resource allocation

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**Why?**

-  Suppose there’s no corner solution

-  At any allocation :math:`(X_1^*,Y_1^*)` (and consequent value for
   :math:`X_2^*,Y_2^*`) the indifference curve of the two consumers are
   tangent.

-  Consider this tangence line.

-  Any of the allocations on that line results in a market equilibrium
   :math:`(X^*,Y^*)`.

**Exercise E**: Find the endowment transfer and the price, starting from
:math:`(64,28,64,4)`, which give the optimal allocation found in D.

Market Efficiency
~~~~~~~~~~~~~~~~~

**The 1st and 2nd theorems establish that**

-  The market is efficient

-  If for one reason or another we want another allocation, we can
   achieve it by redistributing the resources and letting the market
   take its course

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

**An important result: Decentralized efficiency**

-  A market equilibrium requires only that agents know their own
   preferences

-  There is no need for a central planner that knows everyone’s
   preferences

-  We naturally obtain a Pareto-efficient result

-  Hayek’s take: markets are information aggregators

-  Planned economies lose this information (not to mention that it is
   costly to find preferences of every citizen).

Epilogue – II – limits
~~~~~~~~~~~~~~~~~~~~~~

**These two theorems are interesting, but they rest on important
hypotheses**

-  Competitive markets (price takers)

-  Goods are homogeneous (we know what we’re buying)

-  No externalities

-  We can impose lump-sum taxes (for the 2nd theorem)

.. raw:: latex

   \medskip 

.. raw:: latex

   \pause

The general equilibrium theory had quite an impact on economics: think
about how we understand financial markets or macroeconomics.

A bit of history
================

History of the General Equilibrium Theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: latex

   \centering

|image|

.. _history-of-the-general-equilibrium-theory-1:

History of the General Equilibrium Theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

They came from very different backgrounds (Arrow, economics), (Debreu,
mathematics). Düppe (2017) tells the story of how this project came to
be.

.. raw:: latex

   \centering

.. figure:: invitation.png
   :alt: `Duppe (2017), Journal of History of Economic
   Thought <https://www.cambridge.org/core/journals/journal-of-the-history-of-economic-thought/article/div-classtitlearrow-and-debreu-de-homogenizeddiv/761E76D5A52C948615066F502277D9DD>`__

   `Duppe (2017), Journal of History of Economic
   Thought <https://www.cambridge.org/core/journals/journal-of-the-history-of-economic-thought/article/div-classtitlearrow-and-debreu-de-homogenizeddiv/761E76D5A52C948615066F502277D9DD>`__

.. |image| image:: ad1954.png

