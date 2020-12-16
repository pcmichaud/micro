Time
----

Preferences
+++++++++++

Generally, everyone prefers to get benefits as fast as possible and incur cost as late as possible:

-  A coffee now or in an hour?

-  Go to the Gym today or tomorrow?

-  Save now or next year?

Empirical evidence suggest that the origin of preferences can be traced to childhood. But preferences may change over time.  

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/QX_oy9614HQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Discounted Utility
++++++++++++++++++

In his book *The Theory of Interest* in 1930, `Irving Fisher <https://fr.wikipedia.org/wiki/Irving_Fisher>`_ presents a simple theory which is the fundation to modern finance and macro. Preferences are represented using discounted utility. 

If :math:`u(C_t)` denotes utility of consuming in period :math:`t`, discounted utility for a consumption plan :math:`\textbf{C} = (C_1,...,C_T)` is :

.. math:: DU(\mathbf{C}) = \sum_{t=1}^T \delta^{t-1} u(C_t)

:math:`\delta` :math:`\in [0,1]` is the discount factor (higher value indicates patience). The relationship between the discount rate :math:`\rho` and the discount factor is given by:

.. math:: \delta = \frac{1}{1+\rho}


Marginal Rate of Substitution (MRS)
+++++++++++++++++++++++++++++++++++

If :math:`T=2`, then

.. math:: DU(C_1,C_2) = u(C_1) +  \delta u(C_2)

Total differentiating to obtain the MRS yields:

.. math:: \frac{\partial C_2}{\partial C_1}\rvert_{dDU=0} = -\frac{u'(C_1)}{\delta u'(C_2)}

Intertemporal preferences are captured by:

-  Discount factor (:math:`\delta`)

-  The shape of :math:`u`.

**Exercise A**: Find the MRS for :math:`u(C_t) = \log C_t`

How can we estimate the discount rate (factor)? We can use MPL (see course on risk). 

A Danish study estimates discount rates using MPL `(Harrison, Lau and Williams, 2002) <https://www.aeaweb.org/articles?id=10.1257/000282802762024674>`_

|image_mpl|

Results show great dispersion and high discount rates, much higher than interest rates. 

|image_discount|

Intertemporal Budget Constraint
+++++++++++++++++++++++++++++++

**Interest and Financial Markets**

Financial institutions offer :math:`r_S` for each dollar deposited (savings)
. We are asked :math:`r_D` for each dollar borrowed. 

Assume for the moment that :math:`r_D = r_S = r`.

**Resources**

Resources originate from:

-  Initial wealth: :math:`W_0`.

-  Income during both periods, :math:`Y_1`, :math:`Y_2`.

The present value (PV) of these resources :

.. math:: PV_W = W_0 + Y_1 + \frac{Y_2}{1+r}

**Constraint**

Present value of consumption is given by:

.. math:: PV_C = C_1 + \frac{C_2}{1+r}


Ainsi, la contrainte intertemporelle est :math:`PV_C \leq PV_W`:

.. math:: C_1 + \frac{C_2}{1+r} \leq W_0 + Y_1 + \frac{Y_2}{1+r}

**Borrowing and Saving**

We can write the constraint as

.. math:: (1+r)(W_0 + Y_1 - C_1) \ge  C_2 - Y_2

Therefore,

-  If one saves in the first period, one can also consume more than income in the second period. 
-  An individual who borrows in the first period has to consume less than his income in the second period. 

Visually, we have

|image_budget|

*Example*: We can incorporate a pension plan into our budget constraint. A defined benefit pension plan forces the individual to save in the first period (contribute) against a fixed pension benefit in the second period. 

-  Income in the second period is :math:`Y_2 = \phi Y_1` with a replacement rate
   :math:`\phi \in [0,1]`.

-  Income in th first period is reduced by the contribution to the pension plan
   :math:`\tau Y_1`.

The budget constraint is:

.. math:: C_1 + \frac{C_2}{1+r} \leq W_0 + (1-\tau)Y_1 + \frac{\phi Y_1}{1+r}

Actuaries pick the contribution rate :math:`\tau` such that:

.. math:: \tau Y_1 = \frac{\phi Y_1}{1+r_P} \to \tau = \frac{\phi}{1+r_P}

where :math:`r_P` is the implicit return of the pension fund. If :math:`r_P = r`,
the budget constraint is identical! The consumption plan does not change and so private savings is reduced one to one with the contribution made (crowdout effect). Lots of research is devoted to understanding the interplay between pensions and savings.  

**Spread between returns and borrowing costs**

**Exercise B**: What does the budget constraint look like if :math:`r_S<r_D`?

**Exercise C**: How to represent a situation where the agent cannot borrow?

Optimal Choice
++++++++++++++

**Maximization**

The problem is (fix :math:`W_0=0` to simplify): 

.. math:: \max_{C_1,C_2} \{ u(C_1) + \delta u(C_2) : C_1+C_2/(1+r) \leq Y_1 + Y_2/(1+r)\}

Two approaches:

#. Direct approach (substitution of constraint)

#. Lagrangian

**Optimality conditions**

Le Lagrangian has three FOC:

.. math::

   \begin{aligned}
    u'(C_1) - \lambda = 0  \\
   \delta u'(C_2) - \lambda /(1+r) = 0  \\
   C_1+C_2/(1+r) - Y_1 - Y_2/(1+r) = 0  \end{aligned}

With (1) and (2) we get :

.. math:: \frac{u'(C_1)}{\delta u'(C_2)} = 1+r

We can re-arrange, fixing :math:`R=1+r`, to obtain the **Euler** equation:

.. math:: u'(C_1) = R\delta u'(C_2)

Visually

 |image_optimal|

