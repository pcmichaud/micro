Échange
-------

Pourquoi échanger entre consommateur? par quel moyen? Par le troc, un marché ou bien en nommant quelqu'un qui se chargera de partager les biens entre les personnes. Quel mécanisme fera le mieux? 

.. figure:: /images/barter.jpeg
   :scale: 100


Nous verrons qu'il existe généralement des gains à l'échange. L'échange peut seulement être bénéfique. Si ce ne l'est pas, les individus n'échangent pas. Donc permettre l'échange ne peut nuire. Le meilleur résultat peut être atteint de différentes façons (marché, planificateur central, troc) si certaines conditions sont respectées. 

Débutons avec un cadre simple, qui ne restraint pas la généralité des résultats plus tard:

-  Considérons une situation avec deux consommateurs (1 et 2) et deux biens
   (:math:`X` and :math:`Y`)

-  Fonctions d'utilité :math:`U_1(X,Y)` et :math:`U_2(X,Y)`

-  Chaque consommateur a une dotation de chacun des biens,
   :math:`B_1^e = (X_1^e,Y_1^e)` et :math:`B_2^e = (X_2^e,Y_2^e)`.

Exemples

-  Deux fermiers, un a une dotation de pommes de terre et l'autre de bétail. 

-  Deux pays: Le pays 1 a une dotation de pétrole, le pays 2 de la machinerie industrielle. 

- Deux consommateurs sur kijiji ou Ebay: un a une canot et l'autre un ordinateur portable

D'où viennent ces dotations? Pour le moment, de la nature (ressources naturelles ou héritage?). Plus tard, ces dotations proviendront des profits provenant de la production d'un bien à l'aide d'autres biens dans l'économie. 

Équilibre de marché
+++++++++++++++++++

Le marché est une forme d'échange très répandue. En terme de modélisation, le marché est résumé par un vecteur de prix (s'il y a plusieurs biens) et un système légal qui encadre les transactions. 

Si chaque consommateur a une dotation et une demande individuelle pour les biens en fonction des prix, on peut assez facilement trouver un équilibre de marché, içi d'échange, puisqu'il n'y a pas de production. Pensez à `Kijiji <https://www.kijiji.ca/>`_.  

Pour ce qui est des demandes individuelles, 

-  Consommateur 1 choisi de consommer :math:`(X_1^c, Y_1^c)`

- Étant donné les prix :math:`p_X` and :math:`p_Y`, la contrainte budgétaire de chacun des agents est

   .. math:: p_X X_1^c + p_Y Y_1^c  =  p_X X_1^e + p_Y Y_1^e

-  Les prix sont déterminés en équilibre. 


Réalisons d'abord que ce n'est que le prix relatif qui est important pour l'équilibre. Nous avons deux prix inconnues, :math:`p_X` et :math:`p_Y`. La contrainte budgétaire peut être ré-écrite  

   .. math:: X_1^c + \frac{p_Y}{p_X} Y_1^c  =   X_1^e + \frac{p_Y}{p_X} Y_1^e

On peut donc, sans perdre d'information, dénoter :math:`p = p_Y/p_X`, le prix relatif de :math:`Y`en terme de quantité de :math:`X`. On aurait aussi pu définir le prix comme étant :math:`p = p_X/p_Y`!

Comment trouver le prix relatif d'équilibre?

- Étape 1: Demande individuelle: On cherche 

.. math::
   \max_{X_1,Y_1} \left[U_1 : X_1^c + p Y_1^c  \leq   X_1^e + p Y_1^e\right]

On obtient :math:`X_1^c(p)` et :math:`Y_1^c(p)` par le Lagrangien. 

-  Étape 2: Le prix :math:`p^*` est un prix d'équilibre si à :math:`p^*` la demande agrégée est égale à l'offre agrégée. On cherche donc :math:`p^*` tel que: 

   .. math::
      X_1^c(p^*)+X_2^c(p^*) = X_1^e + X_2^e \quad
      et \quad Y_1^c(p^*)+Y_2^c(p^*) = Y_1^e + Y_2^e

Le quantité de :math:`X` échangée est donnée par :math:`X_1^c(p^*) - X_1^e =X_2^e - X_2^c(p^*)`. Si :math:`X_1^c - X_1^e < 0`, le consommateur 1 est offreur de :math:`X` (le consommateur 2 demandeur).

Hypothèses importantes:

-  Le marché est compétitif: Le consommateur prend le prix comme donné. Il est **prenneur de prix**.

-  Tous les biens sont homogènes (identitiques) et perçus de la même façon par l'acheteur et le vendeur. 

-  L'utilité du consommateur 1 ne dépend pas des actions des autres consommateurs: **aucune externalités**

