import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import networkx as nx

df = pd.read_csv('/home/matheus/Projetos/graficospython/Top_Anime_data.csv')


df_sorted = df.sort_values(by='Score', ascending=False)

#Selecionar os 5 maiores valores
top_animes = df_sorted.head(5) 

#UNIDADE 1
#Gráfico das maiores notas (Barras)
plt.figure(figsize=(10, 7))
bars = plt.bar(top_animes['English'], top_animes['Score'], color='skyblue')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 2), ha='center', va='bottom')

plt.xlabel('Animes')
plt.ylabel('Nota')
plt.title('Top 5 Animes com as Notas Mais Altas 2024')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#UNIDADE 1
#Gráfico de Popularidade (Setores)
plt.figure(figsize=(9, 9))
labels = top_animes['English']
sizes = top_animes['Popularity']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
explode = (0.0, 0.1, 0.0, 0.0, 0.0)


plt.pie(sizes, colors=colors, startangle=90, autopct='%1.1f%%', explode=explode, pctdistance=0.65)
plt.axis('equal') 
plt.legend(labels, loc='lower right')
plt.title('Maior popularidade do Top 5')
plt.show()

#UNIDADE 3
#Treemap da Quantidade de Episódios
fig = px.treemap(
    top_animes,
    path=['English'],
    values='Episodes',
    color='Episodes',
    color_continuous_scale='Tealgrn',
    title='Duração em episódios dos animes no Top 5'
)
fig.update_traces(
    texttemplate='%{label}<br>Ep: %{value}', 
    textposition='middle center',
)
fig.show()

#UNIDADE 4
#Grafo
G = nx.Graph()
G.add_node('TV')
top_tv_animes = top_animes[top_animes['Type'] == 'TV']

for anime in top_tv_animes['English']:
    G.add_node(anime)
    G.add_edge('TV', anime)

plt.figure(figsize=(8, 8))
pos = nx.circular_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_nodes(G, pos, nodelist=["TV"], node_size=5000, node_color='green')
plt.show()

