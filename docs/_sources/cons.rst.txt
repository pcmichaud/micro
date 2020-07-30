.. _Cons:

Consommateur
------------

Les fondements de la microéconomie débutent avec le comportement du consommateur. On veut prédire ce que ferait un consommateur dans une situation donnée. On veut faire du sens des comportements observés. La théorie paraîtra simpliste, mais de ces fondements, on sera capable d'assez bien prédire le comportement économique des consommateurs. Des raffinements existent, certains ont même révisé ces fondements pour y introduire une approche comportementale où les individus ont des biais, répondent aux émotions, à des limites cognitives, etc. 

Préférences
+++++++++++

**Préférences définies sur des paniers de biens et services**

-  Panier: vecteur de quantités :math:`x = (x_1, x_2,\cdots,x_n)`.

-  Pour deux paniers :math:`A` and :math:`B`, préférences dictent lequel
   est préféré

-  Préférences sont comme liste de souhait (hierarchisée): ignore les
   prix et les ressources. Viendra plus tard.

-  Les relations de préférences sont dénotées par
   :math:`\succ,\succeq,\sim`.

**Hypothèses importantes sur les préférences**

Ces hypothèses ou axiomes sont nécessaires pour en arriver à une théorie du comportement. On note les plus importantes: 

*Exhaustive*

Pour tous paniers A et B soit le consommateur:

-  préfère **toujours** A à B (:math:`A\succ B`)

-  préfère **toujours** B à A (:math:`B\succ A`)

-  est indifférent entre A et B (:math:`A \sim B`)

Est-ce restrictif?

-  Oui, e.g.: crème glacée vs. soupe (on préfère la crème glacée en été mais la soupe en hiver). 

-  Mais on peut s'en sortir: inclure les circonstances dans les paniers (la saison)

-  Les paniers sont alors (crème glacée, chaleur), (crème glacée,
   froid), (soupe, chaleur), (soupe, froid). La relation de préférence est alors stable et exhaustive.

*Transitivité*

Une question de cohérence...

-  Si trois paniers A, B, C tels que :math:`A\succ B`,
   :math:`B \succ C`, alors le consommateur préfère A à C
   (:math:`A \succ C`).

Cette hypothèse n'est pas toujours vérifiée... Surtout en présence d'incertitude. 

*Non-satiation*

-  Si A contient au moins autant que le panier B, strictement plus d’au
   moins un bien dans le panier, alors :math:`A \succ B`.

-  Version faible (:math:`A \succeq B`,indifférence ou préférence) est
   raisonnable

-  Étiquette des biens: les biens sont désirables (qualité air au lieu de
   pollution). 

Il est peu pratique de fonctionner avec des listes de préférences pour modéliser les comportements. Par exemple, comment prédire l'effet d'un changement de prix avec une liste de préférence? On voudra se rapporcher de l'analyse marginale pour rendre ceci plus pratique. 

Courbes d’indifférence et TMS
+++++++++++++++++++++++++++++

Le premier outil est celui des courbes d'indifférence dans un espace réel (quantités de plusieurs biens). 

Deux biens :math:`X,Y`:

-  Pour tout panier :math:`(X_0,Y_0)`, combinaisons :math:`(X,Y)` telles
   que consommateur indifférent entre :math:`(X,Y)` et
   :math:`(X_0,Y_0)`

-  Courbe indifférence vers nord-est indique niveau utilité plus élevé
   (non-satiation)

Les courbes d’indifférence ne se croisent pas si elle respectve la transitivité.

.. image:: /images/indif.png
   :scale: 25%

*Exercice A*: Montrez que des courbes d’indifférence qui se croisent
ne respectent pas la transitivité.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/P44fP8dFZxM" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


**Taux marginal de substitution (TMS)**

Ces courbes d'indifférences contienent plus d'information qu'on croit ...

-  Pour un panier :math:`(X_0, Y_0)`, TMS de :math:`X` en fonction de
   :math:`Y`: Quantité du bien :math:`Y` que le consommateur est
   prêt à sacrifier pour avoir une unité de plus de :math:`X`.

-  Valeur que le consommateur porte sur un bien :math:`X` en terme
   d’unités d’un autre bien :math:`Y`.

-  Correspond à la pente de la courbe d’indifférence à
   :math:`(X_0,Y_0)`.

**Convexité des courbes d’indifférences**

-  Si la quantité de nourriture (:math:`X`) augmente, comment le TMS de
   :math:`X` en fonction de :math:`Y` change?


Il diminue généralement. Ceci est représenté par des courbes d’indifférences convexes. Même s'il y a non-satiation, on accepte généralement que l'intensité de la préférence associée à une unité additionelle est plus faible avec le nombre d'unités consommées. 

Utilité
+++++++

Les courbes d'indifférence nous permettent de passer vers une représentation des préférences par une fonction. Sur la courbe d'indifférence, chacun des paniers procure le même bien-être. Nous pouvons lui attribuer une valeur ou utilité (arbitraire). En sautant d'une courbe d'indifférence à une autre (plus élevée), on augmente l'utilité. Donc, on peut construire une fonction :math:`U(X,Y)` qui représente ces préférences. La valeur de cette fonction est donc ordinale (elle permet de classer les paniers en ordre de préférence). Ce n'est que l'ordre qui compte. 

