import subprocess

def run_sherlock():
    print("\n[ SkySec | Sherlock ]")
    username = input("Digite o username: ").strip()
    if not username:
        print("[!] Username inválido.\n")
        return

    sherlock_path = "osint_tools/sherlock/sherlock.py"
    try:
        subprocess.run(["python3", sherlock_path, username])
    except Exception as e:
        print(f"[!] Erro ao executar Sherlock: {e}\n")
