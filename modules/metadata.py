from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(path):
    """
    Extrai metadados EXIF de uma imagem.
    path: caminho completo do arquivo de imagem (ex: /sdcard/Download/foto.jpg)
    """

    try:
        # Abrir imagem
        image = Image.open(path)
        exif = image._getexif()

        # Verifica se há metadados
        if not exif:
            print("\n[ SkySec | Metadata ] Nenhum metadado encontrado.\n")
            return

        print("\n[ SkySec | Metadata ]\n")
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
        print()

    except FileNotFoundError:
        print(f"[!] Arquivo não encontrado: {path}")
    except Exception as e:
        print(f"[!] Erro: {e}")
