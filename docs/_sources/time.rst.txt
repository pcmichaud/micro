Le Temps
--------

Préférences
+++++++++++

Les individus préfèrent généralement un bénéfice le plus tôt possible et un coût le plus tard possible:

-  Un café maintenant ou dans une heure?

-  Aller au Gym aujourd'hui ou demain?

-  Épargner aujourd'hui pour dépenser demain?

L'évidence empirique indique que l'origine de ces préférences peut-être tracé à l'enfance... 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Yo4WF3cSd9Q" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Utilité escomptée
+++++++++++++++++

Dans son livre *The Theory of Interest* en 1930, `Irving Fisher <https://fr.wikipedia.org/wiki/Irving_Fisher>`_ présente une théorie assez simple, mais qui servira de modèle pour des centaines de travaux en micro et macroéconomie. Les préférences y sont représentées par l'utilité escomptée. 

Si :math:`u(C_t)` est l'utilité de consommer à la période :math:`t`, l'utilité escomptée pour un plan de consommation :math:`\textbf{C} = (C_1,...,C_T)` est :

.. math:: DU(\mathbf{C}) = \sum_{t=1}^T \delta^{t-1} u(C_t)

:math:`\delta` :math:`\in [0,1]` est le facteur d'escompte (patience)
alors que :math:`\mathbf{C} = (C_1,...,C_T)`. La relation entre le facteur d'escompte et le taux d'escompte :math:`\rho` est donné par:

.. math:: \delta = \frac{1}{1+\rho}

Taux marginal de substitution (TMS)
+++++++++++++++++++++++++++++++++++

Si :math:`T=2`, alors

.. math:: DU(C_1,C_2) = u(C_1) +  \delta u(C_2)

La différentielle totale donne le TMS:

.. math:: \frac{\partial C_2}{\partial C_1}\rvert_{dDU=0} = -\frac{u'(C_1)}{\delta u'(C_2)}

Les préférences intertemporelles sont charactérisées par:

-  Le facteur d'escompte (:math:`\delta`)

-  La forme de :math:`u`.

**Exercice A**: Trouvez le TMS pour :math:`u(C_t) = \ln C_t`

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/owx0w0dqjF4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


Comment estimer le taux d'escompte? On peut utiliser les listes de prix multiples. 

Une expérience au Danemark réalisée auprès de fonctionnaires Danois essaie d'estimer le facteur d'escompte au niveau individuel `(Harrison, Lau and Williams, 2002) <https://www.aeaweb.org/articles?id=10.1257/000282802762024674>`_

|image_mpl|

Les résultats montrent une grande dispersion et des taux d'escompte élevés, beaucoup plus que les taux d'intérêts. 

|image_discount|

La contrainte intertemporelle
+++++++++++++++++++++++++++++

**Marché financiers et intérêt**

Institution financière offre :math:`r_S` pour chaque dollar déposé
(épargne). Elle nous demande :math:`r_D` pour chaque dollar prêté

Supposons pour le moment :math:`r_D = r_S = r`.

**Ressources**

Les ressources proviennent de:

-  Richesse initiale: :math:`W_0`.

-  Revenu dans les deux périodes, :math:`Y_1`, :math:`Y_2`.

La valeur présente des ressources est :

.. math:: VP_W = W_0 + Y_1 + \frac{Y_2}{1+r}

**Constrainte**

La valeur présente de la consommation est:

.. math:: VP_C = C_1 + \frac{C_2}{1+r}

.

Ainsi, la contrainte intertemporelle est :math:`VP_C \leq VP_W`:

.. math:: C_1 + \frac{C_2}{1+r} \leq W_0 + Y_1 + \frac{Y_2}{1+r}

**Emprunt et épargne**

On peut écrire la contrainte comme étant :

.. math:: (1+r)(W_0 + Y_1 - C_1) \ge  C_2 - Y_2

Ainsi,

-  L'individu qui épargne en première période, peut consommer plus que son revenu en 2e période. 
-  L'individu qui emprunte en première période, doit consommer moins que son revenu en 2e période. 

Visualement, on a

|image_budget|

*Exemple*: Un régime de retraite à prestation déterminé force l'individu à épargner dans la première période et donne un revenu additionel dans la deuxième.

-  Revenu en 2e période est :math:`Y_2 = \phi Y_1` avec un taux de remplacement
   :math:`\phi \in [0,1]`.

-  Le revenu de première période est amputé d'une contribution
   :math:`\tau Y_1`.

La contrainte budgétaire est donc:

.. math:: C_1 + \frac{C_2}{1+r} \leq W_0 + (1-\tau)Y_1 + \frac{\phi Y_1}{1+r}

