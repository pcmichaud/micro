.. raw:: latex

   \frame{\titlepage}

.. raw:: latex

   \frame{\tableofcontents}

Does a Tax on Fuel Promote Public Transit?

.. raw:: latex

   \subfloat[price effect]{\includegraphics[scale=0.185]{price.png}}

.. raw:: latex

   \subfloat[income effect]{\includegraphics[scale=0.18]{income.png}}

.. raw:: latex

   \subfloat[cross effect]{\includegraphics[scale=0.18]{transit.png}}

Price and Income Effects
========================

Demand Preferences
~~~~~~~~~~~~~~~~~~

**The problem**

-  Fuel (X) and Public Transit (Y)

-  Utility :math:`U(X,Y)`

-  Budgand constraint: :math:`p_X Y+ p_Y Y = I`

**Optimizing with a given constraint:**

-  :math:`(X^*, Y^*)` such that

   .. math::

      \begin{aligned}
       \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y} \textrm{ and }
      p_X X + p_Y Y = I\end{aligned}

-  At the optimum: the budget is respected and we are indifferent
   between giving up some :math:`X` to acquire :math:`Y` and vice versa.

-  Two equations, two variables: we can solve for :math:`X^*` and
   :math:`Y^*` as a function of :math:`(p_X,p_Y,I)`

Example

-  :math:`U(X,Y) = \log X +  2\log Y`

   .. math::

      \begin{aligned}
      \frac{dU}{dX}\Bigg/\frac{dU}{dY} &=& \frac{p_X}{p_Y} \iff \frac{1/X}{2/Y} = \frac{p_X}{p_Y} \\ \iff  p_Y Y = 2p_X X \end{aligned}

-  With :math:`p_X X + p_Y Y =  I` implies

   .. math:: X^* = \frac{I}{3p_X} \textrm{ and } Y^* = \frac{2I}{3p_Y}

How :math:`X^*` and :math:`Y^*` Vary as a Function of :math:`I`
**Engel’s curve**

-  Individual demands :math:`X(p_X,p_Y,I)`, :math:`Y(p_X,p_Y,I)`.

-  Engel’s curve for :math:`X`: how does :math:`X^*` change when
   :math:`I` changes

-  Proportion of the budget dedicated to :math:`X`:
   :math:`s_X = \frac{p_X X}{I}`

**Normal goods**

-  A good is said to be normal if and only if the demand of the good
   increases with income (constant prices)

-  Example: fuel (luxury car)

**Inferior goods**

-  A good is said to be inferior if demand decreases as income increases
   (constant prices)

-  Example: it depends on initial income levels, but junk food (kraft
   dinner), lottery tickets, perhaps public transit?

How the Demands :math:`X^*` and :math:`Y^*` Change with Prices Keep
:math:`p_Y` and :math:`I` constant. How does the demand adjust to an
increase of :math:`p_X`?

Decomposing Demand Changes When fuel price :math:`p_X` increases, two
forces:

-  Public transit is more affordable than a car (fuel): Want to consume
   more of the cheaper good. This is the **substitution effect**.

   .. math:: \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y}

-  Purchasing power decreases: need more income to by the same basket of
   goods as before the change: **income effect**.

**Objective:** Identify price effects and income effects

Compensated Demand

**Context**

-  Reference price :math:`(p_X,p_Y)`, Reference income :math:`I`, new
   price :math:`(\hat p_X,p_Y)`

-  Reference demand, :math:`X(p_X,p_Y,I)`, reference (indirect) utility
   :math:`V(p_X,p_Y,I)`

-  New demand, :math:`X(\hat p_X, p_Y, I)`, new (indirect) utility
   :math:`V(\hat p_X,p_Y,I)`.

Compensated Demand **Definition**

-  Compensated income: income :math:`I^{cmp}` such that we can achieve
   the reference utility with the new prices

   .. math:: V(p_X,p_Y, I) = V(\hat p_X, p_Y,  I^{cmp})

-  Compensated demand :math:`X^{cmp}= X(\hat p_X, p_Y,  I^{cmp})`