-  Fonction d’utilité: assigne un nombre à chaque panier

-  :math:`U` représente les préférences si et seulement si
   :math:`A \succ B \Rightarrow U(A) > U(B)` et
   :math:`U(A) > U(B)   \Rightarrow A \succ B`

Les préférences sont ordinales (hiérarchiques)

-  Si :math:`f` est une fonction strictement croissante et :math:`U`
   représente des préférences, alors :math:`V(X) = f(U(X))` représente
   les même préférences.

   .. math:: U(X) > U(Y) \iff f(U(X)) > f(U(Y))

-  La valeur de l’utilité n’a pas de signification, l’ordonnancement des
   paniers est important.

-  Exemple: :math:`U(X,Y) = \ln X + \ln Y` et :math:`V(X,Y) = XY` représente les
   mêmes préférences

*Exercice B*: Montrez que :math:`U` et :math:`V` dans l'exemple ont les mêmes
préférences en trouvant la transformation :math:`V=f(U)`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/wsPBuGGIBLE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Comment trouver le TMS à partir de l'utilité?

-  Deux biens, :math:`X`, :math:`Y`. Préférences représentées par la
   fonction d’utilité :math:`U(X,Y)`

-  e.g. :math:`U(X,Y) = \ln X + \ln Y`

TMS de :math:`X` en fonction de :math:`Y`

-  Combien de :math:`Y` sacrifier pour davantage de :math:`X`

-  Formellement: augmente :math:`X` de :math:`\Delta X`: quel est le
   changement :math:`\Delta Y` qui conserve l'indifférence?

Calculer le TMS de :math:`X` en fonction de :math:`Y`

-  On doit avoir :math:`\Delta Y` tel que
   :math:`U(X + \Delta X, Y + \Delta Y) = U(X,Y)`

-  Approximation de premier ordre:

   .. math:: U(X+\Delta X, Y+ \Delta Y) \simeq  U(X,Y)+  \Delta X  \frac{\partial U}{\partial X} + \Delta Y \frac{\partial U}{\partial Y}

   .. math:: \Rightarrow \;\; TMS = \Delta Y/ \Delta X =  -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y}

On réfère à :math:`\frac{\partial U}{\partial X}` comme étant l'utilité marginale de :math:`x` (et vice-versa pour :math:`y`). L'utilité marginale est généralement décroissante mais positive (attention: l'utilité n'est pas décroissante, seule l'utilité marginale). 

Exemple:

-  :math:`U(X,Y) = \ln X + \ln Y`

   .. math:: TMS = -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y} = -Y/X

Prenons la différentielle totale:

.. math::

   \begin{aligned}
   dU = \frac{\partial U}{\partial X}dX + \frac{\partial U}{\partial Y}dY\end{aligned}

Posons :math:`dU = 0`, alors

.. math::

   \frac{dY}{dX}\bigg\rvert_{dU=0} = -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y}

On peut utiliser SymPy pour trouver le TMS:

.. code:: Python

   import simpy as sp 
   x,y,a = sp.symbols('x y a')
   u = x**a * y**(1-a)
   umx = diff(u,x)
   umy = diff(u,y)
   tms = umx/umy

Contrainte budgétaire
+++++++++++++++++++++

Jusqu'içi, le consommateur a tous les paniers devant lui et a des préférences sur ceux-ci. Il peut tout avoir. En pratique, Il pourra acheter les biens, mais à un prix. Et ce prix est important parce qu'il a une richesse limitée pour consommer. Tout achat a un coût d'opportunité. 

-  On ne peut pas dépenser davantage que notre richesse :math:`I`

-  | Deux biens :math:`X`, :math:`Y`: Contrainte:
     :math:`p_X X + p_Y Y = I`
   | Donne ce qui est abordable étant donné :math:`I`

-  | Résoudre pour :math:`Y` en terme de :math:`X`:
     :math:`Y = \frac{I - p_X X}{p_Y}`
   | Le prix relative entre :math:`X` and :math:`Y` en respectant la
     contrainte:

     .. math:: \frac{dY}{dX} = -\frac{p_X}{p_Y}

Acheter une unité de :math:`X` implique un sacrifice de :math:`\frac{p_X}{p_Y}` unités de :math:`Y`. C'est le coût d'opportunité de :math:`X` en terme de :math:`Y`. 

Dans l'espace :math:`(X,Y)`, la contrainte définie les allocations possibles. Celles au dessus ne sont pas possibles. Seules celles entre l'origine est la contrainte sont possibles...

**Normalisation**

-  Contrainte budgétaire demeure la même si prix et richesse multipliés par même
   constante :math:`\lambda`.

-  On peut acheter les mêmes biens.

-  Normalisons :math:`p_Y = 1`. Alors :math:`Y = I - p_X X`. :math:`p_X`
   est maintenant en terme de quantité de :math:`Y` (numéraire) et idem pour :math:`I`.

