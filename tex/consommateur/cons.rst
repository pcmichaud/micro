.. raw:: latex

   \frame{\titlepage}

.. raw:: latex

   \frame{\tableofcontents}

Les préférences
===============

Préférences
~~~~~~~~~~~

**Préférences définies sur des paniers de biens et services**

-  Panier: vecteur de quantités :math:`x = (x_1, x_2,\cdots,x_n)`.

-  Pour deux paniers :math:`A` and :math:`B`, préférences dictent lequel
   est préféré

-  Préférences sont comme liste de souhait (hierarchisée): ignore les
   prix et les ressources. Viendra plus tard.

-  Les relations de préférences sont dénotées par
   :math:`\succ,\succeq,\sim`.

Hypothèses importantes sur les préférences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Exhaustive: Pour tous paniers A et B soit le consommateur**

-  préfère **toujours** A à B (:math:`A\succ B`)

-  préfère **toujours** B à A (:math:`B\succ A`)

-  est indifférent entre A et B (:math:`A \sim B`)

**Est-ce restrictif?**

-  Oui, e.g.: crème glacée vs. soupe

-  On peut inclure les circonstances dans les paniers

-  Les paniers sont alors (crème glacée, chaleur), (crème glacée,
   froid), (soupe, chaleur), (soupe, froid).

Hypothèses importantes sur les préférences (II)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Transitivité**

-  Si trois paniers A, B, C tels que :math:`A\succ B`,
   :math:`B \succ C`, alors le consommateur préfère A à C
   (:math:`A \succ C`).

**Non-satiation**

-  Si A contient au moins autant que le panier B, strictement plus d’au
   moins un bien dans le panier, alors :math:`A \succ B`.

-  Version faible (:math:`A \succeq B`,indifférence ou préférence) est
   raisonnable

-  Étiquette des biens: les biens sont désirables (qualité air vs.
   pollution).

Courbes d’indifférence
~~~~~~~~~~~~~~~~~~~~~~

**Deux biens :math:`X,Y`**:

-  Pour tout panier :math:`(X_0,Y_0)`, combinaisons :math:`(X,Y)` tel
   que consommateur indifférent entre :math:`(X,Y)` and
   :math:`(X_0,Y_0)`

-  Courbe indifférence vers nord-est indique niveau utilité plus élevé
   (non-satiation)

Les courbes d’indifférence ne se croisent pas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Exercice A**: Montrer que des courbes d’indifférence qui se croisent
ne respectent pas la transitivité.

Taux marginal de substitution (TMS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Definition**

-  Biens: :math:`X` et :math:`Y`

-  Pour un panier :math:`(X_0, Y_0)`, TMS de :math:`X` en fonction de
   :math:`Y`: Quantité de chauffage (:math:`Y`) que le consommateur est
   prêt à sacrifier pour avoir une unité de plus de nourriture
   (:math:`X`)

-  Valeur que le consommateur porte sur un bien :math:`X` en termes
   d’unité d’un autre bien :math:`Y`.

-  Correspond à la pente de la courbe d’indifférence à
   :math:`(X_0,Y_0)`.

Convexité des courbes d’indifférences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Si la quantité de nourriture (:math:`X`) augmente comment le TMS de
   :math:`X` en fonction de :math:`Y` change?

Correspond à la convexité des courbes d’indifférences.

Utilité
~~~~~~~

**Représentation des préférences**

-  Fonction d’utilité: assigne un nombre à chaque panier

-  :math:`U` représente les préférences si et seulement si
   :math:`A \succ B \Rightarrow U(A) > U(B)` et
   :math:`U(A) > U(B)   \Rightarrow A \succ B`

.. raw:: latex

   \vfill

Utilité **Les préférences sont ordinales (hiérarchiques)**

-  Si :math:`f` est une fonction strictement croissance et :math:`U`
   représente des préférences, alors :math:`V(X) = f(U(X))` représente
   les même préférences.

   .. math:: U(X) > U(Y) \iff f(U(X)) > f(U(Y))

-  La valeur de l’utilité n’a pas de signification, l’ordonnancement des
   paniers est important.

-  :math:`U(X,Y) = \log X + \log Y` et :math:`V(X,Y) = XY` représente les
   mêmes préférences

**Exercice B**: Montrer que :math:`U` et :math:`V` ont les mêmes
préférences.

Retour vers le TMS **Contexte**

-  Deux biens, :math:`X`, :math:`Y`. Préférences représentées par la
   fonction d’utilité :math:`U(X,Y)`

-  e.g. :math:`U(X,Y) = \log X + \log Y`

**TMS de :math:`X` en fonction de :math:`Y`**

-  Combien de :math:`Y` sacrifié pour davantage de :math:`X`

-  Formellement: augmente :math:`X` de :math:`\Delta X`: quel est le
   changement :math:`\Delta Y` qui conserve indifférence?

Calculer le TMS **TMS de :math:`X` en fonction de :math:`Y`**

-  On doit avoir :math:`\Delta Y` tel que
   :math:`U(X + \Delta X, Y + \Delta Y) = U(X,Y)`

-  Approximation de premier ordre:

   .. math:: U(X+\Delta X, Y+ \Delta Y) \simeq  U(X,Y)+  \Delta X  \frac{\partial U}{\partial X} + \Delta Y \frac{\partial U}{\partial Y}

   .. math:: \Rightarrow \;\; TMS = \Delta Y/ \Delta X =  -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y}

**Exemple**

