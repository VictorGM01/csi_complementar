import numpy as np
import matplotlib.pyplot as plt

opcoes = []  # Inserir as opções de respostas. Ex.: Sim, não, etc

respostas = []  # Inserir a quantidade de respostas na ordem das opções.

explode = ()  # Personalização da explosão de alguma fatia do gráfico

colors = ()  # Inserir as cores de cada fatia na ordem das opções e respostas

wp = {'linewidth': 1, 'edgecolor': "black"}  # tamanho e cor da borda


# Não alterar a função abaixo!
def func(porcentagem):
    return "{:.1f}%".format(porcentagem)


fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(respostas,
                                  autopct=lambda pct: func(pct),
                                  explode=explode,
                                  labels=opcoes,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="magenta"))  # cor dos textos
# Legendas
ax.legend(wedges, opcoes,
          title="Respostas",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

# Título do gráfico
ax.set_title("Insira o título do gráfico (nome da questão do formulário)")
plt.show()

fig.savefig(fname="nome_do_arquivo.png", transparent=True)
