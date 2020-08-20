Concurrence imparfaite
----------------------

Des situations de concurrence parfaite, où il y a beaucoup d'entreprises et aucune n'a de pouvoir de marché, il y en a peu... La grande majorité des marchés ont quelques grands joueurs dominants. Parfois, ceux-ci ont un pouvoir de marché, parfois non. L'analyse de la concurrence imparfaite est subtile et dépend des conditions de production et de stratégies prises par les entreprises pour limiter la concurrence.

La concurrence imparfaite peut mener à un résultat sous-optimal (par rapport à la concurrence parfaite). Dans certaines situations, le régulateur voudra légiférer pour augmenter la compétition, si des barrières artificielles existent. 

.. figure:: /images/antitrust.jpeg
   :scale: 100

Concurrence parfaite
++++++++++++++++++++

Le cas de l'équilibre général en production suppose que les entreprises considère le prix fixe. Ceci mènera à une situation d'équilibre de marché où le premier théorème du bien-être s'applique. Il s'agit d'un optimum de Pareto. 

Cette hypothèse de prix fixe fonctionne bien quand il y a un grand nombre de firmes, chacune étant petite. Ainsi, la firme ne peut affecter le prix du marché avec ses choix de production. 

Considérons l'exemple d'une économie pour un bien :math:`X` et un *numéraire* :math:`M` (dont le prix est normalisé à 1). L'utilité est quasi-linéaire :math:`U(X,M) = V(X) + M`, avec :math:`V(X)` concave, :math:`V'(0) = + \infty`. Les dotations sont :math:`I_0` de :math:`M`, le bien :math:`X` produit par une firme vendu au prix :math:`p`. La firme produit :math:`X` sous une fonction de coût :math:`C(X)`. Supposons :math:`C'(0) = 0`.

**Exercice A** Trouvez le prix d'équilibre si l'entreprise est *prenneur de prix*
et :math:`V(X) = \sqrt{X}`, :math:`C(X) = X^2`.

Le surplus du producteur est donné par: 

