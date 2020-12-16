.. _Intro:

Introduction
------------

Theory and Data
+++++++++++++++


.. |logo1| image:: /images/justice.png
   :align: middle
   :scale: 25%

The website `missingprofits.world <https://missingprofits.world/>`_ computes what each country looses to tax heavens. But how do we reform the tax system so that profits are taxed? What effects would a wealth tax have on inequality? How much revenue could it generate? 

We need micro theory to understand incentive effects created by taxes. We also need data. Economists like Emmanuel Saez and Gabriel Zucman study these questions with data and theory. 

|logo1|

.. |logo2| image:: /images/climat.png
   :align: middle
   :scale: 25%

A carbon tax could be effective to reduce emissions. But what are the effects of such taxes on the economy? In 2019, the Parlementary Budget Office of Canada write a `report <https://www.pbo-dpb.gc.ca/web/default/files/Documents/Reports/2019/Paris_Target/Paris_Target_FR.pdf>`_ which uses an economic model to compute these effects. The model combines data and theory. 



|logo2|

How should we set up the market for advertizing on the internet? What is the price of information? How should we price rankings in search engines? Hal Varian is the chief economist at Google. He is also the author of a well known micro theory book. In his everyday work, he combines theory and data to help companies in the new economy. See this `interview <https://www.youtube.com/watch?v=aUl3OVgT64Y>`_ with him.

.. |logo3| image:: /images/rules.jpeg
   :align: middle
   :scale: 75%
   
|logo3|

Data is everywhere. Theory helps make sense of it:

-  To understand behavior

-  To quantify effects of policies and assess them

-  Pricing and optimisation in firms 

This `article <https://www.quantamagazine.org/to-build-truly-intelligent-machines-teach-them-cause-and-effect-20180515/>`_ from Judea Pearl, a pioner in AI, warns of the dangers of using data without theory (in his words, cause to effect mechanisms). 

Mathematical Toolbox
++++++++++++++++++++

Math is essential to understand behavior, measure effects of changes in the environment (e.g. prices and taxes). Here is a explainer on a number of key tools we will be using. 

Marginal Analysis and Approximations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How do we describe a function, :math:`f(x)`?

-  Functions can be complicated, can be approximated by linear functions for small perturbations...

-  Locally, we can do an approximation of a smooth function for :math:`x` close to :math:`x_0`:

   .. math::


      f(x) \simeq f(x_0) + \alpha (x-x_0)  


To best the best :math:`\alpha`, we have that for  :math:`x` close to :math:`x_0`

.. math::

   
   &f(x) \simeq f(x_0) + \alpha (x-x_0) \\ \\ \iff & f(x) -f(x_0) \simeq \alpha (x-x_0)\\\\
    \iff & \alpha \simeq \frac{f(x) -f(x_0)}{x-x_0}  \simeq\; f'(x_0) 

where :math:`f'(\cdot)` is the first derivative of the function :math:`f(\cdot)`. So,

.. math::

   f(x) \simeq f(x_0) + f'(x_0) (x-x_0)  \\
   f(x) - f(x_0) \simeq f'(x_0) (x-x_0)  \\ 
   \Delta f \simeq f'(x_0) \Delta x 

If we want to predict the change in a function for a small change in its argument, the derivative is the best way to do it... 

Derivatives
^^^^^^^^^^^

**With constants**

-  :math:`f(x) = b + ax`: :math:`f'(x) = a`

-  :math:`f(x) = \log x`: :math:`f'(x) = \frac{1}{x}`

-  :math:`f(x) = e^{ax}`: :math:`f'(x) = ae^{ax}`

-  :math:`f(x) = x^a`: :math:`f'(x) = a x^{a-1}`


**With functions**

-  Product rule: :math:`f(x) = a(x)b(x)`, :math:`f'(x) = a'(x)b(x) + a(x)b'(x)`

