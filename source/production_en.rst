Production
----------

In the exchange economy, endownments were given. In the real world, they do not fall from the sky. They are often produced. Often, goods are produced from other goods by firms. Firms are owned by consumers. Why do firms exist? `Ronald Coase <https://fr.wikipedia.org/wiki/Ronald_Coase>`_ proposed a simple explanation: firms are there to internalize transactions costs in order to produce goods.Without these organizations, difficult to produce at low cost things like laptops, furniture. There are returns to scale which makes it possible for firms to produce on a great scale at low cost. Organizations also promote innovation by bringing together people who make share ideas and develop new products and services. We will present how economists think of decisions make by firms in a production context. This will lead us back to general equilibrium.

Production Function
+++++++++++++++++++

We will think of a simple firm who produces an output from potentially multiple inputs. This process is represented by a production function :math:`F(\cdot)`. The production function can be estimated using econometric methods, in collaboration perhaps with engineers who know a lot about the production process.

**Example: one input and output**

-  e.g. Iron Ore Mine  — input: work  :math:`L`, output: iron
   :math:`Y = F(L) = \sqrt{L}`

The production function determines what is possible for the firm.

**Example: Two inputs, one output**

-  Inputs: Iron ore (:math:`I`), coal (:math:`C`) — Output: Steel
   (:math:`S`)

We could for example think of a function

.. math::
    S(I,C)  = I^{\alpha}C^{\beta}

With data on the quantity of steel produced, the quantity of iron ore and of coal used over time  :math:`t=1,...,T`, we can estimate parameters by considering the following transformation of the production function: 

.. math::
    \log S_t = \log A_t + \alpha \log I_t + \beta \log C_t + \epsilon_t

where :math:`A_t` is a total productivity factor (TFP) and :math:`\epsilon_t` is a noise term. Therefore :math:`\alpha` and :math:`\beta` can be estimated, under certain conditions regarding :math:`\epsilon_t` and the relationship with :math:`(I_t,C_t)`. 

Marginal Rate of Technical Substitution
+++++++++++++++++++++++++++++++++++++++

Suppose there is a shortage of input :math:`Z`. The director is asking you how much more :math:`X` will he need to compensate the loss of :math:`Z` while maintaining production of  production of :math:`Y` constant. 

Consider the production function :math:`Y = F(X,Z)`. Take the total differential:

.. math:: dY = F'_X(X,Z)dX + F'_Z(X,Z)dZ

The marginal productivity of each input is given by  :math:`F'_i(X,Z)` for :math:`i=X,Z`. It provides the production of  :math:`Y` that one obtains when we increase marginally one input  *keeing others fixed*. 

Fix :math:`dY = 0`. We obtain the **marginal rate of technical substitution**:

.. math:: MRST  = \frac{dZ}{dX} = -\frac{F'_X(X,Z)}{F'_Z(X,Z)}

Instead of indifference curves, we obtain isoquants in the space :math:`(X,Z)` which give the combinations of inputs that produce a given quantity of output (constant). The MRST is the slope of the isoquant.

It is the quantity of :math:`Z` that we can save if we increase  :math:`X` marginally. It is negative since the production function is generally positive in its inputs (positive marginal productivities).

**Exercise A**: Find the MRST for :math:`Y=X^{\alpha} Z^{\beta}`

Returns to scale
++++++++++++++++

The factory manager wishes to double production. He is asking you in which proportion he should increase his purchases of inputs. The marginal productivity is not useful for this purpose as it is a concept that looks at how much production increases when one input increases and the others are constant. Second, this is not a marginal change, since we are looking to double production. Turns out we can look at returns to scale of a production function. A function has returns to scale which are:

-  constant: if :math:`F(X,Z)` is homgeneous of degree 1

-  increasing: if :math:`F(X,Z)` is homgeneous of degree greater than 1.

-  decreasing: if :math:`F(X,Z)` is homogeneous of degree smaller than 1.

**Exercise B**: Consider the function
:math:`Y=F(X,Z)=A X^\alpha Z^\beta`. What are the returns to scale of this function?

Cost Minimization
+++++++++++++++++

Given a production level :math:`Y`, what is the best choice of inputs?

.. math:: \min_{X,Z} \{ p_X X + p_Z Z : F(X,Z) \ge Y \}

Write the lagrangian:

.. math:: L(X,Z,\mu) = p_X X + p_Z Z + \mu(Y - F(X,Z))

The FOCs are:

.. math:: p_X - \mu F'_X(X,Z) = 0

.. math:: p_Z - \mu F'_Z(X,Z) = 0

.. math:: F(X,Z) = Y

We can simplify to obtain:

.. math:: \frac{p_X}{p_Z} = \frac{F'_X(X,Z)}{F'_Z(X,Z)}

.. math:: F(X,Z) = Y

