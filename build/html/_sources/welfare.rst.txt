Bien-être
---------

Pour bien évaluer une politique, on peut regarder son efficacité, c'est-à-dire cible-t-elle le groupe visé, est-ce qu'elle a l'effet attendu sur les comportements, et combien coûte-t-elle étant donné son efficacité? 

Par exemple, une réglementation sur la qualité de l'air peut inciter plusieurs individus à changer de comportement. Le coût par unité d'amélioration de la qualité de l'air peut être élevé. Comment statuer si la politique est désirable? 

En général, la qualité de l'air est valorisée par la population. Donc, on peut mesurer les bénéfices par les préférences. Au final, on peut savoir si la réglementation est bénéfique étant donné son coût. Alors qu'on s'arrête souvent aux retombés économiques ou fiscales d'une intervention, on oublie très souvent de compter les bénéfices en terme de bien-être. 

Afin de répondre à ces question, et permettre de juger des politiques, il faut aller une étape plus loin que ce qu'on a fait et se demander comment on peut mesurer le bien-être par les préférences. 

Trois approches existent: une approche utilitarienne, une approche hicksienne et finalement une approche du bonheur rapporté. 

.. figure:: /images/happy.jpeg
   :scale: 100

Utilisarisme
++++++++++++
Pour chaque citoyen :math:`i\in \{1,\ldots,N\}`, on peut construire une fonction d'utilité :math:`U_i` qui représente ses préférences sur pour un panier de bien dans un ensemble :math:`B`. Supposons que chaque citoyen obtient le panier :math:`B_1`, :math:`B_2`, ..., :math:`B_N`. Selon cette approche une mesure d'un bien-être est 

.. math::
   U_1(B_1) + U_2(B_2) + \ldots + U_N(B_N). 

Si on utilise ce critère de bien-être, alors une politique :math:`\mathcal P_0` est mieux que l'alternative :math:`\mathcal P_1` si la somme des utilités est plus élevée. Içi la fonction qui aggrège les utilités des différents citoyens est linéaire, tel que proposé par `Bentham <https://fr.wikipedia.org/wiki/Jeremy_Bentham>`_, mais on peut aussi généraliser à d'autres formes, par exemple l'utilité minimale sous-jacente à la théorie de la justice sociale de (`Rawls <https://fr.wikipedia.org/wiki/John_Rawls>`_). 

Cette approche est problématique et peu utilisée. Elle suppose des utilités cardinales alors que les utilités sont ordinales... On se rappelle que :math:`U_1` represente les préférences du citoyen :math:`1`, mais :math:`f(U_1)` représente les mêmes préférences pour n'importe quelle fonction croissante :math:`f`. Il existe un nombre infini de fonctions d'utilités qui représentent les mêmes préférences. Par exemple, on aurait pu prendre :math:`2\times U_1`, ce qui peut affecter le choix de politique si une politique favorise davantage ce citoyen...

Donc, le classement des politiques est ambigue: on peut avoir :math:`\mathcal P_0` meilleure  si :math:`W = U_1 + U_2` alors que :math:`\mathcal P_1` est meilleure si on utilise :math:`W = 2U_1 + U_2`

En somme, le bien-être devrait dépendre des préférences et non de :math:`U`. Il demeure que sans trahir l'ordinalité des préférences, les utilités demeurent utiles. On peut définir par exemple une **amélioration au sens de Pareto**, si l'utilité de tous les individus est au moins égale au niveau de référence avec un changement de politique. Si personne ne perd, et que certains gagnent, cette situation peut être considérée meilleure au sens de `Pareto <https://fr.wikipedia.org/wiki/Vilfredo_Pareto>`_. L'amélioration au sens de Pareto est indépendante de l'échelle de l'utilité. C'est un concept ordinal. 

Variation compensatoire
+++++++++++++++++++++++

Une approche plus prometteuse est de quantifier de façon monétaire le bien-être à l'aide des préférences. `John Hicks <https://fr.wikipedia.org/wiki/John_Hicks>`_ propose d'utiliser la variation compensatoire. 

Qu'est-ce qu'une politique dans le problème du consommateur? Une politique :math:`\mathcal P` définie une contrainte budgétaire :math:`C_i(\mathcal P,I_i)` pour le citoyen :math:`i` (où :math:`I_i` est le revenu).

On peut utiliser l'utilité indirecte comme point de départ. L'utilité maximale du citoyen :math:`i` étant donné sa contrainte est:

   .. math:: U_i^*(\mathcal P,I_i) = \max_{B \in C_i(\mathcal P, I_i)} U_i(B)

