import pandas as pd
from sklearn.tree import export_graphviz
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

if __name__ == "__main__":
    catDisease = pd.read_csv('data/cat/labeledData.csv', encoding='euc-kr')
    model_cat = pickle.load(open('data/cat/diagnose.pkl', 'rb'))
    model_visualization(model_cat,catDisease)
