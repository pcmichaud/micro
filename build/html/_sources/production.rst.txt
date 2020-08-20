La production
-------------

Les dotations ne tombent pas du ciel. De plus, plusieurs biens doivent être produit à l'aide d'autres biens. L'économie est constituée ce consommateur, certe, mais aussi d'entreprise. Pourquoi les entreprises existent-elles? `Ronald Coase <https://fr.wikipedia.org/wiki/Ronald_Coase>`_ propose une explication simple: les entreprises sont des organisations qui servent à *internaliser* les coûts de transaction pour produire des biens, ou donner des services. Sans ces organisations, difficile de produire à faible coût des ordinateurs portables, des meubles. Il existe des rendements à l'échelle qui font en sorte que les entreprises peuvent produire des grandes quantités de biens à faible coûts. Elles permettent aussi l'innovation, en réunissant ensemble les cerveaux. Dans cette séance, nous abordons les décisions de l'entreprise (plutôt que le consommateur). L'entreprise produit un bien (ou plusieurs) qu'elle vend sur les marchés (offre). Elle demande des inputs pour produire ce bien. Finalement, dans un équilibre général avec production, extension naturelle de l'équilibre général d'échange, elle est détenue par certains consommateurs, qui tirent un revenu provenant de ses profits. 


La fonction de production
+++++++++++++++++++++++++

La firme a des inputs qu'elle transforme en output. La fonction de production :math:`F(\cdot)` accomplie cette transformation. La fonction de production peut être estimé à l'aide de l'économétrie, en collaboration avec les ingénieurs. 

**Exemple: un input et un output**

-  e.g. Mine de fer — input: travail :math:`L`, output: fer
   :math:`Y = F(L) = \sqrt{L}`

La fonction de production détermine les contraintes. Étant donné une quantité d'input, l'entreprise ne peut produire qu'une certaine quantité d'output. 

**Exemple: Deux inputs, one output**

-  Inputs: Minerai de fer (:math:`I`), Charbon (:math:`C`) — Output: Acier
   (:math:`S`)

On pourrait par exemple penser à une fonction: 

.. math::
    S(I,C)  = I^{\alpha}C^{\beta}

Avec des données sur la quantité d'acier produit, la quantité de minerai et de charbon utilisée dans le temps :math:`t=1,...,T` , on peut estimer les paramètres en transformant la fonction de production: 

.. math::
    \log S_t = \log A_t + \alpha \log I_t + \beta \log C_t + \epsilon_t

où :math:`A_t` est un facteur de productivité multifactorielle et :math:`\epsilon_t` est un aléa. Ainsi :math:`\alpha`et :math:`\beta` peuvent être estimés, sous certaines conditions concernant :math:`\epsilon_t` et sa relation avec :math:`(I_t,C_t)`. 

Taux marginal de substitution technique
+++++++++++++++++++++++++++++++++++++++

Il y a pénurie d'un input :math:`Z`. Le directeur de l'usine vous demande combien de :math:`X` de plus aura-t-on besoin pour palier à la baisse de :math:`Z` tout en gardant la production de :math:`Y` constante. 

Considérons la fonction de production :math:`Y = F(X,Z)`. Prennons la différentielle totale:

.. math:: dY = F'_X(X,Z)dX + F'_Z(X,Z)dZ

La productivité marginale de chacun des inputs est donné par :math:`F'_i(X,Z)` pour :math:`i=X,Z`. Elle donne la production de :math:`Y` qu'on obtient en augmentant marginalement un input et en *gardant les autres constants*. 

Fixons :math:`dY = 0`. On obtient le **taux marginal de substitution technique**:

.. math:: TMST = \frac{dZ}{dX} = -\frac{F'_X(X,Z)}{F'_Z(X,Z)}

Au lieu de courbe d'indifférence, nous avons des isoquantes dans l'espace :math:`(X,Z)` qui donne les combinaisons d'input qui produisent une quantité d'output constante. LE TMST est la pente de ces isoquantes.

Il nous donne la quantité de :math:`Z` qu'on peut économiser si on augmente :math:`X` marginalement. Il est négatif parce que la fonction de production est généralement croissante dans les deux inputs (productivité marginale positive). 

**Exercice A**: Trouvez le TMST pour :math:`Y=X^{\alpha} Z^{\beta}`

Les rendements à l'échelle
++++++++++++++++++++++++++