Regardons un exemple. Considérons :math:`U_1(X,Y) = U_2(X,Y) = \log X + \alpha \log Y`. Fixons :math:`p_X= 1`, et donc :math:`p_Y = p`. Les dotations sont données par :math:`(X_1^e, Y_1^e, X_2^e, Y_2^e)`. La solution pour les demandes est:

   .. math::
      \begin{aligned}
      X_1^c &=
      \frac{1}{1+\alpha}(X_1^e + p Y_1^e) \\ 
      Y_1^c &=
      \frac{\alpha}{1+\alpha}\frac{X_1^e + p Y_1^e}{p}
      \end{aligned}

L'équilibre de marché pour :math:`X` implique que

   .. math::

      X_1^c(p) + X_2^c(p) = X_1^e + X_2^e
      \Rightarrow p = \alpha \frac{X_1^e + X_2^e}{Y_1^e + Y_2^e}

Le marché pour :math:`Y` est aussi en équilibre au prix d'équilibre :math:`p`. Pourquoi un seul marché est-il nécessaire?

Loi de Walras
+++++++++++++

On a une seule inconnue, :math:`p` mais deux équations... L'équilibre sur un marché implique l'équilibre sur l'autre. Regardons les deux contraintes budgétaires: 

   .. math::

      X_1^c + p Y_1^c  =   X_1^e + p Y_1^e \quad et \quad
      X_2^c + p Y_2^c  =   X_2^e + p Y_2^e

Si on additionne les deux contraintes on obtient: 

   .. math::

      [X_1^c + X_2^c] + p [Y_1^c + Y_2^c] = [X_1^e + X_2^e] + p[Y_1^e + Y_2^e]

Un équilibre pour :math:`X` implique que

   .. math::

      p[Y_1^c + Y_2^c]  = p [Y_1^e + Y_2^e] \Rightarrow  Y_1^c + Y_2^c = Y_1^e + Y_2^e

La loi de `Walras <https://fr.wikipedia.org/wiki/L%C3%A9on_Walras>`_ permet de se concentrer sur le prix relatif et de trouver le prix d'équilibre sur un seul des marchés sans avoir à regarder l'autre. On peut généraliser cette loi à plus de 2 biens. 

Déterminants du prix d'équilibre
++++++++++++++++++++++++++++++++

Le prix d'équilibre sera fonction des préférences des agents. Dans notre exemple, 

.. math::
   p^* = \alpha \frac{X_1^e + X_2^e}{Y_1^e + Y_2^e}

Donc le prix de :math:`Y` augmente avec la préférence relative pour :math:`Y`, donnée par :math:`\alpha`. L'offre étant fixe, si la demande est élevée, le prix d'équilibre devra être plus élevé pour retrouver un équilibre. Si le bien :math:`Y` est rare, c'est-à-dire que :math:`Y_1^e + Y_2^e` est faible, le prix d'équilibre sera plus élevé. 

Le prix est un signal des préférences et de la rareté relative des biens. Est-ce que l'équilibre de marché garantie le niveau de bien-être le plus élevé que peuvent obtenir les deux agents? Afin de juger de l'allocation de marché, nous devons faire un pas de côté pour définir une allocation optimale, sans le recours au marché. 

Allocation Pareto-efficace
++++++++++++++++++++++++++

On a déjà vu qu'une amélioration de Pareto est possible quand aucun des deux agents ne perd en utilité et qu'au moins un gagne. Quand il n'existe plus d'amélioration au sens de Pareto, on dit que l'allocation est Pareto optimale ou efficace. Nous allons maintenant appliquer ce principe aux allocations de biens. 

Pour ce faire, on aura besoin d'une boîte d'Edgeworth, un outil très utile. C'est en fait un système de coordonées qui permet de tracer en deux dimensions un problème qui en a 4 (les quantités des biens :math:`X` et :math:`Y` pour les consommateurs 1 et 2). Pour ce faire, on utilise le fait qu'il existe une quantité totale fixe des biens X et Y.  L'exercice A vous apprendra à construire une boîte d'Edgeworth. 

.. figure:: /images/endow.png
   :scale: 35

   La boîte a des dimensions égales aux dotations totales des biens :math:`X` et :math:`Y`. 


**Exercice A**: Montrer la :math:`(x^e_1,y_1^e) = (50,20)` et
:math:`(x^e_2,y_2^e)=(20,50)` dans une boîte d'Edgeworth.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/EjjYu4Ysi2g" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


Un certain nombre d'observations peuvent être faite à partir de la boîte d'Edgeworth.

D'abord, un point dans une boite d'Edgeworth ou deux courbes d'indifférence se croisent ne peut être Pareto optimal. Pourquoi? Parce qu'on peut définir un noyau par rapport à ce point comme étant toutes les allocations qui mènent à une amélioration de Pareto. 

