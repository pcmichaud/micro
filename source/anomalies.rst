.. _Intro:

Anomalies
---------

Household finance is concerned with financial choices made by households, from savings, to holding debt, to investing, to retiring and deciding which insurance products to purchase. Household finance is potentially filled with behavior which do not seem to agree with our intuition as economists. These are often called anomalies. But are they? Here are some primary examples:

Annuities
+++++++++

In their simplest form, annuities allow someone to receive a certain stream of payments until death against an immediate investment. An annuity has the advantage of providing an insurance against longevity risk. That is the risk of outliving one's savings or living long. Read the story of `Jeanne Calment <https://en.wikipedia.org/wiki/Jeanne_Calment>`_ who lived to be 122 years but had insurance against longevity risk.   

While that risk appears real, few individuals nearing retirement hold little annuities outside public pensions. 

Should people buy annuities? Read about these opposing views:

* Yes: `Financial Post <https://financialpost.com/personal-finance/annuities-more-income-and-less-worry>`_ 
* No: `Market Watch <https://www.marketwatch.com/story/why-annuities-are-a-bad-idea-for-almost-everyone-2018-03-05>`_

Savings
+++++++

There is a significant fraction of the population that saves little on their own for retirement. Others do not have sufficient liquid saving to cover expenses for two months. 

Is this cause for concern? Read about two opposing views:

* Not a concern: `C.D. Howe Commentary <https://www.cdhowe.org/sites/default/files/attachments/research_papers/mixed/commentary_428.pdf>`_
* Cause for concern: `Center for Policy Alternatives <https://www.policyalternatives.ca/sites/default/files/uploads/publications/Ontario%20Office/2015/07/What_Me_Worry%20FINAL.pdf>`_

Investment
++++++++++

When it comes to portfolio choice, many  put all their eggs in the same basket, invest more in domestic stocks, and trade often. Because they are chasing returns, they often end up buying high and selling low. Some do not understand fees. Others invest in taxable accounts without opening an RRSP or TFSA. 

Should we let people invest or promote the use of financial advisors?

* Invest in index funds according to `Warren Buffet <https://www.businessinsider.com/warren-buffett-best-investment-advice-2017-8>`_
* Maybe advisors: `Forbes <https://www.forbes.com/sites/wadepfau/2015/07/21/the-value-of-financial-advice/?sh=44a94eba1333>`_


Household Debt 
++++++++++++++

We observe lots of household debt, even into retirement. And it is increasing in every segment of the population. 

Is this cause for concern?

* Maybe: `Toronto Star <https://www.thestar.com/politics/political-opinion/2019/11/30/should-canada-be-worried-about-record-consumer-debt.html>`_
* Yes, lots are getting into serious debt issues: `Bloomberg <https://www.bnnbloomberg.ca/businessweek/canadians-are-feeling-the-debt-burn-1.1234735>`_


The bottom line is that behind each of these potential anomalies there are serious policy questions as well as business opportunities. 

Why BEF?
++++++++

Each of these situations started with observing what people do. We need data for that. Luckily we have some and many sources exist. This is the first step to understanding a household finance problem. We first need to understand the facts. In particular, we need to understand the heterogeneity across people and trends over time. This is a serious task.  

Then, interpreting the facts to answer a question requires models, whether it is explicit or implicit. Making sense of many statistics to answer a question calls a conceptual framework into mind. This allows to go from correlations to causation, mechanisms, which inform, if we have the right framework, on what can be done if we want to change the outcome. 

There are two ways of thinking about behavioral economics.

One is positive in nature. We want to have a model of how people make decisions. We might build a model from scratch. More often, we will start from the workhorse neoclassical model, say expected utility if this is behavior that involves risk, or discounted utility if it involves time. That model may do well already in explaining the facts. Some of the biggest advances in behavioral economics have come from adding a simple twist, with important consequences, to otherwise standard models of choice. After all, neoclassical economists were behavioral economists with behavioral theories for explaining patterns of behavior. Lots in these models fit the data well. Friedman, von Neuman and Morgenstern, Fisher,  Modigliani, Yaari and many others were all preoccupied with having a good model of what agents do in order to predict how they would respond to incentives for example.  

