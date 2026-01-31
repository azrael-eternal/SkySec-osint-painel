import subprocess

def run_amass():
    domain = input("Digite o domínio: ")

    print(f"[+] Rodando Amass para {domain}...\n")
    subprocess.run(
        ["amass", "enum", "-d", domain],
        check=False
    )
