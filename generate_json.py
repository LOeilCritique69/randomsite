import os
import json
import re

video_folder = "videos"  # dossier contenant tes vidéos
output_file = "data.json"

def safe_name(filename):
    """
    Renomme le fichier pour qu'il soit safe pour Netlify :
    - remplace les espaces par _
    - supprime les accents et caractères spéciaux
    """
    name, ext = os.path.splitext(filename)
    name = name.encode("ascii", "ignore").decode()   # supprimer accents
    name = re.sub(r'[^A-Za-z0-9_-]', '_', name)     # convertir tout ce qui n'est pas safe en _
    return f"{video_folder}/{name}{ext.lower()}"    # extension minuscule

videos = []
for f in os.listdir(video_folder):
    if f.lower().endswith(('.mp4', '.webm')):
        old_path = os.path.join(video_folder, f)
        new_path = safe_name(f)
        os.rename(old_path, new_path)  # renomme physiquement
        videos.append(new_path)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump({"videos": videos}, f, indent=4)

print(f"{len(videos)} vidéos ajoutées et renommées dans {output_file}")
