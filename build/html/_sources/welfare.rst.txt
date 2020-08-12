Bien-être
---------

Pour bien évaluer une politique, on peut bien sur regarder son efficacité, c'est-à-dire cible-t-elle le groupe visé, est-ce qu'elle a l'effet attendu sur les comportements, et combien coûte-t-elle étant donné son efficacité. Par exemple, réglementation sur la qualité de l'air peut inciter plusieurs individus à changer de comportement. Le coût par unité d'amélioration de la qualité de l'air peut être élevé. Est-ce que ca veut dire que la politique n'est pas désirable? Comme nous le verrons, la réponse est non. La qualité de l'air est valorisé par la population. Donc, il manque des bénéfices qui ne sont pas mesurés. Au final, on peut savoir si la réglementation est bénéfique, si elle améliore le sort de la population. Afin de répondre à cette question, et permettre de juger des politiques, il faut aller une étape plus loin et se demander comment on peut mesurer le bien-être. 

Trois approches existent: une approche utilitarienne, une approche hicksienne et finalement une approche du bonheur rapporté. 

.. figure:: /images/happy.jpeg
   :scale: 100

Utilisarisme
++++++++++++
Pour chaque citoyen :math:`i\in \{1,\ldots,N\}`, on peut construire une fonction d'utilité :math:`U_i` qui représente ses préférences sur pour un panier de bien dans :math:`B`. Supposons que chaque citoyen obtient le panier :math:`B_1`, :math:`B_2`, ..., :math:`B_N`. Selon cette approche une mesure d'un bien-être d'une société est 

.. math::
   U_1(B_1) + U_2(B_2) + \ldots + U_N(B_N). 

Si on utilise ce critère de bien-être, alors une politique :math:`\mathcal P_0` est mieux que l'alternative :math:`\mathcal P_1` si le bien-être est plus élevé. Içi la fonction qui aggrège les utilités est linéaire, tel que proposée par `Bentham <https://fr.wikipedia.org/wiki/Jeremy_Bentham>`_, mais on peut aussi généraliser à d'autres formes, par exemple l'utilité minimale (`Rawls <https://fr.wikipedia.org/wiki/John_Rawls>`_). 

Cette approche est problématique et a été abandonné rapidement. Elle utilise des utilités cardinales alors que les utilités sont ordinales... On se rappelle bien sur que :math:`U_1` represente les préférences du citoyen :math:`1`, mais :math:`f(U_1)` représente les mêmes préférences pour n'importe quelle fonction croissante :math:`f`. Il existe un nombre infini de fonctions d'utilités qui représentent les même préférences. Par exemple, on aurait pu prendre :math:`2\times U_1`, ce qui peut affecter le choix de politique si une politique favorise davantage ce citoyen...

Donc, le classement des politiques est ambigue:

-  :math:`\mathcal P_0` mieux si :math:`WF = U_1 + U_2`

-  :math:`\mathcal P_1` mieux si :math:`WF = 2U_1 + U_2`

En somme, le bien-être devrait dépendre des préférences et non de :math:`U`. Il demeure que sans trahir l'ordinalité des préférences, les utilités demeurent utiles. On peut définir par exemple une amélioration au sens de Pareto, si l'utilité de tous les individus est au moins égale au niveau de référence. Si personne ne perd, et que certains gagnent, cette situation peut être considérée meilleure au sens de `Pareto <https://fr.wikipedia.org/wiki/Vilfredo_Pareto>`_. 

Variation compensatoire
+++++++++++++++++++++++

Une approche plus prometteuse est de quantifier monétairement le bien-être à l'aide des préférences. On peut définir le bien-être en terme monétaire par les préférences. C'est ce qui a été proposé par `John Hicks <https://fr.wikipedia.org/wiki/John_Hicks>`_. 

