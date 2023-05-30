import re            #importando regex = tratamento dos dados

from collections import Counter                                             #counter = é para contar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mt
import seaborn as sns

#importando é sempre pip install matplotlib 

# Extract 

with open('./base/Mente-Milionária.txt','r',encoding = 'utf8') as arquivo:
    texto = arquivo.read()                                  #read le o arquivo

# Quantidade de Palavras

#print(len(texto.split()))            # len = contar o split ele transforma em coleção 

# Eliminando carateres de forma não usual
#dados = texto.replace(",","").replace(".","").replace("?","").replace("\xad","").split()
#print(len(dados))

# Eliminando Caracteres de forma Pythonica
# Transformando dados
regex = re.compile("[a-z-áâãéêíóôõúñçàü]+")      #tranformando para uma expressão regular 
dados = regex.findall(texto.lower())            # findall procura tudo que ta no texto

#quantidade de palavras 
#print(len(dados))

#quantidade de palavras distintas 
#print(len(set(dados)))

# Frequência 
frequencia = Counter(dados).most_common()
frequencia_10 = Counter(dados).most_common(10)    #most ele mostra as palavras que mais se repete
frequencia_30 = dict(Counter(dados).most_common(30))
#print(frequencia_30)

# Frequencia 10 100 1000 10000
posicoes = []
tabela = {}
i = 0
while i <len(frequencia):
    posicao = 10
    
    for indice,item in enumerate(frequencia): # (palavra,10)
        i+=1
        if indice == posicao-1:
            posicoes.append(f'Posição: {posicao}  Palavra: {item[0]}')
            tabela[item[0]] = item[1]
            posicao *=10


#automatizando a criação de arquivo
with open('./Relatórios/zipf_10m.txt','w',encoding='utf8') as arquivo:
    for item in posicoes :
        arquivo.write(f'{item}\n')

# criando DataFrame/visual zipf_10m
def visual10():
    x = posicoes
    y = list(tabela.values())             #para ter uma visualização melhor convertemos para lista

    dados_df = pd.DataFrame({'Palavras': x,'Quantidade': y})

    with open('./Relatórios/zipf_10m.txt','w',encoding='utf8') as arquivo:
        for item in posicoes :
            arquivo.write(f'{item}\n') #escrevendo zipf10m
        arquivo.write(f'\n{str(dados_df)}') # esqeuvendo dataframe
        arquivo.write(f'\n \n Quantidade de palavras: {len(dados)}')
        arquivo.write(f'\n Quantidade de palavras distintas: {len(set(dados))}')

    fig,ax  = plt.subplots(figsize = (10,5))
    x = np.arange(len(dados_df['Palavras']))

    visual = ax.bar(x=x,height="Quantidade",data=dados_df)

    ax.set_title('Análise ZipF', fontsize=14, pad=20)
    ax.set_xlabel('Palavras',fontsize=12,labelpad=10)
    ax.set_ylabel('Quantidade',fontsize=12,labelpad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(dados_df['Palavras'])
    ax.bar_label(visual,size=10,label_type='edge')      #edge é no topo da barra e center o valor no meio da barra
    #plt.show()                                               # mostra o grafico
    plt.savefig('./Relatórios/zipf_10m.png',dpi = 600,bbox_inches='tight')








        






    #print(f'Sergio Abandonou lalinha')

dados_dt = pd.DataFrame(
    {'Palavra': frequencia_30.keys(),'Quantidade':frequencia_30.values()}) 

x = list(frequencia_30.keys())
y = list(frequencia_30.values())

fig,ax = plt.subplots(figsize=(12,6))
mt.style.use(['seaborn'])
sns.barplot(x=x,y=y)
ax.set_title('Zipf 30+',fontsize=12)
ax.set_ylabel('Quantidade de repetições',fontsize=12,color='purple')
#ax.set_xlabel('30 palavras mais repetidas',fontzise=12,color='purple')

plt.xticks(rotation=60,fontsize=12)

for i,v in enumerate (y):
    ax.text(x=i-0.4,y=v+0.9,s=v,fontsize=12)                 #os valores vao mudando a posição

#plt.show()
plt.savefig('./Relatórios/zipf_30mais.png',dpi=600,bbox_inches='tight')


