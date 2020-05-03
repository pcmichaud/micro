Introduction
------------

Théorie et données
^^^^^^^^^^^^^^^^^^

.. |logo1| image:: /images/justice.png
   :width: 100%
   :align: middle
   :alt: Voir `missingprofits.world <https://missingprofits.world/>`_ pour une estimation de ce que perd chaque pays vers les paradis fiscaux

.. |logo2| image:: /images/climat.png
   :width: 100%
   :align: middle
   :alt: Directeur parlementaire du Budget 2019

.. |logo3| image:: /images/rules.jpeg
   :width: 100%
   :align: middle
   :alt: Hal Varian est l’économiste en chef chez Google

.. |logo4| image:: /images/AI.png
   :width: 100%
   :align: middle
   :alt: The Economist, 2015

+---------+---------+---------+---------+
| |logo1| | |logo2| | |logo3| | |logo4| |
+---------+---------+---------+---------+

Les données sont partout. La théorie aide à en faire du sens:

-  Comprendre les comportements (e.g. tester des théories)

-  Quantifier des effets pour porter des jugements positifs et normatifs
   sur des politiques

-  Tarification et optimisation en entreprise

-  Un danger est d’exploiter les données sans cadre théorique (voir cet
   `article <https://www.quantamagazine.org/to-build-truly-intelligent-machines-teach-them-cause-and-effect-20180515/>`__
   sur l’intelligence artificielle)

Structure du cours
^^^^^^^^^^^^^^^^^^

Les thèmes couverts
+++++++++++++++++++

-  Consommation

-  Les marchés et le bien-être

-  La production: choix de production

-  Les comportements stratégiques

-  Les enchères

Évaluation
++++++++++

-  Un devoir individuel (5%)

-  3 devoirs en équipe (30%)

-  Intra (25%) et final (40%)

Autres remarques
++++++++++++++++

-  Auxiliaire enseignement: Nicholas Trottier-Lacourse

-  Référence (non-obligatoires) pour cours:

   -  Hal Varian (2015). *Introduction à la microéconomie*, Deboeck

   -  Hal Varian (2008). *Analyse microéconomique*, Deboeck

-  Théorie et pratique (programmation sur Google Collab)

Rappel Mathématique
^^^^^^^^^^^^^^^^^^^

L’analyse marginale et les approximations
+++++++++++++++++++++++++++++++++++++++++

Astuce de l’approximation:

-  Fonctions généralement compliquées, fonctions linéaires simples...

-  Localement, on peut faire une approximation de toute fonction "lisse"
   à :math:`x_0`, pour :math:`x` près de :math:`x_0`:

   .. math::

      \begin{aligned}
          f(x) \simeq f(x_0) + \alpha (x-x_0) + ...  \end{aligned}

**Exercice A**: Montrer graphiquement une approximation de premier
ordre.

Lien avec dérivée Pour :math:`x` près de :math:`x_0`

.. math::

   \begin{aligned}
   &f(x) \simeq f(x_0) + \alpha (x-x_0) \\ \\ \iff & f(x) -f(x_0) \simeq \alpha (x-x_0)\\\\
    \iff & \alpha \simeq \frac{f(x) -f(x_0)}{x-x_0}  \simeq\; f'(x_0) \quad \text{par définition}\end{aligned}

 Alors

.. math::

   \begin{aligned}
   &f(x) \simeq f(x_0) + f'(x_0) (x-x_0) \quad \text{ ou }\\ \\ &f(x) - f(x_0) \simeq f'(x_0) (x-x_0) \quad \text{ ou } \\ \\
   &\Delta f \simeq f'(x_0) \Delta x\end{aligned}

Les dérivées de fonctions
^^^^^^^^^^^^^^^^^^^^^^^^^


**Avec des constantes**

-  :math:`f(x) = b + ax`: :math:`f'(x) = a`

-  :math:`f(x) = \log x`: :math:`f'(x) = \frac{1}{x}`

-  :math:`f(x) = e^{ax}`: :math:`f'(x) = ae^{ax}`

-  :math:`f(x) = x^a`: :math:`f'(x) = a x^{a-1}`

**Avec des fonctions**

-  :math:`f(x) = a(x)b(x)`, :math:`f'(x) = a'(x)b(x) + a(x)b'(x)`

-  :math:`f(x) = \frac{a(x)}{b(x)}`,
   :math:`f'(x) = \frac{a'(x)b(x) - a(x)b'(x)}{b(x)^2}`

-  :math:`f(x) = a(b(x))`, :math:`f'(x) = a'(b(x))b'(x)`

-  :math:`f(x) = a(x) + b(x)`, :math:`f'(x) = a'(x) + b'(x)`.


