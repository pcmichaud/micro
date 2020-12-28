.. _Intro:

Annuities
---------

Facts
+++++

What is an Annuity?
~~~~~~~~~~~~~~~~~~~

In their simplest form, annuities allow an agent to receive a certain stream of payments until death against an immediate cash payment. An annuity has the advantage of providing an insurance against longevity risk, the risk of outliving one's savings. 

Before we define an annuities, a short primer on mortality risk. The idea is not to make you actuaries and we will skip a lot of the technicalities to stay focused on our objective. Denote by :math:`m(a)` the fraction of individuals alive at age a who die in that year. The probability that someone born survives to age a is therefore given by 

.. math::
    s_0(a) = \prod_{j=0}^{a-1} (1-m(j))

The probability someone of age a survives to age a' is :

.. math::
    s_a(a') = s_0(a')/s_0(a)

The remaining life expectancy is someone currently age a is given by 

.. math::
    e(a) = \sum_{a'=a}^{T} s_a(a')

A common form for mortality probabilities that fit the data well is 

.. math::
    \log m(a) = \alpha + \beta t

This is denoted the Gompertz law of mortality. It is easy to estimate Gompertz parameters from data on mortality risk using linear regression of log mortality rates on age. Surprisingly, it fits the data quite well, except perhaps at very old ages. 

The second component of evaluating an annuity is the discount rate. Annuities are offered mostly by insurance companies. Financial markets lend money to insurers, mostly trough the issuance of bonds. A good measure of the riskiness of insurers is the return on corporate bonds issued by insurers. Denote by :math:`r` this rate of return. 

Let us consider an insurer who is willing to cover an individual who has mortality risk described by the series :math:`m(a')` for :math:`a'=a,...,T`. The net present value of a one dollar annuity is given by:

.. math::
    P(a) = \sum_{a'=a}^T \frac{s_a(a')}{(1+r)^{a'-a}}

The NPV of a :math:`A` dollar annual annuity is simply :math:`P(a)A`. :math:`P(a)` is often called the actuarially fair price of the annuity for a given mortality risk and discount (financial risk). 

If one wants to know how much of an annuity can someone buy with :math:`W`, one can deduce that 

.. math::
    W = P(a)A \\
    A = \frac{W}{P(a)}


Compare the pricing function of an annuity to that of a bond with the same return :math:`r` and maturity :math:`T-a`:

.. math::
     \sum_{a'=a}^T \frac{1}{(1+r)^{a'-a}}

It is easy to see that the price of the annuity is lower than that of the bond. This is intuitive: the bond pays no matter whether the individual is alive or not. The annuity only pays when alive. 

One last important concept is that of the money's worth of an annuity. It is the ratio of the fair price :math:`P(a)` to the observed price :math:`\hat P(a)`, 

.. math::
   MW(a) = \frac{P(a)}{\hat P(a)}

A money's worth above one indicates the price is more than fair while a money's worth less than one indicates an unfair price. The load, or profit, on an annuity is given by 

.. math::
    \hat P(a) = (1+\tau) P(a)  \\
    1+\tau = \frac{\hat P(a)}{P(a)} \\
    \tau = \frac{1}{MW(a)}-1 

Some annuities are sold with a minimum payment garantee: their payment is guaranteed for say 5 years no matter whether someone dies or not. Other annuities are sold jointly on a couple's lives. Finally, it is becoming popular to sell deferred annuities, annuities which start only in the future. 

The Annuity Market
~~~~~~~~~~~~~~~~~~

Before we describe the private annuity market, it is important to note that the government already provides annuities. In addition to first-pillar basic income from the Old Age Pension Program, Canada has set up a mandatory public pension system which provides annuity income, proportional to some measure of career earnings, the Canada and Quebec Pension Plan. Together they provide close to 100% replacement rate to low earners and 40-50% someone in the middle of the lifetime earnings distribution (and significantly less to higher earners). Some workers have also contributed to defined benefit employer pensions which provide them with yet another source of annuity income. These pension plans have come under attack and they are slowly loosing ground, except in the public sector. The bottom line is that a significant fraction of our lifetime income is already converted into annuity income in retirement. 

On top of this, there is a market for annuities. The most prevalent forms are variable annuities which are not really annuities but instead an investment product. It does not in general provide a longevity risk guarantee. The fixed annuity market which will be the focus on our study is quite small. 

Who buys annuities?
~~~~~~~~~~~~~~~~~~~

Data is scant on who receives annuity income outside of public and employer pensions. We first turn out attention to the Survey of Financial Security of Statistics Canada. We then look at a survey that was conducted on the topic in November 2018 by the Retirement and Savings Institute at HEC.

Theory
++++++

Consider a setting with two periods, :math:`t=1,2`. In period 1, the consumer can consume :math:`c_1`, buy bonds, :math:`B`, or buy annuities :math:`A`. Each dollar of bonds yield :math:`r_B` for consumption in period 2 :math:`c_2`. For annuities, the fair return of an annuity is :math:`r_A = r_B/(1-q)` where :math:`q` is the probability of dying in period 2. Hence, each dollar of annuity yields :math:`r_A`for 2nd period consumption. An important point is that for :math:`q>0`, :math:`r_A>r_B`.  

Consider a general utility function :math:`U(c_1,c_2)` concave in both arguments. Utility when dead is normalized to zero. 

The choice problem is 

.. math::
    \max_{A,B} U(W - A - B,r_A A + r_B B)

subject to the short-selling constraint that :math:`B\ge 0`. Inspection of the problem shows that one can reduce bond holdings by 1 unit and increase annuities by 1 unit without affecting utility from first period consumption. But the result of this reshuffling increases consumption in period 2 since :math:`r_A>r_B`. Therefore, no matter what is the utility function when alive, the optimal solution is to set :math:`B^*=0`. The amount of :math:`A` depends on the consumption plan. But all savings, once consumption has been determined, should be put in annuities. 

This is a strong result. Note that it does not depend on using expected utility as long as the consumer has utility from consumption in period 1 and 2. The result was first shown by Yaari (1962) but generalized in these terms in  Brown, Diamond and Davidoff (2005). Two key deviations yield partial annuitization. 

**Bequest**

Consider now a setting where 

.. math::
    \max_{\phi,W'} u(W - W') + \delta ((1-q) u((\frac{R_A}{R_B}\phi + 1) W') + q \eta u((1-\phi)(1+R_B) W'))

The two FOCs are 

.. math:: 
    -u_1 + \delta ((1-q) (\frac{R_A}{R_B}\phi + 1) u_2 + q \eta u'_b(1-\phi)R_B  = 0 \\
    (1-q) u'_2 \frac{R_A}{R_B} W' -  q \eta u'_b R_B W' = 0

**Illiquitity and Shocks**


**Loss Aversion**


**Cognitive Constraints**



Interventions
+++++++++++++

