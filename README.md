O SkySec e um painel modular desenvolvido em Python projetado para centralizar e automatizar tarefas de inteligencia de fontes abertas (OSINT). O objetivo principal e oferecer uma interface simplificada para pesquisadores de seguranca e estudantes que precisam gerenciar multiplas ferramentas de reconhecimento em um unico ambiente.

estrutura: 
skysec.py : Nucleo do programa e gerenciador de interface.
install.py : Script de automacao para configuracao de ambiente e ferramentas.
modules/ : Conectores individuais para cada ferramenta integrada.
osint_tools/ : Diretorio destinado aos binarios e repositorios externos.
logs/ : Armazenamento automatico dos resultados de cada varredura.
data/ : Armazenamento de arquivos e metadados processados.

ferramentas: 
Metadata Analyzer: Extracao de dados EXIF e informacoes latentes em imagens.

Blackbird: Busca automatizada por nomes de usuario em centenas de plataformas.

SpiderFoot: Coleta massiva de dados sobre dominios, IPs e infraestrutura.

Nmap: Mapeamento de portas, servicos e vulnerabilidades de rede.

Amass: Enumeracao profunda de subdominios e ativos de rede.

antes do uso, execute "install.py"
O instalador ira configurar as dependencias do sistema e clonar as ferramentas externas necessarias para a pasta osint_tools.

meu github: azrael-eternal
