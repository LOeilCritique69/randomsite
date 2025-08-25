import os
import json

video_folder = "videos"  # dossier contenant tes vidéos
output_file = "data.json"

# Liste tous les fichiers mp4 et webm
videos = [f"{video_folder}/{f}" for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.webm'))]

# Écrire dans data.json
with open(output_file, "w", encoding="utf-8") as f:
    json.dump({"videos": videos}, f, indent=4)

print(f"{len(videos)} vidéos ajoutées dans {output_file}")