On peut utiliser l'utilité indirecte comme point de départ. Mais d'abord, qu'est-ce qu'une politique dans le problème du consommateur? Une politique :math:`\mathcal P` définie une contrainte budgétaire :math:`C_i(\mathcal P,I_i)` pour le citoyen :math:`i` (où :math:`I_i` est le revenu).

L'utilité maximale du citoyen :math:`i` étant donné sa contrainte est:

   .. math:: U_i^*(\mathcal P,I_i) = \max_{B \in C_i(\mathcal P, I_i)} U_i(B)

-  Exemple: Deux biens :math:`X` et :math:`Y`. Utilité
   :math:`U(X,Y) = \ln X + \ln Y`

   Politique :math:`\mathcal P`: tax multiplicative :math:`\tau` sur le prix de :math:`Y`

   | :math:`U_i^*(\mathcal P,I) = \max_{X,Y} \ln X + \ln Y`
   | s.c. :math:`\quad \quad \quad
     p_X  X + p_Y(1 + \tau) Y = I`



Dénotons :math:`\mathcal P_0` le statut quo et considèrons l'implémentation de la politique :math:`\mathcal P`. On peut définir la variation compensatoire comme étant le montant :math:`\Delta I^{CV}` tel que

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P,
      I - \Delta I^{CV})

C'est le montant qu'on doit retirer au consommateur pour garder son bien-être constant au niveau du statut quo.

Note: convention de signe tel que :math:`\Delta I^{CV}>0` quand le changement de politique est *bénéfique*. Par exemple, une baisse de taxe, une hausse des transferts, une baisse de prix. 

**Exercice A**: Trouvez l'expression de la variation compensatoire pour
:math:`\ln X + \ln Y` et une taxe :math:`\tau` sur le bien :math:`Y`.

:math:`\Delta I^{CV}` dépend seulement des préférences

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV})
      \Rightarrow 2 U^*(\mathcal P_0,I) = 2  U^*(\mathcal P, I- \Delta I^{CV})

-  De manière générale, pour n'importe quelle fonction :math:`f`,

   .. math::

      U^*(\mathcal P_0,I) = U^*(\mathcal P, I - \Delta I^{CV})
      \Rightarrow f[U^*(\mathcal P_0,I)] = f[ U^*(\mathcal P, I - \Delta I^{CV})]

Cas spécial utile
+++++++++++++++++

Considérons les préférences pour un bien :math:`X` et l'argent :math:`Y`. Les préférences sont représentées par :math:`U(X,Y) = V(X) + Y`.

La politique de référence :math:`\mathcal P_0`. Le consommateur choisi l'allocation :math:`(X_0, Y_0)`. Maintenant, considérons un changement :math:`\mathcal P`. Le nouveau choix optimal est :math:`(X_1, Y_1)`.

Dans ce cas, la variation compensatoire est :math:`\Delta I^{CV}` telle que

.. math::

   \begin{aligned}
   U(X_0,Y_0) &=& U(X_1, Y_1- \Delta I^{CV}) \\
   V(X_0) + Y_0 &=& V(X_1) + Y_1 - \Delta I^{CV} \\
   \Delta I^{CV} &=& V(X_1) + Y_1 - V(X_0) - Y_0 \\
   \Delta I^{CV} &=& U(X_1,Y_1) - U(X_0,Y_0)\end{aligned}

La variation compensatoire est égale au changement de l'utilité. Les demandes n'ont pas d'effets revenus. Le TMS de cette fonction d'utilité est: 

