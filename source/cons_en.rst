.. _Cons:

Consumer Demand
---------------

Foundations of microeconomics start with how consumers behave. We might want to predict what a consumer is likely to do in a given situation. We might want to make sense of observed behavior. The theory will appear simplistic. But from this simple theory, we will be able to predict pretty well behavior in certain situations. Refinements exist, in particular to allow consumers to be more *humans*, have biases, cognitive limitations, emotions. 

.. figure:: /images/distribution_conso.jpeg
   :scale: 100
   :align: center

Preferences
+++++++++++

**Preferences are defined over baskets of goods and services**

-  Basket: vector of quantities :math:`x = (x_1, x_2,\cdots,x_n)`.

-  For any baskets :math:`A` and :math:`B`, preferences dictate which one is prefered. 

-  Preferences are just like wishlists. They ignore prices and resources. 

-  Preference relations are denoted
   :math:`\succ,\succeq,\sim`.

**Important assumptions about preferences**

Assumptions (or axioms as they are called) on preferences are necessary to yield a theory of how consumers behavior. These axioms yield predictions. Among the most important we have that they should be: 

*Exhaustive*

For any two baskets A and B, either the consumer:

-  prefers **always** A to B (:math:`A\succ B`)

-  prefers **always** B to A (:math:`B\succ A`)

-  is indifferent between A and B (:math:`A \sim B`)

Is it restrictive?

-  Yes, e.g.: ice cream vs. soup (one prefers ice cream in summer but soup in winter). 

-  But we can accomodate: include circumstances in the preferences (the season)

-  Baskets are now (ice cream, summer), (ice cream, winter, (soup, winter), (soup, summer). The preference relation may now be stable and exhaustive. 

*Transitivity*



Given three baskets A, B, C such that :math:`A\succ B`, :math:`B \succ C`, then if transitivity holds he also prefers A to C (:math:`A \succ C`).

This assumption appears logical. But it sometimes fail. In particular when uncertainty is present. Yet, we will keep it as it is very important for what follows. 

*Non-satiation*

In its simplest form, this assumptions implies that

-  If A has the same quantity of each good as basket B, but stricly more of one good, then :math:`A \succ B`.

-  Weaker version (:math:`A \succeq B`,indifference or preference) is reasonable. 

-  Putting labels on goods so non-satiation makes sense: goods are typically labelled as desirable (air quality instead of pollution).  

It is  not practical to use wishlists to model behavior. For example, how do we predict how consumers react to price changes using a wish list? We will want to get closer to marginal analaysis to make this more practical. 

Finally, it is important to note that preferences are very different across consumers.  `Falk et al. (2018) <https://academic.oup.com/qje/article/133/4/1645/5025666>`_ have analyzed this heterogeneity in 76 countries. 


Indifference Curves
+++++++++++++++++++

One of the first tool we can construct is indifference curves. 

For any two goods :math:`X,Y`:

-  Starting from a basket :math:`(X_0,Y_0)`, find combinations of :math:`(X,Y)` such that consumer is indifferent between :math:`(X,Y)` and
   :math:`(X_0,Y_0)`

-  In the plane (:math:`X,Y`), higher indifference curves indicate a preference.  

Proposition: If transitivity holds, indifference curves cannot cross.

.. figure:: /images/indif.png
   :scale: 25%
   :align: center

*Exercise A*: Show that this last proposition is correct. 

**Marginal Rate of Substitution (MRS)**

These indifference curves contain more information than we think ...

-  For a basket :math:`(X_0, Y_0)`, MRS of :math:`X` in terms of 
   :math:`Y`: Quantity of good  :math:`Y` the consumer is willing to sacrifice to increase :math:`X` by one unit.

-  Marginal value the consumer puts on :math:`X` in terms of quantity of good :math:`Y`.

-  Corresponds to the slope at
   :math:`(X_0,Y_0)`.

**Convexity of indifference curves**

If the quantity of :math:`X` increases, how does the MRS for :math:`X` changes?

It decreases generally. This implies convex indifference curves. Even if there is non-satiation, we generally accept that the intensity of preferences decreases as more of a good is consumed.  

Utility
+++++++

Indifference curves allow us to move away from wish lists to a function. On an indifference curve, each basket gives the same level of satisfaction to the consumer (he is indifferent). Let's fix that level to some arbitrary number, called utility. Jumping from one indifference curve to another changes the level of satisfaction. Hence, indifference curves are like level curves on a topological map, they do not cross.  The main insight is that we can construct a function :math:`U(X,Y)` which represent these preferences. The value of this function is ordinal, it allows to rank the different indifference curves. It is only this order that counts. 

Utility function: assigns a value to each basket. :math:`U` represents these preferences if :math:`A \succ B \Rightarrow U(A) > U(B)` and :math:`U(A) > U(B)   \Rightarrow A \succ B` for any two baskets. 

This has a number of implications. The main one is that there are many utility functions that represent the same preferences... 

If :math:`f` is a stricly increasing transformation (function) and :math:`U` represents some preferences, then :math:`V(X) = f(U(X))` represents the same preferences.

   .. math:: U(X) > U(Y) \iff f(U(X)) > f(U(Y))

In other words, the value attached to utility does not have a real interpretation, it is the ranking of baskets trough the level of these utility levels which matters.

Example: :math:`U(X,Y) = \log X + \log Y` and :math:`V(X,Y) = XY` represent the same preferences. 

*Exercise B*: Show that :math:`U` and :math:`V` if this example have the same preferences by finding the transformation :math:`V=f(U)`.


How to find the MRS from utility?

-  Two goods, :math:`X`, :math:`Y`. Preferences are represented by :math:`U(X,Y)`

-  e.g. :math:`U(X,Y) = \log X + \log Y`

MRS of :math:`X`:

-  How much :math:`Y` should one sacrifice to gain :math:`X`

-  Formally: if we increase :math:`X` by :math:`\Delta X`: what is the change :math:`\Delta Y` which maintains indifference?


We can use total differentiation:

.. math::

   \begin{aligned}
   dU = \frac{\partial U}{\partial X}dX + \frac{\partial U}{\partial Y}dY\end{aligned}

Set :math:`dU = 0`. Then

.. math::

   \frac{dY}{dX}\bigg\rvert_{dU=0} = -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y}

