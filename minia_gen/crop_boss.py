import os
from PIL import Image, ImageDraw


def creer_losange(image_path, taille_losange, start_x, start_y, output_path):
    # Ouvrir l'image à transformer en losange
    image = Image.open(image_path)

    # Découper la zone spécifique pour le losange
    zone_losange = image.crop((start_x, start_y, start_x + taille_losange, start_y + taille_losange))

    # Créer un masque en forme de losange
    masque = Image.new('L', (taille_losange, taille_losange), 0)
    draw_masque = ImageDraw.Draw(masque)
    draw_masque.polygon(
        [(taille_losange // 2, 0), (taille_losange, taille_losange // 2), (taille_losange // 2, taille_losange),
         (0, taille_losange // 2)], fill=255)

    # Appliquer le masque à la zone pour obtenir une forme de losange
    zone_losange.putalpha(masque)

    # Sauvegarder l'image résultante
    zone_losange.save(output_path)


# Chemin du dossier contenant les images à transformer
dossier_images = '../static/minia_gen/boss/'

# Liste des noms des fichiers images à traiter
#images_a_traiter = ['adina.png', 'li.png']  # Exemple avec 2 images, étendre selon besoin
# obtenir la liste des images .png à traiter (toutes les images du dossier)

images_a_traiter = [f for f in os.listdir(dossier_images) if f.endswith('.png')]


# Paramètres pour le losange
taille_losange = 885
start_x = 58
start_y = 97

# Boucle sur les images à traiter
for nom_image in images_a_traiter:
    image_path = os.path.join(dossier_images, nom_image)
    output_path = os.path.join('../static/minia_gen/boss/cropped', nom_image)
    creer_losange(image_path, taille_losange, start_x, start_y, output_path)
