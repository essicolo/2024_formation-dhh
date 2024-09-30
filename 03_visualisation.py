import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import seekwellpandas
    import altair as alt
    return alt, mo, pd, seekwellpandas


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Visualisation

        Créer des graphiques est une tâche essentielle dans un flux de travail en science des données. Un graphique bien conçu est dense en information. La visualisation des données permet d'explorer des tableaux jusqu'à créer des éléments visuels voués à la publication, dont l'information serait autrement difficile, voire impossible à transmettre.

        ## Pourquoi explorer graphiquement ?

        La plupart des graphiques que vous générerez ne seront pas destinés à être publiés. Ils viseront probablement d'abord à explorer des données. Cela vous permettra de mettre en évidence de nouvelles perspectives.

        Prenons par exemple deux variables, `x` et `y`. Vous calculez leur moyenne et leur écart-type.
        """
    )
    return


@app.cell
def __(pd):
    datasaurus = pd.read_csv('data/datasaurus.csv')
    (
        datasaurus
        .group_by('dataset')
        .agg(['mean', 'std'])
    )
    return (datasaurus,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Les moyennes et écarts-type sont semblables pour tous les jeux de données. Si l'on effectuait des tests statistiques, ils ne seraient pas significatifs. On pourrait alors conclure que ces données proviennent de distributions statistiques identiques à un niveau de confiance très sévère. Pour démontrer que ces statistiques ne vous apprendront pas grand-chose sur la structure des données, [Matejka et Fitzmaurice (2017)](https://www.autodeskresearch.com/publications/samestats) ont généré ces 12 jeux de données, ayant chacun pratiquement les mêmes statistiques... mais avec des structures bien différentes :

        <img src=https://www.research.autodesk.com/app/uploads/2023/03/DinoSequential-1.gif width=600>
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Choisir le type de graphique le plus approprié

        De nombreuses manières de présenter les données sont couramment utilisées, comme les nuages de point, les lignes, les histogrammes, les diagrammes en barre et en pointe de tarte. Il existe de même de nombreux guides pour sélectionner le type de graphique approprié selon la situation. Je vous conseille le guide [*From data to viz*](https://www.data-to-viz.com/). En ce qui a trait aux couleurs, le choix n'est pas anodin, ne serait-ce que de sélectionner des couleurs robustes aux handicaps visuels : préférez donc les couleurs de [*Color brewer 2*](colorbrewer2.org).

        ## Les graphiques avec *Vega-altair*

        Le module [*Vega-altair*](altair-viz.github.io), ou `altair`, est une adaptation pour Python du module graphique *vegalite*, populaire en langage Javascript. Il fonctionne sur un mode déclaratif, c'est-à-dire que les attributs graphiques sont liés aux colonnes d'un tableau `pandas`.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Suivant la grammaire graphique de *Vega-altair*, on pourra créer un graphique de points comprenant les attributs suivants après avoir importé le module comme `import altair as alt`.

        1. `alt.Chart()`, le fichier de données.
        2. `.mark_point()`, la géométrie que l'on veut faire apparaître.
        3. `.encode()`, les champs des données que l'on veut associer à des attributs du graphique.
        """
    )
    return


@app.cell
def __(alt, datasaurus):
    (
        alt.Chart(data = datasaurus)
        .mark_point()
        .encode(
            x = 'x',
            y = 'y',
            color = 'dataset'
        )
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""Il existe plusieurs marqueurs et plusieurs types d'encodage présentés dans [le guide d'utilisation de *Vega-altair*](https://altair-viz.github.io/user_guide/data.html). Le *facet* est un attribut d'encodage très pratique qui permet de segmenter le graphique en plusieurs panneaux.""")
    return


@app.cell
def __(alt, datasaurus):
    (
        alt.Chart(data = datasaurus)
        .mark_point()
        .encode(
            x = 'x',
            y = 'y',
            color = 'dataset',
            facet=alt.Facet('dataset', columns=5)
        )
        .properties(width=100, height=100)
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        J'ai introduit quelques notions dans le graphique précédent. Désirant contrôler les panneaux (`facet`) de manière personnalisée, j'ai appelé `alt.Facet()` pour définir l'attribut `facet`. On peut faire de même pour par exemple ajuster les échelles en appelant `alt.X()` ou `alt.Y()`.

        Il reste difficile de couvrir dans un chapitre les cas figures auxquels vous serez confrontés: les [exemples sur le site de *Vega-altair*](https://altair-viz.github.io/gallery/index.html) restent assez complets. Je couvrirai seulement quelques cas de figure pour des données géoréférencées vectorielles - pour les données raster, nous utiliserons plus dans un autre chapitre le module *Matplotlib*.
        """
    )
    return


@app.cell
def __(alt):
    # set MARIMO_OUTPUT_MAX_BYTES=15_000_000
    url_geojson = 'https://www.donneesquebec.ca/recherche/dataset/b4893e20-3a65-44fe-a428-68c79e303fb4/resource/fcdd3e3b-b6dc-45ae-9e88-542b842b1774/download/vdq-hydrobassinversant.geojson'
    data_geojson_remote = alt.Data(url=url_geojson, format=alt.DataFormat(property='features',type='json'))

    (
        alt.Chart(data_geojson_remote, width=500, height=300)
        .mark_geoshape()
        .encode(color='properties.NOM:N')
        .project(type='identity')
        .interactive()
    )
    return data_geojson_remote, url_geojson


@app.cell
def __():
    return


@app.cell
def __():
    return


@app.cell
def __(data_geojson_remote):
    data_geojson_remote
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
