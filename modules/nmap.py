import subprocess

def run_nmap():
    target = input("Digite o alvo (IP ou domínio): ")

    print(f"[+] Rodando Nmap em {target}...\n")
    subprocess.run(
        ["nmap", "-sV", "-Pn", target],
        check=False
    )
