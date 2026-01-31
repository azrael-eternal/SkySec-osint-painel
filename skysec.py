from modules.metadata import extract_metadata
from modules.blackbird import run_blackbird
from modules.spiderfoot import run_spiderfoot
from modules.nmap import run_nmap
from modules.amass import run_amass


def logo():
    print("""
███████╗██╗  ██╗██╗   ██╗███████╗███████╗ ██████╗
██╔════╝██║ ██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
███████╗█████╔╝  ╚████╔╝ ███████╗█████╗  ██║
╚════██║██╔═██╗   ╚██╔╝  ╚════██║██╔══╝  ██║
███████║██║  ██╗   ██║   ███████║███████╗╚██████╗
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ ╚═════╝
""")


def menu():
    print("\n[ SkySec | OSINT Panel ]")
    print("1) Metadata Analyzer")
    print("2) Blackbird (usernames)")
    print("3) SpiderFoot (OSINT)")
    print("4) Nmap (redes)")
    print("5) Amass (domínios)")
    print("0) Sair")


def main():
    logo()

    while True:
        menu()
        choice = input("\nEscolha: ").strip()

        if choice == "1":
            path = input("Caminho da imagem: ")
            extract_metadata(path)

        elif choice == "2":
            run_blackbird()

        elif choice == "3":
            run_spiderfoot()

        elif choice == "4":
            run_nmap()

        elif choice == "5":
            run_amass()

        elif choice == "0":
            print("Saindo do SkySec...")
            break

        else:
            print("[!] Opção inválida.")


if __name__ == "__main__":
    main()

