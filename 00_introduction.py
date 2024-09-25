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
        # Introduction

        Excel est utile pour consigner de petits ensembles de données, effectuer des analyses de base et générer des graphiques simples. Mais avec Excel, la probabilité de commettre des erreurs grandit rapidement avec la complexité des calculs. Les procédures de vérification demandent souvent que les calculs soient audités par des tiers pour s'assurer de leur exactitude. Or, Excel a aussi le défaut d'être difficile à auditer.

        Tout cela peut être heureusement corrigé par des langages de programmation, dont l'utilisation s'est démocratisée avec les outils de calcul en ligne, qui ont néanmoins le désavantage d'une offre gratuite restreinte, et nécessite le déplacement de données parfois conventionnées vers des serveurs privés, ne serait-ce que dans la mémoire vive. Nous favoriserons ici le langage Python et les outils de calcul locaux.

        Ce document est un carnet de calcul (notebook) qui comprend des cellules de texte et des cellules de code. Les cellules de texte sont écrites en format Markdown, une manière [*très* simple](https://www.markdownguide.org/cheat-sheet/) d'écrire avec une mise en forme de base. Pour la partie code, c'est un peu comme dans Excel, sauf que des noms de variable remplacent les noms des cellules.
        """
    )
    return


@app.cell
def __():
    _a = 2
    _b = 4
    _a + _b
    return


@app.cell
def __(mo):
    mo.md(r"""En Python, on peut créer des listes de nombres, de caractères, de n'importe quoi, en utilisant des crochets.""")
    return


@app.cell
def __():
    a = [1, 2, 3]
    a
    return (a,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""Les messages d'erreur sont inévitables, même pour les pros. Ce qui fait la différence entre novices et experts, c'est que les experts savent rapidement comment régler un problème, et ça inclut la capacité à comprendre les messages d'erreur et à corriger la situation. Disons que vous voulez ajouter 1 à chaque élément de la liste.""")
    return


@app.cell
def __(a):
    a + 1
    return


@app.cell
def __(mo):
    mo.md(r"""La variable `a` étant une liste, Python s'attend à ce qu'on ajoute une liste à une liste.""")
    return


@app.cell
def __(a):
    a + [1]
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""Le bogue le plus insidieux est celui qui ne génère pas d'erreur, mais effectue la mauvaise opération. Rappelez-vous que Python est un langage de programmation générique: il ne sait pas que vous voulez effectuer une opération mathématique. Pour ajouter de nouvelles capacités à Python, nous devons importer des modules (aussi appelés librairies ou blbliothèques, et packages en anglais). Pour les calculs sur des matrices et les opérations de mathématiques, nous avons besoin du module *Numpy*, que nous importons avec l'alias de notre choix: par convention, nous prenons `np`, puis nous spécifions que a est un vecteur, sur lequel nous effectuerons notre opération sans problème.""")
    return


@app.cell
def __(a):
    import numpy as np
    np.array(a) + 1
    return (np,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Il existe de nombreux modules en Python, certains très spécialisés, d'autres plus génériques. Certains viennent par défaut avec la distribution Python que vous utiliserez, d'autres devront être installés. Voici une liste de modules que nous utiliserons.

        - *Pandas*. Vous trouverez ce module pour gérer des tableaux dans beaucoup de tutoriels. *Polars* est un outil de gestion de tableaux plus moderne que *Pandas*, mais l'extension *GeoPandas* reposant sur *Pandas*, nous utiliserons *Pandas* malgré ses bizarreries.
        - *Lets-plot*. Il existe de nombreux modules pour générer des graphiques, comme *Matplotlib*, *Plotly*, *Altair*, etc. *Lets-plot* est rapide et polyvalent.
        - *Scipy*. Une collection d'outils pour le calcul scientifique, complémentaire à *Numpy*. Nous ne l'utiliserons pas tellement de manière directe, mais vous le verrez dans bien des tutoriels. *Scipy* contient entre autres des fonctions d'optimisation bien plus performantes que le Solveur de Excel.
        - *Statsmodels*. Pour tout ce qui est statistiques fréquentielles (avec p-values). Je préfère les statistiques bayésiennes avec *PyMC*, mais c'est plus compliqué.
        - *Scikit-Learn*. Un trousse d'outils pour l'apprentissage machine que nous utiliserons. Elle est regardée de haut par les experts, mais reste utile pour créer des modèles professionnels. Néanmoins, les experts utilisent davantage les modules *Keras*, *Tensorflow* et *Pytorch*.

        L'introduction ne fait qu'effleurer la programmation. Truc de pro, ayez toujours tout proche un onglet avec un moteur de recherche ou un assistant IA pour y rechercher vos messages d'erreur.
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
