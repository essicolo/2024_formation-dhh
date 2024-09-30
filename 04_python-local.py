import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Commandes utiles :

        ```
        cd <VOTRE_DOSSIER>
        uv python pin cpython@3.12
        uv init .
        uv venv
        .venv\Scripts\activate
        uv add pandas marimo
        marimo edit
        uv deactivate
        ```
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Installer et gérer Python localement

        Jusqu'à présent, nous avons utilisé Pyodide, une version de Python qui est interprétée par le navigateur (Firefox, Chrome, etc.). C'est simple et fonctionnel... jusqu'à ce que vous aviez à utiliser un module contenant des références à d'autres langages, que ce soit C++, Rust, FORTRAN, qui ne sont pas supportés par l'environnement Pyodide. Dans ce cas, vous allez devoir installer Python localement.

        Il existe de nombreuses approches: installation via le Portail d'Entreprise, distribution Anaconda et ses nombreuses dérivées, utilisation de Pyenv, puis installation des modules avec pip, poetry, conda, mamba, etc. **L'approche que je recommande est d'utiliser [`uv`](https://docs.astral.sh/uv/)**. Quoi que son utilisation passe par un terminal, elle est néanmoins conviviale. Son installation ne demande pas de droit d'administration: 

        1. Ouvrir l'invite de commande `cmd` (`⊞ Win` + tapez 'cmd').
        2. Coller `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

        Pour coller dans un Terminal sur Windows, c'est simplement un clic droit.

        Suivez les instructions pour que `uv` soit reconnue comme commande dans le `cmd` (en collant `set Path=C:\Users\<VOTRE_ID>\.cargo\bin;%Path%`).

        À ce stade, vous avez installé `uv`, mais pas Python. `uv` servira d'abord à gérer les différentes versions de Python sur votre ordinateur. Commençons par installer Python 3.12 (la dernière version au moment d'écrire ces lignes). Tapez `uv python install 3.12`.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Les environnements

        Je vous suggère de gérer autant d'environnement de calcul que vous avez de projet. Pour initier un projet, créez d'abord un dossier local, puis naviguez vers ce dossier dans le `cmd`. Truc: pour reculer d'un dossier dans la hiérarchie, tapez `cd ..`.

        Une fois que vous y êtes, spécifiez la version de Python que vous désirez utiliser:

        ```uv python pin cpython@3.12```

        Optionnellement, créez un environnement type avec (le point est inclus dans la commande et signifie *ici*)

        ```uv init .```
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        Le fichier le plus important est `pyproject.toml`. Il contient l'information nécessaire pour reproduire votre environnement. Mais n'y touchons pas pour l'instant avec la commande 

        ```uv venv```

        L'installateur d'environnement vous dira comment activer cet environnement: en l'occurrence,

        ```.venv\Scripts\activate```

        Le nom de votre environnement devrait apparaître entre parenthèse dans le `cmd`.

        Pour installer un ou plusieurs modules à votre environnement, tapez

        ```uv add marimo pandas seekwellpandas altair```

        Non seulement les modules seront installés, mais si vous ouvrez `pyproject.toml`, vous devriez les voir ajoutés sous la rubrique des dépendances. Pour retirer un module, par exemple `seekwellpandas`,

        ```uv remove seekwellpandas```

        Pour sortir de votre environnement,

        ```uv deactivate```

        Enfin, pour le supprimer, vous pouvez supprimer le dossier `.venv`.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Marimo

        Après avoir installé Marimo (`uv add marimo`), vous pouvez lancer l'interface en tapant

        ```
        marimo edit
        ```

        Si la commande n'est pas reconnue, c'est peut-être parce que l'environnement Python n'est pas activé.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Visual Studio Code

        Distribué par Microsoft en mode *open source*, Visual Studio Code (VScode) peut être utilisé au lieu de Marimo. La méthode classique de travailler en Python est d'écrire un script avec n'importe quel éditeur texte, et le lancer dans un terminal, par exemple `python mon_script.py`. Mais il existe plusieurs manières d'écrire en Python en passant par VScode. Je ne couvrirai que l'approche en mode *pourcentage* et celle en mode *Jupyter* (bien que le module [Quarto](https://quarto.org/) soit aussi très intéressant). Dans tous les cas, installez l'extension **Python** dans VScode (ouvrir le gestionnaire d'extensions dans le menu vertical, cherchez Python). Pour les deux modes, assurez-vous d'ajouter `ipykernel` dans votre environnement :

        ```
        uv add ipykernel
        ```
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Mode pourcentage

        Ce mode n'a pas de nom formel, mais on l'appelle parfois ainsi. Lorsqu'un fichier est enregistré avec l'extension `.py`, un bouton Run Cell apparaît lorsque vous tapez `# %%`. Il s'agit d'un diviseur de cellules. Pour inclure des cellules de texte *Markdown*,

        ```
        # %% [markdown]
        \"""
        # Titre 1

        Votre texte...
        \"""
        ```

        On vous demandera de sélectionner un *kernel* (noyau). L'utilisation des noyaux est une couche supplémentaire de gestion utilisée pour lier un environnement de calcul et une interface de calcul. Heureusement, VScode nous permet de nous en passer. Sélectionnez *Python Environment*, puis sélectionnez l'environnement que vous avez créer avec `uv`. S'il n'apparaît pas, le bouton ↻ en haut à droite du menu de sélection d'environnement devrait le faire apparaître. S'il n'y est toujours pas, redémarrer VScode devrait aider.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### Mode Jupyter

        Les fichiers Jupyter se terminent par l'extension `.ipynb`, hérité de l'ancien nom *IPython notebook*. Si vous créez un fichier avec cette extension, un environnement Jupyter sera généré de facto par VScode. Vous pourrez y intercaler des cellules de calcul en Python (sélectionner la cellule, puis appuyez sur `y`) et des cellules en *Markdown* (idem, appuyez sur `m`). Pour ajouter des cellules au-dessus, `a`, et en dessous, `b`. Pour exécuter une cellule, c'est comme avec *Marimo*, `Ctrl + ↵` ou `Maj + ↵` pour exécuter sans passer à la suivante.
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
