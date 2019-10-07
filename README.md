# ProjetUdeS-ImagerieMedicale

# Installation

Requis: Python 3.5+ | Linux, Mac OS X, Windows

```sh
pip install pipenv
```

Puis dans le dossier du projet:

```sh
pipenv install --python 3.5
```

Le pipfile permettra l'installation de toutes les dépendances nécessaires à l'utilisation du projet.
Puis pour exécuter des commandes dans cet environnement virtuel:

```sh
pipenv shell
```

# Préparez-vous :

Avant de lancer le code, collez à la racine le dossier "Data_MisEnForme" (fourni avec le sujet du TD).
Collez le fichier rat111.nii (déjà présent dans ce projet) dans le dossier CT (c'est un des fichiers qui n'était pas fourni en .nii et que nous avons converti)

Pour lancer le script principal, il suffit finalement de taper dans le dossier du projet:

```sh
pipenv run jupyter notebook
```

Sélectionner le notebook "TD-reconstruction.ipynb" et tout est prêt!
