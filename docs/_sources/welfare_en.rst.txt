Welfare
-------

We can look at efficiency to look at a policy: does it target the right group, does it have the intended effect and how much does it cost? For example, we could evaluate a policy that increases air quality and leads people to changer their behavior. The economic cost per unit of improvement in air quality may be large. But what can we compare it to? What is the threshold above which the policy does not increase welfare. 


Air quality is valued by consumers. Therefore, we can measure benefits from preferences. While many limit themselves to economic and fiscal impacts, benefits may go beyond what we observe in markets. For example, lockdown policies during the pandemic save lives. People value extending life. 


Three popular approaches are used  to measure up welfare impacts of policies (benefits and costs): a utilitarian, hicksian and finally one based on self-reported hapinness. 

.. figure:: /images/happy.jpeg
   :scale: 100


Utilisarism
+++++++++++


For each consumer :math:`i\in \{1,\ldots,N\}`, we can construct a utility function  :math:`U_i` representing preferences over a basket of goods :math:`B`. Consider the situation where each citizen has basket :`B_1`, :math:`B_2`, ..., :math:`B_N`. According to this approach, we can measure welfare of this group of consumers using  

.. math::
   U_1(B_1) + U_2(B_2) + \ldots + U_N(B_N). 


If we use this welfare criterion, a policy :math:`\mathcal P_0` is better than an alternative :math:`\mathcal P_1` if the sum of utility levels is larger. The function that aggregates utilities of each citizen is linear, as proposed by `Bentham <https://fr.wikipedia.org/wiki/Jeremy_Bentham>`_, but can also take other forms, for example taking the utility of the consumer who has the lowest one which implements the social justice criterion of `Rawls <https://fr.wikipedia.org/wiki/John_Rawls>`_. 

This approach is problematic. It assumes that utility levels are comparable across consumers. But we saw that these are ordinal, that the absolute level has no meaning.
Recall that :math:`U_1` represents preferences of citizen :math:`1`, but :math:`f(U_1)` represents the same preference for any strictly increasing function :math:`f`. There exist an infinite number of utility functions which represent the same preferences. For example, we could rescale utility as  :math:`2\times U_1`, which could create an advantage for a policy of this policy is favorable to a particular citizen.  

The ranking of policies is therefore ambiguous: we can have :math:`\mathcal P_0` ranked better if  :math:`W = U_1 + U_2` while  :math:`\mathcal P_1` is better if we use :math:`W = 2U_1 + U_2`.

In the end, welfare should depend on preferences and not on  :math:`U`. But utilities remain useful in some more restricted capacity.  We can for example define a  **Pareto Improvement**, if utility of all consumers is at least equal to their level before a change in policy, but stricly higher for at least one consumer. If no one looses, and some win, this situation is an improvement in a `Pareto <https://fr.wikipedia.org/wiki/Vilfredo_Pareto>`_ sense. Pareto improvements respect the fact that utility is ordinal.  

Compensating Variation
++++++++++++++++++++++

A promising approach is to quantify welfare in monetary terms using preferences.  `John Hicks <https://fr.wikipedia.org/wiki/John_Hicks>`_ has proposed to use compensating variations. 


For the consumer, what is a policy? A policy  :math:`\mathcal P` affects the budget constraint :math:`C_i(\mathcal P,I_i)` of consumer  :math:`i` (where :math:`I_i` is income).


We can use indirect utility as a starting point. The highest level of utility a consumer  :math:`i` can obtain given his budget constraint is:

   .. math:: U_i^*(\mathcal P,I_i) = \max_{B \in C_i(\mathcal P, I_i)} U_i(B)

Example: Two goods  :math:`X` and :math:`Y`. Utility is :math:`U(X,Y) = \log X + \log Y`. A policy :math:`\mathcal P`: implements a multiplicative tax :math:`\tau` on the price of :math:`Y`. Indirect utility is given by:

.. math::
   U_i^*(\mathcal P,I) = \max_{X,Y} \left[\log X + \log Y: p_X  X + p_Y(1 + \tau) Y \leq I \right]
     
Denote :math:`\mathcal P_0` the status quo le statut quo and consider implementing a policy  :math:`\mathcal P`. We can define the compensating variation as the amount of money On peut définir la variation :math:`\Delta I^{CV}` such that

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P,I - \Delta I^{CV})

It is the amount of money we must take away from the consumer to keep his utility constant at the level found under the status quo. 

Note: we use the sign convention  :math:`\Delta I^{CV}>0` when the policy is *beneficial*, for example a tax rebate, an increase in transfers, an increase in air quality or health.  

**Exercise A**: Find the expression of compensating variation for
:math:`U = XY` and a tax :math:`\tau` on good  :math:`Y`.


:math:`\Delta I^{CV}` only depends on preferences

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV}) \\
      \Rightarrow 2 U^*(\mathcal P_0,I) = 2  U^*(\mathcal P, I- \Delta I^{CV})

