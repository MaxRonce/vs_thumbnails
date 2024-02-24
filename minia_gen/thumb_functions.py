from PIL import Image, ImageDraw, ImageFont

from minia_gen.const import *


def transformer_en_losange_centre(image_path, taille_finale_losange=885):
    """
    Prend une image et la transforme en losange centré.
    :param image_path: L'emplacement de l'image à transformer
    :param taille_finale_losange: La taille finale du losange (pixel de cotés)
    :return: L'image transformée en losange (PIL.Image)
    """

    # Ouvrir l'image source
    image = Image.open(image_path)

    # Trouver la dimension la plus petite pour déterminer la taille maximale du losange
    dimension_minimale = min(image.size)

    # Calculer la taille et la position du losange pour qu'il soit centré
    start_x = (image.width - dimension_minimale) // 2
    start_y = (image.height - dimension_minimale) // 2

    # Découper la zone spécifique pour le losange
    zone_losange = image.crop((start_x, start_y, start_x + dimension_minimale, start_y + dimension_minimale))

    # Créer un masque en forme de losange
    masque = Image.new('L', (dimension_minimale, dimension_minimale), 0)
    draw_masque = ImageDraw.Draw(masque)
    draw_masque.polygon([(dimension_minimale // 2, 0), (dimension_minimale, dimension_minimale // 2),
                         (dimension_minimale // 2, dimension_minimale), (0, dimension_minimale // 2)], fill=255)

    # Appliquer le masque à la zone pour obtenir une forme de losange
    zone_losange.putalpha(masque)

    # Réduire la taille du losange à la taille finale spécifiée
    image_losange_finale = zone_losange.resize((taille_finale_losange, taille_finale_losange))

    return image_losange_finale


def ajouter_texte(image: Image, texte: str, font_path: str = FONT_PATH, taille_font: int = FONT_SIZE,
                            position_texte: tuple[float, float] = TEXT_POSITION, couleur_texte: tuple[int] = TEXT_COLOR):
    """
    Ajoute du texte sur une image.
    :param image_path: Une image (PIL.Image), déjà ouverte
    :param texte: Texte à ajouter, ex: '13:55', doit etre un str
    :param font_path: Font à utiliser, ex: '../static/minia_gen/tahomabd.ttf'
    :param taille_font: Int, taille de la font
    :param position_texte: Tuple de deux floats, position du texte sur l'image (X, Y)
    :param couleur_texte: Tuple de 4 ints, couleur du texte (R, G, B, A)
    :return: L'image avec le texte ajouté (PIL.Image)
    """
    # Créer un objet ImageDraw pour permettre le dessin sur l'image
    draw = ImageDraw.Draw(image)

    # Charger la police et définir la taille
    font = ImageFont.truetype(font_path, taille_font)

    # Ajouter le texte à la position spécifiée
    draw.text(position_texte, texte, fill=couleur_texte, font=font)

    return image


def ajouter_icone_class(image : Image, icone_path, position_icone : tuple[int, int] = CLASS_POSITION):
    """
    Ajoute une icône sur une image.
    :param image: Une image (PIL.Image), déjà ouverte
    :param icone_path:  Le chemin de l'icône à ajouter, ex: '../static/minia_gen/classes/cropped/cata.png'
    :param position_icone:  Tuple de deux ints, position de l'icône sur l'image (X, Y)
    :return:  L'image avec l'icône ajoutée (PIL.Image)
    """
    # Ouvrir l'icône de classe
    class_icone = Image.open(icone_path)

    # Coller l'icône sur l'image principale à la position spécifiée
    image.paste(class_icone, position_icone, class_icone)

    return image

def ajouter_icone_boss(image : Image, icone_path, position_icone : tuple[int, int] = BOSS_POSITION):
    """
    Ajoute une icône sur une image.
    :param image: Une image (PIL.Image), déjà ouverte
    :param icone_path:  Le chemin de l'icône à ajouter, ex: '../static/minia_gen/boss/cropped/sh.png'
    :param position_icone:  Tuple de deux ints, position de l'icône sur l'image (X, Y)
    :return:  L'image avec l'icône ajoutée (PIL.Image)
    """
    # Ouvrir l'icône de boss si elle n'est pas déjà ouverte
    if isinstance(icone_path, str):
        boss_icone = Image.open(icone_path)
    else:
        boss_icone = icone_path


    # Coller l'icône sur l'image principale à la position spécifiée
    image.paste(boss_icone, position_icone, boss_icone)

    return image

def generate_image(image_path, class_path, boss_path, texte, output_path, boss_cropped = True, debug = False):
    # Ouvrir l'image principale
    image : Image = Image.open(image_path)

    # Ajouter le texte
    image = ajouter_texte(image, texte)

    # Ajouter l'icône de classe
    image = ajouter_icone_class(image, class_path)

    # Ajouter l'icône de boss
    if boss_cropped:
        image = ajouter_icone_boss(image, boss_path)
    else:
        print('boss_path', boss_path)
        boss_image = transformer_en_losange_centre(boss_path)
        image = ajouter_icone_boss(image, boss_image)


    # Sauvegarder l'image modifiée
    image.save(output_path)

    if debug :
        image.show()

    return output_path

if __name__ == '__main__':

    # Test avec un boss déja croppé et une classe déja croppée
    wing = WING_PATH_FOLDER + 'w1.png'
    boss = BOSS_CROPPED_PATH_FOLDER + 'adina.png'
    classe = CLASS_CROPPED_PATH_FOLDER + 'temp.png'
    texte = '13:55'

    generate_image(wing, classe, boss, texte, '../output/func_test_img.png', boss_cropped=True)

    # Test avec un boss non croppé

    jacky_boss = BOSS_PATH_FOLDER + 'jacky.jpg'
    generate_image(wing, classe, jacky_boss, texte, '../output/losange_adina.png.png', boss_cropped=False, debug=True)






