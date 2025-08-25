import os
import json
import re

video_folder = "videos"  # dossier contenant tes vidéos
output_file = "data.json"

def safe_name(filename):
    """
    Renomme le fichier pour qu'il soit safe pour Netlify :
    - remplace les espaces par _
    - remplace les caractères non ASCII par leurs équivalents ASCII simples
    - supprime les caractères problématiques
    """
    name, ext = os.path.splitext(filename)
    # Normaliser les accents
    name = name.encode("ascii", "ignore").decode()
    # Remplacer les espaces et caractères spéciaux par _
    name = re.sub(r'[^A-Za-z0-9_-]', '_', name)
    return f"{video_folder}/{name}{ext}"

# Liste tous les fichiers mp4 et webm
videos = [safe_name(f) for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.webm'))]

# Écrire dans data.json
with open(output_file, "w", encoding="utf-8") as f:
    json.dump({"videos": videos}, f, indent=4)

print(f"{len(videos)} vidéos ajoutées dans {output_file}")
