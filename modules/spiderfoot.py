# modules/spiderfoot.py
import subprocess
import os

BASE_DIR = "../osint_tools"

def run_spiderfoot():
    target = input("Digite o target (domínio ou username): ")

    path = f"{BASE_DIR}/spiderfoot"
    if not os.path.exists(path):
        print("[+] SpiderFoot não encontrado. Instalando automaticamente...")
        os.makedirs(path, exist_ok=True)
        try:
            # Clona o repositório oficial
            subprocess.run([
                "git", "clone",
                "https://github.com/smicallef/spiderfoot.git",
                path
            ], check=True)
            # Instala dependências
            subprocess.run([
                "pip", "install", "-r", f"{path}/requirements.txt"
            ], check=True)
            print("[+] SpiderFoot instalado com sucesso!")
        except Exception as e:
            print(f"[!] Erro ao instalar SpiderFoot: {e}")
            return

    print(f"[+] Rodando SpiderFoot para: {target}\n")
    try:
        # Roda o SpiderFoot no modo CLI
        subprocess.run(["python3", f"{path}/sf.py", "-s", target], check=True)
    except Exception as e:
        print(f"[!] Erro ao executar SpiderFoot: {e}")
