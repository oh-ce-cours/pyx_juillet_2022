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
