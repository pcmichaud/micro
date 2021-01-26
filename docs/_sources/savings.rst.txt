.. _Intro:

Savings
-------

.. figure:: /images/umbrella.jpeg 
   :scale: 50

Facts
+++++

Stocks and Flows
~~~~~~~~~~~~~~~~

People earn income, for the large part from work, over their entire life. From that income, they spend on goods which they consume, some of which they leave for their heirs. There is no one-to-one relationship between when we earn income and when we spend it. Luckily, we can save some income for later and we can borrow when income is low. There is a lot of saving, and then dissaving, whether it is voluntary or not. For example, paying mandatory pension contributions reduces potential expenditures today against a promise to receive income in the future that allows to spend on goods when old. Paying taxes has also a savvings component since lots of government spending is devoted to the young (who earn no income) and the old, who for example consume a lot of health care. In this set of lectures, we will be mostly concerned with voluntary private savings. Savings are a stock, with the accumulation of contributions, returns and withdrawals being the flows. Let the stock of saving all savings, say at market value, be :math:`w_t`. If we denote by :math:`s_t` contributions when positive and negative when withdrawals, then the stock evolves according to 

.. math::
        w_{t+1} = (1+r_t) w_{t} + s_{t}

Turns out governments have limited information on stocks but also on flows. Admin data in most countries, with the exception of some scandinavian countries, is not available on savings stock and flows such that we follow the equation above. Hence, we must resort to surveys to get information savings flows and stocks. 

Canada has a cross-sectional data infrastructure that allows to get a picture, one in a while of how much people save (and have saved). Statistics Canada runs two surveys, each with their specific purpose, that allow us to paint some portrait of private savings, the Survey of Household Spending `Survey of Household Spending <https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=3508>`_ and the `Survey of Financial Security (SFS) <https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=2620>`_ . The Survey of Household Spending gives us information on income, spending and some measures of direct active savings. This is a good survey for flows. For stocks, the Survey of Financial Survey allows us to construct the balance sheet of Canadians. The SHS is run annually while the SFS is run every five years or so (1999, 2005, 2012, 2016). For researchers at Canadian university, public micro-use files (PUMFS) can be downloaded from `ODESI <http://odesi2.scholarsportal.info.proxy2.hec.ca/webview/>`_. 

Take flows first. Measuring saving contributions can be done in a number of ways, each imperfect. Sometimes, respondents are asked directly whether they have contributed to a savings account, :math:`s_t`. Sometimes, they are asked instead information on spending, :math:`c_t` and income :math:`y_t` and an implied savings variable can be created, :math:`s_t = y_t - c_t`. This is a savings measure that does not account for unrealized capital gains since these are not materialized in income. However,  since :math:`y_t` often includes interest and dividend income, it does include some form of the return component of savings in :math:`r_t w_t`.  Spending surveys get good measures of spending by asking for detailed questions on many categories of goods. There is also the question of how to include pension contributions and taxes in this definition. Finally, some construct savings from asking for changes in wealth at two points :math:`s_t = w_{t} - w_{t-1}`. Again, this is not a direct measure of :math:`s_t` as defined in the equation above since it will include unrealized capital gains. 

The next figure from SHS shows average consumption and spending at the household level by age in 2009. The information is aggregated by age groups. One important point to make is that a period age-profile does not necessarily represent how a cohort behaves over the life-cycle. In other words, the 65 year olds are from a different generation than the 25 year olds in the plot. If there are large differences in income or other characteristics, the period profile is a poor guide to what happens to a cohort over the life-cycle. One useful tool to deal with this when repeated cross-sectional data is available is the synthetic cohort method. `Attanasio (1998) <https://www.jstor.org/stable/146334?seq=1#metadata_info_tab_contents>`_ is a good example applied to savings.  

.. figure:: /images/age-profiles.png
   :class: with-shadow
   :align: center


   Source: Calculations from Survey of Household Spending, 2009

You can check how these data manipulations are done directly in google collab once you have downloaded the PUMFS to your google drive. 

|ImageLink3|_

.. |ImageLink3| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink3: https://colab.research.google.com/drive/13eiz2vuCeDJNTF10VwDc8dlUmd6dpMzk?usp=sharing

We can compare the two definitions of savings rates across income quintiles. The next figure shows the average savings rate using the consumption definition and using wealth changes. While the pattern is similar and slopes are similar, there are some differences between the two measures. Interestingly, those with higher income save more as a fraction of income than those with lower income. 

.. figure:: /images/shs-compare-savings-rate.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Household Spending, 2009

Private savings can take many form. We tend to refer to savings as either being registered or unregistered, depending on whether they are subject to specific tax treatment or not.  Unregistered savings essentially takes the form of cash and deposit accounts, bonds and stocks that are held outside of tax-preferred saving vehicles. Registered forms of  savings include for the most part Tax-free Savings Accounts (TFSA) and Registered Retirement Savings Plan (RRSP). Since unregistered savings are made out of money that has been taxed, we say that saving contributions are taxed. Unregistered savings are also taxed trough the taxation of returns (dividends, etc). But they are not taxed on the stock or amount owned (there is no wealth tax in Canada), nor are they taxed when we take money out of our accounts. We say that they have a TTE tax treatment, for contribution (T), returns (T) and widthrawals (E).  TFSAs are TEE while RRSP are EET. There is one less T, the middle T compared to unregistered funds. In the next figure we plot the fraction of respondents in SHS who contribute and withdraw funds from RRSPs. We see that RRSP contributions are hump-shaped while withdrawals increase around the time of retirement. But there are withdrawals before retirement as well. 