**Exercice B**: Trouvez les dérivées de :
:math:`f(x)=\sqrt{x},\frac{x}{1+x},\frac{1}{2}x^2 + 2x-10,(1+\frac{x}{2})^2`.

** Approximations d’ordres supérieurs **

On peut pousser l’astuce plus loin

-  Polynome d’ordre 2 assez simple...

-  Alors, on approxime par deuxième ordre

-  Polynome d’ordre :math:`k` …

  L’astuce porte le nom d’approximation de Taylor. Connectée aux
dérivées d’ordres supérieurs d’une fonction:

.. math::

   \begin{aligned}
       f(x) = f(x_0) + f'(x_0)(x-x_0) +\frac{1}{2}f''(x_0)(x-x_0)^2 + \ldots \end{aligned}

 On dénote :math:`f'(x), f''(x)` ou :math:`\frac{d f}{d x},\frac{d}{d x}(\frac{d f}{d x}) = \frac{d^2 f}{d x^2}`.

**Concavité et Convexité des fonctions**

Une fonction est convexe si pour tous points :math:`(x_1,x_2)` et tout
:math:`\lambda>0,0<\lambda<1`:

.. math::

   \begin{aligned}
   f(\lambda x_1 + (1-\lambda) x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2)\end{aligned}

et concave si l’inverse est vrai. On dit strictement si les inégalités
sont strictes.

**Approximation et maximisation (sans contrainte)**

Considérons l’approximation de premier ordre:

.. math::

   \begin{aligned}
    f(x_0+\Delta x) \simeq f(x_0)+ f'(x_0)\Delta x \end{aligned}

Observons que:

-  Si :math:`f'(x_0)>0` un petit changement :math:`\Delta x>0` augmente
   :math:`f`

-  Si :math:`f'(x_0) <0` un petit changement :math:`\Delta x <0`
   augmente :math:`f`

-  Si :math:`x_0` est la solution de :math:`\max_x f(x)`, il faut que
   :math:`f'(x_0) =0`

**Maximisation sans contrainte**

Considérons l’approximation de deuxième ordre:

.. math::

   \begin{aligned}
    f(x_0+\Delta x) \simeq f(x_0) + f'(x_0)\Delta x +\frac{1}{2}f''(x_0)\Delta x ^2  \end{aligned}

Pour un maximum (local), il faut que :math:`f'(x_0)=0` (CPO) et
:math:`f''(x_0)<0` (CDO). Observons que:

-  Si :math:`f'(x_0) = 0` mais :math:`f''(x_0)>0`, alors
   :math:`f(x_0+\Delta x) > f(x_0)`.

-  f’(x) doit être positif quand :math:`\Delta x <0` et négatif quand
   :math:`\Delta x>0`.

**Exercice C**: Montrer graphiquement l’optimum d’une fonction concave.

Théorème de l’enveloppe
^^^^^^^^^^^^^^^^^^^^^^^

Considérons la fonction :math:`f(x,p)` où :math:`p` est hors de contrôle
(exogène). On dénote:

.. math::

    V(p) = \max_x f(x,p) , \quad x^*(p) = \arg \max_x f(x,p)

On a que :math:`V(p) = f(x^*(p),p)`. 

Ainsi,

.. math::

   V'(p) = f'_x(x^*(p),p)x^{*'}(p) + f'_p(x^*(p),p)
   
Or, puisque :math:`x^*(p)` maximise :math:`f(x,p)`, :math:`f'_x(x^*(p),p) = 0` par définition. Ainsi, :math:`V'(p) = f'_p(x^*(p),p)`.

**Exercice D**: Démontrer la valeur de cette approximation pour la
fonction :math:`V(p) = (10 - p\frac{x}{2})x`.

**Maximisation avec contrainte**

Considérons le problème:

.. math::

   \begin{aligned}
       \max_x \{f(x):x \leq x_0\}\end{aligned}

Un maximum est atteint si :math:`f'(x)=0` (nécessaire). Or si
:math:`f'(x)>0` pour tout :math:`x \leq x_0`, le maximum contraint est
:math:`x_0`. Relacher la contrainte marginalement de :math:`x_0` fait
gagner :math:`f'(x_0)\Delta x`.

**Plusieurs variables**

Supposons la fonction :math:`f(x,y)`. La dérivée partielle se fait en
gardant fixe (ou exogène) les autres variables:
:math:`f'_x(x,y) = \frac{\partial f(x,y)}{\partial x}`.

**La différentielle totale**

Les combinaisons de :math:`x,y` tels que :math:`f(x,y) = \overline{f}`)
peuvent être trouvées par solution directe, :math:`y=g(x,\overline{f})`.
Mais on peut décrire ces combinaisons plus facilement en utilisant la
différentielle totale (une approximation linéaire):

