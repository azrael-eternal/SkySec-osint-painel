import os
import sys

try:
    from modules.metadata import extract_metadata
    from modules.blackbird import run_blackbird
    from modules.spiderfoot import run_spiderfoot
    from modules.nmap import run_nmap
    from modules.amass import run_amass
except ImportError as e:
    print(f"Erro ao carregar modulos: {e}")
    sys.exit(1)

def logo():
    print(r"""
███████╗██╗  ██╗██╗   ██╗███████╗███████╗ ██████╗
██╔════╝██║ ██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
███████╗█████╔╝   ╚████╔╝ ███████╗█████╗  ██║     
╚════██║██╔═██╗    ╚██╔╝  ╚════██║██╔══╝  ██║     
███████║██║  ██╗    ██║   ███████║███████╗╚██████╗
╚══════╝╚═╝  ╚═╝    ╚═╝   ╚══════╝╚═════╝ ╚═════╝
           by azrael | OSINT Panel
""")

def handle_metadata():
    path = input("Caminho da imagem: ").strip()
    if os.path.exists(path):
        extract_metadata(path)
    else:
        print("Arquivo nao encontrado.")

def menu():
    options = {
        "1": ("Metadata Analyzer", handle_metadata),
        "2": ("Blackbird (usernames)", run_blackbird),
        "3": ("SpiderFoot (OSINT)", run_spiderfoot),
        "4": ("Nmap (redes)", run_nmap),
        "5": ("Amass (dominios)", run_amass),
        "0": ("Sair", None)
    }
    
    print("\n[ SkySec | OSINT Panel ]")
    for key, (desc, _) in options.items():
        print(f"{key}) {desc}")
    return options

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo()

    while True:
        options = menu()
        choice = input("\nEscolha: ").strip()

        if choice == "0":
            print("Saindo...")
            break
        
        if choice in options:
            action = options[choice][1]
            try:
                action()
            except KeyboardInterrupt:
                print("\nOperacao cancelada.")
            except Exception as e:
                print(f"Erro no modulo: {e}")
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
