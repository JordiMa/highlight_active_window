
# highlight_active_window

## Description

`highlight_active_window.py` est un script conçu pour mettre en évidence la fenêtre active en assombrissant le reste de l'écran. Cela permet de protéger les écrans OLED, en particulier les écrans ultra larges (32:9 par exemple), en réduisant le risque de brûlures d'écran causées par des images statiques.

## Fonctionnalités

- Crée des superpositions sombres autour de la fenêtre active.
- Met à jour automatiquement la position et la taille des superpositions en fonction de la fenêtre active.
- Permet de masquer temporairement les superpositions en cliquant dessus, avec réactivation automatique après quelques secondes.

## Paramètres

- `dim_opacity` : Opacité des superpositions sombres. Par défaut à 0.7 (70% de transparence). Ajustez cette valeur selon vos préférences.

## Prérequis

Assurez-vous d'avoir les modules `pyautogui`, `tkinter`, et `pygetwindow` installés. Vous pouvez les installer en utilisant pip :

```bash
pip install pyautogui pygetwindow
```

`tkinter` est généralement inclus avec Python sur les installations Windows. Si ce n'est pas le cas, vous pouvez l'installer en utilisant votre gestionnaire de paquets préféré ou en suivant les instructions spécifiques à votre système d'exploitation.

## Utilisation

1. Assurez-vous d'avoir Python et les modules `pyautogui`, `tkinter`, et `pygetwindow` installés.
2. Téléchargez et placez le script `highlight_active_window.py` dans un répertoire de votre choix.
3. Exécutez le script en utilisant Python :

   ```bash
   python highlight_active_window.py
   ```

   Pour exécuter le script sans afficher l'invite de commande (utile pour une utilisation continue), utilisez `pythonw` :

   ```bash
   pythonw highlight_active_window.py
   ```

## Explications des Fonctions

### `set_window_opacity(window, opacity)`
Définit l'opacité de la fenêtre donnée.

### `create_overlay(on_click_callback)`
Crée une fenêtre de superposition et lie un événement de clic.

### `get_active_window()`
Récupère la boîte englobante de la fenêtre actuellement active.

### `on_overlay_click(event)`
Désactive temporairement les superpositions après un clic et les réactive après 5 secondes.

### `deactivate_overlays()`
Définit l'opacité de toutes les superpositions à 0 (invisible).

### `reactivate_overlays()`
Réinitialise l'opacité de toutes les superpositions à la valeur de l'opacité diminuée.

### `update_overlays()`
Met à jour la position et la taille des superpositions en fonction de la fenêtre active.

## Avertissements

- Le script peut nécessiter des ajustements de paramètres en fonction de la configuration de votre écran et de vos fenêtres.
- Utiliser des valeurs d'opacité trop basses peut rendre difficile la distinction des éléments sur l'écran.

## Contributions

Les contributions sont les bienvenues ! Si vous trouvez des bugs ou avez des suggestions pour améliorer le script, n'hésitez pas à créer une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence Apache 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
