.. _Intro:

Introduction
------------

Théorie et données
++++++++++++++++++




Le site `missingprofits.world <https://missingprofits.world/>`_ calcule ce que perd chaque pays aux paradis fiscaux. Mais comment rapatrier ces profits? Quel effet aurait une taxe sur la richesse pour réduire les inégalités? On a besoin de la théorie pour comprendre l'effet potentiel des incitatifs. Ensuite, les données pour estimer ces effets. Les économistes Emmanuel Saez et Gabriel Zucman s'intéressent à cette question avec théorie et données. 

.. image:: /images/justice.png
    :align: center
    :scale: 25%


Une taxe sur le carbone pourrait être un bon moyen de lutter contre le réchauffement climatique. Mais quels sont les effets d'une telle taxe sur l'économie? En 2019, le Directeur parlementaire du Budget du Canada dans un `rapport <https://www.pbo-dpb.gc.ca/web/default/files/Documents/Reports/2019/Paris_Target/Paris_Target_FR.pdf>`_ utilise un modèle d'équilibre général pour calculer ces effets. Le modèle utilise données et théorie. 


.. image:: /images/climat.png
    :align: center
    :scale: 25%

Comment structurer le marché de la publicité sur internet? Quel est le prix de l'information? Comment rémunérer le classement dans les moteurs de recherche? Hal Varian est l’économiste en chef chez Google. Il est l'auteur d'un livre de théorie très populaire en microéconomie, mais aussi quelqu'un qui conjugue au quotidien données et théorie pour aider les entreprises de la nouvelle économie. Voir cette `entrevue <https://www.youtube.com/watch?v=aUl3OVgT64Y>`_ avec lui.

.. image:: /images/rules.jpeg
    :align: center
    :scale: 75%


Les données sont partout. La théorie aide à en faire du sens:

-  Comprendre les comportements (e.g. tester des théories)

-  Quantifier des effets pour porter des jugements 
   sur des politiques

-  Tarification et optimisation en entreprise

Cet `article <https://www.quantamagazine.org/to-build-truly-intelligent-machines-teach-them-cause-and-effect-20180515/>`_ de Judea Pearl, pourtant un des pionniers de l'intelligence articifielle, met en garde contre une utilisation des données sans cadre théorique. 

Rappel mathématique
+++++++++++++++++++

Les mathématiques sont essentielles, en particulier le calcul différentiel, afin d'analyser le comportement, mesurer l'effet de changements dans l'environnement (prix, taxes). Voici un (rappel) des concepts qui sont importants pour le cours.  

L’analyse marginale et les approximations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Comment décrire une fonction :math:`f(x)`?

-  Fonctions généralement compliquées, fonctions linéaires simples...

-  Localement, on peut faire une approximation de toute fonction *lisse*
   pour :math:`x` près de :math:`x_0`:

   .. math::


      f(x) \simeq f(x_0) + \alpha (x-x_0)  


Pour trouver le meilleur :math:`\alpha`, on a que pour :math:`x` près de :math:`x_0`

.. math::

   
   &f(x) \simeq f(x_0) + \alpha (x-x_0) \\ \\ \iff & f(x) -f(x_0) \simeq \alpha (x-x_0)\\\\
    \iff & \alpha \simeq \frac{f(x) -f(x_0)}{x-x_0}  \simeq\; f'(x_0) 

où :math:`f'(\cdot)` est la dérivée première de la fonction :math:`f(\cdot)`. Donc,

.. math::

   f(x) \simeq f(x_0) + f'(x_0) (x-x_0)  \\
   f(x) - f(x_0) \simeq f'(x_0) (x-x_0)  \\ 
   \Delta f \simeq f'(x_0) \Delta x 

Si on veut prédire le changement dans la valeur d'une fonction, la dérivée est très utile!

La dérivée
^^^^^^^^^^

**Avec des constantes**

-  :math:`f(x) = b + ax`: :math:`f'(x) = a`

-  :math:`f(x) = \log x`: :math:`f'(x) = \frac{1}{x}`

-  :math:`f(x) = e^{ax}`: :math:`f'(x) = ae^{ax}`

-  :math:`f(x) = x^a`: :math:`f'(x) = a x^{a-1}`



**Avec des fonctions**

-  Règle du produit: :math:`f(x) = a(x)b(x)`, :math:`f'(x) = a'(x)b(x) + a(x)b'(x)`

