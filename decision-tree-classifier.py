# Decision Tree Classifier Implementation using Sklearn
# Step1: Load the data
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Step2: Split the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,
random_state = 42)

# Step3: train the model
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
pred = clf.predict(X_test)

# Step4: evaluate the model performance using test set
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test,pred)
print('accuracy rate', acc)
# accuracy rate 1.0

# Step5: print the decision tree
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data) 
graph.render("iris classification")
# 'iris classification.pdf'

import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph

