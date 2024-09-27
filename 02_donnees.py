import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Les données

        Une donnée est une valeur associée à une variable. Une variable peut être une dimension, une date, une couleur, le résultat d'un test statistique, à laquelle on attribue la valeur quantitative ou qualitative d'un chiffre, d'une chaîne de caractère, d'un symbole conventionné, etc.

        Ce chapitre traite de l'importation, l'utilisation et l'exportation de données structurées, en Python, sous forme de vecteurs, matrices, tableaux et ensemble de tableaux (bases de données).

        Bien qu'il soit toujours préférable d'organiser les structures qui accueilleront les données d'une expérience avant-même de procéder à la collecte de données, l'analyste doit s'attendre à réorganiser ses données en cours de route. Or, des données bien organisées au départ faciliteront aussi leur réorganisation.

        Ce chapitre débute avec quelques définitions : les données et leurs types, les vecteurs, les matrices, les tableaux et les bases de données, ainsi que leur signification en Python. Puis, nous verrons comment organiser un tableau selon quelques règles simples, mais importantes pour éviter les erreurs et les opérations fastidieuses pour reconstruire un tableau mal conçu. Ensuite, nous traiterons des formats de tableau courant, pour enfin passer à l'utilisation de pandas, une bibliothèque Python utile pour effectuer des opérations sur les tableaux.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Types de données

        Dans la section précédente, nous avons survolé différents types d'objets : réels, entiers, chaînes de caractères et booléens. Les données peuvent appartenir à d'autres types : dates, catégories ordinales (ordonnées : faible, moyen, élevé) et nominales (non-ordonnées : espèces, cultivars, couleurs, etc.).

        ## Matrices

        Dans la section d'introduction à Python, nous avons vu comment Python permet d'organiser des collections d'objets. Bien qu'il soit important de connaître leur existence pour apprendre à maîtriser Python, les listes et les dictionnaires sont peu pratiques pour le calcul. Nous avons vu en introduction que Python ne permet pas d'effectuer les opérations entre les scalaires et les listes, et offre peu de fonctions mathématiques. Grâce à la *vectorisation*, les matrices *Numpy* peuvent être soumises efficacement à des opérations mathématiques. Mais contrairement à une liste, une matrice ne peut contenir que des valeurs même type. Par convention, les fonctions de *Numpy* sont importés avec l'alias `np`. On peut créer une matrice grâce à des listes imbriquées.
        """
    )
    return


@app.cell
def __():
    import numpy as np
    ma_matrice= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ma_matrice
    return ma_matrice, np


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Les matrices n'ont pas de lignes ou de colonnes, mais plutôt un ordre de dimensions, ou d'*axe* dans le jargon *Numpy*. Une matrice 2D peut indiquer l'élévation d'un point dans l'espace x, y. En 3D, vous pouvez inclure non seulement l'élévation, mais aussi la pluviométrie journalière. Ajouter une évolution dans le temps et vous obtenez une matrice 4D.

        Dans notre cas, l'axe 0 représente les lignes et l'axe 1, les colonnes. Pour appeler les valeurs de la matrice, nous utilisons les crochets `[]`, qui incluent les indices des axes. Notez comment est utilisé le symbole `:`.
        """
    )
    return


@app.cell
def __(ma_matrice):
    ma_matrice[0, 2]
    return


@app.cell
def __(ma_matrice):
    ma_matrice[:, 0]
    return


