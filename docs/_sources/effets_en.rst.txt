.. _Effets:



Price and Income Effects
------------------------

Does a tax on gasoline decrease gas consumption and promotes public transportation? 

To answer a question like this, we need to study empirically how the demand for gasoline and public transportation respond to a tax. A tax results in a price change for the consumer. Hence, a prequisite is that we study how demand responds to price. Second, we may want to compensate individuals for the burden of the tax. For this, we need to know how demand changes as a function of income. Related to this is the question of whether or not such taxes are regressive or not. 

.. figure:: /images/gilets.jpeg
   :scale: 100
   
   The *gilets jaunes* in France in part demonstrated because of new gasoline taxes which they argued reduced their purchasing power. 

Price and income elasticities can be estimated without theory. But theory is necessary to answer the more normative questions and to talk about compensation. 

Demand and Preferences
++++++++++++++++++++++

Let us formalize the problem above: 

-  Gasoline (:math:`X`) et Public transporation (:math:`Y`)

-  Preferences may be represented by :math:`U(X,Y)`. We will assume all consumers have the same preferences. 

-  Budget constraint: :math:`p_X Y+ p_Y Y \leq I`

Demand functions are :math:`(X^*, Y^*)` such that 

.. math::

   \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}  \\
   p_X X + p_Y Y = I

At the optimum, the budget is spent and the consumer is indifferent between reducing or increasing :math:`X` and  :math:`Y`.

We have two equations in two unknowns: the solution for :math:`X^*` and
:math:`Y^*` as a function of :math:`(p_X,p_Y,I)` give the marshallian demands. 

**Example**

For preferences represented by :math:`U(X,Y) = \log X +  2\log Y`,

.. math::

   \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}  \iff \frac{1/X}{2/Y} = \frac{p_X}{p_Y}  \iff  p_Y Y = 2p_X X 

One can use :math:`p_X X + p_Y Y =  I` to obtain

.. math:: 
   X^* = \frac{I}{3p_X}  \quad, Y^* = \frac{2I}{3p_Y}

The question is how to characterize how  :math:`X^*` et :math:`Y^*` change as a function of :math:`I` and prices?

Income Effects
++++++++++++++

We start with variation of income. 

**Engel Curves**

-  The consumer demands :math:`X(p_X,p_Y,I)` and :math:`Y(p_X,p_Y,I)`.

-  The Engel curve for :math:`X`: How :math:`X^*` changes when
   :math:`I` change?

-  There is a version which also looks at the relationship between the budget share of :math:`X`,
   :math:`s_X = \frac{p_X X}{I}` as a function of income.

**Normal Good**

A good is normal if and only if the quantity demanded increases with income (at constant prices). 

**Inferior Good**

A good is inferior if its demand decreases when income increases (at constant prices). 


Is gasoline an inferior or normal good? One study by James Porterba (`(Poterba, 1991) <http://www.nber.org/chapters/c11271>`_) suggests that it is inferior if we look at income but not if we look at spending. The reason has to do with variation in spending from savings. 

|poterba|

.. |poterba| image:: /images/poterba.png 
   :scale: 40%

To quantify income effects, we can use an income elasticity defined as 

.. math::

   \eta_{X,I} = \frac{\partial X}{\partial I}\frac{I}{X}

In practice, it is hard to observe the income elasticity because variation in income is rarely exogeneous. What sort of events could you exploit? 

Price Effects
+++++++++++++

How do the demands :math:`X^*` et :math:`Y^*` change if 
:math:`p_Y` and :math:`I` stay constant but :math:`p_X` changes?

To quantify this margin, we may use a price elasticity of the form: 

.. math::

   \eta_{X,p} = \frac{\partial X}{\partial p_X}\frac{p_X}{X}

This elasticity is invariant to monetary units. A challenge is to find an experiment where the price is varied exogeneously while other factors are kept constant. Taxation is one of the key margin exploited. Other examples include supply shocks. 

In Denmark, one `study <https://www.sciencedirect.com/science/article/abs/pii/S0094119018300779>`_ shows that the price elasticity varies alot across the country and in particular reacts to the distance people need to travel to work and transportation alternatives they face.

.. image:: /images/elasticity_denmark.png
   :scale: 65%

In the U.S., another `analysis <https://www.aeaweb.org/articles?id=10.1257/pol.6.4.302>`_ shows that a distinction should be made between a price change and a tax change. The effect of a tax appears to be more visible and people react more to it.  

.. image:: /images/elasticity_tax_price.png
   :scale: 45%

What are the implications for tax revenue? Hint: Think of the effect of the elasticity on tax revenue. 

An increase in the price (or tax) has a direct effect of lowering utility. One may want to compensate households for this. To compute the compensation, we have to think of the forces of what leads to a behavioral change. 

There are two forces:

-  Public transportation is more affordable than the car (gasoline): consumers will want to substitute towards public transportation. This is a *substitution* effect which comes from the relative price signal.

   .. math:: \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y}

-  At current consumption, one needs more income to buy this basket at the new prices. Hence, the consumer needs to reduce his consumption: *income efect*. 

Compensation will be a function of income and substitution effects. Hence, our **objective:** is to identify these effects and see how they lead to the total price effect. 

Compensated Demand
^^^^^^^^^^^^^^^^^^

Compensated demand allows to separate substitution and income effects. 

**Context**

-  Reference price :math:`(p_X,p_Y)`, reference income :math:`I`

-  New prices :math:`(\hat p_X,p_Y)`, income does not change. 

-  Reference Demand, :math:`X(p_X,p_Y,I)`, indirect utility level at reference price and income
   :math:`V(p_X,p_Y,I)`

-  New Demand, :math:`X(\hat p_X, p_Y, I)`, new indirect utility level
   :math:`V(\hat p_X,p_Y,I)`.

Compensated Income: income :math:`I^{cmp}` such that we maintain utility at reference level despite facing  **new prices**. 

   .. math:: V(p_X,p_Y, I) = V(\hat p_X, p_Y,  I^{cmp})

Compensated demand (or `hicksian <https://fr.wikipedia.org/wiki/John_Hicks>`_) is given by the marshallian demand where we replace income by compensated income :math:`X^{cmp}= X(\hat p_X, p_Y,  I^{cmp})`. There exist a dual theory of consumer choice which alternatively derives the compensated demand from minimizing expenditures subject to maintaining utility above a certain level. We do not do this here. 

Compensated income for a price increase is always higher than reference income. The difference is the compensation required. If the price increase results from a tax, this new compensation is required not to make consumers worse off. Yet, even if the compensation occurs, it still has the potential of changing behavior: a price change results in a potential substitution effect which does not go away if compensation occurs. 
 
**Law of Compensated Demand** If :math:`\hat p_X > p_X`, then :math:`X^{cmp}(p_X,p_Y,I)<X(p_X,p_Y,I)`. Compensated demand for :math:`X` is decreasing in the price :math:`p_X`.

**Exercis A**: Compute compensated income and demand for 
:math:`X` if :math:`U(X,Y) = XY` and :math:`p_XX+p_YY \le I` for a price change :math:`\hat p_X > p_X`.


We can now define substitution and income effects.

**Substitution Effect**

Change in demand caused by a relative price change, keeping utility constant. 

Substitution Effect :math:`=` Compensated Demand - Reference Demand

   .. math:: \Delta X^{{cmp}} =  X(\hat p_X,p_Y,I^{cmp}) - X(p_X,p_Y,I)

**Income Effect**

Change in demand caused by a change in purchasing power, keeping prices constant. 

-  Income Effect :math:`=` New demand - compensated demand

.. math:: \Delta X^{I} = X(\hat p_X,p_Y,I) - X(\hat p_X,p_Y,I^{cmp})

We can approximate the compensated income for a small change in price:

  :math:`\hat p_X = p_X + \Delta p_X`. 

To keep notation light, denote

  :math:`X^* = X(p_X,p_X,I)`, :math:`Y^* = Y(p_X,p_Y,I)`

The define :math:`I^{cmp}= I + \Delta I^{cmp}`,
:math:`X^{cmp}= X^* + \Delta X^{cmp}` and
:math:`Y^{cmp}= Y^* + \Delta Y^{cmp}`.

Therefore,  

