import os

import requests
import re
from PIL import Image, ImageDraw, ImageFont
from const import *
from thumb_functions import *
from read_log import *

def generate_thumbnails(log_url, output_folder):
    # S'assurer que le dossier de sortie existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    log_json = get_json_from_log(log_url)
    duration, boss_code, professions = lire_informations_json(log_json)

    # Trouver l'arrière-plan de la bonne wing et le chemin de l'icône du boss
    wing_background_path = WING_PATH_FOLDER + map_wings_images[map_boss_wings[boss_code]]
    boss_icon_path = BOSS_CROPPED_PATH_FOLDER + map_bosses_images[boss_code]

    # Ouvrir l'arrière-plan de la wing
    wing_background = Image.open(wing_background_path)

    # Ajouter l'icône du boss au fond
    boss_icon = Image.open(boss_icon_path)
    background_with_boss = ajouter_icone_boss(wing_background, boss_icon_path)

    # Ajouter le temps en texte
    background_with_time = ajouter_texte(background_with_boss, duration)

    # Itérer sur chaque profession pour créer une image
    for profession in professions:
        # Cloner l'arrière-plan pour chaque profession
        background_clone = background_with_time.copy()

        # Obtenir le chemin de l'icône de la profession
        class_icon_path = CLASS_CROPPED_PATH_FOLDER + map_classes_professions_images[profession]

        # Ajouter l'icône de la profession
        final_image = ajouter_icone_class(background_clone, class_icon_path)

        # Définir le chemin d'enregistrement pour l'image de la profession
        save_path = os.path.join(output_folder, f"{profession}.png")

        # Sauvegarder l'image de la profession
        final_image.save(save_path)

        # Optionnel: montrer l'image
        # final_image.show()

    return [os.path.join(output_folder, f"{profession}.png") for profession in professions]

if __name__ == "__main__":
    output_folder = '../output/thumbnail/'
    log_url = "https://dps.report/Bo7S-20240217-212945_sh"
    thumbnail_paths = generate_thumbnails(log_url, output_folder)
    for path in thumbnail_paths:
        print(f"Miniature générée à l'emplacement : {path}")