.. figure:: /images/core.png
   :scale: 35

   L'allocation A n'est pas optimale: les courbes d'indifférences se croisent. L'allocation A est une amélioration au sens de Pareto. Le noyau est cette zone entre les deux courbes d'indifférences. 

Quand le noyau est vide, l'allocation est Pareto efficiente ou optimale. Ceci implique que les courbes d'indifférences doivent être tangentes. 

La courbe des contrats est la courbe qui passe par toutes les allocations Pareto efficiente. La frontière de Pareto est la courbe dans l'espace :math:`(U_1,U_2)` qui indique toutes les allocations optimales au sens de Pareto. 

.. figure:: /images/contract.png
   :scale: 35

.. figure:: /images/pareto-frontier.png
   :scale: 50

   Les allocations A et C sont optimales au sens de Pareto. Elles se retrouvent sur la courbe des contrats et sur la frontière de Pareto. Cependant, l'allocation B n'est pas optimale: les courbes d'indifférence se croisent et elle est à l'intérieur de la frontière de Pareto. 

Comment calculer un optimum de Pareto? On peut utiliser le principe de la maximisation contrainte. On pourrait tenter de maximiser le bien-être d'un agent, tout en gardant le bien-être d'un autre agent fixe et en respectant la contrainte de ressources. 

.. math::

   \begin{aligned}
   \max_{X_1,Y_1,X_2,Y_2} u(X_1,Y_1) \end{aligned}

sujet à :

.. math::

   \begin{aligned}
   u(X_2,Y_2)\ge \overline{u}_2 \\
   X_1 + X_2 \le X_e \\
   Y_1 + Y_2 \le Y_e\end{aligned}

On applique la technique du Lagrangien mais cette fois avec trois contraintes. Voici le Lagrangien: 

.. math::
   \begin{split}
    U(X_1,Y_1) + \lambda(U(X_2,Y_2)-\overline{U}_2) \\ 
   - \pi_X (X_1+X_2 - X_e) - \pi_Y (Y_1+Y_2-Y_e) \end{split}


Il y aura donc 6 CPO et 3 multiplicateurs. Les exercices qui suivent vous aideront à comprendre la démarche pour la solution. 

**Exercice B**: Trouvez l'allocation Pareto optimale pour les fonctions d'utilité :math:`u_1` et :math:`u_2` strictement positive and concave,
:math:`u_j = \sqrt{x_j y_j}` pour les consommateurs :math:`j=1,2`, en utilisant la méthode du Lagrangien.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/7hsYEwHfCOc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

**Exercice C**: Trouvez l'allocation Pareto optimale pour les fonctions d'utilités :math:`u_j = \sqrt{x_j y_j}` pour les consommateurs :math:`j=1,2` avec les dotations :math:`x_e = 128` et :math:`y_e=32` si
:math:`\overline{u}_2=48`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/5grk62wBKdk" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

**Exercice D**: Dans l'exercice C, l'allocation :math:`(64,28,64,4)`
est-elle optimale au sens de Pareto? Si elle ne l'est pas, trouvez une amélioration au sens de Pareto dans le noyau.


.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/aK7cvEuO-wA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


**Équilibre de marché dans une boîte d'Edgeworth**

La contrainte budgétaire dépend des dotations et indique les allocations qui sont possibles au prix :math:`p`. Un équilibre de marché implique que le  :math:`TMS` est égal au prix. Puisque le prix est le même pour les deux consommateurs, les :math:`TMS` sont égaux dans un équilibre de marché.


.. figure:: /images/price-equilibrium.png
   :scale: 50

   Un équilibre de marché est donné par A. Il est réalisé à partir de dotations représentées au point E. Le prix relatif :math:`p = p_Y/p_X` donc donc une droite avec pente :math:`-p_X/p_Y = -1/p`. 


Échange et bien-être
++++++++++++++++++++

Considérons le prix d'équilibre: :math:`p^*` et les quantités consommées par le consommateur 1: :math:`X^c_1 = X^c_1(p^*)` et :math:`Y^c_1 = Y^c_1(p^*)`. On a que :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`

Pourquoi? Au prix :math:`p^*`, le panier de dotations :math:`B^e_1 = (X^e_1,Y^e_1)` est disponible mais le consommateur préfère :math:`B^c_1=(X^c_1, Y^c_1)`. Donc, les préférences révèlent que :math:`U_1(X^c_1, Y^c_1) \geq U_1(X^e_1, Y^e_1)`. 


Théorème du bien-être
+++++++++++++++++++++

**Premier théorème**

-  Un équilibre de marché est toujours optimal au sens de Pareto. 

