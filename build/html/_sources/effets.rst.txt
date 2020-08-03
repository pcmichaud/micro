.. _Effets:



Effets Prix et Revenu
---------------------

Est-ce qu'une taxe sur l'essence réduit la consommation d'essence et encourage le transport en commun?

Pour le savoir, on doit étudier empiriquement comment la demande d'essence et de transport en commun réagit à une taxe sur l'essence. On veut peut-être aussi comprendre si cette taxe sera régressive (si elle aura un effet important sur le pouvoir d'achat des moins nantis). Si on veut les compenser, il faudra connaître les effets prix et revenu. 

Les élasticités prix et revenu peuvent être estimés sans théorie. Mais comment utiliser ces informations pour répondre aux questions plus normatives?

La théorie sur le choix du consommateur nous fournira un bon nombre d'outils ...

Demande et Préférences
++++++++++++++++++++++

Formalisons cet exemple: 

-  Essense (X) et Transport en commun (Y)

-  Utilité :math:`U(X,Y)`

-  Contrainte Budgétaire: :math:`p_X Y+ p_Y Y = I`

 Les fonctions de demande :math:`(X^*, Y^*)` sont telles que 

.. math::

   \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}  \\
   p_X X + p_Y Y = I

À l'optimum, le budget est respecté et le consommateur est indifférent entre
réduire :math:`X` pour augmenter :math:`Y` (et vice versa)

Il y a deux équations, deux variables: la solution pour :math:`X^*` et
:math:`Y^*` en fonction de :math:`(p_X,p_Y,I)` donne les demandes marshalliennnes. 

**Exemple**

Pour les préférences représentées par :math:`U(X,Y) = \ln X +  2\ln Y`,

.. math::

   \frac{dU}{dX}\Bigg/\frac{dU}{dY} = \frac{p_X}{p_Y}  \iff \frac{1/X}{2/Y} = \frac{p_X}{p_Y}  \iff  p_Y Y = 2p_X X 

On utilise :math:`p_X X + p_Y Y =  I` ce qui permet d'obtenir

.. math:: 
   X^* = \frac{I}{3p_X}  \quad, Y^* = \frac{2I}{3p_Y}

Comment :math:`X^*` et :math:`Y^*` varient en fonction de :math:`I`?

Effets revenu
+++++++++++++

**Courbe d'Engel**

-  Le consommateur demande :math:`X(p_X,p_Y,I)` et :math:`Y(p_X,p_Y,I)`.

-  La courbe d'Engel pour :math:`X`: Comment :math:`X^*` change quand
   :math:`I` change?

-  Proportion du budget dédiée à :math:`X`:
   :math:`s_X = \frac{p_X X}{I}`

**Bien normal**

Un bien est normal si et seulement si la demande de ce bien augmente avec le revenu (prix constant) 

**Bien inférieur**

Un bien est inférieur si sa demande diminue quand le revenu augmente (à prix constant)

L'essence est-elle un bien inférieur ou normal? Une des études célèbres sur cet enjeu indique que même si on pourrait croire que l'essence est un bien inférieur, ceci dépend si on mesure en proportion du revenu ou des dépenses `(Poterba, 1991) <http://www.nber.org/chapters/c11271>`_? Pourquoi?

|poterba|

.. |poterba| image:: /images/poterba.png 
   :scale: 40%

Pour quantifier les effets revenu, on voudra utiliser une élasticité revenu de la forme: 

.. math::

   \eta_{X,I} = \frac{\partial X}{\partial I}\frac{I}{X}

En pratique, il n'est pas facile d'observer ces élasticités-revenu en s'assurant que le changement de revenu est *exogène*. Quel type d'évennement pourrait-on exploiter?

Effets Prix
+++++++++++

Comment les demandes :math:`X^*` and :math:`Y^*` changent si 
:math:`p_Y` et :math:`I` restent constant mais que :math:`p_X` change?

