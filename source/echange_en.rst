Exchange
--------

Why should consumers exchange goods? by which means? Barter, using markets, or naming someone who will dictate who consumes what? Which mechanism will do best? 

.. figure:: /images/barter.jpeg
   :scale: 100


There are welfare gains to exchanging. Exchange can only be beneficial because no exchange is always possible. We can achieve best results using various mechanisms if certain conditions are respected. We can start in a simple setting which does not restrict the generality of what we will see. 

Consider a situation with two consumers (1 and 2) and two goods
   (:math:`X` and :math:`Y`)

-  Utility functions :math:`U_1(X,Y)` and :math:`U_2(X,Y)`

-  Each consumer has a dotation of each good,
   :math:`B_1^e = (X_1^e,Y_1^e)` and :math:`B_2^e = (X_2^e,Y_2^e)`.

Examples:

-  Two farmers, one with an endowment of potatoes, the other with cattle.

-  Two countries: Country 1 has lots of gas, the other has industrial machinery. 

-  Two consumers on kijiji or Ebay: one has a canoe, the other a laptop.

Where do these endownments come from? For the moment, let's assume they inherited them. 

Market Equilibrium
++++++++++++++++++

The market allows exchange to take place. In terms of modelling, markets can be summarized by a price vector (if there are many goods and a single relative price if two). There needs to be a legal system that enforces transactions, but that is not apparent directly.

If each consumer has an endownment and individual demand as a function of prices, we can easily find the market equilibrium. Think of a setting where there is no production, like `Kijiji <https://www.kijiji.ca/>`_.  

For individual demands,

Consumer 1 picks :math:`(X_1^c, Y_1^c)`, his marshallian demands. 

- Given prices :math:`p_X` and :math:`p_Y`, the budget constraint of each agent is

   .. math:: p_X X_1^c + p_Y Y_1^c  =  p_X X_1^e + p_Y Y_1^e

-  Prices and determined in equilibrium. 


Note again that it is only relative prices that matter for choices. We have two unknown prices, :math:`p_X` and :math:`p_Y` but only the ratio matters. The budget constraint can be rewritten  

   .. math:: X_1^c + \frac{p_Y}{p_X} Y_1^c  =   X_1^e + \frac{p_Y}{p_X} Y_1^e

Without loosing information, denote :math:`p = p_Y/p_X`, the relative price of :math:`Y` in terms of :math:`X`. We could also define the relative price as :math:`p = p_X/p_Y`! We just have to be consistent. 

How do we find the equilibrium price?

- Step 1: Individual demands: We are looking for 

.. math::
   \max_{X_1,Y_1} \left[U_1 : X_1^c + p Y_1^c  \leq   X_1^e + p Y_1^e\right]

We get :math:`X_1^c(p)` and  :math:`Y_1^c(p)` using a lagrangian.

-  Step 2: The price :math:`p^*` is an equilibrium price if at :math:`p^*`  aggregate demand is equal to aggregate supply. We are looking for :math:`p^*` such that 

   .. math::
      X_1^c(p^*)+X_2^c(p^*) = X_1^e + X_2^e \quad
      and \quad Y_1^c(p^*)+Y_2^c(p^*) = Y_1^e + Y_2^e

The quantity of :math:`X` exchanged is given by :math:`X_1^c(p^*) - X_1^e =X_2^e - X_2^c(p^*)`. If :math:`X_1^c - X_1^e < 0`, consumer 1 is a net supplier of :math:`X` (consumer 2 is buying).

Important assumptions:

-  The market is competitive: Consumers take prices as given. They are **price takers**.

-  All goods are homogeneous (identical) and perceived in the same way by buyers and sellers. 

-  Utility of each consumers does not depend on actions of others: **no externalities**

Let's look at an example. Consider :math:`U_1(X,Y) = U_2(X,Y) = \log X + \alpha \log Y`. Fix  :math:`p_X= 1`, and so :math:`p_Y = p`. Endownments are given by :math:`(X_1^e, Y_1^e, X_2^e, Y_2^e)`. The solution for demands is given by:

   .. math::
      \begin{aligned}
      X_1^c &=
      \frac{1}{1+\alpha}(X_1^e + p Y_1^e) \\ 
      Y_1^c &=
      \frac{\alpha}{1+\alpha}\frac{X_1^e + p Y_1^e}{p}
      \end{aligned}

Market equilibrium for :math:`X` implies that

   .. math::

      X_1^c(p) + X_2^c(p) = X_1^e + X_2^e
      \Rightarrow p = \alpha \frac{X_1^e + X_2^e}{Y_1^e + Y_2^e}

The market for :math:`Y` is also in equilibrium at :math:`p`. Why is only one market necessary to find the equilibrium price?

Walras' Law
+++++++++++

We have one unknown, :math:`p` but two equilibrium equations... Market equilibrium on one market actually implies equilibrium on the other. To see this, consider the two budget constraints: 

   .. math::

      X_1^c + p Y_1^c  =   X_1^e + p Y_1^e \quad and \quad
      X_2^c + p Y_2^c  =   X_2^e + p Y_2^e

