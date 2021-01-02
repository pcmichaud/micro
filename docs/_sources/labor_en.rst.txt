Labor Supply
------------

The consumer problem has so far been focused on picking consumption goods. Income is exogeneous. In reality, our income is not exogeneous. We can decide to work more or less to change our income. When we do, we reduce or increase the time we denote to leisure. We can think of leisure as a consumption good. Increasing income, by working more, has an opportunity cost in terms of leisure foregone. In this class, we focus on this margin. 

Many questions can be adressed in this setting: how does subsidized childcare impact labor supply of mothers? How can we make older workers stay longer in the labor force? What are the impacts of replacing our social programs with a guaranteed minimum income. 

.. figure:: /images/punch_card.jpeg
   :scale: 100

Model
+++++

To model this choice, we introduce a new good, leisure time :math:`L`. Time available each day (effective after substracting time to sleep and personal care) is given by :math:`T`. Therefore, time devoted to work is given by :math:`H=T-L`. Here, we assume that there are only two uses of our time: leisure and work. It is possible to introduce more, for example home production of goods.  The Nobel laureate `Gary Becker <https://fr.wikipedia.org/wiki/Gary_Becker>`_ has been one of the pionners in the economic analysis `time allocation <https://www.jstor.org/stable/2228949?seq=1#metadata_info_tab_contents>`_. 

The consumer has preferences for :math:`(C,L)`, where :math:`C` is consumption goods (we normalize the price to 1) and :math:`L` is leisure time (per day, week or year), represented by :math:`u(C,L)`, generally concave in its two arguments. The MRS between consumption and leisure is given by: 

.. math:: 
   TMS = \frac{dC}{dL}|_{dU=0} = - \frac{u'_L(C,L)}{u'_C(C,L)}

and represents, in absolute value, the marginal value granted to an hour of leisure.  Leisure has a positive value. 

When she works, the consumer has an hourly wage :math:`w` and other income :math:`y`. If she works :math:`H=T` hours, she has a full income of :math:`I = w T + y`. She implicitely spends on two goods she consumes, :math:`C` and :math:`L`. Leisure has the opportunity cost per hour worked given by :math:`w`. The budget constraint is given by: 

.. math:: 
   C + w L \leq I = w T + y

Note that both spending and full income is a function of :math:`w`. We can rewrite the constraint using :math:`H=T-L`: 

.. math:: 
   C \leq w H + y

The budget constraint, in the space :math:`(C,L)` is kinked because of the presence of :math:`y` and has a slope :math:`-w`. 

.. figure:: /images/budget_time.png
   :scale: 75

The labor supply problem can be writen as a Lagrangian: 

.. math:: 
   \max_{C,L,\lambda} u(C,L) - \lambda(C + wL - wT - y)

The FOCs are 

.. math:: 
   \frac{u_L(C,L)}{u_C(C,L)} = w \\
   C + wL = wT + y

The first condition states that the absolute value of the MRS (marginal value of an hour of leisure) is equal to its opportunity cost. The second condition is the budget constraint. The solution to this system gives marshallian demands for consumption and for leisure, :math:`L^*(w,y)`. Labor supply is given by  :math:`H^*(w,y) = T - L^*(w,y)`. 

*Exercise A*: Find the demand for leisure and labor supply for :math:`u(C,L) = C^{\alpha}L^{1-\alpha}`.

The lagrange multiplier has an interpretation as marginal utility of income. We also need to realize that the presence of  :math:`y` may result in a corner solution where :math:`L^* = T` and the MRS is larger than the wage. 

