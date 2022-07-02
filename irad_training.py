import datetime
import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt

import imblearn
from imblearn.under_sampling import RandomUnderSampler, NearMiss
from imblearn.over_sampling import RandomOverSampler, SMOTE, SMOTENC
from imblearn.pipeline import Pipeline

from sklearn import metrics, svm
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.model_selection import KFold, RepeatedStratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler

RANDOM_STATE=42

def performance_measure(confusion_matrix):
    """Função para cálculo de métricas de desempenho do algoritmo, baseado na matriz de confusão."""

    FP = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)  
    FN = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
    TP = np.diag(confusion_matrix)
    TN = confusion_matrix.sum() - (FP + FN + TP)

    # Sensitivity, hit rate, recall, or true positive rate
    TPR = TP/(TP+FN)
    # Specificity or true negative rate
    TNR = TN/(TN+FP) 
    # Fall out or false positive rate
    FPR = FP/(FP+TN)
    # False negative rate
    FNR = FN/(TP+FN)

    return (TPR, TNR, FPR, FNR)

def print_statistics(y_test, predictions, target_names = None):
    print("Precisão:  ", metrics.precision_score(y_test, predictions, average='macro'))
    print("Revocação: ", metrics.recall_score(y_test, predictions, average='macro'))
    print("F1 Score:  ", metrics.f1_score(y_test, predictions, average='macro'))
    print("Acurácia:  ", metrics.accuracy_score(y_test, predictions))
    print("Report:")
    
    if(target_names == None):
        print(metrics.classification_report(y_test, predictions))
    else:
        print(metrics.classification_report(y_test, predictions, target_names=target_names))

    confusion_matrix = metrics.confusion_matrix(y_test, predictions, )
    TPR, TNR, FPR, FNR = performance_measure(confusion_matrix)
    print("TPR", TPR)
    print("TNR", TNR)
    print("FPR", FPR)
    print("FNR", FNR)
    print()

    confusion_display = metrics.ConfusionMatrixDisplay(confusion_matrix, display_labels=target_names)
    confusion_display.plot()
        
def cross_validation(classifier, data_x, data_y, x_test, y_test, class_names=None, max_depth=None):
    best_model = None
    best_acc = 0.
    #accuracies, f1_scores = [], []
    
    ini_time = datetime.datetime.now()
    
    #percent_male = len(data_x[data_x['gender'] == 1.]) / len(data_x)
    #print('Percentual homens/mulher: {:.2f} / {:.2f}'.format(percent_male, 1-percent_male))
    #print()
    print('--- Validation ---')
    print()
    
    #stratified Cross Validation
    strat_kfold = RepeatedStratifiedKFold(n_splits=5, n_repeats=1, random_state=RANDOM_STATE)

    for fold, (train_index, test_index) in enumerate(strat_kfold.split(data_x, data_y), 1):
        X_train = data_x.iloc[train_index]
        y_train = np.ravel(data_y.iloc[train_index])
        X_valid = data_x.iloc[test_index]
        y_valid = np.ravel(data_y.iloc[test_index])
        
        #under sampling
        #rus = RandomUnderSampler(random_state=RANDOM_STATE)
        #X_train, y_train = rus.fit_resample(X_train, y_train)
        
        #smote (oversampling)
        #smote = SMOTE(random_state=RANDOM_STATE, sampling_strategy='not majority', n_jobs=8)
        smote = SMOTENC(categorical_features=[0, 1, 2], 
                    random_state=RANDOM_STATE, sampling_strategy='not majority', n_jobs=8)
        
        X_train, y_train = smote.fit_sample(X_train, y_train)
        
        #treina classificador
        model = classifier()
        
        if(max_depth != None):
            model.max_depth = max_depth
            
        model.fit(X_train, y_train)
        y_pred = model.predict(X_valid)
        
        #armazena acurácia e f1 score em cada fold
        accuracy = model.score(X_valid, y_valid)
        f1_score = metrics.f1_score(y_valid, y_pred, average="macro")
        
        #accuracies.append(accuracy)
        #f1_scores.append(f1_score)
        
        print(f'Fold {fold}:')
        print(f'Accuracy: {accuracy}')
        print(f'F1-score: {f1_score}')
        print()

        #armazena melhor acurácia
        if(accuracy > best_acc):
            best_acc = accuracy
            best_model = model
    
    #plota e imprime estatísticas de validação
    '''
    plt.plot(accuracies, label='Acurácia')
    plt.plot(f1_scores, label='F1 Score')
    plt.legend()
    plt.xlabel('Fold')
    plt.show()
    '''
    
    print()
    print('--- Test ---')
    print()
    
    #análise de desempenho
    #imprime predições
    predictions = model.predict(x_test.values)
    print_statistics(y_test.values, predictions, class_names)

    end_time = datetime.datetime.now()
    print('Time spent:', (end_time - ini_time))
    
    return best_model #grid_search #.best_estimator_['classifier']