.. math::
   TMS = \frac{dY}{dX} = - \frac{V'(X)}{1} = -V'(X)

Puisque :math:`p_Y=1` dans le cas où :math:`Y` est de l'argent, :math:`V'(X)` représente la disposition à payer (en dollars) pour une unité de :math:`X`.

Surplus du consommateur
+++++++++++++++++++++++

Supposons le cas de préférences représentés par l'utilité quasi-linéaire pour le bien :math:`X` et l'argent :math:`Y`. :math:`U(X,Y) = V(X) + Y`. Supposons que :math:`V` est concave (:math:`dV/dX` diminue en :math:`X`). 

Considérons une situation où le bien X ne peut être acheter, :math:`\mathcal P_0` et une alternative où :math:`\mathcal P` permet d'acheter le bien :math:`X` au prix :math:`p_X`

.. math::
   \max_{X,Y} U(X,Y) \quad s.c. \quad p_X X + Y = I

On peut substituer la contrainte pour obtenir :math:`\max_{X} V(X) + I - p_X X`. La CPO est 

.. math::
   \frac{dV}{dX}_{|X^*} =  p_X

ce qui permet de trouver la demande :math:`X^*(p_X)`. Dénotons :math:`p_X(X^*) = \frac{dV}{dX}_{|X^*}` la fonction de demande inverse. Ainsi un point sur cette demande inverse donne la disposition à payer pour une unité de :math:`X`.

Dans le cas d'un nouveau produit, la variation compensatoire de :math:`\mathcal P_0` à :math:`\mathcal P` est le surplus du consommateur.

.. math::

   \begin{aligned}
   \Delta I^{CV} &=& V[X^*(p_X)] + I - p_X^*(p_X) - [V(0) + I] \\
   &=& V[X^*(p_X)] - V(0) - p_X X^*(p_X)\end{aligned}

Le premier terme n'est rien d'autre que l'aire sous la courbe de la fonction de demande inverse:

.. math::
   \int_{0}^{X^*} V'(i)di = V(X^*) - V(0)

C'est la somme des dispositions à payer pour chaque unité de :math:`X`. Le deuxième terme est le coût d'acheter la quantité :math:`X^*`. Le surplus provient du fait que le consommateur valorise chaque unité qu'il achète au prix :math:`p_X` au moins plus que ce prix.  

Bien-être et taxation
+++++++++++++++++++++

.. figure:: /images/tax.jpeg
   :scale: 50

La taxation affecte le prix payé par le consommateur. Donc, elle a des effets de bien-être. Dans la théorie du consommateur, nous avons déjà vu qu'une hausse de prix réduit de bien-être du consommateur. Et le revenu compensé permet d'obtenir l'effet substitution. Ce n'est qu'une application de la compensation hicksienne que nous pouvons étendre à l'analyse des taxes. 


   
Considérons l'élimination d'une taxe, le prix passant de :math:`p_X = p+t` à :math:`p_X = p` . On a :math:`X^*(p) > X^*(p+t)` (le bien est normal). Le revenue de la taxe est :math:`T= t\times X^*(p+t)`. 

En terme de variation compensatoire, on a 

   .. math::
      U[X^*(p), I - pX^*(p)] - U[X^*(p+t), I - (p+t) X^*(p+t)]

On obtient que :math:`\Delta I^{CV} > T`: Le consommateur est prêt à payer un montant supérieur au revenu généré par la taxe pour le gouvernement. Donc, l'élimination de la taxe lui est bénéfique. 

La perte de bien-être associée à la taxe est donc de :math:`= \Delta I^{CV} - T`. 

**Exercice B**: Si :math:`V(X) = 10 X - \frac{1}{2}X^2`, trouvez la perte de bien-être associée à une taxe :math:`t` sur le bien :math:`X`. Montrez graphiquement cette perte. 

Bien-être et environnement
++++++++++++++++++++++++++

Généralement, on accorde une valeur positive à la qualité de l'air.  

.. figure:: /images/china_pollution.jpg
   :scale: 50

Il n'y a pas de marché pour la qualité de l'air. Le *Clean Air Act* (1977): le gouvernement american a mis en place un nombre important de mesures pour réduire la pollution. Les lois sont couteuses à implémenter et faire respecter. Question: Étant donné les coûts, est-ce que ces mesures en valent la peine?

Considérons un changement de politique :math:`\mathcal P_0`: aucun control, aucun coûts, à :math:`\mathcal P`: contrôle de la population, ce qui vient à un prix. La variation compensatoire devrait être positive si les citoyens valorisent la qualité de l'air.

Empiriquement, comment faire?

On peut trouver une situation où des gens ont du faire un arbitrage entre pollution et leur richesse financière. Par exemple, l'achat d'une maison dépend bien sur du prix mais aussi de l'environnement, etc. Les prix et la qualité de l'air varie à l'intérieur d'une ville. Dans un marché, les prix devraient être plus élevés quand la qualité de l'air est plus élevée si les acheteurs valorisent la qualité de l'air. 

Bien sur, les prix varient pour toutes sorte de raison. Par exemple, la criminalité dans un quartier pourrait être associée négativement à la qualité de l'air et au prix. Donc, il faudra utiliser des techniques économétriques pour contrôler pour ces différences. 

En utilisant des données provenant de transactions immobilières on peut déterminer la valeur accordée à la qualité de l'air.  Définir X comme étant mesure de la qualité de l'air,  (e.g. concentration de particules) On peut postuler une fonction d'utilité quasi-linéaire:

.. math:: 
   U(X, Y) = V(X) + Y = \alpha X + \beta X^2 +Y

Avec cette fonction d'utilité, :math:`V'(X)` représente la disposition à payer pour la qualité de l'air. En régressant le prix des transactions sur :math:`X` et en controllant pour d'autres facteurs affectant le prix des transactions, on obtient un estimé de :math:`V'(X)`. 

`Chay et Greenstone (2005) <https://www.jstor.org/stable/10.1086/427462>`_ obtiennent des estimés de l'élasticité prix-particule. 

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

Il est donc possible de quantifier ceci une fois tous les paramètres connues. 

**Exercice C**: Pollution par le bruit. L'élasticité prix des maisons à la pollution par le bruit est -0.2. Le gouvernement considère réduire le niveau de pollution de 10% près d'une autoroute. Les ingénieurs nous disent que la technologie nécessaire coûtera 1000$ pour chaque propriété. La politique est financée par une taxe qui mène à une perte de bien être de 43 cents pour chaque dollar à financer. Est-ce que cette politique augmente le bien-être?

Approche bonheur
++++++++++++++++

Pourquoi ne pas simplement demander aux gens s'ils sont heureux? Sur une échelle allant de 1 à 10, ête-vous heureux? Ceci évite d'avoir à spécifier les préférences.  C'est une approche qui gagne une certaine crédibilité avec `le budget 2019 en Nouvelle-Zélande <https://www.weforum.org/agenda/2019/05/new-zealand-is-publishing-its-first-well-being-budget/>`_. C'est `Richard Easterlin <https://fr.wikipedia.org/wiki/Richard_Easterlin>`__ qui a beaucoup popularisé l'utilisation de mesures directes du bien-être. Le Paradox de Easterlin a longtemps suscité de l'intérêt:

.. figure:: /images/easterlin.png
   :scale: 50

Donc, on ne serait pas plus heureux avec davantage de croissance économique. Mais plus tard, on a montré que ce Paradoxe ne tenait plus: 

.. figure:: /images/wolfers.png
   :scale: 50

   `Stevenson and Wolfers (2013), AER: Papers and
   Proceedings <http://users.nber.org/~jwolfers/papers/Satiation(AER).pdf>`__

Il n'en demeure pas moins, que ces mesures peuvent être utile. Pourquoi ne pas utiliser les mesures directes du bien-être pour évaluer les politiques?

-  Avantages: méthode directe sans avoir besoin d'un modèle qui prend en compte toutes les dimensions du bien-être.

-  Inconvénients: On peut mesurer le bien-être de différentes façons et les gens ont des manières différentes de répondre. Plusieurs biais psychologiques en jeu. 

Très peu d'études utilisent les mesures d'évaluation de politiques. Mais il y a beaucoup d'intérêt, pour de bonnes raisons. 