.. figure:: /images/labor_choice.png
   :scale: 75

   The situation A shows a labor supply choice with higher hours of work than situation B which shows a situation where the worker does not work (corner solution. In this case, the MRS is larger than the wage :math:`L=T`. 

Substitution and Income Effects
+++++++++++++++++++++++++++++++

The presence of :math:`w` in full income, which makes the analysis of wage changes more challenging. An increase in the wage now increases the opportunity cost (leading to a substitution effect) but also increases full income (making leisure more desirable if leisure is a normal good).  

To understand these effects, we first note that the choice problem can be re-written to involve only one decision, leisure time, by substituting the budget constraint,

.. math:: 
   \max_L u(wT - wL + y,L)

The FOC is:

.. math::
   -w u_C + u_L = 0

where :math:`u_C` is the marginal utility of consumption and :math:`u_L`, the marginal utility of leisure. Total differentiating and setting :math:`dy=0`, we get

.. math::
   \frac{d L}{d w} = \frac{U_C}{\Delta} + h \frac{d L}{d y}

where :math:`\Delta` is negative. Hence, the effect of a change in the wage is the sum of a negative term (first term) and a positive income effect term (if leisure is normal). The effect of a wage change on leisure is undetermined and will depend on the relative strenght of these two effects.  

We can re-write to obtain a Slutsky equation for labor supply by first rewriting in terms of hours worked: 

.. math::
   \frac{dH}{dw} = \frac{dH}{dw}|_{dU=0} + H \frac{dH}{dy}

The substitution effect is now positive and the income effect negative. In terms of elasticities we have: 

.. math::
   \eta_{w} = \eta^{cmp}_{w} + \frac{wH}{y} \eta_{Y}

We can estimate the wage and income elasticity in different ways. For example, `Imbens et al. (2001) <https://www.aeaweb.org/articles?id=10.1257/aer.91.4.778>`_ estimate the income elasticity from looking at lottery winners. This allows to estimate :math:`\eta_{Y}`. They find an income elasticity between -0.05 and -0.1. 

.. figure:: /images/winners.png
   :scale: 100

   Imbens et al. (2001)

For wage elasticities, the literature is vast. Generally the elasticity is smaller for men, larger for women, in particular for the choice of entering the labor market or not.  

*Exercise B*: Find the wage elasticity and compensated wage elasticity for :math:`u(C,H) = C - \frac{H^{1+\frac{1}{\epsilon}}}{1+\frac{1}{\epsilon}}`.

It is possible that a wage increase leads to a reduction of hours worked. This happens when the income effect dominates the substitution effect. This can be observed in certain occupations. Physician labor supply is the prime example. After large increases in salaries, the fraction of physicians working part-time has increased substantially. 

.. figure:: /images/medecins.png
   :scale: 50

A particular case which involves an income effect that is exactly equal to the substitution effect (in absolute terms) is income targeting. This `study <https://www.cmu.edu/dietrich/sds/docs/loewenstein/NYCCabdrivers.pdf>`_ on taxi drivers in New York is a good example. 

Taxation
++++++++

Taxation can take many forms. In its simplest form, it is a tax rate :math:`\tau` on work income. If we look at the budget constraint, we have : 

.. math:: 
   C \leq (1-\tau) w H + y

Therefore, increasing the tax rate is similar to reducing the wage. We denote the after-tax wage as the net wage. Since we know that the effect of a change in wage has an undetermined effect, it is therefore not possible in general to put a sign on the effect of a change in work income taxation. 

.. figure:: /images/labor_taxation.png
   :scale: 75

   Relative to a baseline A, the effect of the tax depends on the shape of indifference curves. It is possible that the worker works less (situation D, substitution effect dominates) or more (situation B, income  effect dominaires).  

In addition, the implementation of the tax is important to assess the change. The more permanent is a tax, the more workers will feel the income effect while if a tax is transitory, the substitution effect is likely more important. Furthermore, if there is compensation, for example for low wage earnings, this needs to be taken into account and the compensated wage elasticity should be used. 

The bottom line is that the effect of taxes on labor supply are far from trivial and depend on a multitude of dimensions. 

**Exercise C**: In the case where preferences are given by :math:`u(C,H) = C - \frac{H^{1+\frac{1}{\epsilon}}}{1+\frac{1}{\epsilon}}`, find the effect of a tax :math:`\tau` on labor supply and the welfare loss associated with taxation. 



In reality, the tax system cannot be summarized by a single tax rate  :math:`\tau`. First, income taxes are progressive and the marginal tax rate changes across tax brakets. In addition, income tax credits impact the effective marginal tax rate since they are often function of work income. Generalizing, taxes paid are a function :math:`\tau(wH,y)` which depend on sources of income tax and the level. 

.. math:: 
   C \leq w H + y - \tau(wH,y)

One such measure that is useful is the effective marginal tax rate (EMTR). It can be computed as  

.. math:: 
   EMTR(H) =  \frac{\tau(w(H+\Delta H),y) - \tau(wH,y)}{w\Delta H}

The EMTR is useful to measure the effective marginal tax rate one will pay when working an additional hour. In the Python example below, you will compute such measures for a worker in Quebec. 

.. figure:: /images/taxman.jpeg
   :scale: 100

An interesting method for assessing the effect of taxation is to look for bunching at places where the effective marginal tax rate changes abruptly. The American study of `Saez (2010) <https://www.aeaweb.org/articles?id=10.1257/pol.2.3.180>`_ is a good example of a *bunching* study. They find *bunching* in the first income tax bracket but not for other tax brackets. 

.. figure:: /images/bunching.png
   :scale: 100

   Saez (2010)

Transfers
+++++++++

Governments provide transfers to households with low income. These transfers impact choices in the same way that :math:`y` does. Therefore, they have primarly an income effect in household behavior and increase the likelihood of a corner solution (zero hours worked). 

In addition, they can have substitution effects since transfers are often taken away (clawed back) when work income increases. They can therefore increase EMTRs when someone attempts to exit low income status. If badly designed, these transfers can act as a poverty trap. 

Social assistance in Quebec is reduced dollar for dollar. This is a 100% implicit tax rate. Another benefit that counters that effect is the work income tax credit (prime au travail in Quebec). It first increases as the first dollars are earned and then reduced. Overall, the design of a good transfer system that provides good coverage for low income households and incentives to return to work is not a simple task. 

.. figure:: /images/clawback.png
   :scale: 75

   Source: Final report, `Comité sur le revenu minimum garanti <https://www.mtess.gouv.qc.ca/grands-dossiers/revenu_min_garanti.asp>`_, Volumne 2. 


Graphically, we end up with a budget constraint that looks like this when transfers are clawed back. 

.. figure:: /images/labor_negtax.png
   :scale: 75

If is hard with the preferences in the figure to incentivize return to work with the transfer provided. The incentive to return is not there. 

**Question for discussion**: For or against a guaranteed minimum income, in particular to help people get out of poverty? What do you need as economists to answer this question?

Background reading for discussion: 

- Report from the `Expert committee on basic income <https://www.mtess.gouv.qc.ca/publications/pdf/RMG_Rapportfinal_volume1_v3_Accessible_FR.pdf>`_. 

Python Example
++++++++++++++

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/tax_example.ipynb