Pour décrire les changements de demande, on utilise l'élasticité: 

.. math::

   \eta_{X,p} = \frac{\partial X}{\partial p_X}\frac{p_X}{X}

Ell est invariante aux unités monétaires. Encore une fois, un enjeu important c'est d'estimer cette élasticité dans un contexte où le changement de prix est *exogène*. Heureusement, il y a les taxes qui changent parfois pour des raisons indépendantes de la demande... Sinon, des chocs d'offre (manipulation du prix d'un cartel, désastre naturel). 

Au Danemark, une `étude <https://www.sciencedirect.com/science/article/abs/pii/S0094119018300779>`_ montre que l'elasticité varie considérablement à travers le pays et en particulier dépendant de la distance qu'ont les gens à faire chaque jours. 

.. image:: /images/elasticity_denmark.png
   :scale: 65%

Au États-Unis, une autre `analyse <https://www.aeaweb.org/articles?id=10.1257/pol.6.4.302>`_ montre qu'il faut faire la distinction entre l'effet d'un changement de prix et une taxe. L'effet d'une taxe est plus important? Pourquoi? Quelles implications pour les revenus de taxes? Indice: regarder l'effet de l'élasticité sur les revenus de la taxe. 

.. image:: /images/elasticity_tax_price.png
   :scale: 45%

Une hausse de prix (ou taxe) a l'effet direct de réduire le bien-être du consommateur. On pourrait vouloir compenser certains ménages parce que la taxe poursuit un objectif noble (e.g. climat, redistribution). Afin de calculer la compensation possible suite à une taxe, il faut décomposer le changement de demande pour l'essence quand le prix :math:`p_X` augmente. Il y a deux forces:

-  Le transport en commun est plus abordable que l'automobile (essence): le consommateur voudra substituer vers le transport en commun. C'est un effet *substitution* qui provient du *signal de prix*.

   .. math:: \frac{U'_X(X,Y)}{U'_Y(X,Y)} = \frac{p_X}{p_Y}