The first equation gives the optimal  *mix* of inputs. This mix has to be such that the :math:`MRST` is equal to the relative price of inputs. The relative price gives the cost, in units of :math:`Y` of a unit of :math:`X`. If this cost is smaller than the savings we make by increasing :math:`X`, we can increase :math:`X` and reduce costs. One can do this up to the point where :math:`MRST` is equal to the relative price of inputs. There is then no more savings to do, we have minimized costs!

The second constraint uses this optimal *mix* of inputs found with the first and pins the levels by using the fixed level of production :math:`Y`. The solution to this system of equations is a pair of conditional demand functions for inputs

.. math:: X(p_X,p_Z,Y)

and 

.. math:: Z(p_X,p_Z,Y)

We denote those as *conditional* because they depend on a fixed output level.

**Exercise C**: Find the conditional demand functions for 
:math:`Y=X^{1/2} Z^{1/4}`.

What are the properties of these functions?

-  They are homogeneous of degree zero in :math:`(p_X,p_Z)`

-  They are symmetric:
   :math:`\frac{\partial X(p_X,p_Z,Y)}{\partial p_Z} = \frac{\partial Z(p_X,p_Z,Y)}{\partial p_X}`

-  They depend negatively on own price: :math:`\frac{\partial X(p_X,p_Z,Y)}{\partial p_X}<0`.


Cost Functions
++++++++++++++

Substituting the conditional demands in the objective function, we get:

.. math:: C(p_X,p_Z,Y) = p_X X(p_X,p_Z,Y) + p_Z Z(p_X,p_Z,Y).

This function provides the minimum cost of producing a certain level of output.

Properties:

-  Non-decreasing in :math:`(Y,p_X,p_Z)`

-  Homogeneous of degree 1 in :math:`(p_X,p_Z)`

-  Concave in :math:`(p_X,p_Z)`

**Exercise D**: Find the cost function for :math:`Y=X^{1/2} Z^{1/4}`.

Sheppard Lemma 
++++++++++++++

An interesting result is that 

.. math:: \frac{\partial C(p_X,p_Z,Y)}{\partial p_X} = X^*(p_X,p_Z,Y)

This result can be useful to find conditional demands. Note that we need to assume the firm minimizes costs in order to use this Lemma. 

**Exercise E**: Show that this is true to find :math:`X(p_X,p_Z,Y)` using the production function :math:`Y=X^{1/2} Z^{1/4}`.

Marginal Cost 
+++++++++++++

The marginal cost of producing an output (while minimizing costs) is given by: 

.. math:: c(p_X,p_Z,Y) = \frac{\partial C(p_X,p_Z,Y)}{\partial Y} 

We use the convention of using lower case :math:`c` to denote marginal cost while upper case C for total costs. 

Using the enveloppe theorem we can show that

.. math:: \frac{\partial C(p_X,p_Z,Y)}{\partial Y} = \mu

:math:`\mu` is therefore the marginal cost at the optimum.

**Exercise F**: Find the marginal cost for :math:`Y=X^{1/2} Z^{1/4}`.

If the production function has returns to scale which are:

-  Constant: :math:`C(p_X,p_Z,Y)` is linear in :math:`Y`, :math:`c(p_X,p_Z,Y)` is  constant. 

-  Increasing: :math:`C(p_X,p_Z,Y)` is concave in :math:`Y`, :math:`c(p_X,p_Z,Y)` is decreasing. 

-  Decreasing: :math:`C(p_X,p_Z,Y)` is convex in :math:`Y`, :math:`c(p_X,p_Z,Y)` is increasing. 

Profit Maximization
+++++++++++++++++++

The firm minimizes costs for a given level of output, but it also needs to pick the level of output. A natural objective is to maximize profits.

Profits are given by: 

   .. math:: \Pi = R - C

where :math:`R` represents revenue and :math:`C`, costs. Given an input :math:`X` and output :math:`Y = F(X)`, profits are given by:

   .. math::

      C(X) = p_X X , \quad R(Y) = p_Y Y \\
      \Pi(X) = p_Y F(X) - p_XX

At the optimum, we have 

   .. math::

      p_Y F'(X) - p_X = 0 \iff F'(X) =
      \frac{p_X}{p_Y}

**Exercise G** Consider :math:`F(X) = \sqrt X`, find the choice of
:math:`X` which maximizes profits. 

The supply function of the firm (output) is given by :math:`Y^* = F(X^*)`. 

**Exercise H** Consider :math:`F(X) = \sqrt X`. Find the supply function of the firm for :math:`Y`.

When we have two inputs and one output, we can proceed by: 

-  Cost minimization for :math:`(X,Z)` as a function of  :math:`Y`.

-  Profit maximization for :math:`Y` using the cost function (function of :math:`Y`).

**Exercise I** For :math:`Y=X^{1/2} Z^{1/4}`, find the supply function for :math:`Y`.