If we add them up, we get: 

   .. math::

      [X_1^c + X_2^c] + p [Y_1^c + Y_2^c] = [X_1^e + X_2^e] + p[Y_1^e + Y_2^e]

An equilibrium for :math:`X` implies that

   .. math::

      p[Y_1^c + Y_2^c]  = p [Y_1^e + Y_2^e] \Rightarrow  Y_1^c + Y_2^c = Y_1^e + Y_2^e

`Walras' Law <https://fr.wikipedia.org/wiki/L%C3%A9on_Walras>`_ enables us to focus on one market to find the equilibrium relative price. We can generalize to more than two goods. 

What determines the equilibrium price?
++++++++++++++++++++++++++++++++++++++

The equilibrium price is a function of preferences of agents and endownments. In the example,


.. math::
   p^* = \alpha \frac{X_1^e + X_2^e}{Y_1^e + Y_2^e}

The price of :math:`Y` increases with the relative preference for :math:`Y`, given by :math:`\alpha`. Supply being fixed, if demand is increasing, the equilibrium price has to increase to equate supply and demand (as demand decreases in the price). If the good :math:`Y` is scarce (endownments are small  :math:`Y_1^e + Y_2^e`), the equilibrium price has to increase as well. 

The price is a signal of preferences and the relative scarcity of goods. Does this market equilibrium yield the highest  welfare possible for agents? To make a judment on allocations, we need to side-track to define what is an optimal allocation of resources in a context that is independent of whether or not we use markets.

Pareto Optimal Allocations
++++++++++++++++++++++++++

We have seen that a Pareto improvement is possible when none of the consumers looses but at least one gains. When there is no Pareto improvement possible, we say that an allocation is Pareto optimal or efficient. We can apply this to allocations in an exchange economy.  

To do that, we need **Edgeworth boxes**, a useful tool. Think of it as a coordinate system that will allow to plot in 2D allocations when in fact there are 4 dimensions, quantities of goods :math:`X` and :math:`Y` for consumers 1 and 2. To do that, we will use the fact that there exist a fixed quantity of goods X and Y in an exchange economy, endownments.  Exercice A will get you to construct an Edgeworth Box. 

.. figure:: /images/endow.png
   :scale: 35

   The box has dimensions equal to the total endownment of goods :math:`X` and :math:`Y`. 


**Exercise A**: Show the endownments :math:`(x^e_1,y_1^e) = (50,20)` and
:math:`(x^e_2,y_2^e)=(20,50)` in an Edgeworth Box.


A number of observations can be made from an Edgeworth Box.

First, a point in the box where two indifference curves cross cannot be Pareto optimal. Why? Because we can define a core, a set of points who are Pareto improvements from the point where the indifference curves cross. Hence, the allocation cannot be aPareto optimal allocation. 

.. figure:: /images/core.png
   :scale: 35

   Allocation E cannot be optimal: Indifference curves cross. Allocation A is a Pareto improvement. The core is the zone between the two indifference curves. 

When the core is empty, the allocation is Pareto optimal. This implies that a Pareto optimal allocation is one where the indifference curves are tangent.

The *contract curve* is the curve that links all Pareto optimal allocations. Indeed there are many Pareto optimal allocations. The *Pareto frontier* is the curve in the space :math:`(U_1,U_2)` which indicates all Pareto optimal allocations in terms of utility levels. 

.. figure:: /images/contract.png
   :scale: 35

.. figure:: /images/pareto-frontier.png
   :scale: 50

Allocations A and C are Pareto optimal. They are found on the contract curve and on the Pareto frontier. But allocation B is not optimal because indifference curves cross. It is therefore below the Pareto frontier.

How do we compute a Pareto optimal allocation? We can use constrained optimization. The most efficient way is going to be to maximize utility of one agent, keeping utility of the other at some level (hence looking for Pareto improvements), and meeting the constraints for resources of each goods.

.. math::

   \begin{aligned}
   \max_{X_1,Y_1,X_2,Y_2} u(X_1,Y_1) \end{aligned}

subject to :

.. math::

   \begin{aligned}
   u(X_2,Y_2)\ge \overline{u}_2 \\
   X_1 + X_2 \le X_e \\
   Y_1 + Y_2 \le Y_e\end{aligned}

We construct a Lagrangian with three constraints: 

.. math::
   \begin{split}
    U(X_1,Y_1) + \lambda(U(X_2,Y_2)-\overline{U}_2) \\ 
   - \pi_X (X_1+X_2 - X_e) - \pi_Y (Y_1+Y_2-Y_e) \end{split}


There are 7 FOCs and 3 multipliers. The following exercises will help you practice this technique. 

**Exercise B**: Find the Pareto optimal allocation for utility functions :math:`u_1` and :math:`u_2` strictly positive and concave, :math:`u_j = \sqrt{x_j y_j}` for consumers :math:`j=1,2`, using the Lagrangian method.

