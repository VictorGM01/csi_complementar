from prettytable import PrettyTable

requisitos_nao_funcionais = PrettyTable()  # cria instância da tabela

# define nome das colunas
requisitos_nao_funcionais.field_names = ["Atividades", "Requisitos Não Funcionais"]

# define conteúdo das linhas
requisitos_nao_funcionais.add_rows(
    [
        ["Criação do Layout da Aplicação",
         "Figma"],
        ["", ""],
        ["Configuração do Ambiente de Desenvolvimento",
         "Windows, PyCharm, Git"],
        ["", ""],
        ["Criação das Páginas da Aplicação",
         "Windows, PyCharm, Git, GitHub"],
        ["", ""],
        ["Configuração do Ambiente de Produção",
         "Windows, PyCharm, Git, Heroku CLI, Heroku, Namecheap"],
        ["", ""],
        ["Tecnologias",
         "Django, Python3, HTML5, CSS3, JavaScript, jQuery, PostgreSQL, SQLite"]
    ]
)

print("\033[92m")
print(requisitos_nao_funcionais)
