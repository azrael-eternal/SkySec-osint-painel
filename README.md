# 🔎 SkySec — OSINT Panel

SkySec é um **painel de ferramentas OSINT** feito em Python, focado em **automação**, **modularidade** e **facilidade de uso**.  
Ele integra várias ferramentas populares de OSINT em um único menu interativo.

> Projeto educacional voltado para **cibersegurança, OSINT e aprendizado prático**.

---

## 🚀 Funcionalidades

Atualmente o SkySec integra:

- 🖼️ **Metadata Analyzer**
  - Extração de metadados de imagens (EXIF)
- 👤 **Blackbird**
  - Enumeração de usernames em centenas de sites
- 🌐 **SpiderFoot**
  - OSINT automatizado (domínios, IPs, emails, infra)
- 📡 **Nmap**
  - Varredura de portas e serviços
- 🌎 **Amass**
  - Enumeração de subdomínios e infraestrutura

Tudo acessível via **menu interativo em terminal**.

---

## 📁 Estrutura do Projeto

skySec/
├── skysec.py
├── install.py
├── requirements.txt
├── README.md
├── modules/
│ ├── metadata.py
│ ├── blackbird.py
│ ├── spiderfoot.py
│ ├── nmap.py
│ └── amass.py
├── osint_tools/
│ ├── blackbird/
│ └── spiderfoot/
├── data/
└── logs/ 


---

## 🐧 Requisitos

- Linux (Kali Linux recomendado)
- Python **3.10+**
- `git`
- Ferramentas do sistema:
  - `nmap`
  - `amass`

No Kali, normalmente já vêm instaladas.

---
Uso:
python3 -m venv venv
source venv/bin/activate

python install.py

▶️ Uso

Depois da instalação:

python skysec.py


Você verá o menu:

1) Metadata Analyzer
2) Blackbird (usernames)
3) SpiderFoot (OSINT)
4) Nmap
5) Amass
0) Sair


Basta escolher a opção desejada.


Uso no termux (Android)

1️⃣ Instalar o Termux (correto)

Instale apenas por uma dessas opções:

F-Droid (recomendado)

GitHub oficial do Termux

❌ Não use a versão da Play Store (quebrada).

2️⃣ Atualizar o ambiente
pkg update && pkg upgrade -y

3️⃣ Instalar dependências básicas
pkg install -y \
python \
git \
clang \
make \
openssl \
libxml2 \
libxslt \
rust

4️⃣ Clonar o SkySec
git clone https://github.com/noirscarletbond-ux/SkySec-osint-painel.git 
cd skySec

5️⃣ Criar e ativar virtualenv (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate


Se venv não funcionar:

pip install virtualenv
virtualenv venv
source venv/bin/activate

6️⃣ Instalar dependências Python
pip install -r requirements.txt
⚠️ Se der erro em cryptography ou lxml, é limitação do Termux.
Você pode:

ignorar SpiderFoot

usar o SkySec completo no PC

7️⃣ Executar o SkySec
python skysec.py
 

👤 Autor

SkySec foi criado por azrael com o objetivo de estudo, aprendizado e centralização de ferramentas OSINT em um único painel simples.


⚖️ Uso Ético & Responsabilidade

Este projeto foi desenvolvido exclusivamente para fins educacionais e legais.

✅ Uso permitido

Você pode usar o SkySec para:

aprendizado em cybersecurity

estudos de OSINT

testes em seus próprios dados

auditorias com autorização explícita

laboratórios, CTFs e ambientes de estudo