-  Besoin de plus de revenu pour acheter le même panier de référence (réduction pouvoir d'achat): *effet revenu*. Les `gilets jaunes <https://www.rtl.fr/actu/conso/pouvoir-d-achat-une-etude-de-l-insee-explique-la-colere-des-gilets-jaunes-7797202617>`_ ont certainement perçu cet effet. 

Notre **objectif:** Identifier les effets prix et revenus

Demande compensée
^^^^^^^^^^^^^^^^^

La demande compensée est un passage obligé. Elle permettra de séparer ces effets. 

**Contexte**

-  Prix de référence :math:`(p_X,p_Y)`, revenu de référence :math:`I`, nouveau prix :math:`(\hat p_X,p_Y)`

-  Demande de référence, :math:`X(p_X,p_Y,I)`, utilité indirecte de référence
   :math:`V(p_X,p_Y,I)`

-  Nouvelle demande, :math:`X(\hat p_X, p_Y, I)`, nouvelle utilité indirecte
   :math:`V(\hat p_X,p_Y,I)`.

Le concept de revenu compensé: revenu :math:`I^{cmp}` tel qu'on peut préserver le niveau d'utilité de référence **aux nouveaux prix**. 

   .. math:: V(p_X,p_Y, I) = V(\hat p_X, p_Y,  I^{cmp})

La demande compensée (ou `hicksienne <https://fr.wikipedia.org/wiki/John_Hicks>`_) est donnée par la demande marshallienne où l'on remplace le revenu par le revenu compensé :math:`X^{cmp}= X(\hat p_X, p_Y,  I^{cmp})`.

Le revenu compensé pour une hausse de prix est toujours plus élevé que le revenu de référence. La différence est la compensation requise. Si la hausse de prix est une nouvelle taxe, cette compensation est la compensation requise pour maintenir le bien-être du consommateur constant tout en ayant modifié les comportements. 

**Loi de la demande compensée** Si :math:`\hat p_X > p_X`, alors :math:`X^{cmp}(p_X,p_Y,I)<X(p_X,p_Y,I)`. La demande compensée :math:`X` est décroissante dans le prix :math:`p_X`.

**Exercice A**: Calculez le revenu et la demande compensée pour
:math:`X` si :math:`U(X,Y) = XY` et :math:`p_XX+p_YY \le I` pour un changement de prix :math:`\hat p_X > p_X`.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/0dfoolULChE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Précisons maintenant davantage les effets substitutions et revenu. 

**Effet substitution**

Changement de demnde causé par un changement de prix relatif, en gardant l'utilité constante. 

Effet substitution :math:`=` Demande compensée - Demande de référence

   .. math:: \Delta X^{{cmp}} =  X(\hat p_X,p_Y,I^{cmp}) - X(p_X,p_Y,I)

**Effet revenu**

Changement de la demande causé par un changement du pouvoir d'achat, en gardant les prix constants. 

-  Effet revenu :math:`=` Nouvelle demande - demande compensée

.. math:: \Delta X^{I} = X(\hat p_X,p_Y,I) - X(\hat p_X,p_Y,I^{cmp})

On peut approximer le revenu compensé pour un petit changement de prix paramétrisé 

  :math:`\hat p_X = p_X + \Delta p_X`. 

Pour nettoyer la notation et y voir clair, dénotons

  :math:`X^* = X(p_X,p_X,I)`, :math:`Y^* = Y(p_X,p_Y,I)`

Définissons ensuite :math:`I^{cmp}= I + \Delta I^{cmp}`,
:math:`X^{cmp}= X^* + \Delta X^{cmp}` et
:math:`Y^{cmp}= Y^* + \Delta Y^{cmp}`.

Alors, 

.. math::

   \begin{aligned}
   I^{cmp}& =  \hat p_X X^{cmp}+  p_Y Y^{cmp}\\
    & =  (p_X + \Delta p_X)(X^* + \Delta X^{cmp}) + p_Y(Y^* + \Delta Y^{cmp})\\ 
     &=  \underbrace{p_X X^* + p_YY^*}_{=I} +\underbrace{\Delta p_X \Delta X^{cmp}}_{\simeq 0} + \Delta p_X X^* \\
     & \quad \quad \quad + \underbrace{ p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}}}_{=0}\\ & \simeq I+  \Delta p_X X^* \\
    \Delta I^{cmp}&\simeq \Delta p_X X^*\end{aligned}

Pourquoi :math:`p_X\Delta X^{{cmp}} + p_Y \Delta Y^{{cmp}} = 0`?

:math:`(X^*,Y^*)` et :math:`(X^{cmp},Y^{cmp})` sont sur la même courbe d'indifférence, ce qui implique

   .. math:: \frac{\Delta Y^{cmp}}{\Delta X^{cmp}} = TMS_{X\to Y}

:math:`(X^*,Y^*)` est optimal aux prix :math:`p_X, p_Y`, ce qui implique que :math:`TMS_{X\to Y} = -\frac{p_X}{p_Y}`.

#. Alors, :math:`p_X \Delta X^{cmp}+ p_Y \Delta Y^{cmp}= 0`.

**Exercice B**: Voir si cette approximation est bonne pour
:math:`U(X,Y) = XY` avec prix et revenu de référence
:math:`(p_X,p_Y,I) = (1,1,100)` et :math:`\Delta p_X = 1` dans un premier temps et 
:math:`\Delta p_X = 0.1` dans un 2e temps.


.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Ovjh0AhL6mY" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Équation de Slutsky
+++++++++++++++++++

L'équation de `Slutsky <https://fr.wikipedia.org/wiki/Eugen_Slutsky>`_ permet de relier l'effet prix total, l'effet prix compensé (hicksien) et l'effet revenu. Le premier et le dernier sont observables, le 2e ne l'est pas et est nécessaire pour calculer une compensation. 

