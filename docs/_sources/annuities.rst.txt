.. _Intro:

Annuities
---------

Facts
+++++

In their simplest form, annuities allow an agent to receive a certain stream of payments until death against an immediate cash payment. An annuity has the advantage of providing an insurance against longevity risk, the risk of outliving one's savings. 

Few individuals nearing retirement hold little annuities outside public pensions. 

Is this cause for concern?

Theory
++++++

Consider a setting with two periods, :math:`t=1,2`. In period 1, the consumer can consume :math:`c_1`, buy bonds, :math:`B`, or buy annuities :math:`A`. Each dollar of bonds yield :math:`R_B` for consumption in period 2 :math:`c_2`. For annuities, the fair return of an annuity is :math:`R_A = R_B/(1-q)` where :math:`q` is the probability of dying in period 2. Hence, each dollar of annuity yields :math:`R_A`for 2nd period consumption. An important point is that for :math:`q>0`, :math:`R_A>R_B`.  

Consider a general utility function :math:`U(c_1,c_2)` concave in both arguments. Utility when dead is normalized to zero. 

The choice problem is 

.. math::
    \max_{A,B} U(W - A - B,R_A A + R_B B)

subject to the short-selling constraint that :math:`B\ge 0`. Inspection of the problem shows that one can reduce bond holdings by 1 unit and increase annuities by 1 unit without affecting utility from first period consumption. But the result of this reshuffling increases consumption in period 2 since :math:`R_A>R_B`. Therefore, no matter what is the utility function when alive, the optimal solution is to set :math:`B^*=0`. The amount of :math:`A` depends on the consumption plan. But all savings, once consumption has been determined, should be put in annuities. 

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

