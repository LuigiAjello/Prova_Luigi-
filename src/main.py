import os
from pathlib import Path
BASE_DIR = str(Path(os.path.dirname(__file__)).parent)
from dotenv import load_dotenv 
load_dotenv()
import pandas as pd 
from meuPacote.atletas import getAge, getCountry, getMedal
from meuPacote.email import enviar_email

def main():
    fileNomes = BASE_DIR + '/data/nomesAtletas.xlsx'
    dfNomes = pd.read_excel(fileNomes)
    listaNomes = dfNomes['nome'].tolist()
    dfDados = pd.DataFrame()
    listaidade = []
    listapais = []
    listamedalha = []
    
    for numero in listaNomes:
        idade = getAge(numero)
        listaidade.append(idade)
        
    for numero in listaNomes:
        pais = getCountry(numero)
        listapais.append(pais)
        
    for numero in listaNomes:
        medalha = getMedal(numero)
        listamedalha.append(medalha) 
        
    dfDados['nome'] = listaNomes
    dfDados['idade'] = listaidade
    dfDados['pais'] = listapais
    dfDados['medalha'] = listamedalha

    dfDados.to_excel(BASE_DIR + '/data/listaFinal.xlsx')
    
    atletas_ouro_acima_30 = dfDados[(dfDados['idade'] > 30) & (dfDados['medalha'] == 'Gold')]
    nomes_atletas_ouro_acima_30 = atletas_ouro_acima_30['nome'].tolist()
    
    num_atletas_eua = dfDados[dfDados['pais'] == 'United States'].shape[0]
    
    atleta_mais_velho = dfDados[dfDados['idade'] == dfDados['idade'].max()]
    nome_mais_velho = atleta_mais_velho['nome'].iloc[0]
    idade_maxima = atleta_mais_velho['idade'].iloc[0]
    
    num_paises_distintos = dfDados['pais'].nunique()
    
    usuario = os.environ.get("YAHOO_USER") 
    senha = os.environ.get("YAHOO_PASSWORD") 
    destinatario = "lupixajello@gmail.com"
    assunto = "Prova AP2"
    
    mensagem = f'''
Nome dos atletas com mais de 30 anos e que ganharam medalha de ouro:
{', '.join(nomes_atletas_ouro_acima_30)}

Os atletas dos Estados Unidos são:
{', '.join(dfDados[dfDados['pais'] == 'United States']['nome'].tolist())}
No total, foram {num_atletas_eua} atletas

O nome do atleta mais velho a ganhar medalha de ouro foi {nome_mais_velho} com {int(idade_maxima)} anos

Ao todo, foram {num_paises_distintos} países
'''

    enviar_email(usuario, senha, destinatario, assunto, mensagem)
    
if __name__ == '__main__':
    main()