-  :math:`U(X,Y) = \log X + \log Y`

   .. math:: TMS = \frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y} = -Y/X

Par différentielle totale

Prenons la différentielle totale:

.. math::

   \begin{aligned}
   dU = \frac{\partial U}{\partial X}dX + \frac{\partial U}{\partial Y}dY\end{aligned}

 Posons :math:`dU = 0`, alors

.. math::

   \begin{aligned}
   \frac{dY}{dX}\bigg\rvert_{dU=0} = -\frac{\partial U}{\partial X}/ \frac{\partial U}{\partial Y}\end{aligned}

Contrainte budgétaire
=====================

Contrainte Budgétaire

-  On ne peut pas dépenser plus que notre richesse :math:`I`

-  | Deux biens :math:`X`, :math:`Y`: Contrainte:
     :math:`p_X X + p_Y Y = I`
   | Définie ce qui est abordable étant donné :math:`I`

-  | Résoudre pour :math:`Y` en terme de :math:`X`:
     :math:`Y = \frac{I - p_X X}{p_Y}`
   | Le taux de change entre :math:`X` and :math:`Y` en respectant la
     contrainte:

     .. math:: \frac{dY}{dX} = -\frac{p_X}{p_Y}

Contraintes, la suite
~~~~~~~~~~~~~~~~~~~~~

**Normalisation**

-  Contrainte budgétaire la même si prix et richesse multiplié par même
   constante :math:`\lambda`.

-  On peut acheter les mêmes biens.

-  Normalisons :math:`p_Y = 1`. Alors :math:`Y = I - p_X X`. :math:`p_X`
   est maintenant en terme de quantité de :math:`Y` (numéraire).

**Exercice C**: Montrer qu’une contrainte budgétaire ne change pas si on
multiplie prix et revenu par :math:`\lambda>0`.

Choix du consommateur
=====================

.. _choix-du-consommateur-1:

Choix du consommateur
~~~~~~~~~~~~~~~~~~~~~

-  La contrainte est une donnée fixe. Quel est le plus haut niveau
   d’utilité sur cette contrainte?

-  On ne peut pas aller sur une courbe d’indifférence plus élevée que la
   contrainte

-  Toutes courbes plus basses est sous-optimale.

-  La courbe d’indifférence qui touche la contrainte (souvent tangente)
   donne le meilleur niveau de bien-être possible

Conditions mathématiques
========================

Approche Directe
~~~~~~~~~~~~~~~~

**Le problème est**

-  Maximise :math:`U(X,Y)` étant donné par contrainte
   :math:`p_X X+ p_YY = I`

.. raw:: latex

   \pause

**Étape 1: Substituer la contrainte**

-  Si achète :math:`X` alors on consomme
   :math:`Y(X) = \frac{I - p_X X}{p_Y}`

-  Utilité seulement fonction de :math:`X`: :math:`V(X) = U(X,Y(X))`

.. raw:: latex

   \pause

**Étape 2: Maximiser sans contrainte**

-  Voir que la solution de coin n’est pas optimale (cas :math:`X= 0` et
   :math:`Y=0`)

-  Prendre condition de premier ordre

Approche Directe

**La CPO**

-  

   .. math:: \frac{dV}{dX} = 0 \iff \frac{dU}{dX} + \frac{dY}{dX}\frac{dU}{dY} = 0

   .. math:: \iff \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}

TMS sur la courbe d’indifférence = Pente de la contrainte budgétaire

Solution
~~~~~~~~

**Exercice D**: Trouvez les demandes pour :math:`u(x,y) = XY` sous la
contrainte :math:`p_X X + p_Y Y \le I`.

Approche générale
=================

Lagrangien I On peut poser le lagrangien

.. math::

   \begin{aligned}
   L(X,Y,\lambda) = U(X,Y) - \lambda (p_X X + p_Y Y - I)\end{aligned}

.. raw:: latex

   \pause

Si on maximise: :math:`\max_{X,Y,\lambda} L(X,Y,\lambda)`, les CPO sont

.. raw:: latex

   \pause

.. math::

   \begin{aligned}
   U'_X(X,Y) - \lambda p_X = 0 \\
   U'_Y(X,Y) - \lambda p_Y = 0 \\
   p_X X + p_Y Y = I\end{aligned}

Lagrangien II En prenant le ratio des deux premières CPO, on a:

.. math::

   \begin{aligned}
   \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y} \\
   p_X X + p_Y Y = I\end{aligned}

**Exercice E**: Trouvez les demandes pour :math:`u(X,Y) = XY` tel que
précédement mais par le lagrangien.

Utilité Indirecte

L’utilité indirecte :math:`V(p_X,p_Y,I)` est le niveau d’utilité maximal
à atteindre avec les prix :math:`(p_X,p_Y)` et

.. math:: V(p_X,p_Y,I) = \max_{X,Y} \{ u(X,Y) : p_X X + p_Y Y \le I\}

**Exercice F**: Montrez que
:math:`\frac{\partial V}{\partial I} = \lambda` où :math:`V` l’utilité
indirecte.

Identité de Roy

Si l’utilité indirecte est donnée par :math:`V(p_X,p_Y,I)` alors on peut
retrouver les demandes par l’identité de Roy:

.. math:: X^*(p_X,p_Y,I) = \frac{\partial{V(p_X,p_Y,I)}/\partial{p_X}}{\partial{V(p_X,p_Y,I)}/\partial{I}}

**Exercice F**: Montrez que ceci est vrai en utilisant le théorème de
l’enveloppe.