Exemple: Deux biens :math:`X` et :math:`Y`. Utilité :math:`U(X,Y) = \log X + \log Y`. Une politique :math:`\mathcal P`: avec une taxe multiplicative :math:`\tau` sur le prix de :math:`Y`. Alors l'utilité indirecte est donnée par:

.. math::
   U_i^*(\mathcal P,I) = \max_{X,Y} \left[\log X + \log Y: p_X  X + p_Y(1 + \tau) Y \leq I \right]
     
Dénotons :math:`\mathcal P_0` le statut quo et considèrons l'implémentation de la politique :math:`\mathcal P`. On peut définir la variation compensatoire comme étant le montant :math:`\Delta I^{CV}` tel que

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P,I - \Delta I^{CV})

C'est le montant qu'on doit retirer au consommateur pour garder son bien-être constant au niveau du statut quo.

Note: on utilise une convention de signe telle que :math:`\Delta I^{CV}>0` quand le changement de politique est *bénéfique*. Par exemple, une baisse de taxe, une hausse des transferts, une baisse de prix. 

**Exercice A**: Trouvez l'expression de la variation compensatoire pour
:math:`U = XY` et une taxe :math:`\tau` sur le bien :math:`Y`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/6imTJaSOFIc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


:math:`\Delta I^{CV}` dépend seulement des préférences

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV}) \\
      \Rightarrow 2 U^*(\mathcal P_0,I) = 2  U^*(\mathcal P, I- \Delta I^{CV})

De manière générale, pour n'importe quelle fonction :math:`f`,

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV}) \\
      \Rightarrow f[U^*(\mathcal P_0,I)] = f[ U^*(\mathcal P, I - \Delta I^{CV})]

Cas spécial utile
+++++++++++++++++

Considérons les préférences pour un bien :math:`X` et l'argent :math:`Y`. Les préférences sont représentées par :math:`U(X,Y) = V(X) + Y`. 

La politique de référence est :math:`\mathcal P_0`. Le consommateur choisi l'allocation :math:`(X_0, Y_0)`. Maintenant, considérons un changement :math:`\mathcal P`. Le nouveau choix optimal est :math:`(X_1, Y_1)`.

Dans ce cas, la variation compensatoire est :math:`\Delta I^{CV}` ou

.. math::

   \begin{aligned}
   U(X_0,Y_0) &= U(X_1, Y_1- \Delta I^{CV}) \\
   V(X_0) + Y_0 &= V(X_1) + Y_1 - \Delta I^{CV} \\
   \Delta I^{CV} &= V(X_1) + Y_1 - V(X_0) - Y_0 \\
   \Delta I^{CV} &= U(X_1,Y_1) - U(X_0,Y_0)\end{aligned}

La variation compensatoire est égale au changement de l'utilité. De par la linéarité dans l'argent, l'utilité est en dollars.  Le TMS de cette fonction d'utilité est: 