Seul les prix relatifs affectent l'allocation. 

*Exercice C*: Montrez qu’une contrainte budgétaire ne change pas si on
multiplie prix et revenu par :math:`\lambda>0`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Bcz1ECmSiDs" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Choix du consommateur
+++++++++++++++++++++

-  La contrainte est fixe. Le consommateur peut choisir la courbe d'indifférence sur laquelle il sera, et donc quelle combinaison il consommera étant donné la contrainte. Quel est le plus haut niveau
   d’utilité qu'il peut atteindre sur la contrainte?

-  On ne peut pas aller sur une courbe d’indifférence plus élevée que la
   contrainte

-  Toutes les courbes plus basses sont sous-optimales.

-  La courbe d’indifférence qui touche la contrainte (souvent tangente)
   donne le meilleur niveau de bien-être possible

**Approche Directe**

Le problème est

-  Maximiser :math:`U(X,Y)` étant donné la contrainte
   :math:`p_X X+ p_YY = I`

Étape 1: Substituer la contrainte

-  Si achète :math:`X` alors on consomme
   :math:`Y(X) = \frac{I - p_X X}{p_Y}`

-  Utilité seulement fonction de :math:`X`: :math:`V(X) = U(X,Y(X))`


Étape 2: Maximiser sans contrainte

-  Prendre condition de premier ordre (CPO)

La CPO:


   .. math:: \frac{dV}{dX} = 0 \iff \frac{dU}{dX} + \frac{dY}{dX}\frac{dU}{dY} = 0

   .. math:: \iff \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}

-TMS sur la courbe d’indifférence = Pente de la contrainte budgétaire

On peut faire ce travail par SymPy: 

.. code:: Python

   import sympy as sp 
   x,y,a, p_x, p_y, I = sp.symbols('x y a p_x p_y I')
   u = x**a * y**(1-a)
   budget = sp.Eq(p_x*x + p_y*y,I)
   yx = sp.solve(budget,y)[0]
   ux = u.subs(y,yx)
   cpo = sp.Eq(sp.diff(ux,x),0)
   xstar = sp.solve(cpo,x)[0]


*Exercice D*: Trouvez les demandes pour :math:`u(x,y) = XY` sous la
contrainte :math:`p_X X + p_Y Y \le I`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/gKWqAtD9ttw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


On peut poser le lagrangien:

.. math::

   L(X,Y,\lambda) = U(X,Y) - \lambda (p_X X + p_Y Y - I)

Si on maximise: :math:`\max_{X,Y,\lambda} L(X,Y,\lambda)`, les CPO sont

.. math::

   U'_X(X,Y) - \lambda p_X = 0 \\
   U'_Y(X,Y) - \lambda p_Y = 0 \\
   p_X X + p_Y Y = I

En prenant le ratio des deux premières CPO, on a:

.. math::

   \begin{aligned}
   \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y} \\
   p_X X + p_Y Y = I\end{aligned}

*Exercice E*: Trouvez les demandes pour :math:`u(X,Y) = XY` comme
précédement mais par le lagrangien.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/cbpdV7mBVaQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Les demandes :math:`X^*(p_X,p_Y,I)` et :math:`Y^*(p_X,p_Y,I)` sont appelées demandes marshalliennes (`Alfred Marshall <https://fr.wikipedia.org/wiki/Alfred_Marshall>`_). Nous étudierons leurs propriétés dans le prochain cours. Elles seront très utiles pour étudier le comportement et les politiques publiques (e.g. taxation). Ces demandes sont observables, contrairement à l'utilité. On apprendra sur l'utilité par ces demandes.    

Utilité Indirecte
+++++++++++++++++

L’utilité indirecte :math:`V(p_X,p_Y,I)` est le niveau d’utilité maximale
atteint avec les prix :math:`(p_X,p_Y)` et le revenu :math:`I`,

.. math:: V(p_X,p_Y,I) = \max_{X,Y} \{ u(X,Y) : p_X X + p_Y Y \le I\}.

*Exercice F* : Montrez que
:math:`\frac{\partial V}{\partial I} = \lambda` où :math:`V` est l’utilité
indirecte.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/YSyHk5wacoc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Identité de Roy
+++++++++++++++

Si l’utilité indirecte est donnée par :math:`V(p_X,p_Y,I)` alors on peut
retrouver les demandes par l’identité de Roy:

.. math:: X^*(p_X,p_Y,I) = -\frac{\partial{V(p_X,p_Y,I)}/\partial{p_X}}{\partial{V(p_X,p_Y,I)}/\partial{I}}

*Exercice G*: Montrez que ceci est vrai en utilisant le théorème de
l’enveloppe.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/KX0-XtNgH6g" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>



Exemple Consommateur
++++++++++++++++++++

Voir ce notebook pour un bel exemple qui utilise Python pour résoudre le problème du consommateur avec fonction d'utilité CES (Constant Elasticity of Substitution)

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Consommateur.ipynb

