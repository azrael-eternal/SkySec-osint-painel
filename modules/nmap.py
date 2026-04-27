import subprocess
import os
from datetime import datetime

def run_nmap():
    target = input("Alvo (IP ou dominio): ").strip()
    if not target:
        print("[!] Alvo invalido.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"nmap_{target}_{timestamp}.txt"
    log_path = os.path.join("logs", log_filename)

    print(f"[+] Iniciando varredura em {target}")
    print(f"[+] Resultados serao salvos em: {log_path}\n")

    try:

        result = subprocess.run(
            ["nmap", "-sV", "-Pn", target],
            capture_output=True,
            text=True,
            check=True
        )

        print(result.stdout)

        with open(log_path, "w") as f:
            f.write(f"SkySec Nmap Scan Report\nTarget: {target}\nDate: {timestamp}\n")
            f.write("-" * 30 + "\n")
            f.write(result.stdout)

    except FileNotFoundError:
        print("[!] Erro: Nmap nao encontrado no sistema.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao executar Nmap: {e.stderr}")
    except Exception as e:
        print(f"[!] Erro inesperado: {e}")