For any function :math:`f`,

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV}) \\
      \Rightarrow f[U^*(\mathcal P_0,I)] = f[ U^*(\mathcal P, I - \Delta I^{CV})]

Special case
++++++++++++

Consider preferences for a good :math:`X` and cash :math:`Y`. Preferences are represented by  :math:`U(X,Y) = V(X) + Y`. 

The policy in the status quo is :math:`\mathcal P_0`. The consumer picks the allocation  :math:`(X_0, Y_0)`. Now, consider the change  :math:`\mathcal P`. The new optimal choice is  :math:`(X_1, Y_1)`.

In this case, the compensating variation is :math:`\Delta I^{CV}` 

.. math::

   \begin{aligned}
   U(X_0,Y_0) &= U(X_1, Y_1- \Delta I^{CV}) \\
   V(X_0) + Y_0 &= V(X_1) + Y_1 - \Delta I^{CV} \\
   \Delta I^{CV} &= V(X_1) + Y_1 - V(X_0) - Y_0 \\
   \Delta I^{CV} &= U(X_1,Y_1) - U(X_0,Y_0)\end{aligned}

The compensating variation is equal to a change in utility. Because of the linearity of utility in cash, utility is in dollars. The MRS is given by: 

.. math::
   TMS = \frac{dY}{dX} = - \frac{V'(X)}{1} = -V'(X)

Since :math:`p_Y=1` in the case where :math:`Y` is cash, :math:`V'(X)` represents the willingness to pay (in dollars) for an additional unit of  :math:`X`.

Consumer Surplus
++++++++++++++++

Consider the case of quasi-linear preferences for the good  :math:`X` and cash  :math:`Y`, :math:`U(X,Y) = V(X) + Y`. Let us assume that  :math:`V` is concave (:math:`dV/dX` decreases in :math:`X`). 

The status quo is a situation where the good   :math:`X` cannot be purchased, :math:`\mathcal P_0` and an alternative where :math:`\mathcal P` allows to purchase :math:`X` at price :math:`p_X`. The problem is given by

.. math::
   \max_{X,Y} U(X,Y) \quad s.t. \quad p_X X + Y = I

We can substitute the constraint to obtain :math:`\max_{X} V(X) + I - p_X X`. The FOC 

.. math::
   \frac{dV}{dX} =  p_X

which allows to find demand :math:`X^*(p_X)`. Denote :math:`p_X(X^*) = \frac{dV}{dX}`, the inverse demand function. A point on this inverse demand reads as the willingness to pay for an additional unit of :math:`X`.

In the case of a new product, the compensating variation from  :math:`\mathcal P_0` to :math:`\mathcal P` is consumer surplus.

.. math::

   \begin{aligned}
   \Delta I^{CV} &=& V[X^*(p_X) + I - p_X X^*(p_X)] - [V(0) + I] \\
   &=& V(X^*(p_X)) - V(0) - p_X X^*(p_X)\end{aligned}

The first term is the area under the inverse demand curve, from zero to the quantity demanded:

.. math::
   \int_{0}^{X^*} V'(i)di = V(X^*) - V(0)

It amounts to the sum of willigness to pay for each unit of  :math:`X`. The second term is the cost of purchasing quantity  :math:`X^*`. The surplus is due to the fact that the consumer values each unit that he purchases at price  :math:`p_X` more than the price he paid :math:`p_X`.  

.. figure:: /images/surplus.png
   :scale: 75

   The area  A+B is given by :math:`V(X^*) - V(0)` while  area B is expenditures :math:`p_{X}X^*`. Therefore consumer surplus is  A+B - B = A. 

**Exercise B**: If :math:`V(X) = 10 X - \frac{1}{2}X^2`, find the expression of consumer surplus. 

Welfare and Taxation
++++++++++++++++++++

.. figure:: /images/tax.jpeg
   :scale: 50

Taxation impacts the price paid by the consumer. Therefore, it has effects on welfare (since higher prices lower welfare). Compensated income will help quantify the welfare loss from higher prices (or taxes). 


Consider eliminating a tax, the price decreases from  :math:`p_X = p+t` to :math:`p_X = p` . We have :math:`X^*(p) > X^*(p+t)` (we are not in a  *Giffen* good situation). Income from the tax is :math:`T= t X^*(p+t)`. When the government collects a tax, we assume that the revenues are distributed lump-sum (an amount for each consumer, not dependent on actions). From a welfare point of view, revenue collected from the government is not loss (implicitely it funds services, etc). Here we recognize its cash value.

In terms of compensating variation, we have 

   .. math::
     \Delta I^{CV} =  U[X^*(p), I - pX^*(p)] - U[X^*(p+t), I - (p+t) X^*(p+t)] > 0

We obtain that :math:`\Delta I^{CV} > T`: The consumer is willing to pay an amount which is superior to the revenue generated by the tax. Hence, eliminating the tax is beneficial. 

The welfare gain associated with eliminating the tax is therefore  :math:`\Delta W = \Delta I^{CV} - T`. Why is  :math:`T` substracted? Removing the tax, the government cannot redistribute anymore the proceeds lump-sum. Hence, we have to substract it from the change in consumer surplus. If we introduce a tax, we have  :math:`\Delta W = \Delta I^{CV} + T` since we need to redistribute the tax proceeds lump-sum, which is gain for consumers.   

**Exercise C**: If :math:`V(X) = 10 X - \frac{1}{2}X^2`, find the welfare loss associated with a new tax  :math:`t` on good  :math:`X`. Show this loss graphically.  


Welfare and Air Quality
+++++++++++++++++++++++

Generally, consumers have a positive preference for air quality.   

.. figure:: /images/china_pollution.jpg
   :scale: 50

There is no market for air quality. With the  *Clean Air Act* (1977), the American government has put in place a number of regulations which reduce pollution and improve air quality.  

Consider a policy change from :math:`\mathcal P_0`: no control and costs, to :math:`\mathcal P`: pollution controls and costs. The compensating variation should be positrive for consumers if they value air quality. 

Empirically, how can recover such a preference?

We can aim to find a situation where consumers had to face a trade-off between pollution and income (wealth). For example, the decision to purchase a home may depend on the price of the home but also air quality of the neighborhood. Price and air quality vary inside a city. In a market, prices should be higher if air quality is higher if consumers value air quality.   

Using data from real estate transactions, we can determine the value given to air quality. Define :math:`X` as air quality,  (e.g. air particule concentration) We might want to assume preferences are given by:

.. math:: 
   U(X, Y) = V(X) + Y = \alpha X + \beta X^2 +Y

With this utility function, :math:`V'(X)` represents a willingness to pay for air quality. Running a linear regression real estate transaction amounts on  :math:`X` controlling for other factors, we obtain an estimate of :math:`V'(X)`. 

`Chay et Greenstone (2005) <https://www.jstor.org/stable/10.1086/427462>`_ obtain a price-particule elasticity between  -0.2 and -0.35. 

.. figure:: /images/chay.png
   :scale: 50

Now, how do we evaluate a policy with these informations? The government implements :math:`X_{GOV}`. The total cost of these measures is  :math:`c X_{GOV}` with :math:`c>1` is the marginal cost, including the welfare loss from raising this amount of revenue to fund these measures. 

The policy change is from  :math:`(0,0)` to :math:`(X_{GOV}, - c X_{GOV})`. Consumer surplus is the compensating variation:

.. math:: 
   \Delta I^{CV} =  V(X_{GOV}) - V(0) - c X_{GOV} .

This serves as a basis for performing cost-benefit analysis. Once this analysis is done, a follow-up question to ask is: what is the optimal amount of air quality? 

Optimal air quality is the level which maximizes: 

.. math:: 
   U(X) = V(X) + I - c X 

The FOC is

   .. math:: V'(X^*) = c

We can therefore find out this optimal level once we know these qualities.  

**Exercise D**: Noise pollution. The price elasticity of house prices to noise pollution is -0.2. The government considers reducing pollution by 10% near a highway. Engineers estimate the necessary technology will cost 1000$ per house protected (a sound wall). The policy is financed by a tax, which leads to a welfare loss of 43 cents for each dollar that needs to be raised. Would building the sound wall be beneficial in terms of welfare?

This approach is used a lot. It does not require per se knowledge of preference. However, it raises a number of distributive issues if preferences differ across consumers. When the benefits are larger than the cost, but some loose from the policy, we say that the policy is potentially beneficial, implying that compensation may need to take place. 


Self-reported Hapiness
++++++++++++++++++++++

Why not simply ask consumers of they are happy, or happier after a policy change? On a scale of 1 to 10, are you happy? This avoids making assumptions about preferences, utility.  It is an approach that has gained credibility with  `the 2019 budget in New Zealand <https://www.weforum.org/agenda/2019/05/new-zealand-is-publishing-its-first-well-being-budget/>`_.  `Richard Easterlin <https://fr.wikipedia.org/wiki/Richard_Easterlin>`__ is generally credited with making these measures popular. The Easterlin paradox has attracted a lot of attention.

.. figure:: /images/easterlin.png
   :scale: 50

This would suggest that we are not happier with more income: money does not buy hapiness. But later, with more data, the expected relationship was shown to hold, in particular for low levels of income. 

.. figure:: /images/wolfers.png
   :scale: 50

   `Stevenson and Wolfers (2013), AER: Papers and
   Proceedings <http://users.nber.org/~jwolfers/papers/Satiation(AER).pdf>`__


Since happiness is more than income, these measures can be useful. One could use them directly in policy evaluation: 


-  Advantages: direct method, model free.

-  Disadvantages: We can measure welfare in different ways and people have different ways of answering. Various psychological and framing effects possible.  

Few studies use them. But there is a lot of interest, for good reasons. 

For those who want to go deeper, here is an interview with  Angus Deaton on happiness: 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/pfHcdee4R3M" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Python Example
++++++++++++++

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Welfare.ipynb