.. figure:: /images/shs-rrsp-takeup.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Household Spending, 2009

Contribution rates and amounts (conditional on contributing) are quite skewed in terms of income as the next figure shows. 

.. figure:: /images/rrsp-contrib-amounts.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Household Spending, 2009

Registered savings are very popular. For example Statistics Canada reports for 2018, a total of  43.5 billion dollars in `RRSP contributions <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110004401>`_ while the number of 66 billion for `TFSA <https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/income-statistics-gst-hst-statistics/tax-free-savings-account-statistics/tax-free-savings-account-statistics-2018-tax-year.html>`_ in the same year. 

Adding unregistered to registered savings, we often denote total savings as liquid wealth or financial wealth. Implicitely, this allows to make the distinction with another form of wealth, the stock of real assets, such as cars and real estate. The Survey of Financial Security allows us to draw a good portrait of financial wealth. In the next figure,  we zooming in to the near retirees (age 55-65). We first look at the composition of financial wealth by education, a good marker of lifetime income. 

.. figure:: /images/wealth_composition.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Financial Security, 2009

We see that nearly half of financial wealth is RRSP and that this share is roughly similar across education groups. The share of cash, or bank accounts, is smaller for those with higher education and the fraction in stocks slightly larger with education (also mutual funds). The next figure shows the distribution of financial wealth as a fraction of after-tax income. 

.. figure:: /images/wealth_ratios_by_educ.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Financial Security, 2009


All of these respondents are not retired. We see that financial wealth is larger relative to income for those with higher education. On average, college educated households have 3 times their after-tax income in financial wealth compared to roughly 1.25 for those with less than high school. In fact, means mask a lot of heterogeneity and considerable skewness in the distribution of financial wealth. The next figure shows an histograph of the distribution of financial wealth relative to after-tax income. We see that more than 25% of respondents have close to no financial wealth.  

.. figure:: /images/finwealth_density.png
   :class: with-shadow
   :align: center

   Source: Calculations from the Survey of Financial Security, 2009

These calculations using the SFS can be replicated using this notebook. 

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/drive/1ig20Bjzkpgm9e1QotJL0hkxJUXUItPWj?usp=sharing

Replacement Rates
~~~~~~~~~~~~~~~~~

Before one even contemplates to make the decision of how much to save, it is useful to ask the question as to what the public pension system, and employers, replace in terms of life-time income. A short primer on the Canadian retirement income system is available here. But to summarize it succintly for our purposes:

* First pillar: Old age security (OAS) and guaranteed income supplement (GIS). They are not based on career earnings, but provide a flat pension which is clawed back at various rates depending on other retirement income. 

* Second pillar: Canada (and Quebec) Pension Plan provide a benefit which is a function of lifetime earnings against contributions which are made while working. 

* Third pillar: Employer Defined benefit and Defined Contribution plans. DB plans provide an annuity against contributions made while working. Define contribution plans set an accumulation scheme for workers to contribute, sometimes with employers matching their contributions. 

* Fourth pillar: Private retirement savings

The top three pillars interact with each other in complex ways. In addition, the tax system impacts disposable income, while working and when retired. 

One common measure of the generosity of a retirement system is to compute the ratio of disposable income after retirement to that before retirement, an effective replacement rate. Both measures of pre and post disposable retirement income  can be computed a number of ways, sometimes after tax and sometimes before tax. Sometimes average career earnings are used while other times earnings at some age are used. When defined contribution plans are in play, one needs to decide how to annuitize their value to compute an annual flow of disposable income.  

To showcase the effective replacement rates in the Canadian retirement system, we use a retirement income simulator produced by the Retirement and Savings Institute at HEC. That calculator allows to project someone's outcomes all the way to retirement based on inputs regarding earnings and other characteristics. It can also be used on a dataset of potential cases. 








Theory
++++++

Why do people save? How much should people save? It is useful to first look at a benchmark, the life-cycle model in order to answer these questions. 

Existing level of mandatory savings. Unknown preferences 

Some studies have tried to determine whether people save enough for retirement. They reach very different conclusions. 

`Liu, Ostrovsky and Zhou  (2013) <https://www150.statcan.gc.ca/n1/en/pub/11-622-m/11-622-m2013029-eng.pdf?st=7KHtrmbl>`_

A last group of studies attempted to see how spending changed at the time of retirement. Taking the standard life-cycle model literally, these studies anchor their test on the prediction that the Euler equation would predict a smooth path for consumption around the time of retirement. The most famous study was realized by X. Latter authors mention a number of issues with this test since it considers a very restrictive version of the life-cycle model. 

If we accept that some are saving too little, one may ask why that is. For example, one big policy problems in the late 1990s was the relative disappearance of mandatory savings trough employer pensions in the U.S., so called defined benefit pensions. Individual accounts were setup where workers could enroll and decide to save a fraction of their salary, with some of that matched by their employer. Turns out enrollment rates were very low, despite very large returns, even among groups where saving more was probably optimal. 

One leading explanation is that we tend to procastinate when something entails immediate costs against delayed rewards. This leads us to be time-inconsistent, we postone an action to the future and when the future comes, we postpone it again. The standard model does not allow for that. If one is extremely impatient, then it is optimal not to save period. This form of procastination was operationalized by Laison (1997) by twitsing the discount function we use in the exponential discounting model. Based on evidence from psychology, it appears that we discount the short time at a much higher rate than the long-term. 


Interventions
+++++++++++++

Opt-Out

Save More Tomorrow

Active Decisions