-  Règle du quotient: :math:`f(x) = \frac{a(x)}{b(x)}`,
   :math:`f'(x) = \frac{a'(x)b(x) - a(x)b'(x)}{b(x)^2}`

-  Règle de chaine: :math:`f(x) = a(b(x))`, :math:`f'(x) = a'(b(x))b'(x)`

-  Règle d'addition (et soustraction): :math:`f(x) = a(x) + b(x)`, :math:`f'(x) = a'(x) + b'(x)`.


.. todo:: **Exercice A**: Trouvez les dérivées de :math:`f(x)=\sqrt{x},\frac{x}{1+x},\frac{1}{2}x^2 + 2x-10,(1+\frac{x}{2})^2`.




.. todo:: **Exercice B**: Faire une approximation de premier ordre pour :math:`f(x)=\sqrt{x}`. 



**Approximations d’ordres supérieurs**

Si la fonction a des dérivées supérieures non nulles, ou bien :math:`x` est loin de :math:`x_0`, l'approximation de premier ordre que nous avons vu produira une approximation assez mauvaise... Par ailleurs, on veut peut-être aussi caractériser des fonctions par autre chose que seulement leur pente. (est-ce une courbe, etc?). 

On peut pousser plus loin le concept d'approximation,

-  Polynome d’ordre 2 devrait être meilleur...

-  Alors, on approxime par deuxième ordre

-  Polynome d’ordre :math:`k`: on peut certainement généraliser.

  Ce type d'approximation est appelée approximation de `Taylor <https://en.wikipedia.org/wiki/Brook_Taylor>`_. On utilise alors les
dérivées d’ordres supérieurs d’une fonction:

.. math::

   f(x) = f(x_0) + f'(x_0)(x-x_0) +\frac{1}{2}f''(x_0)(x-x_0)^2 + \ldots

On dénote :math:`f'(x), f''(x)` ou :math:`\frac{d f}{d x},\frac{d}{d x}(\frac{d f}{d x}) = \frac{d^2 f}{d x^2}`.

**Concavité et Convexité des fonctions**

Une fonction est concave si pour tout point :math:`(x_1,x_2)` et tout
:math:`0<\lambda<1`:

.. math::

   f(\lambda x_1 + (1-\lambda) x_2) \geq \lambda f(x_1) + (1-\lambda)f(x_2)

et convexe si faux. On dit strictement concave (ou convexe) si les inégalités
sont strictes (n'incluent pas zéro).

**Approximation et maximum (minimum)**

Considérons l’approximation de premier ordre

.. math::

   f(x_0+\Delta x) \simeq f(x_0)+ f'(x_0)\Delta x.

Observons que:

-  Si :math:`f'(x_0)>0` un petit changement :math:`\Delta x>0` augmente
   :math:`f`

-  Si :math:`f'(x_0) <0` un petit changement :math:`\Delta x <0`
   augmente :math:`f`

-  Si :math:`x_0` est la solution de :math:`\max_x f(x)`, il faut que
   :math:`f'(x_0) =0`! C'est la condition de premier ordre (CPO) nécessaire.

Considérons l’approximation de deuxième ordre pour voir si elle est suffisante:

.. math::

   f(x_0+\Delta x) \simeq f(x_0) + f'(x_0)\Delta x +\frac{1}{2}f''(x_0)\Delta x ^2  

Pour un maximum (local), il faut que :math:`f'(x_0)=0` (condition de premier ordre, CPO) et
:math:`f''(x_0)<0` (condition de deuxième ordre, CDO). Observons que:

-  Si :math:`f'(x_0) = 0`, mais :math:`f''(x_0)>0`, alors
   :math:`f(x_0+\Delta x) > f(x_0)`.

-  f’(x) doit être positif quand :math:`\Delta x <0` et négatif quand
   :math:`\Delta x>0`.

On peut trouver le maximum (minimum) d'une fonction en Python numériquement ou avec SymPy. 

.. todo:: **Exercice C**: Trouvez l'optimum de la fonction :math:`f(x) = x(10-x)`.


Dérivée partielle
^^^^^^^^^^^^^^^^^

Supposons la fonction :math:`f(x,y)`. La dérivée partielle se fait en
gardant fixes (ou exogènes) les autres variables:
:math:`f'_x(x,y) = \frac{\partial f(x,y)}{\partial x}`.


.. _envelop:

Théorème de l’enveloppe
^^^^^^^^^^^^^^^^^^^^^^^

Considérons la fonction :math:`f(x,p)` où :math:`p` est hors de contrôle de l'agent qui optimise
(exogène). On dénote:

.. math::

    V(p) = \max_x f(x,p) , \quad x^*(p) = \arg \max_x f(x,p)

La première fonction, :math:`\max` retourne la valeur maximale de la fonction en choissant :math:`x` et en gardant :math:`p` constant. C'est une fonction qui dépend de :math:`p` seulement (:math:`x` a été choisi tel qu'il maximise la fonction). La deuxième retourne le :math:`x` qui maximise :math:`f(x,p)` en gardant encore une fois :math:`p` constant. C'est donc une fonction de :math:`p`. 