-  | **Property:** IF :math:`\hat p_X > p_X`, then
     :math:`X^{cmp}<X(p_X,p_Y,I)`
   | the compensated demand of :math:`X` is decreasing in terms of
     :math:`p_X`.

Compensated Demand

**Exercise A**: Calculate the compensated income and demand for
:math:`X` if :math:`U(X,Y) = XY` and :math:`p_XX+p_YY \le I` for a price
change :math:`\hat p_X > p_X`.

Substitution and Income Effects

**Substitution effect**

-  Change in demand caused by relative price change, keeping utility
   constant:

-  Substitution Effect :math:`=` Compensated demand - Reference demand

   .. math:: \Delta X^{{cmp}} =  X(\hat p_X,p_Y,I^{cmp}) - X(p_X,p_Y,I)

**Income effect**

-  A change in demand caused by a change in purchasing power keeping
   prices constant

-  Income effect :math:`=` New demand - Compensated demand

.. math:: \Delta X^{I} = X(\hat p_X,p_Y,I) - X(\hat p_X,p_Y,I^{cmp})

| Approximating the Compensated Income Consider a small price change
  :math:`\hat p_X = p_X + \Delta p_X`. To keep notation simple:
  :math:`X^* = X(p_X,p_X,I)`, :math:`Y^* = Y(p_X,p_Y,I)`

We define :math:`I^{cmp}= I + \Delta I^{cmp}`,
:math:`X^{cmp}= X^* + \Delta X^{cmp}` and
:math:`Y^{cmp}= Y^* + \Delta Y^{cmp}`.

.. math::

   \begin{aligned}
   I^{cmp}& =  \hat p_X X^{cmp}+  p_Y Y^{cmp}\\
    & =  (p_X + \Delta p_X)(X^* + \Delta X^{cmp}) + p_Y(Y^* + \Delta Y^{cmp})\\ 
     &=  \underbrace{p_X X^* + p_YY^*}_{=I} +\underbrace{\Delta p_X \Delta X^{cmp}}_{\simeq 0} + \Delta p_X X^* \\
     & \quad \quad \quad + \underbrace{ p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}}}_{=0}\\ & \simeq I+  \Delta p_X X^* \\
    \Delta I^{cmp}&\simeq \Delta p_X X^*\end{aligned}

A Trick to identify Compensated Income

Why does :math:`p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}} = 0`?

#. :math:`(X^*,Y^*)` and :math:`(X^{cmp},Y^{cmp})` are on the same
   indifference curve, which implies

   .. math:: \frac{\Delta Y^{cmp}}{\Delta X^{cmp}} = MRS_{X\to Y}

#. :math:`(X^*,Y^*)` is optimal at the prices :math:`p_X, p_Y`, which
   implies :math:`MRS_{X\to Y} = -\frac{p_X}{p_Y}`.

#. Therefore, :math:`p_X \Delta X^{cmp}+ p_Y \Delta Y^{cmp}= 0`.

**Exercise B**: Check if this approximation works for
:math:`U(X,Y) = XY` with reference prices and income
:math:`(p_X,p_Y,I) = (1,1,100)` and :math:`\Delta p_X = 1` and
:math:`\Delta p_X = 0.1`.

The Slutsky Equation This equation comes from the decomposition of the
price elasticity of demand.

To keep notation simple, consider

.. math::

   \begin{aligned}
    X^* &= X(p_X,p_Y,I), &     X(p_X + \Delta p_X, p_Y,I) &= X^* + \Delta X^*,\\ && X(p_X + \Delta p_X, p_Y,I) &= X^{cmp}+\Delta X^I\end{aligned}

We get

.. math::

   \begin{aligned}
   \underbrace{\Delta X^*}_{\text{Total effect}} = \underbrace{\Delta X^{cmp}}_{\text{Substitution effect}} + \underbrace{\Delta X^I}_{\text{Income effect}}\end{aligned}

**Exercise D**: Find the income and substitution effects in exercise C.

The Slutsky Equation Since

.. math:: \Delta X^I =   -\frac{\partial X}{\partial I} \Delta I^{cmp}=  -\frac{\partial X}{\partial I}  \Delta p_X X^*

 Then,

