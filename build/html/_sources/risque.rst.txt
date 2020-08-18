Le Risque
---------

De manière générale, les gens n'aiment pas le risque. 

.. figure:: /images/risk-scared.jpeg
   :scale: 100

Pour s'en convaincre, imaginez vous faire offrir à la retraite:

-  **Plan A**: un revenu certain de: 50 000/an

-  Un revenu incertain à la retraite (dès suite de placements)

   ====================== ======================
   **Plan B**             50% chance 10 000/an
   \                      50% chance 90 000/an
   ====================== ======================

-  Revenu espéré est de 50 000 dans les deux cas, lequel choisissez-vous?

Rendement et risque
+++++++++++++++++++

Imaginez que le placement est maintenant:

   ====================== ======================
   **Plan C**             50% chance 10 000/an
   \                      50% chance 100 000/an
   ====================== ======================

ou encore mieux, 

   ====================== ======================
   **Plan D**             50% chance 10 000/an
   \                      50% chance 150 000/an
   ====================== ======================

À un moment, vous allez probablement choisir le placement risqué parce que le rendement espéré est plus élevé. Les préférences en situation de risque sont fonctions des gains mais aussi du risque (les probabilités et les gains). La théorie du consommateur que nous avons vu ne couvre pas ce cas. 

L'approche d'espérance d'utilité (EU)
+++++++++++++++++++++++++++++++++++++

**Lotterie**

-  Lotterie :math:`\mathcal L = (p,X \;; 1-p,Y)` : avec probabilité
   :math:`p` d'obtenir :math:`X`, et probabilité :math:`1-p` d'obtenir
   :math:`Y`. L'espérance de la lotterie est :math:`\mathbb{E}_{L} = pX + (1-p)Y`. 

-  Espérance d'utilité semble naturelle

   .. math::

      \mathbb{E}_{{ \mathcal L}} (u) = p\times u(X) + (1-p) \times
      u(Y)

**Préférences sur des lotteries**

-  Le consommateur préfère la lotterie :math:`\mathcal L_1` à la lotterie :math:`\mathcal L_2` si

   .. math::

      \mathbb{E}_{{ \mathcal L_1}} (u) > \mathbb{E}_{{ \mathcal L_2}} (u)

-  La représentation des préférences par l'espérance d'utilité est appelé utilité
   `von Neumann <https://fr.wikipedia.org/wiki/John_von_Neumann>`__ et
   Morgenstern (vNM).

**Exemple**

Si :math:`u(X) = \sqrt{X}` et le consommateur fait face aux lotteries :math:`\mathcal L_1 = (0.5,0\;; 0.5,16)` et :math:`\mathcal L_2 = (1,6)`.

-  **Exercice A**: Quel est le rendement espéré de chaque lotterie?

-  **Exercice B** Si le consommateur a des préférences vNM, laquelle des lotteries choisira-t-il?

-  **Exercice C**: Est-ce que la fonction d'utilité :math:`u(X) = X` donne le même choix?


.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/0d2D_VJD9L4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

En situation de certitude, l'utilité est ordinale: seul l'ordre compte. Cependant, en situation de risque, l'utilité espérée à la vNM est cardinale, car elle dépend des probabilités qui sont ont une échelle (entre 0 et 1). Donc, les transformations monotones ne sont pas permises. Mais une transformation est permise: la transformation affine: :math:`\widehat u = a u +b` avec :math:`a>0`. On peut montrer que cette transformation n'affecte pas les préférences

   .. math::

      \begin{aligned}
      \mathbb{E}_{L_1} \widehat u \geq \mathbb{E}_{L_2} \widehat u & \iff  a\mathbb{E}_{L_1} u + b \geq a\mathbb{E}_{L_2} u + b \\ & \iff 
       \mathbb{E}_{L_1} u  \geq \mathbb{E}_{L_2} u\end{aligned}


Aversion au risque
++++++++++++++++++

L'attitude au risque varie d'un individu à l'autre: 