**Exercise C**: Find the Pareto optimal allocation if endownments are :math:`x_e = 128` and :math:`y_e=32` if
:math:`\overline{u}_2=48`.

**Exercise D**: In exercise C, is the allocation :math:`(64,28,64,4)`
Pareto optimal? If it is not, find a Pareto improvement in the core.


**Market Equilibrium in an Edgeworth Box**

The budget constraint depends on endownments and shows allocations which are possible at price :math:`p`. A market equilibrium implies that the  :math:`MRS` is equal to the price. Since the price is the same for each consumer, it implies that the :math:`MRS` of each consumer are equal in a market equilibrium.


.. figure:: /images/price-equilibrium.png
   :scale: 50

   A market equilibrium is given by A. It occurs starting from endownments represented at point E with the relative price :math:`p = p_Y/p_X` a line with slope :math:`-p_X/p_Y = -1/p`. 


Exchange and Welfare
++++++++++++++++++++

Consider the equilibrium price: :math:`p^*` and quantities consumed by consumer 1: :math:`X^c_1 = X^c_1(p^*)` and :math:`Y^c_1 = Y^c_1(p^*)`. We have that :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`

Why? at price math:`p^*` the endownment :math:`B^e_1 = (X^e_1,Y^e_1)` is available but the consumer prefers :math:`B^c_1=(X^c_1, Y^c_1)`. So preferences reveal that :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`. 


Weflare Theorems
++++++++++++++++

**First Theorem**

-  A market equilibrium is Pareto optimal. 

If an allocation is Pareto optimal, we can't improve the welfare of one consumer without decreasing that of others. 

Why this result? With the market equilibrium :math:`X^c_1(p^*),Y^c_1(p^*),X^c_2(p^*),Y^c_1(p^*)` indifference curves are tangent to the budget line. If they are tangent, it means that we have a Pareto optimal allocation. 

**Second Theorem**

-  We can reach any Pareto optimal allocation using a market equilibrium if we allow redistribution of resources (endownments). 

This requires the possibility of implementing lump-sum taxes on endownments or confiscating. The Pareto optimal allocation is decentralized using a market equilibrium with redistribution.

Why does it work?

For any allocation :math:`(X_1^*,Y_1^*)`, and corresponding values for :math:`(X_2^*,Y_2^*)`,  indifference curves are tangent. With the market line (budget line) drawn, we can redistribution endownments to get on the budget line and make the market equilibrium feasible. The budget line, determined by the price, is a tool to get to :math:`(X^*,Y^*)`. But this is not feasible from any allocation of endownments. 


.. figure:: /images/transfer-equilibrium.png
   :scale: 50

   The Pareto optimum A cannot be reached from :math:`E_0`. But a Transfer of :math:`T_X` of good :math:`X` from consumer 2 to consumer 1 allows to reach endownment situation  :math:`E_1`, from which we can reach Pareto optimal allocation A with a market equilibrium at price :math:`p`. 

**Exercise E**: Find the transfer of endownments and the market equilibrium price, starting from :math:`(64,28,64,4)`, which gives the allocation found in exercise D.


Market Efficiency
+++++++++++++++++

The two theorems establish that

-  The market is efficient 

- If we want another Pareto optimal allocation using markets, we can obtain it by redistribution of endownments. 

This is a result which is very important in economics: the decentralized market economy allows to get what the planner would have obtained without sacrifying freedom for agents to do what they want and have private property. 

The market economy only requires that agents know their own preferences. According to  `Hayek <https://fr.wikipedia.org/wiki/Friedrich_Hayek>`_, markets, when they function well, aggregate all the necessary information on the scarcity of goods  and preferences. 

Limitations
+++++++++++

These results are encouraging, but they rest on important assumptions: 

-  Markets are competitive (price takers)

-  Goods are homogeneous (we know what we purchase)

-  There are no externalities

-  We can impose  *lump-sum* taxes (for the second theorem)

General equilibrium theory, of which the exchange economy is the foundation, has had an enduring impact in both micro and macro, in particular for modelling financial markets. Many, including governments, use these models to make projections and analyze interventions. 

History 
+++++++

|image|

.. |image| image:: /images/ad1954.png

`Kennet Arrow <https://fr.wikipedia.org/wiki/Kenneth_Arrow>`_ and `Gérard Debreu <https://fr.wikipedia.org/wiki/G%C3%A9rard_Debreu>`_ are generally credited for showing the existence of general equilibrium. They came from different backgrounds and were interested in the question for different reasons. Düppe (2017) documents how this project came about and the tensions that arose between the two men as they wrote this important paper. 

.. figure:: /images/invitation.png

   `Duppe (2017), Journal of History of Economic
   Thought <https://www.cambridge.org/core/journals/journal-of-the-history-of-economic-thought/article/div-classtitlearrow-and-debreu-de-homogenizeddiv/761E76D5A52C948615066F502277D9DD>`__

Python Example
++++++++++++++


|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Equilibre%20Echange.ipynb