This theory is the basis for the life-cycle model (*the Life-Cycle Hypothesis*), proposed by `Franco Modigliani <https://en.wikipedia.org/wiki/Franco_Modigliani>`_, which allows to understand decisions over age. 

**Exercise D**: Find the optimal choice :math:`C_1` and
:math:`C_2` if :math:`u(C)=\frac{C^{1-\sigma}}{1-\sigma}` and the consumer faces a simple budget constraint. 

*Example*: Are Canadians saving enough for retirement?

A question often making headlines. 

.. figure:: /images/retraite.png
   :alt: Le Conseiller, Globe and Mail, L’Actualité

   Le Conseiller, Globe and Mail, L’Actualité

This is a difficult question. One can simulate outcomes using very sophisticated models but how do we determine what is enough? Is saving too much also a problem?

.. figure:: /images/mckinsey.png
   :alt: McKinsey (2015)

   McKinsey (2015)

For more recent calculations, see this `report <https://ire.hec.ca/en/wp-content/uploads/sites/3/2020/06/cpr-report-2020-final.pdf>`_ of the Retirement and Savings Institute at HEC. 

**Optimal Savings** 

What does theory tell us about optimal savings?

**Exercise E**: Find the solution for optimal savings at the beginning of period 2 if :math:`u(C)=\frac{C^{1-\sigma}}{1-\sigma}` and the budget constraint is given by :

.. math:: C_1 + \frac{C_2}{1+r} \leq (1-\tau)Y_1 + \frac{\phi Y_1}{1+r}



More sophisticated computations can be done to compute how much people should save and compare it to how much they have actually saved: 

.. figure:: /images/savings.png
   :alt: Scholz et al. (2007, Journal of Political Economy)

   `Scholz et al. (2007, Journal of Political Economy) <https://www.journals.uchicago.edu/doi/10.1086/506335>`_

Conclusions are sometimes surprising compared to what we hear in the media. A vast majority appears to save enough. Some even save too much. 

Present bias
++++++++++++

As we have seen, individuals can be very impatient. But their preferences may still fit discounted utility theory. There is no contradiction. But, there exist violations of discounted utility which have to do with the way people discount the very short term and the medium and long-term. If the discount function is not exponential, but rather hyperbolic for example, then individuals make inconsistent plans which they will not follow upon. 

*Example*: Picking a movie

You have to pick one movie to watch today and one you will watch next week:

Assume `Mommy <https://www.youtube.com/watch?v=d7rtSqI0ZeA>`_  has an immediate benefit of 4 and also a future benefit of 4 but that `Les Boys <https://www.youtube.com/watch?v=OFl0fuIRl9A>`_ has an immediate benefit of 7 (but no future benefit).

**Exercise F**: What is your discounted utility if you pick a movie today and  :math:`\delta=1`. What happens if we delay movie watching to next week but you have to pick today?


What is likely to happen when next week comes? Do you follow up with the plan in Exercise F?


Empirical evidence suggest that in such choice situations, lots of people will pick Les Boys if they watch tonight. If they pick for next week today, they will pick Mommy. Discounted utility does not allow for such choice reversals, what is often called dynamic inconsistency.  

**Present-Bias and Quasi-Hyperbolic Preferences**

Laibson (1997, QJE) proposes a simple modification to discounted utility, but with major implications. He produces to use a quasi-hyperbolic discount faction that discounts more heaviliy the immediate short term than the long-term:

.. math:: QH(\mathbf{c}) = u(C_1) + \beta \sum_{t=2}^T \delta^{t-1} u(C_t)

The parameter :math:`\beta` acts as a measure of present bias (the lower it is, the larger the bias) while :math:`\delta` controls impatience in the long-term (similar to discounted utility discount factors). These preferences depend on the horizon. 

**Exercise G**: What is the MRS between :math:`C_1` and
:math:`C_2`? And :math:`C_2` vs. :math:`C_3`? Compare with discounted utility.

Using the two movie example, assume now :math:`\beta=0.5`.

**Exercice H**: Repeat Exercise F. 

*Example*: Who buys Annual Gym memberships?

`Della Vigna et Malmendier (2006) <https://www.aeaweb.org/articles?id=10.1257/aer.96.3.694>`_ study the choice between taking an annual membership to a Gym vs. purchasing individual passes valid for one visit to the Guym. An daily pass costs 10$. But given how rarely some people go to the gym, those who purchase an annual membership often end up paying much more per visit. Why do they buy the membership? Don't they know that they may suffer from present-bias? 

.. figure:: /images/Gym.png
    :alt: Della Vigna et Malmendier (2006)

There is evidence that many under-estimate their degree of present bias. Some models have been constructed to capture this degree of naiveté. 

Example: How do we help people to save?

-  Saving is, in some respect, similar to going to the Gym: costly in the short-term (sacrifice consumption), benefits in the long-term (future consumption).

-  To help people with these biases, nudges can be used. Turns out that making people do something by default increases retention into a particular behavior. 

-  Shea et Madrian (2001, QJE) is a famous example. Moving from opt-in to opt-out increases participation in a pension plan.  

.. figure:: /images/shea.png
   :alt: Shea et Madrian (2001, QJE)

   `Shea et Madrian (2001, QJE) <https://academic.oup.com/qje/article-abstract/116/4/1149/1903159?redirectedFrom=fulltext>`_

**Commitment**

People who have present-bias may have a demand for devices that help them keep their future selves in check... David Laibson and may others, study mechanisms of this sort, applied to savings and health for example. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/a7Y6_2JLTrA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


.. |image_mpl| image:: /images/mpl.png
.. |image_discount| image:: /images/Results.png
.. |image_budget| image:: /images/budget.png
.. |image_optimal| image:: /images/optimal.png

Intertemporal Choice Python
+++++++++++++++++++++++++++

Here is Python example. 

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Intertemporel.ipynb