-  **Riscophobie (aversion au risque)**: si :math:`L = (p, X\;; 1-p,Y)`
   et on dénote :math:`Z = p X + (1-p)Y`, alors le consommateur est riscophobe si s'il préfère :math:`\mathcal L' = (1,Z)`
   à :math:`\mathcal L`.

-  **Riscophilie (propension au risque)**: Il ou elle préfère :math:`\mathcal L = (p, X\;; 1-p,Y)` à
   :math:`\mathcal L' =
   (1,Z)`

- **Risconeutre**:   Alors le consommateur est indifférent entre :math:`\mathcal L = (p, X\;; 1-p,Y)` et :math:`\mathcal L' =(1,Z)`.

**Qu'observe-t-on?**

-  Beaucoup de riscophobie

-  Un peu de riscophilie, mais ne tient souvent pas compte de la valeur de l'expérience de prendre des risques... Exemple du casino souvent donné... 

Aversion au risque et concavité de l'utilité
++++++++++++++++++++++++++++++++++++++++++++

**Riscophobie**

Le consommateur a une fonction d'utilité :math:`u`. En contexte, vNM, c'est le seul objet qu'on peut modéliser pour capter les comportements de riscophobie et de riscophilie. On peut donc se douter que les propriétés de :math:`u` auront quelque chose à voir avec ces comportements. 

Fixons deux états :math:`(X,Y)` et la probabilité :math:`p` que :math:`X` soit réalisé. Alors la richesse espérée est :math:`Z = pX + (1-p)Y`.

L'aversion au risque implique que 

   .. math::
      u(Z) > pu(X) + (1-p)u(Y). 

Une fonction :math:`u` qui respecte cette inégalité est concave (voir rappel mathématique). Dans le domaine des statistiques, on réfère à ce résultat comme étant l'inégalité de Jensen. Le cas de la riscophilie correspond à une fonction d'utilité convexe. 

**Neutralité au risque**

Si l'individu est neutre face au risque, il y a indifférence entre

   .. math:: \mathcal L = (p, X\;; 1-p,Y) \quad et \quad  \mathcal L' = (1,Z)

La fonction d'utilité doit donc être contrainte à être linéaire dans la richesse  :math:`u(X) = a X + b`, avec le cas particulier :math:`u(X) = X`.

Mesurer l'aversion au risque
++++++++++++++++++++++++++++

Comment mesurer le degré de riscophobie? Comment comparer deux individus et dire qu'un est plus riscophobe qu'un autre? Deux mesures sont bien utiles dans ce contexte, soit le coefficient d'aversion au risque absolue et le coefficient d'aversion au risque relatif. 

