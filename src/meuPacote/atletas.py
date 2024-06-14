import os
from pathlib import Path
BASE_DIR = str(Path(os.path.dirname(__file__)).parent.parent)
import pandas as pd
file = BASE_DIR + '/data/athlete_events_filtered.csv'
df = pd.read_csv(file)

def getAge(nome):
    """
    Funcao para pegar a idade do atleta consultado

    Parameters:
    nome (str): nome do atleta

    Returns:
    age (int): idade do atleta
    """
    age = df.loc[df.Name==nome, ['Age']].values[0][0]
    return age

def getCountry(nome):
    """
    Funcao para pegar o pais do atleta consultado

    Parameters:
    nome (str): nome do atleta

    Returns:
    country (str): pais do atleta
    """
    country = df.loc[df.Name==nome, ['Team']].values[0][0]
    return country

def getMedal(nome):
    """
    Funcao para pegar a idade do atleta consultado

    Parameters:
    nome (str): nome do atleta

    Returns:
    medal (str): medalha do atleta
    """
    medal = df.loc[df.Name==nome, ['Medal']].values[0][0]
    return medal