-  Quotient rule: :math:`f(x) = \frac{a(x)}{b(x)}`,
   :math:`f'(x) = \frac{a'(x)b(x) - a(x)b'(x)}{b(x)^2}`

-  Chain rule: :math:`f(x) = a(b(x))`, :math:`f'(x) = a'(b(x))b'(x)`

-  Addition (substraction) rule: :math:`f(x) = a(x) + b(x)`, :math:`f'(x) = a'(x) + b'(x)`.


**Exercise A**: Find the first derivative of :
:math:`f(x)=\sqrt{x},\frac{x}{1+x},\frac{1}{2}x^2 + 2x-10,(1+\frac{x}{2})^2`.


**Exercise B**: Compute a first-order approximation of
:math:`f(x)=\sqrt{x}` around :math:`x_0`. 


**Higher Order Approximations**

We can compute higher order derivatives. The second derivative is the first derivative of the first derivative, etc. If these higher-order derivatives are not zero, we can improve the approximation of the function for small perturbations. 

We denote :math:`f'(x), f''(x)` or :math:`\frac{d f}{d x},\frac{d}{d x}(\frac{d f}{d x}) = \frac{d^2 f}{d x^2}` the second derivative of a function. In this course, you will not need to go above second derivatives. 

**Concavity and Convexity of Functions**

A function is concave if for all (pair of) points,  :math:`(x_1,x_2)` and all
:math:`0<\lambda<1`:

.. math::

   f(\lambda x_1 + (1-\lambda) x_2) \geq \lambda f(x_1) + (1-\lambda)f(x_2)

and convexe is false. We say stricly concave (or convex) if these inequalities are strict. The second derivative is useful for concavity and convexity. A function is stricly concave is the second derivate is negative for all points, and stricly convex if positive for all points. 

**Approximation and Optimum**

Consider the first order approximation

.. math::

   f(x_0+\Delta x) \simeq f(x_0)+ f'(x_0)\Delta x.

We have that if:

-  :math:`f'(x_0)>0`, a small change  :math:`\Delta x>0` increases
   :math:`f`

-  :math:`f'(x_0) <0` a small change :math:`\Delta x <0`
   increases :math:`f`

-  :math:`f'(x_0) =0`, then :math:`x_0` is the solution to :math:`\max_x f(x)`. 

This last first order condition (FOC) is necessary for an optimum. We need the first derivative to be zero at the optimum. 

The FOC is not sufficient. We also need a second condition, i.e. that the second derivative is negative. Here we skip the details, but this avoids inflexion points, where the FOC is satisfied but where we do not have a maximum or a minimum.

**Exercise C**: Find the maximum for the function :math:`f(x) = x(10-x)`.

Partial Derivatives
^^^^^^^^^^^^^^^^^^^

Consider the function :math:`f(x,y)`. The partial derivative changes one variable, keeping the others fixed:
:math:`f'_x(x,y) = \frac{\partial f(x,y)}{\partial x}`.

Total Differentiation
^^^^^^^^^^^^^^^^^^^^^

Sometime, it makes sense to look at combinations of :math:`(x,y)` that keep the function fixed to some value :math:`f(x,y) = \overline{f}`. We can invert the function, :math:`y=g(x,\overline{f})`. But, we can also use total differentiation which exploits linear approximations. 

We can perturb a function starting at a point and this equation holds:

.. math::

   \begin{aligned}
   df(x,y) = f'_x(x,y)dx + f'_y(x,y)dy\end{aligned}

The operator d denotes a change. If we set  :math:`df(x,y)=0`, we can re-arrange to obtain

.. math::

   \frac{dy}{dx}\Bigr|_{df=0} = -\frac{f'_x(x,y)}{f'_y(x,y)}

We add  :math:`df=0` to indicate that it is a derivative, keeping the value of the function fixed. 

**Exercise D**: Find :math:`\frac{dy}{dx}\Bigr|_{df=0}` using total differentiation :math:`f(x,y)=\log(xy)`. 