Si une allocation est Pareto-optimale, on ne peut améliorer le sort d'un consommateur sans réduire celui d'un autre. 

Pourquoi ce résultat? À l'allocation d'équilibre :math:`X^c_1(p^*),Y^c_1(p^*),X^c_2(p^*),Y^c_1(p^*)` les courbes d'indifférences sont tangentes à la même contrainte budgétaire. Si elles sont tangentes, c'est donc qu'on a une allocation Pareto optimale. 

**Deuxième théorème**

-  On peut obtenir n'importe quelle allocation Pareto optimale par un équilibre de marché où on devra redistribuer les dotations. 

Ceci nécessite la possibilité d'imposer des taxes, ou confisquer des dotations: paiments ou taxes dites *lump-sum*. On dit alors que l'allocation des ressources est décentralisée (le fruit d'un équilibre de marché et de redistribution des dotations). 

Pourquoi ca fonctionne?

Pour toute allocation :math:`(X_1^*,Y_1^*)`, et valeurs conséquentes pour :math:`(X_2^*,Y_2^*)`,  les courbes d'indifférence sont tangentes. À cette ligne de tangence, on peut redistribuer les dotations pour trouver un point sur cette ligne. N'importe quelle dotation finale (après transfert) sur cette ligne, mène à un équilibre de marché avec :math:`(X^*,Y^*)`.

.. figure:: /images/transfer-equilibrium.png
   :scale: 50

   L'optimum de Pareto A n'est pas atteignable à partir de la dotation :math:`E_0`. Mais un transfert de :math:`T_X` du bien :math:`X` provenant du consommateur 2 au consommateur 1, permet d'atteindre la dotation  :math:`E_1`, à partir de laquelle on peut attendre l'optimum de Pareto A avec un équilibre de marché au prix :math:`p`. 

**Exercice E**: Trouvez le transfert de dotation et le prix, partant de :math:`(64,28,64,4)`, qui donne l'allocation trouvée à l'exercice D.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/4kcC7SgOY9I" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


Efficience des marchés
++++++++++++++++++++++

Les premier et deuxième théorèmes établissent que

-  Le marché est efficient

-  Si on veut une autre allocation efficiente, on peut l'obtenir est redistribuant les ressources et en laissant le marché faire son travail. 

C'est un résultat important en économie: l'économie décentralisée permet d'obtenir ce que le planificateur aurait pu faire sans sacrifier la liberté des agents économiques. 

Un équilibre de marché nécessite seulement que les agents connaissent leur propre préférence. Il n'y a pas de besoin pour un planificateur central qui connait les préférences de tous. Selon `Hayek <https://fr.wikipedia.org/wiki/Friedrich_Hayek>`_, les marchés sont des aggrégateurs d'information. Les économies planifiées perdent cette information (sans mentionner le coût énorme de réussir à connaître les préférences de tous les citoyens). 

Limitations
+++++++++++

Ces résultats encourageant reposent cependant sur des hypothèses très fortes: 

-  Marchés sont compétitifs (on a des prenneurs de prix)

-  Les biens sont homogènes (on sait ce qu'on achète)

-  Aucune externalités

-  On peut imposer des taxes *lump-sum* (pour le 2e théorème)

Même si son cadre est simpliste, et certains diront que peu de marchés remplissent ces conditions, il s'agit d'un modèle qui permet de fixer un *benchmark*, ou un contre-factuel, afin de réflechir aux failles de marchés de manière précise et structuré. 

La théorie de l'équilibre générale a eu un impact certain sur l'économie: en particulier en macroéconomie et pour les marchés financiers. Comme nous le verrons plus tard, les gouvernements mais aussi d'autres organisations, utilisent ces modèles pour prédire l'effet de différentes politiques, notamment en ce qui attrait au climat. 

Un peu d'histoire
+++++++++++++++++

|image|

.. |image| image:: /images/ad1954.png

`Kennet Arrow <https://fr.wikipedia.org/wiki/Kenneth_Arrow>`_ et `Gérard Debreu <https://fr.wikipedia.org/wiki/G%C3%A9rard_Debreu>`_ sont ceux qu'on créditent habituellement pour avoir montré l'existence de l'équilibre général. Ils venaient de background très différent et étaient intéressés à cette question pour des raisons différentes. Düppe (2017) raconte et documente comment ce projet s'est réalisé, non sans des tensions évidentes. 

.. figure:: /images/invitation.png

   `Duppe (2017), Journal of History of Economic
   Thought <https://www.cambridge.org/core/journals/journal-of-the-history-of-economic-thought/article/div-classtitlearrow-and-debreu-de-homogenizeddiv/761E76D5A52C948615066F502277D9DD>`__

Exemple Python
++++++++++++++


|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Equilibre%20Echange.ipynb