.. math:: 
    SP(X) = \int_0^X (P - C'(i))di. 

Manipulation stratégique du prix
++++++++++++++++++++++++++++++++

Une firme qui peut par son choix de production affecter le prix d'équilibre et faire un profit additionelle a un pouvoir de marché. Elle peut réduire sa production, au delà de la quantité qui serait Pareto optimale en concurrence parfaite. Ceci mènera à un prix qui est au dessus du coût marginal et ainsi augmenter ses profits. 

Pour comprendre la nature de cette stratégie, observons que l'entreprise choisie  :math:`X` afin de maximiser

    .. math:: \Pi = p(X)X - C(X)

La CPO est 

   .. math:: \frac{d\Pi}{dX} = 0 \iff p'(X)X + p(X) = C'(X)

Ceci mène à un choix :math:`X_{PM}` such tel que 

.. math::
    p(X_{PM}) + p'(X_{PM}) X_{PM} = C'(X_{PM})

Le premier terme à droite est l'effet *marginal* d'une augmentation de la quantité. L'unité supplémentaire rapporte :math:`p(X_{PM})`. Cet effet est aussi présent quand la firme est *prenneur de prix*, la quantité est choisie tel que le prix (revenu marginal) est égale au coût marginal de produire cette unité. 

Un deuxième terme est présent à gauche. Il s'agit de l'effet *infra-marginal*. Quand la firme augmente sa quantité d'une unité, le prix baisse (pas de bien Giffen svp...). Ainsi, le revenu qu'elle fait sur les :math:`X_{PM}`unités déjà produite baisse. Cet effet est négatif (puisque :math:`p'(\cdot)` est négatif. Ainsi, le revenu marginal est plus faible qu'en l'absence de manipulation stratégique. L'entreprise diminuera donc sa production jusqu'à rétablir cette égalité. 

**Exercice B** Trouvez le prix d'équilibre si l'entreprise fait de la manipulation stratégique du prix et
:math:`V(X) = \sqrt{X}`, :math:`C(X) = X^2`. Comparer graphiquement par rapport à la situation où la firme est *preneur de prix*.

**Exercice C** : Dans l'exercice B, trouvez l'expression du prix d'équilibre en fonction de l'élasticité prix de la demande. Analyser la relation. 

Monopole
++++++++

Le monopole existe quand une seule firme est présente sur un marché. Si la demande n'est pas complètemenet élastique, elle va se prêter à la manipulation stratégique du prix d'équilibre. 

Puisque qu'au niveau de production optimal :math:`X_{PM}` on a 

   .. math:: p(X_{PM}) + p'(X_{PM})X_{PM} = C'(X_{PM})

et donc si :math:`p'(X_{PM})<0`, alors :math:`p(X_{PM}) > C'(X_{PM})`.

Le monopole fixe la production à un prix plus élevé que le coût marginal. Si la production of a firm has no impact on the price, elle produit :math:`X_{PT}` à :math:`p(X_{PT}) = C'(X_{PT})`. Donc, :math:`X_{PM} < X_{PT}`.

.. figure:: /images/monopoly.jpeg
   :scale: 150

Pour faire de l'analyse de bien-être concernant le monopole, il faut d'abord se demander pourquoi le monopole existe. Le monopole peut être artificiel parce que l'entreprise a crée des *barrières à l'entrée* sur le marché. Si ces barrières ne sont pas justifiées, par exemple, un cablo-distributeur qui empêche un autre d'utiliser les mêmes poteaux pour accéder aux clients, elles mèneront à une perte de bien-être pour le consommateur. La réglementation peut créer, de manière indirecte, une barrière à l'entrée. Pensons à la SAQ au Québec. Ces monopoles *articifiels* mènent généralement à une perte de bien-être. 

D'autres situations sont plus compliquées. Par exemple, des coûts fixes important, et donc des économies d'échelle importante peuvent justifier un monopole, qui dit alors *naturel*. Un exemple souvent donné est celui d'Hydro-Québec. Avant la nationalisation de l'électricité, plusieurs petits producteurs existaient, avec des coûts de production élevés et donc des prix plus élevés. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/1zLxUzcKiEA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Question pour discussion en classe, est-ce que la SAQ est un monopole naturel ou devrait-il être démantelée?

Voir ce rapport bien remplie de `PWC <http://www.finances.gouv.qc.ca/documents/Autres/fr/AUTFR_RapportSAQ2018.pdf0>`_ pour le Ministère des Finances du Québec. Voir aussi cette entrevue avec le PDQ de la SAQ: 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/jLaJ99mg0XE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Pas facile de trancher...

Dans le cas d'un monopole artificiel, Le monopole fait des profits. Ces profits sont donnés par:

   .. math:: \Pi_{PM} = (p(X_{PM}) - p(X_{PT})) X_{PM}

Ces profits reduisent le surplus du consommateur sur les unités produites par le monopole. Mais cette *rente* ne consistue pas une perte de bien-être. Ce sont les unités qui ne sont pas produites qui mènent à une perte de bien-être. Le monopole mène à une perte de bien-être parce que :math:`X_{PT}>X_{PM}` et :math:`V'(X)-C'(X)>0` sur ces unités.

**Exercice D**: Montrez les profits et la rente du monopoleur dans le graphique fait à l'exercice B. 


Duopole
+++++++

On utilise le terme *duopole* pour dénoter un marché avec deux firmes et *oligopole* pour un marché avec un faible nombre de firmes. Dans cette section, nous nous concentrerons sur une situation à deux firmes et discuteront du cas avec plusieurs firmes.

Pour modéliser comment les deux firmes d'un *duopole* se comporte, on doit déterminer si celles-ci se font la compétition sur les quantités ou sur les prix. La distinction a des implications importantes. Dans une situation où la capacité est un enjeu, c'est-à-dire qu'une seule des firmes ne peut innonder le marché, ou des investissements sont importants pour bâtir un inventaire, on parlera de compétition sur les quantités, où à la `Cournot <https://fr.wikipedia.org/wiki/Antoine-Augustin_Cournot>`_. Quand la production se fait rapidement, sans coûts fixes important, et que chacune des firmes est capable de fournir le marché, on parle plutôt de compétition sur les prix, où à la `Bertrand <https://fr.wikipedia.org/wiki/Joseph_Bertrand>`_.  

Cournot
~~~~~~~

La compétition à la Cournot se fait sur les quantités. Un exemple souvent donné est celui des avions commerciaux, où Boeing et Airbus se font concurrence. Produire un avion est coûteux et aucun des deux transporteurs peut ajuster rapidement sa production. La décision de production (et la vente) devient donc un enjeu stratégique. 

.. figure:: /images/cournot.jpeg
   :scale: 100

   Source: The Wall Street Journal. 

On peut regarder, sans perte de généralité le cas de deux entreprises identiques produisant les quantités :math:`X_A` et :math:`X_B`.

Les consommateurs ont des préférences représentées par :math:`U(X,M) =V(X) + M` et plus spécifiquement, 

   .. math:: V(X) = D_0 X - \frac{\alpha}{2} X^2

Les coûts des deux entreprises sont représentés par :math:`C_A(X) = C_B(X)= c X`. On a déjà vu que dans le cas de préférence quasi-linéaire, la demande inverse est représentée par :math:`P(X) = V'(X) = D_0 - \alpha X`. 

Avant d'analyser l'équilibre en duopole, on peut d'abord s'intérroger sur le *benchmark*, ce à quoi on va comparer la situation de duopole. Un choix naturel est la production efficiente au sens de Pareto, ce qui est obtenu si les deux entreprises sont *preneur de prix*. 

Alors l'entreprise produit :math:`X` tel que son coût marginal est égale à la disposition à payer marginale des consommateurs:

   .. math::
      c = D_0 - \alpha X

et donc 
   .. math::

      X_{Pareto} = \frac{D_0 - c}{\alpha}

Regardons aussi ce que fait un monopole. Il maximise 

   .. math:: \Pi(X) =  P(X) X - c X = (D_0- \alpha X) X - c X

et donc produit

   .. math:: X_{Mon} = \frac{D_0 - c}{2\alpha} = \frac{1}{2} X_{Pareto}

On retrouve bien qu'il produit moins que la situation de concurrence parfaite (*preneur de prix*). Maintenant, tournons-nous vers une situation de duopole à la Cournot. Les deux entreprises voudront manipuler le prix, mais voilà, il y a une pièce manquante car elles ont une interaction stratégique. Puisque le revenu marginal de l'entreprise A est :math:`D_0 -   \alpha(X_B + X_A) - \alpha X_A`, il dépend du choix de production de la firme B, et vice-versa. Donc, la décision de A affecte la décision de B. Si elles veulent agir stratégiquement, chaque entreprise doit prévoir ce que fera l'autre entreprise. Pour en arriver à un équilibre, il faudra donc introduire de nouveaux concepts provenant de la théorie des jeux, en particulier l'équilibre de `Nash <https://fr.wikipedia.org/wiki/John_Forbes_Nash>`_. 

Plaçons-nous du point de vue de la firme B. Elle doit anticiper ce que fera la firme A étant donné son choix. Elle peut faire l'hypothèse que la firme A maximisera ses profits étant donné son choix :math:`X_B`. Donc, quel est le choix optimal de production de la firme A étant donné le choix de la firme B. Elle a les profits, 

   .. math:: \Pi_A = P \times X_A - C(X_A) = [D_0 - \alpha(X_B + X_A)]X_A - C(X_A)

La CPO de la maximisation des profits est

   .. math:: D_0 -   \alpha(X_B + X_A) - \alpha X_A - c  = 0

Donc le choix optimal :math:`X_A` étant donné :math:`X_B` est la meilleure réponse (best response),

   .. math:: X_A = \frac{D_0 -  c - \alpha X_B}{ 2 \alpha} = \frac{D_0 - c}{2\alpha} - \frac{1}{2}X_B

Ces fonctions de réponses sont symmétriques, puisque les firmes sont identiques. Donc, 

   .. math:: X_B = \frac{D_0 -  c - \alpha X_A}{ 2 \alpha} = \frac{D_0 - c}{2\alpha} - \frac{1}{2}X_A

Dans un équilibre de Nash :math:`(X^*_A,X^*_B)`, :math:`X^*_A` est la meilleure réponse à :math:`X^*_B` et vice-versa. Aucun a intérêt à dévier de cet équilibre, et donc ce sont les choix de production des deux firmes. Une condition nécessaire est que les fonctions de coûts des deux firmes soient connues de part et d'autre. 

Dans notre exemple, on a   

   .. math:: X^*_A =  \frac{D_0 - c - \alpha X_B^*}{ 2 \alpha} \quad et \quad  X^*_B = \frac{D_0 - c -  \alpha X_A^*}{2 \alpha}

Puisque symmétriques, :math:`X^*_A = X^*_B = X^*` donne

   .. math:: X^*_A = X^*_B = X^* = \frac{D_0 - c}{3\alpha}

La production totale est

   .. math:: 2 X^* = \frac{2}{3} \frac{D_0 - c}{\alpha}

C'est plus qu'en monopole mais moins qu'en concurrence parfaite. 

Quelques exercices: 

| **Exercice E**: Faire un graphique des fonctions de meilleures réponses dans l'espace 
  (:math:`X_A,X_B`) et indiquer l'équilibre de Nash. 

| **Exercice F**: En débutant à :math:`X_A = \frac{D_0 - c}{2\alpha}`,
  :math:`D_0=10,c=1,\alpha=1`, montrez comment appliquer de manière séquentielle les fonctions de meilleures réponses amènent inévitablement à l'équilire de Nash. 
| **Exercice G**: Supposons que la firme A a un coût marginal :math:`c_A` et la firme 
  B, :math:`c_B`, avec :math:`c_A=2>c_B=1`. Aussi supposons
  :math:`D_0=10,\alpha=1`. Trouvez les productions d'équilibre des deux firmes.

Que se passe-t-il quand on augmente le nombre de firme? 

Supposons N firmes identiques :math:`F_1,F_2,\cdots,F_N`. Étant donné :math:`X_2, X_3, \cdots, X_N`, la firme :math:`F_1` produit  :math:`X_1` qui maximise

   .. math:: \Pi_1 = [D_0 - \alpha(X_1 + X_2 + \cdots + X_N)]X_1 - c\times X_1

La meilleure réponse est 

   .. math:: X_1 = \frac{D_0 - c - \alpha[X_2 + X_3 + \cdots + X_N]}{ 2 \alpha}

**Exercice H**: Dérivez la fonction de meilleure réponse dans cet exemple.


Dans un équilibre de Nash avec plusieurs firmes, 

:math:`X_1` optimal étant donné :math:`X_2, X_3, \cdots, X_N`, et similairement pour chaque firme. En utilisant la symmétrie, 

   .. math:: X_1^* = X_2^* = \cdots = X_N^* = \frac{D_0 - c}{(N+1) \alpha}

La production totale est

   .. math:: \frac{N}{N+1} \frac{D_0 -c}{\alpha}

On peut retrouver les quantités du monopole et du duopole par cette formule. On peut aussi voir que pour N grand, on obtient la quantité en concurrence parfaite. 

En terme de prix, on obtient, 

   .. math:: p_N = \frac{1}{N}D_0 +\frac{N}{N+1}c

Ainsi, le prix est égale à :math:`c` quand N devient grand est est le plus élevé quand on est en monopole. 

En concurrence (N très grand), les firmes deviennent en terme effectif des *preneurs de prix*, ce qui élimine les rentes de pouvoir de marché. 

Bertrand 
~~~~~~~~

La situation de compétition par les prix est assez différente en terme d'implication mais utilise les mêmes concepts que la compétition à la Cournot. Prenons :math:`N` firmes identiques avec coût marginal :math:`c_i=c \quad \forall i=1,...,N`.

Supposons, :math:`p_i = c \quad \forall i`. Si une firme :math:`j` essaie de dévier et annonce un prix :math:`p_j>c`, elle ne vendra plus rien. Si elle annonce, :math:`p_j<c`, elle fera une perte. 

L'équilibre de Nash est donc :math:`p_i=c \quad \forall i`. Donc, même avec deux firmes seulement, on a le résultat de concurrence parfaite. 

L'hypothèse importante est que le consommateur peut observer les prix des compétiteurs sans aucun coût. Les biens sont aussi homogènes. 

Pour discussion en classe, est-ce que le cas de Bell vs. ses compétiteurs pour ce qui est de la cablo-diffusion est un bon exemple de barrière à l'entrée dans un contexte de compétition par les prix?

.. figure:: /images/duopoly.jpeg
   :scale: 100

Voir cette lettre de `Robert Gagné <https://www.lapresse.ca/debats/opinions/2020-07-11/bell-un-frein-a-la-prosperite-du-quebec.php>`_ et la réponse de `Bell <https://www.lapresse.ca/debats/opinions/2020-07-16/bell-contribue-a-accelerer-la-prosperite-du-quebec.php>`_ et de Videotron par le biais de `Pierre-Karl Péladeau <https://www.ledroit.com/opinions/lobstruction-systematique-de-bell-et-autres-pratiques-anticoncurrentielles-417568f9e28fc42e9805555ad9c34087>`_. 


Exemple Python 
++++++++++++++

À venir...