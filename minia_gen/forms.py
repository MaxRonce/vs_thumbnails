from django import forms

CHOIX_AILES = [
    ('w1', 'w1'),
    ('w2', 'w2'),
    ('w3', 'w3'),
    ('w4', 'w4'),
    ('w5', 'w5'),
    ('w6', 'w6'),
    ('w7', 'w7'),
]

# Vous pouvez ajuster les choix de boss en fonction des ailes
CHOIX_BOSS = {
    'w1': [('vg', 'vg'), ('gors', 'gors'), ('sab', 'sab')],
    'w2': [('sloth', 'sloth'), ('trio', 'trio'), ('matt', 'matt')],
    'w3': [('esc', 'esc'), ('kc', 'kc'), ('xera', 'xera')],
    'w4': [('cairn', 'cairn'), ('mo', 'mo'), ('sam', 'sam'), ('dei', 'dei')],
    'w5': [('sh', 'sh'),('river', 'river'),('statues', 'statues'), ('dhuum', 'dhuum')],
    'w6': [('ca', 'ca'), ('twins', 'twins'), ('qadim', 'qadim')],
    'w7': [('adina', 'adina'), ('sabir', 'sabir'), ('qpeer', 'qpeer')],
}

CHOIX_CLASSES = [('Chronomancer', 'Chronomancer'),
                 ('Virtuoso', 'Virtuoso'),
                 ("Mirage", "Mirage"),
                 ("Weaver", "Weaver"),
                 ("Tempest", "Tempest"),
                 ("Catalyst", "Catalyst"),
                 ("Scourge", "Scourge"),
                 ("Reaper", "Reaper"),
                 ("Harbinger", "Harbinger"),
                 ("Scrapper", "Scrapper"),
                 ("Holosmith", "Holosmith"),
                 ("Mechanist", "Mechanist"),
                 ("Soulbeast", "Soulbeast"),
                 ("Druid", "Druid"),
                 ("Untamed", "Untamed"),
                 ("Deadeye","Deadeye"),
                 ("Daredevil", "Daredevil"),
                 ("Specter", "Specter"),
                 ("Herald", "Herald"),
                 ("Renegade", "Renegade"),
                 ("Vindicator","Vindicator"),
                 ("Firebrand", "Firebrand"),
                 ("Dragonhunter", "Dragonhunter"),
                 ("Willbender", "Willbender"),
                 ("Berserker", "Berserker"),
                 ("Spellbreaker", "Spellbreaker"),
                 ("Bladesworn","Bladesworn")
                 ]

class GenerateurMiniaturesForm(forms.Form):
    aile = forms.ChoiceField(choices=CHOIX_AILES, label="Choisir une aile de raid")
    boss = forms.ChoiceField(choices=[], label="Choisir un boss")  # Les choix sont initialisés vide
    classe = forms.ChoiceField(choices=CHOIX_CLASSES, label="Choisir une classe")
    temps = forms.CharField(label="Temps réalisé")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'aile' in self.initial:
            aile = self.initial['aile']
            self.fields['boss'].choices = CHOIX_BOSS.get(aile, [])

    def clean_boss(self):
        aile = self.cleaned_data.get('aile')
        boss = self.cleaned_data.get('boss')
        if boss not in dict(CHOIX_BOSS.get(aile, [])):
            raise forms.ValidationError("Choix de boss invalide pour l'aile sélectionnée.")
        return boss
