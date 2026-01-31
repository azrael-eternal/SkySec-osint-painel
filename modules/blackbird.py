import os
import subprocess
import json

BASE_DIR = "osint_tools"
BLACKBIRD_DIR = f"{BASE_DIR}/blackbird"
BLACKBIRD_REPO = "https://github.com/p1ngul1n0/blackbird.git"
DATA_DIR = "data"

# Arquivos JSON padrão que o Blackbird precisa
REQUIRED_FILES = [
    "wmn-data.json",
    "wmn-metadata.json",
    "wmn-names.json",
    "wmn-profiles.json"
]

def install_blackbird():
    if os.path.exists(f"{BLACKBIRD_DIR}/blackbird.py"):
        return True

    print("[+] Blackbird não encontrado. Instalando automaticamente...")

    os.makedirs(BASE_DIR, exist_ok=True)

    try:
        subprocess.run(
            ["git", "clone", BLACKBIRD_REPO, BLACKBIRD_DIR],
            check=True
        )
        print("[+] Blackbird instalado com sucesso!")
        return True
    except Exception as e:
        print(f"[!] Falha ao instalar Blackbird: {e}")
        return False

def prepare_data():
    # Cria a pasta data se não existir
    os.makedirs(DATA_DIR, exist_ok=True)

    # Inicializa arquivos JSON vazios se não existirem
    for filename in REQUIRED_FILES:
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="UTF-8") as f:
                json.dump([], f)  # cria JSON vazio
    print("[+] Pasta data pronta com todos os arquivos necessários.")

def run_blackbird():
    print("\n[ SkySec | Blackbird ]")

    if not install_blackbird():
        return

    prepare_data()

    username = input("Digite o username: ").strip()
    if not username:
        print("[!] Username inválido.")
        return

    blackbird_path = os.path.join(BLACKBIRD_DIR, "blackbird.py")

    if not os.path.exists(blackbird_path):
        print(f"[!] Arquivo {blackbird_path} não encontrado!")
        return

    try:
        # Rodando Blackbird com parâmetro -u
        subprocess.run(
            ["python3", blackbird_path, "-u", username],
            check=False
        )
    except Exception as e:
        print(f"[!] Erro ao executar Blackbird: {e}")