Behavioral economics was born as a separate field from mainstream neo-classical microeconomics because standard models often fail to fit observed behavior. They may need enrichment to capture some of the behaviors we observe. Some economists were first relunctant to embrace departures from the standard model. This inertia is common in science.  What characterizes most behavioral economists these days is that they combine theory, data and experimentation  to understand what we need to take into account to enrich our workhorse model. The distinction between what is behavioral and what is mainstream is rapidly fading away... 

But there is another motivation, normative, for doing behavioral economics. We asked the question earlier: are these patterns cause for concern? Are they anomalies? 

How should an economist answer a question like that?  This is a hard question. A natural starting point is to think of a benchmark: what should people do optimally and does their action makes them worse off relative to that benchmark? One benchmark dear to economists is the neoclassical model, which means everything and nothing, but perhaps in its most simplistic form for our purposes an expected discounted utility model with unbiased expectations applied to modelling financial decisions. If that model maps well into what people are doing, it is hard to think of why the observed behavior is a cause for concern. People are acting close to optimally according to our benchmark, with preferences which respect certain axioms, are time consistent and were expectations are unbiased. Despite having its own limits, e.g. how do we know the preferences of someone?, this is the approach taken by many behavioral economists. 
Turns out, people do not act close to optimally by that metric. There is a gap, no matter how rich our neoclassical model is, between what people do and what we think they should be doing. After all, we are humans, with emotions, and we have limited cognitive abilities. We often lack information and it is costly to figure out things. 


When we are able to develop a satisfactory model of how decisions are made. We can then compare it to the benchmark. Understand where do deviations come from and then, find ways to help individuals make choices closer to the benchmark. This approach can take the form of education, decision aids, financial advice or even what is called choice architecture, a topic we will encounter later in the course. Are these interventions efficient? How much do they cost? Are they leading to undesirable outcomes? Equiped with models, one is better able to answer these questions. 

Is Theory Useful?
+++++++++++++++++

Modelling behavior that deviates from standard models often takes us to more complicated models. Models are useful because they make our statements sharper, allow us to make falsiable predictions. But we do not want to do theory for the sake of doing theory. When possible, we will try and keep the math simple. For example, there is no need to consider a multi-period model of intertemporal choice if we can convey basic ideas in a two-period model. Hence, the requirements for this course is that you have a basic understanding of calculus and of intermediate microeconomics (see my class notes for 20-851A if that is far in your mind, in particular the risks and time lectures). But we will also want to develop abilities to roam free from simple models into more realistic ones by getting a sense of how to use numerical methods (programming) to solve models. This is a skill that will seem difficult at first. But will prove useful by the end of the course. 

Empirical Methods
+++++++++++++++++

Data is needed to observe the facts. One needs to be able to analyze data, describe it. We will spend quite a bit of time doing that. Little econometrics or statistics is needed for the class, But learning how to manipulate micro data is an essential skill that we will develop. Dealing with measurement error and other problems that plague data is important. I will be heavily using Python. But note that you can use Stata or R if you feel more comfortable. If you are not familiar with Python, there are a series of tutorials that are available in my lectures. One bonus is that one can use Python to do both numerical work as well as data work which is not the case for Stata.  

We will also look into methods to elicit preferences, expectations and learn from choices in experimental settings. The idea is that by the time you finish this course, you are able to review critically a study using elicitation or experimental methods and if you go on to do research on your own, are able to conduct an experiment. 

Coming back to Anomalies
++++++++++++++++++++++++

The course is structured around 4 areas of choice in household finance we started with above. These were not picked at random as they will allow us to browse trough a wide array of models and methods...  We will learn in each case to construct basic facts, develop an understanding of what the benchmark model predicts, and review how choices can be improved with an intervention toolkit. We will roughly spend three courses on each topic, covering the facts, the theory and interventions. 