.. math::
   TMS = \frac{dY}{dX} = - \frac{V'(X)}{1} = -V'(X)

Puisque :math:`p_Y=1` dans le cas où :math:`Y` est de l'argent, :math:`V'(X)` représente la disposition à payer (en dollars) pour une unité de :math:`X`.

Surplus du consommateur
+++++++++++++++++++++++

Supposons le cas de préférences représentées par l'utilité quasi-linéaire pour le bien :math:`X` et l'argent :math:`Y`. :math:`U(X,Y) = V(X) + Y`. Supposons que :math:`V` est concave (:math:`dV/dX` diminue en :math:`X`). 

Considérons une situation où le bien :math:`X` ne peut être acheté, :math:`\mathcal P_0` et une alternative où :math:`\mathcal P` permet d'acheter le bien :math:`X` au prix :math:`p_X`. Le problème est donné par

.. math::
   \max_{X,Y} U(X,Y) \quad s.c. \quad p_X X + Y = I

On peut substituer la contrainte pour obtenir :math:`\max_{X} V(X) + I - p_X X`. La CPO est 

.. math::
   \frac{dV}{dX} =  p_X

ce qui permet de trouver la demande :math:`X^*(p_X)`. Dénotons :math:`p_X(X^*) = \frac{dV}{dX}`, la fonction de demande inverse. Ainsi un point sur cette demande inverse donne la disposition à payer pour une unité de :math:`X`.

Dans le cas d'un nouveau produit, la variation compensatoire de :math:`\mathcal P_0` à :math:`\mathcal P` est le surplus du consommateur.

.. math::

   \begin{aligned}
   \Delta I^{CV} &=& V[X^*(p_X)] + I - p_X^*(p_X) - [V(0) + I] \\
   &=& V[X^*(p_X)] - V(0) - p_X X^*(p_X)\end{aligned}

Le premier terme n'est rien d'autre que l'aire sous la courbe de la fonction de demande inverse:

.. math::
   \int_{0}^{X^*} V'(i)di = V(X^*) - V(0)

C'est la somme des dispositions à payer pour chaque unité de :math:`X`. Le deuxième terme est le coût d'acheter la quantité :math:`X^*`. Le surplus provient du fait que le consommateur valorise chaque unité qu'il achète au prix :math:`p_X` davantage que le prix :math:`p_X`.  

.. figure:: /images/surplus.png
   :scale: 100

   La zone A+B est donné par :math:`V[X_0] - V(0)` alors que la zone B est la dépense :math:`p_{X0}X_0`. Ainsi le surplus du consommateur est A+B - B = A. 

**Exercice B**: Si :math:`V(X) = 10 X - \frac{1}{2}X^2`, trouvez l'expression du surplus du consommateur. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/R1OKZp8Hqj0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


Bien-être et taxation
+++++++++++++++++++++

.. figure:: /images/tax.jpeg
   :scale: 50

La taxation affecte le prix payé par le consommateur. Donc, elle a des effets sur le bien-être. Dans la théorie du consommateur, nous avons déjà vu qu'une hausse de prix réduit le bien-être du consommateur. Nous avons qu'à appliquer le concept de revenu compensé à l'analyse des taxes. 

Considérons l'élimination d'une taxe, le prix passant de :math:`p_X = p+t` à :math:`p_X = p` . On a :math:`X^*(p) > X^*(p+t)` (le bien n'est pas *Giffen*). Le revenu de la taxe est :math:`T= t X^*(p+t)`. 

En terme de variation compensatoire, on a 

   .. math::
      U[X^*(p), I - pX^*(p)] - U[X^*(p+t), I - (p+t) X^*(p+t)]

On obtient que :math:`\Delta I^{CV} > T`: Le consommateur est prêt à payer un montant supérieur au revenu généré par la taxe pour le gouvernement. Donc, l'élimination de la taxe lui est bénéfique. 

La perte de bien-être associée à la taxe est donc :math:`\Delta W = \Delta I^{CV} - T`. 

**Exercice C**: Si :math:`V(X) = 10 X - \frac{1}{2}X^2`, trouvez la perte de bien-être associée à une taxe :math:`t` sur le bien :math:`X`. Montrez graphiquement cette perte. 


.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/u74TNMcFb2k" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Bien-être et environnement
++++++++++++++++++++++++++

Généralement, on accorde une valeur positive à la qualité de l'air.  

.. figure:: /images/china_pollution.jpg
   :scale: 50

Il n'y a pas de marché pour la qualité de l'air. Avec le *Clean Air Act* (1977), le gouvernement american a mis en place un nombre important de mesures pour réduire la pollution. Les lois sont couteuses à implémenter et faire respecter. Pour justifier ces lois, on doit montrer que les bénéfices sont élevés. 

Considérons un changement de politique :math:`\mathcal P_0`: aucun contrôle, aucun coût, à :math:`\mathcal P`: contrôle de la pollution, ce qui implique des coûts. La variation compensatoire devrait être positive si les citoyens valorisent la qualité de l'air.

Empiriquement, comment faire pour estimer les préférences?

On peut trouver une situation où des gens ont du faire un arbitrage entre pollution et leur richesse financière. Par exemple, l'achat d'une maison dépend bien sur du prix mais aussi de l'environnement, etc. Les prix et la qualité de l'air varient à l'intérieur d'une ville. Dans un marché, les prix devraient être plus élevés quand la qualité de l'air est plus élevée si les acheteurs valorisent la qualité de l'air. 

En utilisant des données provenant de transactions immobilières on peut déterminer la valeur accordée à la qualité de l'air.  Définir :math:`X` comme étant mesure de la qualité de l'air,  (e.g. concentration de particules) On peut postuler une fonction d'utilité quasi-linéaire:

.. math:: 
   U(X, Y) = V(X) + Y = \alpha X + \beta X^2 +Y

Avec cette fonction d'utilité, :math:`V'(X)` représente la disposition à payer pour la qualité de l'air. En régressant le prix des transactions sur :math:`X` et en controllant pour d'autres facteurs affectant le prix des transactions, on obtient un estimé de :math:`V'(X)`. 

`Chay et Greenstone (2005) <https://www.jstor.org/stable/10.1086/427462>`_ obtiennent des estimés de l'élasticité prix-particule (entre -0.2 et -0.35). 

.. figure:: /images/chay.png
   :scale: 50

Maintenant, comment évaluer une politique avec ces informations? Le gouvernment dépense :math:`X_{GOV}`. Le coût pour financer ces dépenses est :math:`c X_{GOV}` avec :math:`c>1` est le coût incluant la perte de bien-être dû à la taxation nécessaire.

La politique change de  :math:`(0,0)` à :math:`(X_{GOV}, - c X_{GOV})`. Le surplus du consommateur est la variation compensatoire:

.. math:: 
   \Delta I^{CV} =  V(X_{GOV}) - V(0) - c X_{GOV} .

Une fois l'analyse faite, on peut aussi se demander quelle serait la qualité de l'air optimale afin de voir s'il est encore possible de resserer les restrictions. 

La pollution optimale est le niveau de pollution qui maximise: 

.. math:: 
   U(X) = V(X) + I - c X 

La CPO est

   .. math:: \frac{dV}{d X}_{|X^*} = c

Il est donc possible de quantifier ceci une fois tous les paramètres connus. 

**Exercice D**: Pollution par le bruit. L'élasticité prix des maisons à la pollution par le bruit est -0.2. Le gouvernement considère réduire le niveau de pollution de 10% près d'une autoroute. Les ingénieurs nous disent que la technologie nécessaire coûtera 1000$ pour chaque propriété. La politique est financée par une taxe qui mène à une perte de bien être de 43 cents pour chaque dollar à financer. Est-ce que cette politique augmente le bien-être?


.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/ud9JiRUpcfg" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Cette approche est très utilisée. Même si a priori, ces problèmes semblent dépendre de la spécification des préférences, ce n'est pas toujours le cas, comme le montre l'exercice D (on a besoin que de l'élasticité prix dans l'exercice). Une autre enjeu est la possibilité que certains aient une variation compensatoire négative alors que pour d'autres celles-ci sont positives. A moins de spécifier un mécanisme pour aggréger les variations compensatoires (une somme?), ce qui n'est pas neutre d'un point de vue de l'équité, l'approche la plus commune sera de parler d'amélioration potentielle de Pareto si la somme des variations compensatoires est positive et où une forme de compensation pourrait être prévue pour ceux qui y perdent. La pluspart des politiques font des perdants. Il est donc tout aussi important de statuer sur la désirabilité de la politique que d'identifier les perdants afin de les compenser. 

Approche bonheur rapporté
+++++++++++++++++++++++++

Pourquoi ne pas simplement demander aux gens s'ils sont heureux? Sur une échelle allant de 1 à 10, ête-vous heureux? Ceci évite d'avoir à spécifier les préférences.  C'est une approche qui gagne une certaine crédibilité avec `le budget 2019 en Nouvelle-Zélande <https://www.weforum.org/agenda/2019/05/new-zealand-is-publishing-its-first-well-being-budget/>`_. C'est `Richard Easterlin <https://fr.wikipedia.org/wiki/Richard_Easterlin>`__ qui a beaucoup popularisé l'utilisation de mesures directes du bien-être. Le Paradox de Easterlin a longtemps suscité de l'intérêt:

.. figure:: /images/easterlin.png
   :scale: 50

Donc, on ne serait pas plus heureux avec davantage de revenu, un résultat contre-intuitif: l'argent ne fait pas le bonheur. Mais plus tard, on a montré que ce Paradoxe ne tenait plus: 

.. figure:: /images/wolfers.png
   :scale: 50

   `Stevenson and Wolfers (2013), AER: Papers and
   Proceedings <http://users.nber.org/~jwolfers/papers/Satiation(AER).pdf>`__

Il n'en demeure pas moins, que ces mesures peuvent être utile puisque le bonheur, c'est plus qu'un portefeuille bien garnie. Pourquoi ne pas utiliser les mesures directes du bien-être pour évaluer les politiques?

-  Avantages: méthode directe sans avoir besoin d'un modèle qui prend en compte toutes les dimensions du bien-être.

-  Inconvénients: On peut mesurer le bien-être de différentes façons et les gens ont des manières différentes de répondre. Plusieurs biais psychologiques en jeu. 

Très peu d'études utilisent ces mesures pour évaluater des politiques. Mais il y a beaucoup d'intérêt, pour de bonnes raisons. 

Pour ceux qui veulent approfondir, voici une entrevue avec Angus Deaton sur la mesure du bonheur: 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/pfHcdee4R3M" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Exemple Python Bien-être
++++++++++++++++++++++++

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/Welfare.ipynb

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Diiljk3X1iE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

