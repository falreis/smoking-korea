import numpy as np
from scipy import stats

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import export_graphviz
from io import StringIO
import pydotplus

def plot_theme(style="white"):
    sns.set_theme(style=style)

def draw_tree(tree_classifier, feature_names=None, class_names=None, filename='tree.png'):
    dot_data = StringIO()
    export_graphviz(tree_classifier, out_file=dot_data,  
                    feature_names=feature_names, class_names=class_names,
                    proportion=True, rounded=True, filled=True, 
                    rotate=True, impurity=False, label='all')

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png(filename)
    
def seaborn_plot(g, title=None, title_pos=1.03):
    sns.set(font_scale=1.2)
    g.despine(left=True)
    
    if(g.legend != None):
        g.legend.set_title("")
        
    if(g.fig != None):
        g.fig.suptitle(title, y=title_pos, fontsize = 16)
        
def seaborn_bar(data, x, title, labels=None):
    sns.set(font_scale=1.2)
    
    if(labels != None):
        for r1, r2 in labels:
            data = data.replace(to_replace=r1, value=r2)
    
    plt.figure(figsize = (15,6))
    g = sns.countplot(data=data, x=x, palette="dark", alpha=.6)

    for p in g.patches:
        height = p.get_height()
        value = height / sum(data[x].value_counts())
        g.text(p.get_x()+p.get_width()/2., height + 20, 
               '{0:.2%}'.format(value), ha="center", fontsize=12)

    g.set_title(title, fontsize=16)
    
def seaborn_bar_hue(data, x, hue, title, labels=None):
    def percentage_above_bar_relative_to_xgroup(ax):
        all_heights = [[p.get_height() for p in bars] for bars in ax.containers]
        for bars in ax.containers:
            for i, p in enumerate(bars):
                total = sum(xgroup[i] for xgroup in all_heights)
                percentage = f'{(100 * p.get_height() / total) :.1f}%'
                ax.annotate(percentage, (p.get_x() + p.get_width() / 2, p.get_height()), 
                            size=11, ha='center', va='bottom')
                
    if(labels != None):
        for r1, r2 in labels:
            data = data.replace(to_replace=r1, value=r2)

    plt.figure(figsize = (15,6))
    g = sns.countplot(data=data, x=x, hue=hue, palette="dark", alpha=.6)

    percentage_above_bar_relative_to_xgroup(g)
    g.set_title(title, fontsize=16)
        
def bar_plot_with_labels(x, y):
    sns.set(font_scale=1)
    
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]+.001, "{:.2f}%".format(y[i]*100), ha = 'center')

    #plota a importância dos parâmetros do random forest
    plt.figure(figsize=(15, 10))
    plt.bar(x, y)# linewidth=2, markersize=12)
    addlabels(x, y)
    plt.xticks(rotation=90)
    plt.show()