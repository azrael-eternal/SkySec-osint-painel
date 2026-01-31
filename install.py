import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "osint_tools")

BLACKBIRD_REPO = "https://github.com/p1ngul1n0/blackbird.git"
SPIDERFOOT_REPO = "https://github.com/smicallef/spiderfoot.git"

def run(cmd, cwd=None):
    try:
        subprocess.run(cmd, check=True, cwd=cwd)
    except subprocess.CalledProcessError:
        print(f"[!] Erro ao executar: {' '.join(cmd)}")
        sys.exit(1)

def ensure_dirs():
    for d in ["osint_tools", "data", "logs"]:
        path = os.path.join(BASE_DIR, d)
        os.makedirs(path, exist_ok=True)

def check_system_tool(tool):
    if subprocess.call(["which", tool], stdout=subprocess.DEVNULL) != 0:
        print(f"[!] {tool} não encontrado no sistema.")
    else:
        print(f"[+] {tool} OK")

def install_requirements():
    print("[*] Instalando dependências Python...")
    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def clone_blackbird():
    path = os.path.join(TOOLS_DIR, "blackbird")
    if not os.path.exists(path):
        print("[*] Clonando Blackbird...")
        run(["git", "clone", BLACKBIRD_REPO, path])
    else:
        print("[+] Blackbird já existe")

def clone_spiderfoot():
    path = os.path.join(TOOLS_DIR, "spiderfoot")
    if not os.path.exists(path):
        print("[*] Clonando SpiderFoot...")
        run(["git", "clone", SPIDERFOOT_REPO, path])
    else:
        print("[+] SpiderFoot já existe")

def main():
    print("=== SkySec Installer ===")

    ensure_dirs()
    install_requirements()

    clone_blackbird()
    clone_spiderfoot()

    print("\n[*] Verificando ferramentas do sistema:")
    check_system_tool("nmap")
    check_system_tool("amass")

    print("\n[✓] Instalação concluída!")
    print("Ative a venv e rode: python skysec.py")

if __name__ == "__main__":
    main()
