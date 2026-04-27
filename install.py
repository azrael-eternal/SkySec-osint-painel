
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(BASE_DIR, "osint_tools")

REPOS = {
    "blackbird": "https://github.com/p1ngul1n0/blackbird.git",
    "spiderfoot": "https://github.com/smicallef/spiderfoot.git"
}

def run(cmd, cwd=None):
    try:
        subprocess.run(cmd, check=True, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao executar {' '.join(cmd)}: {e.stderr.decode().strip()}")
        return False
    return True

def ensure_dirs():
    for d in ["osint_tools", "data", "logs"]:
        os.makedirs(os.path.join(BASE_DIR, d), exist_ok=True)

def check_system_tool(tool):
    is_installed = subprocess.call(["which", tool], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    status = "OK" if is_installed else "NAO ENCONTRADO"
    print(f"{tool.ljust(10)} : {status}")

def setup_tools():
    for name, url in REPOS.items():
        path = os.path.join(TOOLS_DIR, name)
        if not os.path.exists(path):
            print(f"Instalando {name}...")
            run(["git", "clone", url, path])
            
            # Instala requirements especificos da ferramenta clonada
            req_path = os.path.join(path, "requirements.txt")
            if os.path.exists(req_path):
                run([sys.executable, "-m", "pip", "install", "-r", req_path])
        else:
            print(f"{name.ljust(10)} : INSTALADO")

def main():
    print("SKYSEC INSTALLER\n")

    ensure_dirs()
    
    print("Verificando pacotes Python...")
    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    if os.path.exists("requirements.txt"):
        run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    print("Configurando ferramentas OSINT...")
    setup_tools()

    print("\nVerificando ferramentas de sistema:")
    check_system_tool("nmap")
    check_system_tool("amass")

    print("\nProcesso concluido.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInstalacao cancelada.")
        sys.exit(1)
