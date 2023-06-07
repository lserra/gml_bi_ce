import os
from pathlib import Path

from dotenv import load_dotenv

ABOUT = """
Esta é uma plataforma de dados que possbilita obter leads e insights.
Também, é possível usar estes dados com nossas outras ferramentas, para melhorar o 
relacionamento com o cliente, fazer rastreamento de reputação ou obter mais feedback.
Esta ferramenta é gratuita (versão Community Edition). 
Nesta base de dados, existem aproximadamente 6M de empresas (CNPJ).
Estes dados podem ser filtrados por: UF, Município e Porte da Empresa.
Além disso, é possível exportar os dados para um formato de arquivo CSV e salvá-los em
seu próprio computador.
"""

LGPD = """
Os dados apresentados, são dados **NÃO SENSÍVEIS** e de **ORIGEM PÚBLICA**, e não 
requerem autorização prévia para exibição conforme
[Decreto nº 8.777/2016](http://www.planalto.gov.br/CCIVIL_03/_Ato2015-2018/2016/Decreto/D8777.htm),
que Institui a **Política de Dados Abertos** e pela 
[Lei nº 12.527/2011](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm),
que regulamenta a **Garantia de acesso a Informações** previsto na Constituição Federal.

Apesar da legalidade, respeitamos aqueles que expressam ativamente seu desejo em ocultar 
seus dados. Para isso utilize o link para 
[Solicitar Privacidade](https://www.getmoreleads.com.br/privacidade/optout).
"""


class Config:
    # load the environment variables from .env file
    APP_PATH = Path(__file__).parent
    env_path = APP_PATH / ".env"
    if env_path.exists():
        load_dotenv()
    else:
        raise IOError(".env file NOT found")

    # retrieving keys and adding them to the project
    # from the .env file through their key names
    AUTHOR = os.getenv("AUTHOR")
    APP_NAME = os.getenv("APP_NAME")
    APP_DESC = os.getenv("APP_DESC")
    APP_FULL_DESC = ABOUT
    APP_WARN_LGPD = LGPD
    DOMAIN = os.getenv("DOMAIN")
    EMAIL = os.getenv("EMAIL")
    ROOT_URL = os.getenv("ROOT_URL")
    DB_PATH = f"{APP_PATH}/data/output/gmlbi.db"