Coefficient absolue: 

   .. math::
      A(X) = -\frac{u''(X)}{u'(X)} 

Coefficient relatif: 

   .. math::
      R(X) = -\frac{u''(X)X}{u'(X)} 

Pourquoi ces mesures? Puisque la riscophobie est reliée à la concavité, les deux mesures augmentent quand la deuxième dérivée augmente (elle est négative pour concave, d'où le moins). Ensuite, on normalise par l'utilité marginale :math:`u'(X)`, pour fixer les unités puisque :math:`u` est ordinale.

La mesure absolue permet de regarder le niveau de riscophobie pour une lotterie en montant absolue. Le coefficient relatif permet de regarder le degré de riscophobie pour une lotterie en proportion de la richesse. 

La distinction entre les deux est utile. Par exemple, on pourrait croire intuitif que la mesure absolue décroit dans la richesse (la lotterie est faible par rapport à la richesse) tandis que le coefficient relatif devrait être relativement constant puisque la lotterie reste constante en proportion de la richesse. Donc, pour une décision d'investissement de portefeuille, où la taille du portefeuille est à peu près constante en proportion de la richesse, le coefficient relatif parait la bonne mesure. Pour un risque plus absolue, par exemple, une lotterie au casino, le coefficient absolue paraît plus utile. 


Comment mesurer ce coefficient? Une méthode très utilisée est le liste de prix multiples. `Holt et Laury (2002) <https://pubs.aeaweb.org/doi/pdfplus/10.1257/000282802762024700>`__ ont fait une application à la mesure des attitudes façes au risque, qui démontre entre autre l'importance de donner des incitatifs financiers à ceux qui participent. 

Une liste de prix multiple présente deux lotteries sous différentes configurations. Le répondant doit choisir la lotterie qu'il préfère. Une lotterie sera choisie au hasard à la fin de l'expérience et sera jouée. Le répondant se verra payer le montant. Voici exemple tiré de Holt et Laury: 


.. image:: /images/mpl.png
   :scale: 100%

On utilisera une fonction d'utilité de type, 

.. math::

   U(X) = \frac{X^{1-r}}{1-r}.

Dans ce cas, on peut montrer que :math:`R(X) = r`, d'où son nom, fonction d'utilité CRRA (*constant relative risk aversion*). 

**Exercice D**: En utilisant la fonction d'utilité CRRA, dans l'expérience MPL ici-haut, calculer l'interval dans lequel doit se trouver :math:`r` si l'individu l'option A jusqu'au 7e choix et ensuite l'option B à partir du 8e choix?

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/tEUxxgxm03Y" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>



Prime de risque
+++++++++++++++

Considérons la lotterie  :math:`\mathcal L =(p,X\;;1-p,Y)`. On dénote :math:`Z` l'espèrance de la lotterie :math:`Z = pX+ (1-p)Y`. On pourrait s'intéresser à :math:`Z'` tel que 

.. math::
   u(Z') = pu(X) + (1-p)u(Y)

:math:`Z'` est un équivalent certain pour :math:`\mathcal L` étant donné les préférences représentées par :math:`u`.

Si l'agent est riscophobe, :math:`Z' < Z` et on dénote :math:`\pi = Z-Z'` la prime de risque. Son interprétation dépend du contexte. Quand l'action concerne la prise de risque (par défaut l'individu est en situation de certitude), on l'interprète comme étant la compensation minimum demandée par l'agent pour prendre le risque. La prime de risque représente alors le montant minimal qu'il faut payer avec certitude à l'agent pour qu'il prenne le risque. En contexte d'investissement boursier, le rendement excédentaire requis par un investisseur riscophobe sera égal à cette prime de risque. Plus l'actif est risqué, plus il demandera une compensation (rendement) élevée.  

En assurance, la prime de risque sera plutôt le montant maximal que l'agent est prêt à payer pour éliminer le risque puisque la situation sans action, est risquée, alors qu'une assurance complète élimine le risque. Il s'agit donc d'une disposition à payer pour éliminer un risque. 

**Exercice E**: Un agent a les préférences représentées par :math:`u(X)=\log X`. Sa richesse initialile est :math:`X_0 = 100` et il fait façe à un risque de perdre 50 avec probabilité 0.5 et gagner 50 avec une probabilité 0.5. Quel est le montant maximal qu'il est prêt à payer pour éliminer ce risque?

Une approximation à la prime de risque existe pour un risque faible. Dénotant :math:`\sigma^2` la variance d'un risque absolue avec moyenne zéro, la prime de risque pour un agent ayant une richesse initiale de :math:`X` est bien approximée par: 

.. math::
   \tilde\pi = \frac{1}{2}\sigma^2 A(X)

On remarque que la prime augmente avec l'aversion au risque et la variance du risque. Une variante pour les risques relatifs prend une forme similaire.  

**Exercice F**: Avec :math:`u(X) = \sqrt X`, la prime de risque est-elle plus faible que dans l'exercice précédent?

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/um8t_1HnvEs" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Assurance
+++++++++

L'assurance est un marché qui existe parce que la population est riscophobe de manière générale. Il y a un marché pour l'assurance de biens (voitures, maisons, etc) mais aussi l'assurance des personnes (vie, rentes viagères, santé). Même nos gouvernements mettent en place des assurances, comme l'assurance-emploi (anciennement assurance-chômage). 

Prennons le cas du chômage. Considérons un exemple simple où deux individus peuvent être dans les états suivants:

-  Employé avec probabilité 0.5, revenu de 100 

-  Au chômage avec probabilité 0.5, revenu de 0

Dénotons les revenus réalisées des deux individus, :math:`I_i` (:math:`i=1,2`). Un programme d'assurance-emploi dicte plutôt que les deux individus reçoivent :math:`(I_1+I_2)/2` peu importe leur statut d'emploi. 

L'assurance est bénéfique *ex ante* pour deux agents riscophobes (avant la réalisation du risque): 

- Sans assurance: utilité espérée de chacun des agents est :math:`.5 [u(0) + u(100)]`

-  Avec insurance, 25 % les deux ont 0, 50% que 1 seul travaille, 25% les deux travaillent. Donc l'espérance d'utilité de chacun des agents est :math:`.25[u(0) + 2u(50) + u(100)]`

L'assurance est bénéfique si

   .. math::

      .25[u(0) + 2u(50) + u(100)] > .5 [u(0) + u(100)]

ou si :math:`u(50) > .5[u(0)+u(100)]`. Donc, vrai si :math:`u` concave ou agent riscophobe (encore l'inégalité de Jensen). 

En pratique, l'assurance-emploi pourrait être informelle entre les gens. Mais le problème est qu'après la réalisation du risque, l'individu qui a toujours un emploi ne veut plus partager. Une façon de voir un régime d'assurance, ou bien un assureur, est qu'il permet de sauver sur ces coûts de transaction (agence) entre les assurés.  

L'autre avantage est que l'assureur pourra mutualiser davantage d'agents au sein du régime. 

**La loi des grands nombre**

-  Considérons une variable aléatoire :math:`Z` égale à :math:`X` avec probabilité :math:`p` et :math:`Y` avec probabilité :math:`1-p`

-  Si :math:`Z_1,
   \cdots , Z_n` sont indépendantes avec la même distribution
   :math:`(p,X \;; 1-p,Y)` alors

   .. math::

      si\; N \to +\infty,\quad  \frac{1}{N} (Z_1 + Z_2 + \cdots + Z_n)
      \to pX + (1-p)Y

-  La réalisation moyenne, qui demeure aléatoire avec :math:`N` petit, devient certaine quand `N` tend vers l'infini. 

**Mutualisation**

-  Quand un grand nombre partage le risque, il élimine le risque par l'effet de mutualisation. Les assurées reçoivent exactement le revenu moyen. 

-  Si les agents sont riscophobes, ce résultat est désirable. 


Assurance et entrepreneuriat
++++++++++++++++++++++++++++

**Devenir entrepreneur**

-  Un individu a une richesse de 9 et peut décider de la garder ou bien de l'utiliser pour démarrer une entreprise. Sa richesse finale, s'il démarre une entreprise est donnée par la lotterie suivant:    :math:`\mathcal L = (.5,0 \;; .5,25)`. Ses préférences sont vMN avec :math:`u(X) = \sqrt{X}`. 

-  **Exercice G**: Est-ce qu'il démarre l'entreprise?

**L'ange investisseur**

-  Plutôt que d'investir seul, l'entrepreneur peut obtenir un financement d'un ange investisseur qui lui donne la moitié du capital pour la moitié du rendement.

-  L'entrepreneur garde donc 4.5 avec certitude s'il démarre l'entreprise. Mais il doit donner la moitié des rendements. 

-  La lotterie est maintenant :math:`\mathcal L' = (.5,4.5 \;; .5,17)`

-  **Exercice H**: Quel sera son choix?

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/_cXjJyzut54" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

L'émission, *Les Dragons* de Radio-Canada est une application directe de cet exemple. La participation est toujours conditionnelle à une part des profits. La négociation porte donc sur la part des profits en rapport à la part de l'investissement initial. En voici un exemple ou les deux entrepreneurs ont négocié fort... 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/ICyUEUUgq8Q" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

En plus des différentes entreprises privées qui font ce genre d'investissements, des organisations comme Investissement Québec, les Fonds de travailleur (FTQ et Fondaction), Anges Québec, sont tous des mécanismes d'assurance qui peuvent promouvoir l'entrepreneuriat en partageant le risque. 

Critique de l'espérance d'utilité
+++++++++++++++++++++++++++++++++


-  Paradoxe d'Allais

-  Paradoxe de Ellsberg

-  Kahneman et Tversky: L'effet des perspectives

Expérience de choix I

On tire un nombre entier entre 0 et 99 avec probabilité 1/100 pour chaque nombre entier:

=========== == ==== =====
Lotteries   0  1-10 11-99
:math:`L_1` 50 50   50
:math:`L_2` 0  250  50
=========== == ==== =====

Expérience de choix II

Maintenant, on considère une autre paire avec les mêmes règles de tirages. 

=========== == ==== =====
Lotteries   0  1-10 11-99
:math:`L_3` 50 50   0
:math:`L_4` 0  250  0
=========== == ==== =====

Maurice Allais et son Paradoxe

**Exercice I**: Montrez que :math:`L_1 \succ L_2` et
:math:`L_4 \succ L_3` sont des choix incohérents si les préférences sont représentées par l'espérance de l'utilité.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/nM_R-796R0E" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


.. figure:: /images/allais.png


Voir cet article pour toute l'histoire derrière le Paradoxe... `Munier (1991) <https://pubs.aeaweb.org/doi/pdf/10.1257/jep.5.2.179>`_

Expérience de choix III

Une urne contient 90 billes. 30 sont rouges. Les autres 60 sont soit noires ou blanches. La proportion de billes blanches ou noires n'est pas connue. On vous demande de faire un choix entre les deux configurations de paiements suivants (lotteries): 

=========== ===== ===== =======
Lotteries   rouge noire blanche
:math:`L_1` 50    0     0
:math:`L_2` 0     50    0
=========== ===== ===== =======

Choice

Le même contexte pour ces deux lotteries. 

=========== ===== ===== =======
Lotteries   rouge noire blanche
:math:`L_3` 50    0     50
:math:`L_4` 0     50    50
=========== ===== ===== =======


Le Paradoxe d'Ellsberg

**Exercice J** Montrez que la combinaison de choix :math:`L_1 \succ L_2` et
:math:`L_4 \succ L_3` ne peut survenir si l'agent a des préférences représentées par l'espérance d'utilité.

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/U0rcjieEqg0" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>
   
M. Ellsberg est bien connue pour ce Paradoxe, mais encore davantage pour ses mésaventures avec le gouvernement américain... `Pentagon Papers <https://fr.wikipedia.org/wiki/Daniel_Ellsberg>`__

Kahneman and Tversky: Les perspectives

Ces auteurs, tous deux récipiendaires d'un Prix Nobel, montrent que nous sommes influencés par les perspectives (framing) quand nous faisons des choix en situation risquée: 

Imaginons qu'une nouveau virus pourrait tuer 600 personnes. Deux interventions sont présentées.

-  (Perspective positive): A) 200 sauvées, B) 1/3 probabilité que 600 sont sauvés,
   2/3 que personne n'est sauvé

-  (Perspective négative): C) 400 vont mourrir, D) 1/3 probabilité que personne décède, 2/3 probabilité que tous décèdent. 

En pratique, A est plus populaire que B, mais D est plus populaire que C. Or, en terme de personnes en vie, les deux choix mènent aux mêmes résultats. 

Si les perspectives vous intéressent, allez lire ce chef d'oeuvre: `Khaneman et Tversky
(1979) <https://www.uzh.ch/cmsssl/suz/dam/jcr:00000000-64a0-5b1c-0000-00003b7ec704/10.05-kahneman-tversky-79.pdf>`__

Exemple Python risque
+++++++++++++++++++++

|ImageLink|_

.. |ImageLink| image:: https://colab.research.google.com/assets/colab-badge.svg
.. _ImageLink: https://colab.research.google.com/github/pcmichaud/micro/blob/master/notebooks/AversionRisqueExemple.ipynb

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/OE9ymCfWH4E" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>