Un lien évident existe entre les deux :math:`V(p) = f(x^*(p),p)`.  On peut utiliser ce lien pour étudier comment la valeur maximale de :math:`f` change quand on change :math:`p`:

.. math::

   V'(p) = f'_x(x^*(p),p)x^{*'}(p) + f'_p(x^*(p),p)
   
On a par définition :math:`x^*(p)` maximisant :math:`f(x,p)`. Donc, :math:`f'_x(x^*(p),p) = 0` de par la CPO. 

Ainsi, le premier terme de :math:`V'(p)` est zéro. 

On obtient :math:`V'(p) = f'_p(x^*(p),p)`.

Ceci implique que la dérivée de la valeur maximale par rapport à une variable exogène est la dérivée de la fonction objective par rapport à cette variable exogène, sans utiliser la règle de chaine (sans changer la solution optimale). C'est un raccourci (approximation) qui sera utile à plusieurs moments dans le cours. 

.. todo:: **Exercice D**: Trouvez la forme de :math:`V'(p)` pour la fonction :math:`V(p) = (10 - p\frac{x^*(p)}{2})x^*(p)` où :math:`x^*(p) = \arg \max_x f(x,p)` et :math:`f(x,p) =(10 - p\frac{x}{2})x`.




La différentielle totale
^^^^^^^^^^^^^^^^^^^^^^^^

Les combinaisons de :math:`x,y` telles que :math:`f(x,y) = \overline{f}`)
peuvent être trouvées en inversant la fonction, :math:`y=g(x,\overline{f})`.
Mais on peut décrire ces combinaisons en utilisant la
différentielle totale (une approximation linéaire):

On peut décrire la forme d'une fonction à un point donné par:

.. math::

   \begin{aligned}
   df(x,y) = f'_x(x,y)dx + f'_y(x,y)dy\end{aligned}

Si on pose :math:`df(x,y)=0`, on peut réarranger pour obtenir

.. math::

   \frac{dy}{dx}\Bigr|_{df=0} = -\frac{f'_x(x,y)}{f'_y(x,y)}

On qualifie la dérivée par le :math:`df=0` pour indiquer que c'est une dérivée obtenue en contraignant la valeur de la fonction à être constante.

.. todo:: **Exercice E**: Trouvez :math:`\frac{dy}{dx}\Bigr|_{df=0}` par différentielle totale pour :math:`f(x,y)=\log(xy)`. Faire sur papier et par SymPy. 



Homogénéité d'une fonction
^^^^^^^^^^^^^^^^^^^^^^^^^^

La dérivée partielle informe sur le comportement de la fonction quand un des arguments varie alors que les autres demeurent constants. Mais on pourrait aussi s'intéresser au comportement d'une fonction quand tous les arguments augmentent (ou diminuent) d'une même proportion. On utilise le concept d'homogénéité. Il y a deux façons de s'y prendre: 

Approche directe: Une fonction est homogène de degré :math:`r` si pour tout
:math:`\lambda>0`,

.. math::

   f(\lambda x_1, \lambda x_2, ... \lambda x_n) = \lambda^r f(x_1,x_2,...,x_n)

Théorème d'Euler: Si une fonction est homogène de degré :math:`r`, alors:

.. math::

   r f(x_1,x_2,...,x_n) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}x_i.

.. todo:: **Exercice F**: Trouvez le degré d’homogénéité de la fonction :math:`f(x,y)=x^\alpha y^\beta` des deux façons.

Approximation et maximum
^^^^^^^^^^^^^^^^^^^^^^^^

.. math::


   f(x,y) \simeq f(x_0,y_0) + f'_x(x_0,y_0)(x-x_0) + f'_y(x_0,y_0)(y-y_0)  \\
       +\frac{1}{2}f''_{xx}(x_0,y_0)(x-x_0)^2  + \frac{1}{2}f''_{yy}(x_0,y_0)(y-y_0)^2 + \\
       +f''_{xy}(x_0,y_0)(x-x_0)(y-y_0).

