import os

from django.shortcuts import render, redirect

from minia_gen.const import *
from minia_gen.forms import GenerateurMiniaturesForm
from minia_gen.thumb_functions import generate_image
from vs_minia import settings


# Create your views here.

# Hello World
def hello_world(request):
    return render(request, 'index.html')

# form to chose boss and class

def generer_miniature(request):
    image_url = None
    if request.method == 'POST':
        form = GenerateurMiniaturesForm(request.POST)
        if form.is_valid():
            aile = form.cleaned_data['aile']
            boss = form.cleaned_data['boss']
            classe = form.cleaned_data['classe']
            temps = form.cleaned_data['temps']

            # Générer l'image ici en utilisant les données du formulaire
            wing_background_path = WING_PATH_FOLDER + map_wings_images[aile]
            boss_icon_path = BOSS_CROPPED_PATH_FOLDER + map_bosses_images[boss]
            class_icon_path = CLASS_CROPPED_PATH_FOLDER + map_classes_professions_images[classe]
            output_path = os.path.join(settings.MEDIA_ROOT, 'thumbnail', f"{classe}.png")

            # Assurez-vous que le dossier de sortie existe
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Générer l'image
            generate_image(wing_background_path, class_icon_path, boss_icon_path, temps, output_path)

            # Construire l'URL de l'image pour l'afficher dans le template
            image_url = os.path.join(settings.MEDIA_URL, 'thumbnail', f"{classe}.png")

    else:
        form = GenerateurMiniaturesForm()

    context = {
        'form': form,
        'image_url': image_url  # Ajouter l'URL de l'image au contexte pour l'afficher dans le template
    }
    return render(request, 'minia_gen/minia_form.html', context)