Le directeur de l'usine souhaite doubler la production. Il vous demande dans quelle proportion on doit augmenter les achats d'inputs. La productivité marginale ne nous est pas utile pour deux raisons: elle mesure un effet marginal (doubler est loin d'être marginal) et elle mesure l'effet marginal gardant les autres inputs constant. Or la question du directeur ne garde pas certains inputs constants. On fera appel aux rendements à l'échelle de la fonction. 

Une fonction de production a des rendements à l'échelle:

-  constant: si :math:`F(X,Z)` est homogène de degré 1

-  croissant: si :math:`F(X,Z)` est homogène d'un degré plus grand que 1

-  décroissant: si :math:`F(X,Z)` est homogène d'un degré plus petit que 1

**Exercice B**: Considérez la fonction
:math:`Y=F(X,Z)=A X^\alpha Z^\beta`. Quelles sont les rendements à l'échelle de la fonction?

Miminisation des coûts
++++++++++++++++++++++

Maintenant que nous comprenons les capacités techniques de l'entreprise, nous pourrions nous demander qu'elle serait le meilleur choix d'inputs pour un niveau d'output donné. Pensons à une entreprise qui essaie de réduire ses coûts mais ne cherche pas nécessairement à changer son niveau de production. 

Étant donné un niveau de production :math:`Y`, quel est le meilleur choix des
inputs?

.. math:: \min_{X,Z} \{ p_X X + p_Z Z : F(X,Z) \ge Y \}

Posons le lagrangien:

.. math:: L(X,Z,\mu) = p_X X + p_Z Z + \mu(Y - F(X,Z))

Les CPO sont:

.. math:: p_X - \mu F'_X(X,Z) = 0

.. math:: p_Z - \mu F'_Z(X,Z) = 0

.. math:: F(X,Z) = Y

On peut simplifier pour obtenir les deux équations:

.. math:: \frac{p_X}{p_Z} = \frac{F'_X(X,Z)}{F'_Z(X,Z)}

.. math:: F(X,Z) = Y

La première équation nous donne le *mix* des inputs qui est optimal. Il doit être tel que le :math:`TMST` est égal au prix relatifs des inputs. Le prix relatif donne ce que coûte en unité de :math:`Y` une unité de :math:`X`. Si ce coût est plus faible que l'économie que l'on fait en augmentant :math:`X`, on peut augmenter :math:`X` et réduire les coûts totaux. Au point où le :math:`TMST` est égal au prix relatifs des inputs, il n'y a plus d'économie à faire. On a minimisé les coûts. 

La deuxième contrainte vient appliquer le *mix* des inputs trouvés avec la première équation au niveau de production choisi en terme de :math:`Y`. C'est là que peuvent intervenir les rendements à l'échelle.  

La solution à ce système d'équation est une paire de demande conditionelle pour les inputs

.. math:: X^*(p_X,p_Z,Y),Z^*(p_X,p_Z,Y)

On les dit *conditionnelles* parce qu'elles dépendent d'un niveau d'output fixe. 

**Exercice C**: Trouvez les demandes conditionnelles pour 
:math:`Y=X^{1/2} Z^{1/4}`.

Quelles sont les propriétés de ces fonctions?

-  Homogène de degré zéro en :math:`(p_X,p_Z)`

-  Symmétrique:
   :math:`\frac{\partial X^*(p_X,p_Z,Y)}{\partial p_Z} = \frac{\partial Z^*(p_X,p_Z,Y)}{\partial p_X}`

-  Effets prix négatifs: :math:`\frac{\partial X^*(p_X,p_Z,Y)}{\partial p_X}<0`.


Fonction de coût
++++++++++++++++

En substituant les demandes condionnelles on peut obtenir la fonction de coûts:

.. math:: C(p_X,p_Z,Y) = p_X X^*(p_X,p_Z,Y) + p_Z Z^*(p_X,p_Z,Y)

Cette fonction nous donne pour des prix et une quantité d'output donné, le coût totale qui minimise les coûts. 

Propriétés:

-  Non-décroissante en :math:`(Y,p_X,p_Z)`

-  Homogène de degré 1 en :math:`(p_X,p_Z)`

-  Concave en :math:`(p_X,p_Z)`

Parfois des données sur les coûts, les prix ainsi que les inputs sont disponibles mais pas l'output. On peut alors estimer les paramètres de la fonction de production par la fonction de coûts. 

**Exercice D**: Trouvez la fonction de coût pour :math:`Y=X^{1/2} Z^{1/4}`.

Lemme de Sheppard
+++++++++++++++++

Un résultat intéressant est 

.. math:: \frac{\partial C(p_X,p_Z,Y)}{\partial p_X} = X^*(p_X,p_Z,Y)

Ce résultat peut être utile pour retrouver les demandes conditionnelles. 

**Exercice E**: Montrez que ceci est vrai pour trouver :math:`X^*` en utilisant la fonction de production :math:`Y=X^{1/2} Z^{1/4}`.

Coût marginal 
+++++++++++++

Le coût marginal de produire un output (en minimisant les coûts) est donné par: 

.. math:: c(p_X,p_Y,Y) = \frac{\partial C(p_X,p_Y,Y)}{\partial Y} 

On utilise la convention de :math:`c` minuscule dénote le coût marginal et C majuscule, les coûts totaux. 

En utilisant le théorème de l'enveloppe, on peut montrer que

.. math:: \frac{\partial C(p_X,p_Y,Y)}{\partial Y} = \mu

:math:`\mu` is therefore the marginal cost at the optimum.

**Exercice F**: Trouvez le coût marginal pour :math:`Y=X^{1/2} Z^{1/4}`.

Si la fonction de production a des rendements à l'échelle qui sont:

-  Constant: :math:`C(p_X,p_Z,Y)` est linéaire en :math:`Y`, :math:`c(p_X,p_Z,Y)` est constant. 

-  Croissant: :math:`C(p_X,p_Z,Y)` est concave en :math:`Y`, :math:`c(p_X,p_Z,Y)` est décroissant. 

-  Décroissant: :math:`C(p_X,p_Z,Y)` est convexe en :math:`Y`, :math:`c(p_X,p_Z,Y)` est croissant. 

Maximisation des profits
------------------------

La firme minimise ses coûts mais doit aussi choisir son niveau d'output. Donc, plus généralement, elle doit maximiser ses profits. 

Les profits sont donnés par: 

   .. math:: \Pi = R - C

où :math:`R` représente les revenus et :math:`C`, les coûts. Étant donné un input :math:`X` et output :math:`Y = F(X)`, les profits sont donnés par:

   .. math::

      C(X) = p_X X , \quad R(Y) = p_Y Y \\
      \Pi(X) = p_Y F(X) - p_XX

À l'optimum, on a 

   .. math::

      p_Y F'(X) - p_X = 0 \iff F'(X) =
      \frac{p_X}{p_Y}

**Exercise G** Supposons :math:`F(X) = \sqrt X`, trouvez le choix de
:math:`X` qui maximise les profits. 

L'offre de la firme est donné par :math:`Y^* = F(X^*)`. 

**Exercise H** Supposons que :math:`F(X) = \sqrt X`, trouvez l'offre de l'entreprise
pour :math:`Y`.

Quand deux inputs sont présent, et un output, on peut procéder de la façon suivante: 

-  Minimisation des coûts pour :math:`(X,Z)` en fonction de :math:`Y`.

-  Maximisation des profits pour :math:`Y` en utilisant la fonction de coûts (fonction de
   :math:`Y`).

**Exercice I** Pour :math:`Y=X^{1/2} Z^{1/4}`, trouvez l'offre de :math:`Y`.

Économie de production
++++++++++++++++++++++

En situation d'échange, nous avons été capable de définir l'équilibre de marché ainsi que l'optimum de Pareto. Dans une économie de production, on peut faire la même chose. Il faut rajouter une entreprise et spécifier ce qu'elle produit, et avec quels biens. Il faut aussi répartir ses profits, s'il y en a, auprès des consommateurs, actionnaires. En équilibre général, rien ne se perd ...

Considérons une situation avec deux biens: :math:`X` et :math:`Y`. L'entreprise a une fonction de production :math:`Y = F(X)`. 

**Comportement de la firme**

-  Étant donné les prix :math:`p_Y` et :math:`p_X` l'entreprise maximise ses profits. 

   .. math:: \Pi(X) = p_Y F(X) - p_X X

-  On peut trouver la demande de l'input :math:`X^{F,d}(p_X,p_Y)`, l'offre de l'entreprise :math:`Y^{F,s}(p_X,p_Y)` et les profits, s'il y en a :math:`\Pi`. 

**Comportement des consommateurs**

-  On a deux consumers C1 et C2

-  Les préférences des consommateurs sont représentées par :math:`U_1(X, Y)` et
   :math:`U_2(X,Y)`

-  Le consommateur 1 a une dotation :math:`(X^{C1,e},
   Y^{C1,e})` alors que le consommateur 2 a :math:`(X^{C2,e}, Y^{C2,e})`

-  Chaque consommateur a une participation aux profits dans l'entreprise :math:`\rho_{1}` and
   :math:`\rho_2 = 1- \rho_1`.

Ainsi, le consommateur 1 (même chose pour 2) doit résoudre
   .. math::

      \max_{X,Y} \left[U_1(X,Y): p_{X} X +  p_{Y}Y \leq p_{X}X^{C1,e}+ p_{Y}Y^{C1,e} + \rho_{1}\Pi \right]

-  Donne les demandes du consommateur 1: :math:`X^{C1,d}(p_X,p_Y)` et
   :math:`Y^{C1,d}(p_X,p_Y)` 

**L'équilibre de marché**

On peut normaliser :math:`p_{X} = 1` et donc :math:`p_{Y} = p` (voir le cours sur l'échange si pas clair). Étant donné :math:`p`, on peut trouver les demandes :math:`X` et :math:`Y` pour chaque consommateur, la demande de :math:`X` de l'entreprise et l'offre 
   :math:`Y` de l'entreprise.

Le marché pour  :math:`X` est en équilibre au prix :math:`p` si et seulement si

   .. math::

      X^{C1,d} + X^{C2,d} + X^{F,d} = X^{C1,e} + X^{C2,e}  

La loi de Walras s'applique et si :math:`p` est le prix d'équilibre pour le marché de :math:`X`, le marché de :math:`Y` est aussi en équilibre. 

Un exemple...


Supposons 

-  :math:`F(X) =  \log(1+X)`

-  :math:`U_1(X,Y) =
   U_2(X,Y) = \log X + \alpha \log Y`

-  :math:`X^{C1,e} = 2` et :math:`X^{C2,e} =
   Y^{C1,e} = Y^{C2,e} = 0`

-  :math:`\rho_1 =0` et :math:`\rho_2 = 1`

-  price :math:`p_X = 1`, :math:`p_Y = p`

Pour l'entreprise, la maximisation des profits implique

   .. math::

      \max_X p\log(1+X) - X\;\; \Rightarrow \;\; X^{F,d}
      = p- 1 \;\; et \;\; Y^{F,s} = \log p

Les profits sont donc :math:`\Pi = p \log p - p+1`

Du côté des consommateurs, étant donné un revenu, :math:`I`, les consommateurs maximisent l'utilité

.. math::

   \max_{X,Y} \left[\log X + \alpha \log Y : X + pY \leq I \right]

Les revenus sont donnés par  :math:`I_1 = 2` et :math:`I_2 = \Pi =  p \log p - p +1`. 
   
Les demandes sont 

   .. math::

      X^{C1,d} = \frac{1}{1+\alpha}I_1  
      Y^{C1,d} = \frac{\alpha}{1+\alpha} \frac{I_1}{p}
      X^{C2,d} = \frac{1}{1+\alpha} I_2 
      Y^{C2,d} = \frac{\alpha}{1+\alpha} \frac{I_2}{p}

Un équilibre de marché pour :math:`X` est donné par:

   .. math:: X^{F,d} + X^{C1,d} + X^{C2,d} = X^{C1,e} + X^{C2,e} = 2

ce qui donne: 

   .. math::

       p-1 + \frac{1}{1+\alpha}2 + \frac{1}{1+\alpha}(p\log p - p +1 ) = 2.
       
       
Donc, le prix d'équilibre est la solution à :math:`\alpha p +p\log p = 3 \alpha`. On peut trouver numériquement (:math:`p^*`). 

Si on résume la méthode pour trouver un équilibre de production (peut importe le nombre de consommateur, etc): 

-  Étant donné les prix, la maximisation des profits donne les demandes d'inputs et l'offre d'output de la firme. On retrouve donc aussi les profits à re-distribuer. 

-  Étant donné les prix, les dotations et les profits de l'entreprise, on peut calculer le revenu et les demandes de chaque consommateur.

-  Des équations d'équilibre des marchés, on trouve la solution pour les prix d'équilibre. 

Les théorèmes du bien-être s'applique, tout comme en échange. Une condition clé est que l'entreprise est prenneur de prix concernant son output et de ses inputs. Elle n'est pas stratégique. Il existe des situations, comme nous le verrons, où l'entreprise peut tirer profit de la manipulation des prix.

Exemple Python 
++++++++++++++

À venir...