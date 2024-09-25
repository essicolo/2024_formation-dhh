# Initiation à Python pour le calcul spatio-temporel

## Description

Ce dépôt contient les supports de cours pour l'initiation à Python pour le calcul spatio-temporel.

## Démarrage

Pour démarrer le cours, vous devez d'abord installer votre machine. Je suppose que vous travaillez sur Windows. La manière la plus conviviale de démarrer en Python est, à mon expérience, `uv`. Vous n'avez pas besoin des privilèges d'administration pour installer `uv`. Ouvrez un terminal (⊞ Win + R, puis tapez `cmd` et appuyez sur Entrée) et tapez la commande suivante,

```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

puis suivez les directives.

`uv` est un outil complet pour gérer Python sur votre machine.

- Avant de créer un environnement virtuel, vous devez d'abord installer Python. Pour ce faire, tapez `uv python install 3.12`, ce qui installera sur votre machine la version de Python de votre choix, ici 3.12.
- Naviguer dans cmd vers le dossier dans lequel vous désirez travailler, par exemple `cd C:\Users\<votre-id>\documents locaux\formation-dhh`. Signifiez à `uv` que ce répertoire travaillera avec Python 3.12 en tapant `uv python pin cpython@3.12`. Ceci épinglera la version de Python 3.12 à ce répertoire.
- Initialisez votre environnement virtuel en tapant `uv init`. Cela créera les fichiers de démarrage pour travailler avec Python dans ce répertoire.
- Créez un environnement virtuel en tapant `uv venv`, puis activez-le tel qu'indiqué, avec `.venv\Scripts\activate`.
- Vous êtes maintenant dans votre environnement virtuel. Pour installer des modules, tapez `uv install numpy scipy pandas geopandas matplotlib lets-plot marimo`
    - `numpy`: calcul numérique,
    - `scipy`: calcul scientifique,
    - `pandas`: tableaux de données,
    - `geopandas` données géographiques,
    - `matplotlib` visualisation de base,
    - `lets-plot` visualisation avancée,
    - `marimo`: interface d'utilisation.
- Pour démarrer l'interface d'utilisation, tapez `marimo edit`. Une fenêtre s'ouvrira dans votre navigateur.
- Pour quitter, tapez `Ctrl + C` dans le terminal pour quitter  `marimo`, puis tapez `deactivate` pour quitter votre environnement virtuel.