from PIL import Image, ImageDraw, ImageFont

# Ouvrir l'image principale
image = Image.open('../static/minia_gen/boss/adina.png')

# Ouvrir la troisième image à transformer en losange
image3 = Image.open('../static/minia_gen/boss/cropped/sh.png')

# Trouver la dimension la plus petite pour déterminer la taille maximale du losange
dimension_minimale = min(image3.size)

# Calculer la taille et la position du losange pour qu'il soit centré
taille_losange = dimension_minimale  # Le losange remplira la plus petite dimension de l'image
start_x = (image3.width - taille_losange) // 2
start_y = (image3.height - taille_losange) // 2

# Créer un masque en forme de losange de la même taille que la zone ciblée
masque = Image.new('L', (taille_losange, taille_losange), 0)
draw_masque = ImageDraw.Draw(masque)
draw_masque.polygon([(taille_losange//2, 0), (taille_losange, taille_losange//2), (taille_losange//2, taille_losange), (0, taille_losange//2)], fill=255)

# Découper la zone spécifique de image3
zone_losange = image3.crop((start_x, start_y, start_x + taille_losange, start_y + taille_losange))

# Appliquer le masque à la zone pour obtenir une forme de losange
zone_losange.putalpha(masque)

# Réduire la taille du losange à 500x500
zone_losange_reduite = zone_losange.resize((885, 885))

# Position où coller l'image en forme de losange sur l'image principale
position_losange = (58, 97)

# Coller l'image en losange sur l'image principale
image.paste(zone_losange_reduite, position_losange, zone_losange_reduite)

# Sauvegarder l'image modifiée
image.save('../output/test_image_modifiee2332.png')

image.show()
