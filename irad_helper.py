import datetime
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

RANDOM_STATE=42

def load_data(filename):
    data = pd.read_csv(filename, delimiter=',')
        
    # Remove duplicate
    data = data[~data.ID.duplicated(keep='first')]
    
    return data

def split_data(x_data, y_data, test_size=0.2):
    """Função para divisão dos conjuntos de treinamento e testes."""

    return train_test_split(
        x_data,
        y_data, 
        test_size = test_size, #percentual do conjunto de treino
        random_state = RANDOM_STATE, #seed random, para resultados semelhantes
        shuffle = True
    )