On peut décrire la forme de cette fonction par:

.. math::

   \begin{aligned}
   df(x,y) = f'_x(x,y)dx + f'_y(x,y)dy\end{aligned}

Si on pose :math:`df(x,y)=0`,

.. math::

   \begin{aligned}
   \frac{dy}{dx}\Bigr|_{df=0} = -\frac{f'_x(x,y)}{f'_y(x,y)}\end{aligned}

**Exercice E**: Trouvez :math:`\frac{dy}{dx}\Bigr|_{df=0}` par
différentielle totale pour :math:`f(x,y)=\log(xy)`.

Homogénéité des fonctions
^^^^^^^^^^^^^^^^^^^^^^^^^

Une fonction est homogène de degré :math:`r` si pour tout
:math:`\lambda>0`,

.. math::

   \begin{aligned}
   f(\lambda x_1, \lambda x_2, ... \lambda x_n) = \lambda^r f(x_1,x_2,...,x_n)\end{aligned}

Si une fonction est homogène de degré :math:`r`, alors ceci est aussi
vrai (théorème d’Euler):

.. math::

   \begin{aligned}
   r f(x_1,x_2,...,x_n) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}x_i\end{aligned}

**Exercice F**: Trouvez le degré d’homogénéité de la fonction
:math:`f(x,y)=x^\alpha y^\beta` des deux façons.

**Approximation et Maximum**

.. math::

   \begin{aligned}
   f(x,y) \simeq f(x_0,y_0) + f'_x(x_0,y_0)(x-x_0) + f'_y(x_0,y_0)(y-y_0)  \\
       +\frac{1}{2}f''_{xx}(x_0,y_0)(x-x_0)^2  + \frac{1}{2}f''_{yy}(x_0,y_0)(y-y_0)^2 + \\
       +f''_{xy}(x_0,y_0)(x-x_0)(y-y_0) \end{aligned}

Condition pour un maximum:

-  Nécessaire: :math:`f'_x(x,y)=0, f'_y(x,y)=0`

-  Suffisante:
   :math:`\frac{1}{2}f''_{xx}(x_0,y_0)(x-x_0)^2  + \frac{1}{2}f''_{yy}(x_0,y_0)(y-y_0)^2 +f''_{xy}(x_0,y_0)(x-x_0)(y-y_0)<0`

**Maximisation avec contrainte**

Approche directe. Quand le problème prend la forme:

.. math::

   \begin{aligned}
   \max_{x,y} \{ f(x,y): g(x,y)=m\}\end{aligned}

Et qu’on peut inverser :math:`g(x,y)=m` tel que :math:`y=q(x,m)`, alors
la solution du problème contraint pour :math:`x` est la même que celui
de :

.. math::

   \begin{aligned}
   \max_{x} \{ f(x,q(x))\}\end{aligned}

La CPO est :math:`f'_x(x,q(x,m)) + f'_y(x,q(x,m))q'(x,m) = 0`. On peut
résoudre pour :math:`x^*` et utiliser :math:`y=q(x)` pour trouver
:math:`y^*`. Facile, mais quand plus de 2 variables?

**Exercice G**: Maximiser la fonction :math:`f(x,y) = \log x + \log y`
sous la contrainte :math:`x+y \le m`.

Le Lagrangien
^^^^^^^^^^^^^

La méthode de Lagrange consiste à résoudre pour :math:`(x,y)`,

.. math::

   \begin{aligned}
   f'_x(x,y) -  \lambda g'_x(x,y) = 0 \\
   f'_y(x,y) -  \lambda g'_y(x,y) = 0 \\
   g(x,y) = m\end{aligned}

Ce sont les CPO du lagrangien:

.. math::

   \begin{aligned}
       \max_{x,y,\lambda} f(x,y) - \lambda (g(x,y)-m)\end{aligned}

**Exercice H**: Maximiser la fonction :math:`f(x,y) = \log x + \log y`
sous la contrainte :math:`x+y \le m` par la méthode du Lagrangien.

**L’interprétation du multiplicateur**

La valeur de :math:`\lambda` n’est pas nécessaire pour résoudre les
valeurs optimales de :math:`x` et :math:`y`. Mais elle a une
interprétation.

Par le théorème de l’enveloppe, si

.. math:: V(m) = \max_{x,y,\lambda} f(x,y) - \lambda (g(x,y)-m)

alors :math:`V'(m) = \lambda`.

**Exercice I**: Démontrer dans le problème précédent qu’une augmentation
marginale de :math:`m` sur le maximum est bien égale à :math:`\lambda`.

Notebook Python
^^^^^^^^^^^^^^^

Ouvrir dans google collab |ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/DebutPython.ipynb
