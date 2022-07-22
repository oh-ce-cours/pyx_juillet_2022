from pathlib import Path
import tarfile
import puremagic

zip_path = Path(
    "../medias/administrationSysteme/manipulationFichiers/fichiersVrac.tar.gz"
)
extraction_path = Path(
    "../medias/administrationSysteme/manipulationFichiers/fichiersVrac_dezippe_python"
)

# on dézippe le fichier
extraction_path.mkdir(parents=True, exist_ok=True)
file = tarfile.open(zip_path)
file.extractall(extraction_path)
file.close()

# on va récupérer les extensions réelles des fichiers
resultats = {}
for filename in extraction_path.iterdir():
    str_filename = str(filename)
    extension = puremagic.from_file(str_filename)
    if extension == ".jfif":
        extension = ".jpg"
    # print(extension, str_filename)
    if extension not in resultats:
        resultats[extension] = []
    resultats[extension].append(filename)

print(resultats)