Production Economy
++++++++++++++++++

In an exchange economy, we have solved for a market equilibrium as well as a Pareto optimum. In a production economy, we can do the same. We have to add a firm and specify what it produces and with which goods. We also have to distribute profits from the firm, if any, to consumers who are shareholders of this firm. In general equilibrium, nothing is lost...

Consider a situation with two goods: :math:`X` and :math:`Y`. The firm has a production function :math:`Y = F(X)`. 

**Firm Behavior**

-  Given prices :math:`p_Y` and  :math:`p_X`, a firm maximizes profits. 

   .. math:: \Pi(X) = p_Y F(X) - p_X X

-  We can find demand for the input :math:`X^{F,d}(p_X,p_Y)`, supply of the firm :math:`Y^{F,s}(p_X,p_Y)` and profits, if any, :math:`\Pi`. 

**Consumer Behavior**

-  Consider two consumers C1 and C2

-  Preferences of consumers are represented by :math:`U_1(X, Y)` and
   :math:`U_2(X,Y)`

-  Consumer 1 has endownments :math:`(X^{C1,e},
   Y^{C1,e})` while consumer 2 has :math:`(X^{C2,e}, Y^{C2,e})`

-  Each consumer gets a share of profits from the firm :math:`\rho_{1}` and
   :math:`\rho_2 = 1- \rho_1`.

Consumer 1 (same for 2) has to solve

.. math::

   \max_{X,Y} \left[U_1(X,Y): p_{X} X +  p_{Y}Y \leq p_{X}X^{C1,e}+ p_{Y}Y^{C1,e} + \rho_{1}\Pi \right]

-  Yields demands for consumer 1: :math:`X^{C1,d}(p_X,p_Y)` and
   :math:`Y^{C1,d}(p_X,p_Y)` (same for 2) 

**Market equilibrium**

We can normalize :math:`p_{X} = 1` and so  :math:`p_{Y} = p` (see notes on exchange if unclear). Given :math:`p`, we can find demands :math:`X` and :math:`Y` for each consumer, demand of :math:`X` from the firm and supply :math:`Y`.

The market for  :math:`X` is in equilibrium at price :math:`p` if and only if

   .. math::

      X^{C1,d} + X^{C2,d} + X^{F,d} = X^{C1,e} + X^{C2,e}  

Walras' Law applies and if :math:`p` is the equilibrium price on the market for :math:`X`, the market for :math:`Y` is also in equilibrium. 

An example...


Assume 

-  Production: :math:`F(X) =  \log(1+X)`

-  Preferences: :math:`U_1(X,Y) = U_2(X,Y) = \log X + \alpha \log Y`

-  Endowments: :math:`X^{C1,e} = 2` et :math:`X^{C2,e} = Y^{C1,e} = Y^{C2,e} = 0`

-  Profits: :math:`\rho_1 =0` and :math:`\rho_2 = 1`

-  Price: :math:`p_X = 1`, :math:`p_Y = p`

For the firm, profit maximization yields

   .. math::

      \max_X p\log(1+X) - X\;\; \Rightarrow \;\; X^{F,d}
      = p- 1 \;\; et \;\; Y^{F,s} = \log p

Profits are given by :math:`\Pi = p \log p - p+1`

On the consumer side, given their income, :math:`I`, consumers maximize utility

.. math::

   \max_{X,Y} \left[\log X + \alpha \log Y : X + pY \leq I \right]

Income is given by  :math:`I_1 = 2` and :math:`I_2 = \Pi =  p \log p - p +1`. 
   
Demands are 

   .. math::

      X^{C1,d} = \frac{1}{1+\alpha}I_1  \\
      Y^{C1,d} = \frac{\alpha}{1+\alpha} \frac{I_1}{p} \\
      X^{C2,d} = \frac{1}{1+\alpha} I_2  \\
      Y^{C2,d} = \frac{\alpha}{1+\alpha} \frac{I_2}{p}

A market equilibrium for :math:`X` is given by:

   .. math:: X^{F,d} + X^{C1,d} + X^{C2,d} = X^{C1,e} + X^{C2,e} = 2

which gives: 

   .. math::

       p-1 + \frac{1}{1+\alpha}2 + \frac{1}{1+\alpha}(p\log p - p +1 ) = 2.
       
       
The equilibrium price is the solution to :math:`\alpha p +p\log p = 3 \alpha`. We can solve numerically (:math:`p^*`). 

If we summarize the method

-  Given prices, profit maximization gives input demands and supply of the firm. We can compute the profits.

-  Given prices, endownments and profits, we can compute income and consumer demands.
  
-  From excess demand functions, we can find the equilibrium price. 

Welfare theorems apply. The firm needs to be a price-taker. 

Python example 
++++++++++++++

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Production.ipynb