Condition pour un maximum:

-  Nécessaire: :math:`f'_x(x,y)=0, f'_y(x,y)=0`

-  Suffisante:
   :math:`\frac{1}{2}f''_{xx}(x_0,y_0)(x-x_0)^2  + \frac{1}{2}f''_{yy}(x_0,y_0)(y-y_0)^2 +f''_{xy}(x_0,y_0)(x-x_0)(y-y_0)<0`

La condition suffisante est reliée au déterminant du Hessien de la fonction (un concept qui nous n'utiliserons pas en classe, mais qui devrait rappeler des souvenirs). 

Maximisation avec contrainte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Approche directe** 

Quand le problème prend la forme:

.. math::

   \begin{aligned}
   \max_{x,y} \{ f(x,y): g(x,y) \leq m\}\end{aligned}

Et qu’on peut inverser :math:`g(x,y)=m` tel que :math:`y=q(x,m)`, alors
la solution du problème contraint pour :math:`x` est la même que celui
de :

.. math::

   \begin{aligned}
   \max_{x} \{ f(x,q(x,m))\}\end{aligned}

La CPO est :math:`f'_x(x,q(x,m)) + f'_y(x,q(x,m))q'(x,m) = 0`. On peut
résoudre pour :math:`x^*` et utiliser :math:`y=q(x)` pour trouver
:math:`y^*`. 

.. todo:: **Exercice G**: Maximisez la fonction :math:`f(x,y) = \log x + \log y` sous la contrainte :math:`x+y \le m`.

Avec plusieurs variables et contraintes, cette approche n'est pas très pratique...

**Le lagrangien**

La méthode de `Lagrange <https://fr.wikipedia.org/wiki/Joseph-Louis_Lagrange>`_ consiste à résoudre pour :math:`(x,y)`,

.. math::

   \begin{aligned}
   f'_x(x,y) -  \lambda g'_x(x,y) = 0 \\
   f'_y(x,y) -  \lambda g'_y(x,y) = 0 \\
   g(x,y) = m\end{aligned}

où :math:`\lambda` est un multiplicateur de Lagrange. 

Ces trois équations sont les CPO du lagrangien:

.. math::

   \begin{aligned}
       \max_{x,y,\lambda} L(x,y,\lambda) = f(x,y) - \lambda (g(x,y)-m)\end{aligned}

Le lagrangien :math:`L(x,y,\lambda)` est une fonction objective modifiée qui permet de pénaliser la maximisation pour la contrainte (pour s'assurer qu'elle soit respectée). On remarque que si :math:`\lambda = 0`, on a les deux CPO non-contraintes :math:`f'_x(x,y)=0` et :math:`f'_y(x,y)=0` qui donnent une solution optimale sans avoir besoin de la troisième. Seulement si la contrainte est *mordante* (si :math:`\lambda \neq 0`) aurons-nous une solution différente... 

.. todo:: **Exercice H**: Maximisez la fonction :math:`f(x,y) = \log x + \log y` sous la contrainte :math:`x+y \le m` par la méthode du lagrangien.

**L’interprétation du multiplicateur**

Il n'est pas nécessaire de résoudre pour la valeur de :math:`\lambda` afin de trouver les
valeurs optimales de :math:`x` et :math:`y`. Mais, si on le fait, :math:`\lambda` a une
interprétation utile pour certaines applications que nous verrons.

Par le théorème de l’enveloppe, si

.. math:: V(m) = \max_{x,y,\lambda} f(x,y) - \lambda (g(x,y)-m)

alors :math:`V'(m) = \lambda`. La valeur maximale augmente de :math:`\lambda` quand on augmente (marginalement) :math:`m` (quand on relâche la contrainte).

.. todo:: **Exercice I**: Démontrez dans le problème précédent (H) qu’une augmentation marginale de :math:`m` a pour effet d'augmenter le maximum de :math:`\lambda`. Pour ce faire résoudre les CPO du lagrangien pour :math:`x,y,\lambda`, remplacez ces expressions dans :math:`f(x,y)` et prendre la dérivée par rapport à  :math:`m`. Montrez que cette dérivée est égale à la valeur de :math:`\lambda`. 

Note sur les logarithmes
^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: Dans les notes, nous utiliserons :math:`\log` en base :math:`e=2.718281828459` et non en base 10. Donc, il s'agit du logarithme naturel (:math:`\ln = \log_e`). Python utilise aussi la base exponentielle. 