.. math::

   \begin{aligned}
   I^{cmp}& =  \hat p_X X^{cmp}+  p_Y Y^{cmp}\\
    & =  (p_X + \Delta p_X)(X^* + \Delta X^{cmp}) + p_Y(Y^* + \Delta Y^{cmp})\\ 
     &=  \underbrace{p_X X^* + p_YY^*}_{=I} +\underbrace{\Delta p_X \Delta X^{cmp}}_{\simeq 0} + \Delta p_X X^* \\
     & \quad \quad \quad + \underbrace{ p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}}}_{=0}\\ & \simeq I+  \Delta p_X X^* \\
    \Delta I^{cmp}&\simeq \Delta p_X X^*\end{aligned}

Why does :math:`p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}} = 0`?

:math:`(X^*,Y^*)` and :math:`(X^{cmp},Y^{cmp})` are on the same indifference curve and close to each other for a small price change, which implies,

   .. math:: \frac{\Delta Y^{cmp}}{\Delta X^{cmp}} = MRS_{X}

:math:`(X^*,Y^*)` is optimal at prices :math:`p_X, p_Y`, which implies :math:`MRS_{X} = -\frac{p_X}{p_Y}`.

Therefore, :math:`p_X \Delta X^{cmp}+ p_Y \Delta Y^{cmp}= 0`.

**Exercise B**: See if this is a good approximation for 
:math:`U(X,Y) = XY` with reference price and income
:math:`(p_X,p_Y,I) = (1,1,100)` and :math:`\Delta p_X = 1`. Redo the exercise for 
:math:`\Delta p_X = 0.1`.


.. figure:: /images/price_change.png
   :scale: 75

   In the :math:`(X,Y)` space, consider a price increase for good :math:`X`. The index 1 refers to the reference situation and index 2 to the situation with the new prices. The consumer is initially at point A (reference). With the price change, the budget constraint has a steeper slope. After the price change, the consumer is at price C. To decompose this price change, we compensate the consumer at the new prices. He chooses point B, with the same utility as in the reference situation. The passage from A to B is the substitution effect. The passage from B to C is the income effect. The sum of the two yield the total effect of the price change. 

Slutsky Equation 
++++++++++++++++

The `Slutsky <https://fr.wikipedia.org/wiki/Eugen_Slutsky>`_ equation allows to look the total price effect, the substitution effect and the income effect. The first and the last are observable given sufficient exogeneous variation. The second one is necessary to compute the compensation required.  

To keep notation simple, consider 

.. math::

   \begin{aligned}
    X^* &= X(p_X,p_Y,I), &     X(p_X + \Delta p_X, p_Y,I) &= X^* + \Delta X^*,\\ && X(p_X + \Delta p_X, p_Y,I) &= X^{cmp}+\Delta X^I\end{aligned}

We get

.. math::

   \begin{aligned}
   \underbrace{\Delta X^*}_{\text{Effet total}} = \underbrace{\Delta X^{cmp}}_{\text{Effet substitution}} + \underbrace{\Delta X^I}_{\text{Effet prix}}\end{aligned}

**Exercice C**: Find the substitution and income effects in exercise B (:math:`\Delta p_X = 1`). 


Since

.. math:: \Delta X^I =   -\frac{\partial X}{\partial I} \Delta I^{cmp}=  -\frac{\partial X}{\partial I}  \Delta p_X X^*

then,

.. math::

   \begin{aligned}
   \Delta X^* &=   \underbrace{\Delta X^{{cmp}}}_{\leq 0} -   \underbrace{\frac{\partial X}{\partial I}\times \Delta p_X X^*}_{\geq 0 \text{ si normal, } <0 \text{ si inférieur}} \end{aligned}

In terms of elasticities,

.. math::

   \begin{aligned}
   \frac{\Delta X^*}{\Delta p_X}\frac{p_X}{X^*} & = \frac{\Delta X^{cmp}}{\Delta p_X}\frac{p_X}{X^*} - \frac{\partial X}{\partial I} \Delta p_X X^*\times\frac{p_X}{\Delta p_X X^*}\frac{I}{I} \end{aligned}

The Slutsky equation becomes:

.. math:: \eta_{X,p} = \eta^{cmp}_{X,p}  - \eta_{X,I} \cdot s_X

**Exercice D**: For Cobb-Douglas preferences :math:`U(X,Y) = X^\alpha Y^{1-\alpha}`, compute compensated price elasticity using the Slutsky equation. 


Cross-price Effects
+++++++++++++++++++

Let us first talk about the nature of goods, complements or substitutes. Turns out compensated demands are necessary to define those precisely. Goods :math:`X` and :math:`Y` are:

-  Substitutes: if the cross-price effect is positive:
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} >0`

-  Complements: If the cross-price effect is negative:
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} <0`

What is your prior about the cross-price elasticity of public transporation? How would it factor into your analysis of a policy that taxes gasoline to reduce carbon emissions?

Properties of Demand Functions
++++++++++++++++++++++++++++++

-  Homogeneity of degree zero (no monetary illusion)

   .. math:: X(\lambda p_X,\lambda p_Y,\lambda I) = X(p_X,p_Y,I)

-  Symmetry:

   .. math:: \frac{\partial X^{cmp}}{\partial p_Y} =\frac{\partial Y^{cmp}}{\partial p_X}

-  Additivity:

   .. math:: p_X \frac{\partial X(p_X,p_Y,I)}{\partial I} + p_Y \frac{\partial Y(p_X,p_Y,I)}{\partial I} = 1

-  Negativity (Law of compensated demand):

   .. math:: \frac{\partial X^{cmp}}{\partial p_X}<0,\frac{\partial Y^{cmp}}{\partial p_Y}<0

Price indices of cost-of-living
+++++++++++++++++++++++++++++++

To measure how the cost-of-living changes, we use consumer price indices (CPI). One such index is the Laspeyres index:

.. math:: \pi_L = \frac{\hat p_X  X + \hat p_Y Y}{p_X X + p_Y Y}

Note that  :math:`X` and :math:`Y`, bought in the reference situation, are also used after the price change. This CPI keeps quantities fixed, at least in the short term. The policy question is that many government benefits are indexed to the CPI and it is not clear whether the CPI really reflects changes in purchasing power. The objective of this indexation is to maintain power purchasing power of these benefits constant but it does not account for the fact that consumers substitute away from goods whose price increases more, in relative terms. Another issue is that monetary policy is also based on inflation which is measured using the CPI. 

For an increase in the price of :math:`X`, the effect on purchasing power can be measured with:

   .. math:: \pi_I =  \frac{I^{cmp}}{I}

This will depend on preferences. It is possible that this Hicksian price index yield a different answer than the Laysperes price index. In particular, if the income share of a good decreases when its price increase, the Hicksian index often yields a lower increase in the cost-of-living than what the Laysperres index would suggest. We call this bias the substitution bias in price indices. 

Before the pandemia hit and a lockdown was imposed, gasoline consumption went down. The price of gas also decreased (for may reasons). Does a Laysperes index give a good indication of the change in purchasing power during this period? Thist `article <https://www.nber.org/papers/w27352>`_ does the computation for the U.S. and shows that inflation is under-estimated.  

Giffen Goods
++++++++++++

There exist a type of good for which demand increases with the price! Look back at the Slutsky equation: 

.. math:: \eta_{X,p} = \eta^{cmp}_{X,p}  - \eta_{X,I} \cdot s_X.

The first term is always negative. This comes from the Law of compensated demand... To get a positive elasticity, we therefore need the second term to be negative (so that it becomes positive when substracted). 

A necessary condition is therefore that the good is inferior :math:`\eta_{X,I}<0`. But to overcome the negative substitution effect, this is not sufficient. We need this negative income effect to be large and (or) the budget share to be large. 

So, it is possible that :math:`\eta_{X,p}>0`. But do we see this case in reality? (read the story behind Giffen goods on `wikipedia <https://en.wikipedia.org/wiki/Giffen_good>`_). The best example we know comes from China. A subsidy program for rice was introduced, bringing down the price (`Jensen et Miller (2008) <https://www.aeaweb.org/articles?id=10.1257/aer.98.4.1553>`_). This lead to a reduction in rice consumption.

Firm pricing and demand analysis
++++++++++++++++++++++++++++++++

Why would a firm study properties of the demand it faces? Because it can potentially increase sales if it has market power, an ability to affect or manipulate the price on the market. Firms can also price discreminate: segment the market or offer bundles at different prices. The can exploit complementarities between goods to offer bundles.  All of this requires good knowledge of demand. 

Econometric analysis can be used along with some theory, to extract information from firm and market data. In the retail industry, firms purchase for example scanner data to learn about consumers and their sensitivity to prices. 


Python example
++++++++++++++

See this notebook which uses the CES utility function to study price and income effects. 

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/PriceEffectTutorial.ipynb