Le taux de contribution est choisi par l'actuaire :math:`\tau` tel que:

.. math:: \tau Y_1 = \frac{\phi Y_1}{1+r_P} \to \tau = \frac{\phi}{1+r_P}

où :math:`r_P` est le taux de rendement implicite du régime de retraite. Si :math:`r_P = r`,
la contrainte budgétaire ne change pas! Le plan de consommation ne change pas et donc l'épargne privée est réduite d'un même montant que la contribution (Effet d'éviction). 

**Écarts de taux emprunts vs. épargne**

**Exercice B**: À qui ressemble la contrainte si :math:`r_S<r_D`?

**Exercice C**: Comment représenter une situation où l'agent ne peut emprunter?

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/sub6hdZWQiE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


Choix optimal
+++++++++++++

**Maximisation**

Le problème est (fixons :math:`W_0=0` pour simplifier): 

.. math:: \max_{C_1,C_2} \{ u(C_1) + \delta u(C_2) : C_1+C_2/(1+r) \leq Y_1 + Y_2/(1+r)\}

Deux approches:

#. Approche directe (substitution de la contrainte)

#. Lagrangien

**Conditions d'optimalité**

Le Lagrangien a 3 CPO:

.. math::

   \begin{aligned}
    u'(C_1) - \lambda = 0  \\
   \delta u'(C_2) - \lambda /(1+r) = 0  \\
   C_1+C_2/(1+r) - Y_1 - Y_2/(1+r) = 0  \end{aligned}

Avec (1) et (2) on obtient :

.. math:: \frac{u'(C_1)}{\delta u'(C_2)} = 1+r

On peut réarranger et en fixant :math:`R=1+r`, on obtient l'équation de **Euler**:

.. math:: u'(C_1) = R\delta u'(C_2)

Visualement

 |image_optimal|

Cette théorie serviva de fondation pour la théorie du cycle de vie (*the Life-Cycle Hypothesis*), proposée par `Franco Modigliani <https://en.wikipedia.org/wiki/Franco_Modigliani>`_, qui permettra de comprendre les choix en fonction de l'âge d'un agent. L'équation de Euler dérivée ici-haut suggère qu'un individu aime lisser sa consommation sur le cycle de vie, et par conséquent, s'il fait fasse à des revenus élevées durant son jeune âge et faible plus tard, épargne quand il est jeune et consomme cette épargne quand il est plus vieux. Ceci servira de fondation pour l'étude de l'épargne, de l'assurance-vie, de l'immobilier et d'un tas d'autres décisions financières. 

**Exercice D**: Trouvez le choix optimal de :math:`C_1` et
:math:`C_2` si :math:`u(C)=\frac{C^{1-\sigma}}{1-\sigma}` et avec une contrainte budgétaire classique. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/L5GuC9FIfGA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


*Exemple*: Épargne-t-on assez pour la retraite?

Une question très présente dans le débat public. 

.. figure:: /images/retraite.png
   :alt: Le Conseiller, Globe and Mail, L’Actualité

   Le Conseiller, Globe and Mail, L’Actualité

On peut simuler des taux de remplacement effectif mais difficile de dire ce qui est assez ou non...

.. figure:: /images/mckinsey.png
   :alt: McKinsey (2015)

   McKinsey (2015)

Pour des calculs plus récents, voir ce `rapport <https://ire.hec.ca/en/wp-content/uploads/sites/3/2020/06/cpr-report-2020-final.pdf>`_ de l'Institut Retraite et Épargne. 


**Épargne optimale** 

Qu'est-ce que la théorie nous dit sur l'épargne optimale?

**Exercice E**: Trouvez une expression pour le niveau optimal d'épargne en début de 2e période si :math:`u(C)=\frac{C^{1-\sigma}}{1-\sigma}` et la contrainte est donnée par:

.. math:: C_1 + \frac{C_2}{1+r} \leq (1-\tau)Y_1 + \frac{\phi Y_1}{1+r}

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/s-as6pPdrTE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>

Des calculs plus sophistiqués donneront peuvent être fait pour comparer l'épargne accumulée à la retraite à l'épargne optimale selon un modèle: 

.. figure:: /images/savings.png
   :alt: Scholz et al. (2007, Journal of Political Economy)

   `Scholz et al. (2007, Journal of Political Economy) <https://www.journals.uchicago.edu/doi/10.1086/506335>`_

Les conclusions sont parfois surprenantes comparativement à ce qu'on observe dans les médias. 

Biais pour le présent
+++++++++++++++++++++

Les gens peuvent être très impatients. Mais leur préférence peut tout de même respecter les principes de l'utilité escomptée. Cependant, il existe plusieurs violations de l'utilité escomptée. Nous nous concentrons ici sur le biais pour le présent. 

*Exemple*: Choisir un film

Vous devez choisir un film à regarder aujourd'hui et un la semaine prochaine:


Supposons que `Mommy <https://www.youtube.com/watch?v=d7rtSqI0ZeA>`_  a un bénéfice immédiat de 4 et un bénéfice futur de 4 mais que `Les Boys <https://www.youtube.com/watch?v=OFl0fuIRl9A>`_ a un bénéfice immédiat de 7 (aucun bénéfice futur).

**Exercice F**: Quel est l'utilité escomptée is vous choisissez aujourd'hui et :math:`\delta=1`. Que se passe-t-il si vous choisissez plutôt pour la semaine prochaine?

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/mykC_IdabOE" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


L'évidence empirique montre que les gens préfèrent les Boys si le choix se fait aujourd'hui mais Mommy si le choix est fait pour la semaine prochaine. L'utilité escomptée ne permet pas d'expliquer que le choix dépend de l'horizon. Cet exemple est un parmi d'autres d'incohérence intertemporelle.  

**Biais pour le présent**

Laibson (1997, QJE) propose une modification assez simple aux préférences escomptées, soit l'introduction d'une fonction d'escompte quasi-hyperboliques:

.. math:: QH(\mathbf{c}) = u(C_1) + \beta \sum_{t=2}^T \delta^{t-1} u(C_t)

Le paramètre :math:`\beta` agit comme paramètre de biais pour le présent (facteur d'escompte à court terme) alors que :math:`\delta` contrôle l'impatience à long-terme. Ces préférences dépendent maintenant de l'horizon...

**Exercice G**: Quel est le TMS entre les consommations :math:`C_1` et
:math:`C_2`? Et :math:`C_2` vs. :math:`C_3`? Comparer avec l'espérance d'ut

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/WLyiWOGTd2A" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


En utilisant l'exemple des deux films, supposons maintenant :math:`\beta=0.5`.

**Exercice H**: Quel film choisissez-vous pour aujourd'hui et pour la semaine présente si vous avez des préférences quasi-hyperboliques? Et si le choix se fait la semaine prochaine?

Solution, voir vidéo Exercice F. 

Les préférence quasi-hyperboliques capturent bien ce pattern de choix. 

*Exemple*: Qui s'abonne au Gym?

Une passe d'une visite coûte 10$. Le coût par visite des gens qui s'abonne est beaucoup plus élevé que 10$. Pourquoi les gens achètent-ils un abonnement? Sont-ils naifs par rapport au fait qu'ils ont des préférences quasi-hyperboliques?

.. figure:: /images/Gym.png
   :alt: Della Vigna et Malmendier (2006)

   `Della Vigna et Malmendier (2006) <https://www.aeaweb.org/articles?id=10.1257/aer.96.3.694>`_

Il y a évidence que certains sous-estiment leur degré de biais pour le présent. Ils sont naif par rapport à leur problème de contrôle. 

Exemple: Comment aider les gens à épargner?

-  Épargner est similaire à aller au Gym: coûteux dans le court-terme, bénéfique à long-terme.

-  Pour aider les gens avec ces biais, on pourrait décider de changer l'option de défaut: opt-in vs. opt-out. Au lieu de devoir décider d'épargner (défaut = n'épargne pas), on peut par défaut forcer les gens à épargner et ils peuvent arrêter s'ils le veulent (défaut = épargne)...

-  Shea et Madrian (2001, QJE) montre que l'épargne, à court-terme pour les entreprises qui changent le défault, augmente. 

.. figure:: /images/shea.png
   :alt: Shea et Madrian (2001, QJE)

   `Shea et Madrian (2001, QJE) <https://academic.oup.com/qje/article-abstract/116/4/1149/1903159?redirectedFrom=fulltext>`_

Moins évident à long-terme...


**Engagement**

Les gens au prise avec un problème de la sorte, pourrait vouloir, rationellement, qu'on limite leur choix. Par exemple, en ne leur permettant pas de succomber à la temptation à court-terme *dans leur propre intérêt*. David Laibson de Harvard, et plusieurs autres, étudient des mécanismes de la sorte, appliquées à la santé et l'épargne par exemple. 

.. raw:: html

    <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/a7Y6_2JLTrA" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 50%; height: 50%;"></iframe>
    </div>


.. |image_mpl| image:: /images/mpl.png
.. |image_discount| image:: /images/Results.png
.. |image_budget| image:: /images/budget.png
.. |image_optimal| image:: /images/optimal.png