Homogeneity of a Function
^^^^^^^^^^^^^^^^^^^^^^^^^

A partial derivative provides information of how a function changes when we change one variable, keeping others fixed. But sometimes we want to understand how a function changes when all its variables change in the same proportion. Just like we want to know whether if we double a receipe for a cake, we get two cakes, or something else. This is called the degree of homogeneity of a function. There are two ways to proceed: 

Direct approach: A function is homogeneous of degree :math:`r` if for all
:math:`\lambda>0`,

.. math::

   f(\lambda x_1, \lambda x_2, ... \lambda x_n) = \lambda^r f(x_1,x_2,...,x_n)

Euler Theorem: If a function is homogeneous of degree :math:`r`, then:

.. math::

   r f(x_1,x_2,...,x_n) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}x_i.

**Exercise E**: Find the degree of homogeneity of the function 
:math:`f(x,y)=x^\alpha y^\beta` using both methods.

Maximum and Approximation
^^^^^^^^^^^^^^^^^^^^^^^^^

We need as many first order conditions as there are variables we maximize over. The necessary conditions are

:math:`f'_x(x,y)=0, f'_y(x,y)=0`

for a function :math:`f(x,y)`. The second order conditions are a bit more complicated and we do not cover it here. 

Constrained Maximization
^^^^^^^^^^^^^^^^^^^^^^^^

A constrained problem takes the form: 

.. math::

   \begin{aligned}
   \max_{x,y} \{ f(x,y): g(x,y) \leq m\}\end{aligned}

**Direct approach** 

If we can invert :math:`g(x,y)=m` to get a function :math:`y=q(x,m)`, then the solution of the constrained problem for :math:`x` is the same the solution to the unconstrained problem:

.. math::

   \begin{aligned}
   \max_{x} \{ f(x,q(x,m))\}\end{aligned}

For the FOC is :math:`f'_x(x,q(x,m)) + f'_y(x,q(x,m))q'(x,m) = 0`. We can solve for :math:`x^*` eand use :math:`y=q(x)` to find
:math:`y^*`. 

**Exercise F**: Maximize the function :math:`f(x,y) = \log x + \log y`
subject to the constraint :math:`x+y \le m`.

With more than 2 variables and many constraints, this approach is not pratical...

**The Lagrangian**


The method proposed by  `Lagrange <https://fr.wikipedia.org/wiki/Joseph-Louis_Lagrange>`_ is to solve for the pair :math:`(x,y)` using the set of three conditions:

.. math::

   \begin{aligned}
   f'_x(x,y) -  \lambda g'_x(x,y) = 0 \\
   f'_y(x,y) -  \lambda g'_y(x,y) = 0 \\
   g(x,y) = m\end{aligned}

where :math:`\lambda` is a lagrange multiplier. 

If we think backwards, these three equations are the first order conditions to the Lagragian:

.. math::

   \begin{aligned}
       \max_{x,y,\lambda} L(x,y,\lambda) = f(x,y) - \lambda (g(x,y)-m)\end{aligned}

The lagrangian :math:`L(x,y,\lambda)` is a modified objective function which penalizes the constraint added to the unconstrained maximization of the objection function. If :math:`\lambda = 0`, the first two FOC above are the unconstrained FOC, :math:`f'_x(x,y)=0` and :math:`f'_y(x,y)=0` which yield the unconstrained optimum. If one of the constraint is binding (if  :math:`\lambda \neq 0`) will we get a different solution. 

**Exercise G**: Maximize the function :math:`f(x,y) = \log x + \log y`
under the constraint :math:`x+y \le m` using a Lagrangian.

Note on logs
^^^^^^^^^^^^

In these notes, we use :math:`\log` to denote the logarithm with base :math:`e=2.718281828459` and not base 10. So, it is the natural log (:math:`\ln = \log_e`). Python also uses this base in the numpy library. 
