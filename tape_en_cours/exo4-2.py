from pathlib import Path
import tarfile
import puremagic

# on dézippe le fichier
zip_path = Path(
    "../medias/administrationSysteme/manipulationFichiers/fichiersVrac.tar.gz"
)
extraction_path = Path(
    "../medias/administrationSysteme/manipulationFichiers/fichiersVrac_dezippe_python"
)

extraction_path.mkdir(parents=True, exist_ok=True)
file = tarfile.open(zip_path)
file.extractall(extraction_path)
file.close()