Pour garder la notation simple, considérons

.. math::

   \begin{aligned}
    X^* &= X(p_X,p_Y,I), &     X(p_X + \Delta p_X, p_Y,I) &= X^* + \Delta X^*,\\ && X(p_X + \Delta p_X, p_Y,I) &= X^{cmp}+\Delta X^I\end{aligned}

On obtient

.. math::

   \begin{aligned}
   \underbrace{\Delta X^*}_{\text{Effet total}} = \underbrace{\Delta X^{cmp}}_{\text{Effet substitution}} + \underbrace{\Delta X^I}_{\text{Effet prix}}\end{aligned}

**Exercice C**: Trouvez les effets revenu et prix de l'exercice B (:math:`\Delta p_X = 1`). 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/04cuRQMZi5c" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Puisque

.. math:: \Delta X^I =   -\frac{\partial X}{\partial I} \Delta I^{cmp}=  -\frac{\partial X}{\partial I}  \Delta p_X X^*

 alors,

.. math::

   \begin{aligned}
   \Delta X^* &=   \underbrace{\Delta X^{{cmp}}}_{\leq 0} -   \underbrace{\frac{\partial X}{\partial I}\times \Delta p_X X^*}_{\geq 0 \text{ si normal, } <0 \text{ si inférieur}} \end{aligned}

En terme d'élasticité,

.. math::

   \begin{aligned}
   \frac{\Delta X^*}{\Delta p_X}\frac{p_X}{X^*} & = \frac{\Delta X^{cmp}}{\Delta p_X}\frac{p_X}{X^*} - \frac{\partial X}{\partial I} \Delta p_X X^*\times\frac{p_X}{\Delta p_X X^*}\frac{I}{I} \end{aligned}

L'équation de Slutsky est donc:

.. math:: \eta_{X,p} = \eta^{cmp}_{X,p}  - \eta_{X,I} \cdot s_X

**Exercice D**: Pour les préférences Cobb-Douglas :math:`U(X,Y) = X^\alpha Y^{1-\alpha}`, calculez l'élasticité prix compensée à l'aide de l'équation de Slutsky. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/si2THh8yqRI" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Effets prix croisés
+++++++++++++++++++

D'abord, on peut inférer la nature des biens par les fonctions de demande. Les biens :math:`X` et :math:`Y` sont:

-  Substituts: si l'effet prix croisé
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} >0`

-  Compléments: si l'effet prix croisé
   :math:`\frac{\partial X^{cmp}}{\partial p_Y} <0`

Qu'en est-il pour le transport en commun et les taxes sur l'essence? Cette élasticité est-elle importante pour la politique publique?

Propriétés des fonctions de demandes
++++++++++++++++++++++++++++++++++++

-  Homogénéité de degré zéro (pas d'illusion monétaire)

   .. math:: X(\lambda p_X,\lambda p_Y,\lambda I) = X(p_X,p_Y,I)

-  Symmétrie:

   .. math:: \frac{\partial X^{cmp}}{\partial p_Y} =\frac{\partial Y^{cmp}}{\partial p_X}

-  Additivité:

   .. math:: p_X \frac{\partial X(p_X,p_Y,I)}{\partial I} + p_Y \frac{\partial Y(p_X,p_Y,I)}{\partial I} = 0

-  Negativité (loi de la demande compensée):

   .. math:: \frac{\partial X^{cmp}}{\partial p_X}<0,\frac{\partial Y^{cmp}}{\partial p_Y}<0

Indices de prix et de coût de la vie
++++++++++++++++++++++++++++++++++++

Pour mesurer un changement du coût de la vie (pouvoir d'achat), on utilise des indices de prix à la consommation. Un indice souvent utilisé est l'indice de Laspeyres:

.. math:: \pi_L = \frac{\hat p_X  X + \hat p_Y Y}{p_X X + p_Y Y}

Ainsi X et Y, consommé dans la situation de référence, sont aussi utilisées après le changement de prix. L'indice des prix à la consommation garde les quantités (part des dépenses) fixes dans le court terme (les changent mais pas très fréquemment). Plusieurs prestations gouvernementales sont indexées annuellement de la sorte afin de maintenir le pouvoir d'achat (pensions, crédit d'impôt, etc). Mais est-ce un bon indice pour mesurer une variation du coût de la vie?

La théorie qu'on vient de voir indique qu'il faut tenir compte des réactions comportementales. Si le prix d'un bien augmente, il y aura substitution. Pour bien mesurer la consommation, on revient à la théorie:  

-  Après une augmentation de prix du bien :math:`X`, la compensation nécessaire pour garder le bien-être constant est:

   .. math:: \pi_I =  \frac{I^{cmp}}{I}

Tout dépendant des préférences, il se peut que l'indice de prix hicksien donne une réponse différente de l'indice de Laysperes. En particulier, si la part d'un bien décroit si son prix augmente, l'indice Hicksien pourrait donner une augmentation du coût de la vie plus faible qu'un indice de type Laysperes. C'est ce qu'on appelle un biais de substitution. 

Avec la pandémie et le confinement, la consommation d'essence a chuté. Le prix de l'essence a aussi chuté (pour pleins de raisons, incluant une décision des cartels). Est-ce qu'un indice de Laysperes donne un bon reflet du changement du pouvoir d'achat dans un tel contexte? Cet `article <https://www.nber.org/papers/w27352>`_ fait le calcul pour les États-Unis et montre que l'inflation est sous-estimée considérablement. 

Biens Giffen
++++++++++++

Il existe un type de bien pour lequel la demande augmente avec le prix! On peut comprendre ce type de bien avec l'équation de Slutsky:

.. math:: \eta_{X,p} = \eta^{cmp}_{X,p}  - \eta_{X,I} \cdot s_X.

Le premier terme à droite est toujours négatif. C'est le résultat de la loi de la demande compensée. Il faut donc que le 2e terme soit négatif (puisqu'il est soustrait du premier terme). 

On en déduit qu'une condition nécessaire est que le bien soit inférieur (demande diminue quand revenu augmente) et que le bien consitue une part importante du budget pour que ce deuxième terme soit suffisament élevé. 

Ainsi, il est possible que :math:`\eta_{X,p}>0`. Mais est-ce que ce cas spécial existe?

L'exemple classique donné est le cas des pommes de terre en Irlande, même si des doutes existent sur cet exemple (voir ce résumé de l'histoire derrière les biens Giffen `wikipedia <https://en.wikipedia.org/wiki/Giffen_good>`_). Un meilleur exemple est donné par l'analyse d'un programme implanté en Chine qui donnait une subvention pour la consommation de riz (`Jensen et Miller (2008) <https://www.aeaweb.org/articles?id=10.1257/aer.98.4.1553>`_). La subvention (baisse de prix) a mené à une diminution de la consommation de riz. Les auteurs ne trouvent pas la même chose pour le blé... 

Les entreprises et l'analyse de la demande
++++++++++++++++++++++++++++++++++++++++++

Pourquoi une entreprise devrait-elle étudier les propriétés de la demande pour ses biens? Elle peut potentiellement augmenter ses revenus en:

* fixant un prix qui maximise ses revenus si elle a un pouvoir de marché
* discriminant par les prix (segmentation) 

L'analyse économétrique peut être utilisée à partir des données de l'entreprise, ou du marché (scanner data?). 

Exemple Effet prix et revenu
++++++++++++++++++++++++++++

Voir ce notebook pour un bel exemple qui utilise Python pour calculez la compensation et trouvez les effets prix et revenu avec fonction d'utilité CES (Constant Elasticity of Substitution)

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/PriceEffectTutorial.ipynb

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/1Y7FVxKgIbg" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>
