import os

file_path = "MdpMemoire.txt"

# Vérifier si le fichier existe et le supprimer
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Supprimé: {file_path}")

# Recréer le fichier
with open(file_path, 'w') as file:
    pass  # Le fichier est créé mais reste vide

print(f"Recréé: {file_path}")