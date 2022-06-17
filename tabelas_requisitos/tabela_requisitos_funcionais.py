from prettytable import PrettyTable

requisitos_funcionais = PrettyTable()  # cria instância da tabela

# define nome das colunas
requisitos_funcionais.field_names = ["Atividades", "Requisitos Funcionais"]

# define conteúdo das linhas
requisitos_funcionais.add_rows(
    [
        ["Disponibilização de  Artigos",
         "Expor artigos, escritos de maneira acessível, sobre a \n Cibersegurança"],
        ["", ""],
        ["Disponibilização de Tutoriais",
         "Apresentar tutoriais em diveros formatos com exemplos de \n aplicações dos conteúdos dos artigos"],
        ["", ""],
        ["Disponibilização de Ferramentas para Proteção",
         "Exibir ferramentas voltadas à cibersegurança. \n Ex.: Gerador de senhas"],
        ["", ""],
        ["Garantia da Acessibilidade",
         "Apresentar todos os conteúdos de maneira que sejam acessíveis \n para todos os públicos"],
        ["", ""],
        ["Envio Diário de E-mails",
         "Enviar newsletter, para os usuários cadastrados no banco de dados,\n com avisos sobre a inclusão de conteúdos na aplicação"],
        ["", ""],
        ["Informações Sobre os Projeto",
         "Disponibilzar informações sobre os desenvolvedores e orientadores \n do projeto e sobre a instituição de ensino da qual fazem parte"],
        ["", ""],
        ["Disponibilização de Meio para Contato",
         "Expor um formulário para que os usuários possam contatar os \n desenvolvedores"],
        ["", ""],
        ["Exposição de Resultados das Pesquisas",
         "Disponibilizar gráficos com os principais resultados das pesquisas\n do projeto"],
    ]
)

print("\033[92m")
print(requisitos_funcionais)