Budget Constraint
+++++++++++++++++

Until now, the consumer has available all baskets and he has preferences over those. In practice, he is limited by the resources he has, each time he has to purchase goods, at some price. Hence, those actions have an opportunity costs. 

-  One cannot spend more than income (or wealth) :math:`I`

-  | Two goods :math:`X`, :math:`Y`: Constraint:
     :math:`p_X X + p_Y Y \leq I`. This constraint determines what is available given :math:`I` and prices. 

-  | Setting to equality, we can solve for :math:`Y` in terms of :math:`X`:
     :math:`Y = \frac{I - p_X X}{p_Y}`
   | The relative price between :math:`X` et :math:`Y` holding the budget constant is:

     .. math:: \frac{dY}{dX} = -\frac{p_X}{p_Y}

Buying a unit of :math:`X` implies a sacrifice of :math:`\frac{p_X}{p_Y}` units of :math:`Y`. It is the opportunity cost of :math:`X` in terms of :math:`Y`. 


.. figure:: /images/budget_cons.png
   :scale: 75
   :align: center

   In the space :math:`(X,Y)`, the budget line defines all possible allocation. Those above are not feasible. Those on the line or below are feasible. 


**Normalization**

-  The budget constraint remains the same if we multiply prices and income by the same constant :math:`\lambda`.

-  One can buy the same goods. Hence, currencies do not impact the budget constraint. Only purchasing power and relative prices do. 

-  Therefore we will sometimes set :math:`p_Y = 1`. Then :math:`Y = I - p_X X`. :math:`p_X`
   is in terms of the quantity of :math:`Y` (numéraire) and idem pour :math:`I`.

Only relative prices matter. 

*Exercice C*: Show that the budget constraint does not change if we multiply prices and income by :math:`\lambda>0`.


Consumer choice
+++++++++++++++

-  The constraint is a given and therefore fixed. The consumer can pick on which indifference curve he wants to be and where on that curve. It seems natural to predict that he will want to pick the feasible basket which maximizes his utility. 

-  He can't go on an indifference curve above the budget line. 

-  Those allocations below the budget line cannot be optimal if we have non-satiation. He has money to spare and could spend it on goods which provide (marginal) utility. 

-  The indifference curve that touches on the constraint (tangent)
   gives the highest feasible level of utility. 

.. figure:: /images/choice_cons.png
   :scale: 75
   :align: center

   The points A, C et D are possible given the constraint. Therefore, point B can be elimited even if the MRS (slope at  B) is close to the price ratio. Point D can also be elimited because the consumer does not spend all his budget. He can jump on a higher indifference curve by increasing consumption of each good. Bundles A and C spend exhaust the budget. But C is not optimal. In absolute terms, the MRS is larger than the opportunity cost (price ratio) of consuming another unit of X. Therefore, she can increase X and reduce Y yielding higher utility. Point A is optimal: MRS is equal to the price ratio. 

**Direct approach**

The problem is

