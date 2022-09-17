import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import export_graphviz
import matplotlib.font_manager as fm
import pickle
import pydot

def model_visualization(model,
                        df):
    estimator = model.estimators_[5]
    export_graphviz(estimator,
                    out_file='data/image/tree.dot',
                    feature_names=df.columns[1:],
                    class_names=df['질병명'],
                    max_depth=2,  # 표현하고 싶은 최대 depth
                    precision=3,  # 소수점 표기 자릿수
                    filled=True,  # class별 color 채우기
                    rounded=True,  # 박스의 모양을 둥글게
                    )

    (graph,) = pydot.graph_from_dot_file('data/image/tree.dot')
    graph.write_png('data/image/tree_visualization.png')

def visualize_feature_importance(model,
                                 df):
    feature_importance = model.feature_importances_
    ft_importance = pd.Series(feature_importance, index=df.columns[1:])
    ft_importance = ft_importance.sort_values(ascending=False)

    plt.figure(figsize=(12, 10))
    plt.title("feature importance")

    f = [f.name for f in fm.fontManager.ttflist]
    print(f)

    plt.rc('font', family='Nanum Myeongjo')
    sns.barplot(x=ft_importance[:11], y=df.columns[1:12])
    plt.show()

if __name__ == "__main__":
    catDisease = pd.read_csv('data/cat/labeledData.csv', encoding='euc-kr')
    model_cat = pickle.load(open('data/cat/diagnose.pkl', 'rb'))
    model_visualization(model_cat,catDisease)
    visualize_feature_importance(model_cat,catDisease)