.. math::

   \begin{aligned}
   \Delta X^* &=   \underbrace{\Delta X^{{cmp}}}_{\leq 0} -   \underbrace{\frac{\partial X}{\partial I}\times \Delta p_X X^*}_{\geq 0 \text{ if normal, } <0 \text{ if inferior}} \end{aligned}

 As an elasticity,

.. math::

   \begin{aligned}
   \frac{\Delta X^*}{\Delta p_X}\frac{p_X}{X^*} & = \frac{\Delta X^{cmp}}{\Delta p_X}\frac{p_X}{X^*} - \frac{\partial X}{\partial I} \Delta p_X X^*\times\frac{p_X}{\Delta p_X X^*}\frac{I}{I} \end{aligned}

 The Slutsky equation is given by:

.. math:: \eta_{X,p} and = \eta^{cmp}_{X,p}  - \eta_{X,I} \times s_X

Properties of Demand Functions
==============================

The nature of goods

The goods :math:`X` and :math:`Y` are:

-  Substitutes: if the cross effect is
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} >0`

-  Compléments: if the cross effect is
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} <0`

Properties

-  Homogeneity of degree 0

   .. math:: X(\lambda p_X,\lambda p_Y,\lambda I) = X(p_X,p_Y,I)

-  Symetry:

   .. math:: \frac{\partial X^{cmp}}{\partial p_Y} =\frac{\partial Y^{cmp}}{\partial p_X}

-  Additivity:

   .. math:: p_X \frac{\partial X(p_X,p_Y,I)}{\partial I} + p_Y \frac{\partial Y(p_X,p_Y,I)}{\partial I} = 0

-  Negativity:

   .. math:: \frac{\partial X^{cmp}}{\partial p_X}<0,\frac{\partial Y^{cmp}}{\partial p_Y}<0

Special Cases
=============

Giffen Goods **Direction of income and wealth effects**

-  When indifference curves are convex, the compensated demand for
   :math:`X` decreases as :math:`p_X` increases

-  Income effects depend on whether the good is normal or inferior at
   reference income and prices.

-  If normal good, price increase causes a negative income effect (same
   direction as price effect)

-  If inferior good, price increase causes a positive income effect
   (opposite direction)

**Giffen Goods**

-  If the income effect is larger than the substitution effect, as the
   price :math:`p_X` increases, the demand for :math:`X` increases.

-  Classic example : Potatoes in Ireland (circa 1850, according to
   legend).

Chinese Rice Subsidy

.. raw:: latex

   \subfloat{\includegraphics[scale=0.3]{china.png}}

.. raw:: latex

   \subfloat{\includegraphics[scale=0.5]{elasticity_share.png}}

Doctors How can a wage increase cause a drop in work hours?

.. raw:: latex

   \centering

.. figure:: docteurs.png
   :alt: `TVA
   Nouvelles <https://www.tvanouvelles.ca/2018/05/17/medecins-de-familles-la-moitie-travaillent-4-jours-et-moins>`__

   `TVA
   Nouvelles <https://www.tvanouvelles.ca/2018/05/17/medecins-de-familles-la-moitie-travaillent-4-jours-et-moins>`__

Price and Costs of Living Indexes

To measure changes in costs of living, we often use consumption price
indices. A very common one is the Laspeyres index:

.. math:: \pi_L = \frac{\hat p_X X + \hat p_Y Y}{p_X X + p_Y Y}

-  The Quebec Pension Plan (QPP) and private pension plans are often
   indexed using this kind of index.

-  Is this a good index to capture an increase in the cost of living?

The Ideal Price Index

Need account for behavioral changes. Therefore, a price increases
implies substitution.

-  Following a price increase for the good :math:`X`, the necessary
   compensation to keep welfare constant is

   .. math:: \pi_I =  \frac{I^{cmp}}{I}

   .

-  In a Cobb-Douglas situation :math:`u(X,Y)=X^{\alpha}Y^{1-\alpha}`:

   .. math:: \pi_I = \frac{I^{cmp}}{I} = \left(\frac{\hat p_X}{p_X}\right)^\alpha