-  Maximize :math:`U(X,Y)` given the constraint
   :math:`p_X X+ p_YY = I`

Step 1: Substitute the constraint

-  If buys :math:`X` can consume 
   :math:`Y(X) = \frac{I - p_X X}{p_Y}`

-  Utility now function of :math:`X` only: :math:`V(X) = U(X,Y(X))`


Step 2: Maximize unconstrained

-  Look at first order condition (FOC)

The FOC is:


   .. math:: \frac{dV}{dX} = 0 \iff \frac{dU}{dX} + \frac{dY}{dX}\frac{dU}{dY} = 0

   .. math:: \iff \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}

MRS  equal to relative price comes out naturally as FOC. 

*Exercise D*: Find demands for :math:`u(x,y) = XY` under the constraint :math:`p_X X + p_Y Y \le I`.



As an alternative, we can set up the Lagrangian:

.. math::

   L(X,Y,\lambda) = U(X,Y) - \lambda (p_X X + p_Y Y - I)

The constrained problem is therefore :math:`\max_{X,Y,\lambda} L(X,Y,\lambda)`. The FOCs are

.. math::

   U'_X(X,Y) - \lambda p_X = 0 \\
   U'_Y(X,Y) - \lambda p_Y = 0 \\
   p_X X + p_Y Y = I

Taking the ratio of the first two FOC (after sending price terms to rhs), we get:

.. math::

   \begin{aligned}
   \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y} \\
   p_X X + p_Y Y = I\end{aligned}

Hence, MRS equal to price ratio and budget constraint met are the two conditions for an optimum. 

*Exercice E*: Find demands for :math:`u(X,Y) = XY` using the Lagrangian.


Demand functions :math:`X^*(p_X,p_Y,I)` and :math:`Y^*(p_X,p_Y,I)` are called Marshallian demands (`Alfred Marshall <https://fr.wikipedia.org/wiki/Alfred_Marshall>`_).

Indirect utility
++++++++++++++++

Indirect utility :math:`V(p_X,p_Y,I)` is the maximum level of utility the consumer can reach with prices :math:`(p_X,p_Y)` and income :math:`I`,

.. math:: V(p_X,p_Y,I) = \max_{X,Y} \{ u(X,Y) : p_X X + p_Y Y \le I\}.

Now a number of key points can be made about this function. The first is that the Lagrange multiplier has an interpretation: 

By definition,

.. math:: V(p_X,p_Y,I) = U(X^*,Y^*) - \lambda(p_X X^* + p_Y Y^*-I)

Hence, the derivative with respect to :math:`I` is

.. math:: V_I(p_X,p_Y,I) = U_X X_I^* + U_Y Y_I^* - \lambda (p_X X_I^* + p_Y Y_I^*-1)

where I subindices denote partial derivatives and we omit arguments for brievety. We can collect terms to get 

.. math:: V_I(p_X,p_Y,I) = (U_X - p_X \lambda) X_I^*(p_X,p_Y,I) + (U_Y - p_Y \lambda) Y_I^*(p_X,p_Y,I) + \lambda 

Now from the FOC to the Lagrangian, the first and second terms are zero at the optimum (:math:`U_X - p_X \lambda=0` and :math:`U_Y - p_Y \lambda=0`), yielding 

.. math:: V_I(p_X,p_Y,I) =  \lambda 

The marginal utility of income in a static consumer choice problem is the Lagrange multiplier. An important mathetimatical note: the result above where the two terms involving the FOC cancel out is due to a well-known theorem in constrained optimization: the envelop theorem. We will refer to it a few times. In words, it states that when evaluating the derivative of the objective function at the optimum with respect to one of the exogeneous variables (say a price or income), one does not need to look at re-optimization (the fact that the optimal decisions change). Only the enveloppe matters: how the function changes directly as a function of the exogeneous variables. The logic is simple: Given a derivative looks at a very small change, the induced change to the optimal solution has an effect on the objective function that is small and zero by the FOC. This only works for small changes. 

Roy Identity
++++++++++++

Given the indirect utility function :math:`V(p_X,p_Y,I)` we can retrieve demand functions using:

.. math:: X^*(p_X,p_Y,I) = -\frac{\partial{V(p_X,p_Y,I)}/\partial{p_X}}{\partial{V(p_X,p_Y,I)}/\partial{I}}

*Exercice G*: Show that this is true using the envelop theorem.

Consumer Demand Example 
+++++++++++++++++++++++

See this example in Python for a special utility function that is often used in practice: the CES (Constant Elasticity of Substitution)

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/drive/1ANuye-BnoZAL2rPBFN7rYNsXEDBOWBrW?usp=sharing
