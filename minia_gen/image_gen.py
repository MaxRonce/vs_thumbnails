from PIL import Image, ImageDraw, ImageFont

# Ouvrir l'image
image = Image.open('../static/minia_gen/boss/adina.png')

image2 = Image.open('../static/minia_gen/classes/cropped/cata.png')

# Créer un objet ImageDraw
draw = ImageDraw.Draw(image)

# Spécifier la police et la taille (optionnel)
font = ImageFont.truetype('../static/minia_gen/tahomabd.ttf', 225)

# Spécifier la position du texte (x, y)
position_texte = (1135, 100) # Exemple de position

position2 = (1275, 350)

# Spécifier la couleur du texte, blanc légèrement transparent
color = (255, 255, 255, 220)

# Ajouter le texte
draw.text(position_texte, '13:55', fill=color, font=font)


image.paste(image2, position2, image2)


image_boss = Image.open('../static/minia_gen/boss/cropped/sh.png')
boss_position = (58, 97)
image.paste(image_boss, boss_position, image_boss)



# Sauvegarder l'image modifiée dans le dossier output
image.save('../output/test_image_all.png')
