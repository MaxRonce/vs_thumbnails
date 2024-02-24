import re

import requests
from const import boss_dict

def get_json_from_log(log_url):
    return requests.get(f"https://dps.report/getJson?permalink={log_url}").json()

def parse_duration(duration_str):
    # Utiliser une expression régulière pour trouver les minutes, secondes et millisecondes
    match = re.match(r"(\d+)m (\d+)s (\d+)ms", duration_str)
    if match:
        # Extraire les minutes et les secondes
        minutes, seconds = match.groups()[:2]
        # Formater en mm:ss
        return f"{int(minutes):02d}:{int(seconds):02d}"
    else:
        # Retourner une chaîne vide ou une valeur par défaut si la correspondance échoue
        return "00:00"

def lire_informations_json(data):
    # Extraire la durée en millisecondes et la convertir en minutes
    duration_ms = data.get('duration', '')

    # ex string : "03m 13s 586ms", parse en mm:ss
    duration_ms = parse_duration(duration_ms)
    # Extraire l'id du combat
    fight_id = data.get('triggerID', '')

    fight_name = boss_dict.get(int(fight_id), '')

    # Extraire la profession de chaque joueur
    players_professions = list(set([player.get('profession', '') for player in data.get('players', [])]))

    return duration_ms, fight_name, players_professions

if __name__ == "__main__":
    log_url = "https://dps.report/Bo7S-20240217-212945_sh"
    log_json = get_json_from_log(log_url)
    duration, name, professions = lire_informations_json(log_json)

    print(f"Durée du combat: {duration}")
    print(f"Nom du combat: {name}")
    print(f"Professions des joueurs: {professions}")
