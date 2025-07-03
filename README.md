# Générateur de QR Code

Un générateur simple et rapide de QR codes pour vos liens, textes ou toute autre information.

## Fonctionnalités

- Génération de QR codes à partir de texte ou d’URL
- Personnalisation de la taille du QR code
- Export en format image (PNG/JPG)
- Interface conviviale (CLI ou graphique selon le projet)
- 100% local, aucun enregistrement nécessaire

## Installation

Clone le dépôt :

```bash
git clone https://github.com/DARKBG01/Generateur-de-QrCode.git
cd Generateur-de-QrCode
```

Installe les dépendances nécessaires (exemple pour Python) :

```bash
pip install qrcode[pil]
```

## Utilisation

1. Lance le script principal (par exemple : `python generateur_qrcode.py`).
2. Saisis le texte ou l’URL à encoder.
3. Le QR code est généré et sauvegardé dans le dossier du projet.

### Exemple en ligne de commande

```bash
python generateur_qrcode.py "https://github.com/"
```

Le QR code sera enregistré sous forme d’image dans le dossier courant.

## Auteur

- [DARKBG01](https://github.com/DARKBG01)

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d’informations.