@app.cell
def __(ma_matrice):
    ma_matrice[:2, 1:]
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Tableaux

        De manière générale, un tableau de données est une organisation de données en deux dimensions, comportant des *lignes* et des *colonnes*. Il est préférable de respecter la convention selon laquelle les lignes sont des observations et les colonnes sont des variables. Ainsi, un tableau est une collection de vecteurs de même longueur, chaque vecteur représentant une variable. Chaque variable est libre de prendre le type de données approprié. La position d'une donnée dans le vecteur correspond à une observation.

        ## Base de données

        Imaginez que vous consignez des données de différents sites (A, B et C), et que chaque site possède ses propres caractéristiques. Il est redondant de décrire le site pour chaque observation. Vous préférerez créer deux tableaux: un pour décrire vos observations, et un autre pour décrire les sites. De cette manière, vous créez une collection de tableaux interreliés: une *base de données*.

        Dans Python, les données structurées en tableaux, ainsi que les opérations sur les tableaux, peuvent être gérés grâce au module *Pandas*, comme nous le ferons au cours de cette formation, ou *Polars*, qui offre une interface plus moderne et plus rapide, mais dont la capacité à gérer des objets spatiaux n'est qu'à ses débuts. Mais avant de se lancer dans l'utilisation de ces outils, voyons quelques règles à suivre pour bien structurer ses données.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Organiser un tableau de données

        Afin de repérer chaque cellule d'un tableau, on attribue à chaque ligne et à chaque colonne colonnes un identifiant *unique*, que l'on nomme *indice* pour les lignes et *entête* pour les colonnes.

        ***Règle no 1.** Une variable par colonne, une observation par ligne.* 

        Les unités expérimentales sont décrites par une ou plusieurs variables par des chiffres ou des lettres. Chaque variable devrait être présente en une seule colonne, et chaque ligne devrait correspondre à une unité expérimentale où ces variables ont été mesurées. La règle parait simple, mais elle est rarement respectée. Prenez par exemple le tableau suivant.

        | Site | Traitement A | Traitement B | Traitement C |
        | --- | --- | --- | --- |
        | Sainte-Patente | 4.1 | 8.2 | 6.8 |
        | Sainte-Affaire | 5.8 | 5.9 | NA |
        | Saint-Gréement | 2.9 | 3.4 | 4.6 |

        *Tableau 1. Rendements obtenus sur les sites expérimentaux selon les traitements.*
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Qu'est-ce qui cloche avec ce tableau ? Chaque ligne est une observation, mais contient plusieurs observations d'une même variable, le rendement, qui devient étalé sur plusieurs colonnes. *À bien y penser*, le type de traitement est une variable et le rendement en est une autre :

        | Site | Traitement | Rendement |
        | --- | --- | --- |
        | Sainte-Patente | A | 4.1 |
        | Sainte-Patente | B | 8.2 |
        | Sainte-Patente | C | 6.8 |
        | Sainte-Affaire | A | 5.8 |
        | Sainte-Affaire | B | 5.9 |
        | Sainte-Affaire | C | NA |
        | Saint-Gréement | A | 2.9 |
        | Saint-Gréement | B | 3.4 |
        | Saint-Gréement | C | 4.6 |

        *Tableau 2. Rendements obtenus sur les sites expérimentaux selon les traitements.*

        Plus précisément, l'expression *à bien y penser* suggère une réflexion sur la signification des données. Certaines variables peuvent parfois être intégrées dans une même colonne, parfois pas. Par exemple, les concentrations en cuivre, zinc et plomb dans un sol contaminé peuvent être placés dans la même colonne "Concentration" ou déclinées en plusieurs colonnes Cu, Zn et Pb. La première version trouvera son utilité pour des créer des graphiques (chapitre 5), alors que la deuxième favorise le traitement statistique.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ***Règle no 2.** Ne pas répéter les informations.*

        Reprenons la même expérience. Supposons que vous mesurez la précipitation à l'échelle du site.

        | Site | Traitement | Rendement | Précipitations |
        | --- | --- | --- | --- |
        | Sainte-Patente | A | 4.1 | 813 |
        | Sainte-Patente | B | 8.2 | 813 |
        | Sainte-Patente | C | 6.8 | 813 |
        | Sainte-Affaire | A | 5.8 | 642 |
        | Sainte-Affaire | B | 5.9 | 642 |
        | Sainte-Affaire | C | NA | 642 |
        | Saint-Gréement | A | 2.9 | 1028 |
        | Saint-Gréement | B | 3.4 | 1028 |
        | Saint-Gréement | C | 4.6 | 1028 |

        *Tableau 3. Rendements obtenus sur les sites expérimentaux selon les traitements.*
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Segmenter l'information en deux tableaux serait préférable.

        | Site | Précipitations |
        | --- | --- |
        | Sainte-Patente | 813 |
        | Sainte-Affaire | 642 |
        | Saint-Gréement | 1028 |

        *Tableau 4. Précipitations sur les sites expérimentaux.*

        Les tableaux 2 et 4, ensemble, forment une base de données (collection organisée de tableaux).
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ***Règle no 3.** Ne pas bousiller les données.*

        Par exemple.

        - *Ajouter des commentaires dans des cellules*. Si une cellule mérite d'être commentée, il est préférable de placer les commentaires soit dans un fichier décrivant le tableau de données, soit dans une colonne de commentaire juxtaposée à la colonne de la variable à commenter. Par exemple, si vous n'avez pas mesuré le pH pour une observation, n'écrivez pas "échantillon contaminé" dans la cellule, mais annoter dans un fichier d'explication que l'échantillon no X a été contaminé. Il peut aussi être pratique de les inscrire dans une colonne `commentaire_pH`.
        - *Inscriptions non systématiques*. Il arrive souvent que des catégories d'une variable ou que des valeurs manquantes soient annotées différemment. Il arrive même que le séparateur décimal soit non systématique, parfois noté par un point, parfois par une virgule. Par exemple, une fois importés dans votre session, les catégories `St-Ours` et `Saint-Ours` seront traitées comme deux catégories distinctes. De même, les cellules correspondant à des valeurs manquantes ne devraient pas être inscrites parfois avec une cellule vide, parfois avec un point, parfois avec un tiret ou avec la mention `NA`. Le plus simple est de laisser systématiquement ces cellules vides.
        - *Inclure des notes dans un tableau*. La règle "une colonne, une variable" n'est pas respectée si on ajoute des notes un peu n'importe où sous ou à côté du tableau.
        - *Ajouter des sommaires*. Si vous ajoutez une ligne sous un tableau comprenant la moyenne de chaque colonne, qu'est-ce qui arrivera lorsque vous importerez votre tableau dans votre session de travail ? La ligne sera considérée comme une observation supplémentaire.
        - *Inclure une hiérarchie dans les entêtes*. Afin de consigner des données de texture du sol, comprenant la proportion de sable, de limon et d'argile, vous organisez votre entête en plusieurs lignes. Une ligne pour la catégorie de donnée, *Texture*, fusionnée sur trois colonnes, puis trois colonnes intitulées *Sable*, *Limon* et *Argile*. Votre tableau est joli, mais il ne pourra pas être importé conformément dans un votre session de calcul : on recherche *un entête unique par colonne*. Votre tableau de données devrait plutôt porter les entêtes *Texture sable*, *Texture limon* et *Texture argile*. Un conseil : réserver le travail esthétique à la toute fin d'un flux de travail.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Formats de tableau

        Plusieurs outils sont à votre disposition pour créer des tableaux. Je vous présente ici les plus communs.

        ### *.xls* ou *.xlsx*
        Microsoft Excel est un logiciel de type *tableur*, ou chiffrier électronique. L'ancien format *xls* a été remplacé par le format *xlsx* avec l'arrivée de Microsoft Office 2010. Il s'agit d'un format propriétaire, dont l'alternative libre la plus connue est le format *ods*, popularisé par la suite bureautique LibreOffice. Les formats *xls*, *xlsx* ou *ods* sont davantage utilisés comme outils de calcul que d'entreposage de données. Ils contiennent des formules, des graphiques, du formatage de cellule, etc. **Je ne les recommande pas pour stocker des données**.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### *.csv* et *.json*
        Le format *csv*, pour *comma separated values*, est un fichier texte, que vous pouvez ouvrir avec n'importe quel éditeur de texte brut (Bloc note, [Visual studio code](https://code.visualstudio.com/), etc.). Chaque colonne doit être délimitée par un caractère cohérent (conventionnellement une virgule, mais en français un point-virgule ou une tabulation pour éviter la confusion avec le séparateur décimal) et chaque ligne du tableau est un retour de ligne. Il est possible d'ouvrir et d'éditer les fichiers csv dans un éditeur texte, mais il est parfois plus pratique de les ouvrir avec des tableurs (LibreOffice Calc, Microsoft Excel, Google Sheets, etc.).

        Comme le format *csv*, le format *json* indique un fichier en texte clair. Il est utilisé davantage pour le partage de données des applications web. En analyse et modélisation, ce format est surtout utilisé pour les données géoréférencées sous la forme *geojson*. L'encodage est géré de la même manière qu'un fichier *csv*.

        **Encodage**. Puisque les formats *csv* et *json* sont des fichiers texte, un souci particulier doit être porté sur la manière dont le texte est encodé. Les caractères accentués pourraient être importés incorrectement si vous importez votre tableau en spécifiant le mauvais encodage. Pour les fichiers en langues occidentales, l'encodage UTF-8 devrait être utilisé. Toutefois, par défaut, Excel utilise un encodage de Microsoft. Si le *csv* a été généré par Excel, il est préférable de l'ouvrir avec votre éditeur texte, de l'enregistrer dans l'encodage UTF-8, puis de s'assurer que le délimiteur décimal est un point et que le délimiteur de colonne est une virgule.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Autres formats

        D'autres formats existent comme [Parquet](parquet.apache.org) pour le stockage de données massives et géoréférencées, ou bien [Arrow](arrow.apache.org) pour le partage de données entre applications. L'extension .db est utilisée avec [SQLite](sqlite.org), un format de base de données utilisé surtout pour entreposer des données génériques, en format ligne. L'extension .db est aussi utilisée avec [DuckDB](duckdb.org), un format pour les bases de données stockées en format de colonnes.

        ### Entreposer ses données

        La manière la plus sécure pour entreposer ses données est de les confiner dans une base de données sécurisée sur un serveur sécurisé dans un environnement sécurisé. C'est aussi la manière la moins accessible. Des espaces de stockage nuagiques, comme Onedrive ou [autre](https://alternativeto.net/software/microsoft-onedrive/), peuvent être pratiques pour les backups et le partage des données avec une équipe de travail (qui risque en retour de bousiller vos données). Le suivi de version est possible chez certains fournisseurs d'espace de stockage. Mais pour un suivi de version plus rigoureux, les espaces de développement (comme GitHub) sont plus appropriés. Dans tous les cas, il est important de garder (1) des copies anciennes pour y revenir en cas d'erreurs et (2) un petit fichier décrivant les changements effectués sur les données.

        ### Suggestion

        En *csv* pour les petits tableaux, en *parquet* pour les plus gros ou contenant des données spatiales, en *db* avec [DuckDB](https://duckdb.org/) pour les bases de données plus complexes, puis migrer vers [PostGIS](https://postgis.net/) si vous devez gérer des droits d'utilisation. Ce cours se concentre toutefois sur les données de type *csv*, *geojson* et *parquet*.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Jouer avec les données avec *Pandas*

        Pour démarrer, j'ai créé un dossier `data`, et j'y ai déposé le jeu de données *Palmer penguins*, [arrangé par Allison Horst](https://allisonhorst.github.io/palmerpenguins/) à partir de recherches sur le dimorphisme sexuel chez les manchots ([Gorman et al., 2014](https://doi.org/10.1371/journal.pone.0090081)).

        <center>
            <img src="https://github.com/allisonhorst/palmerpenguins/raw/main/man/figures/lter_penguins.png" width=20%>
            <img src="https://github.com/allisonhorst/palmerpenguins/raw/main/man/figures/culmen_depth.png" width=20%>
            <p><a href="https://github.com/allisonhorst/palmerpenguins">Images par Allison Horst</a></p>
        </center>
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Le module *Pandas* est d'une aide précieuse pour l'analyse de données en Python. Il permet d'importer des données dans votre session de travail, de les explorer, de les transformer et de les exporter. Les tableaux de classe `pandas` peuvent faire le pont vers d'autres modules que nous utiliserons plus loin.

        Importos le module *Pandas* avec son alias conventionnellement adopté (`pd`) et importez vos données dans une session Python. Dans le *csv*, les valeurs manquantes sont inscrites comme `NA`.
        """
    )
    return


@app.cell
def __():
    import pandas as pd
    import seekwellpandas
    penguins = pd.read_csv("data/penguins.csv", na_values='NA')
    penguins
    return pd, penguins, seekwellpandas


@app.cell
def __(mo):
    mo.md(
        r"""
        Conformément aux règles de construction d'un tableau, *Pandas* demande à ce que chaque colonne possède un entête unique, et qu'une colonne ne contienne qu'un type de données.

        ### Sélectionner et filtrer des données

        On utilise le terme *sélectionner* lorsque l'on désire choisir une ou plusieurs lignes et colonnes d'un tableau (la plupart du temps des colonnes). L'action de *filtrer* signifie de sélectionner des axes (la plupart du temps des lignes) selon certains critères.

        #### Sélectionner

        Il y a plusieurs manières de sélectionner une colonne. La plus rapide consiste à fournir une liste entre crochets directement après avoir appelé le tableau.
        """
    )
    return


@app.cell
def __(penguins):
    penguins[["bill_depth_mm", "bill_length_mm"]]
    return


@app.cell
def __(mo):
    mo.md(r"""Une sélection négative, par exclusion, peut être effectuée avec la méthode `.drop()`.""")
    return


@app.cell
def __(penguins):
    (
        penguins
        .pop(['bill_depth_mm', 'bill_length_mm'])
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
