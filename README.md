# Decision-tree-classifier

[watch the video](https://youtu.be/RmajweUFKvM)

A decision tree is a tree-based supervised learning method used to predict the output of a target variable.<br>Imagine you want to predict whether it is going to snow tomorrow? or not?, so that you can decide whether to wake up early or not to shove the snow.
To predict this event, you utilize the historical weather data, and here is the related scattered plot for the given data.<br>
![Capture1](https://user-images.githubusercontent.com/81442054/135790577-cb6667af-4d7f-4838-aedb-4400c7511e43.PNG)

As you can see in the plot, all the red data point - the snow instances - happen under the temperature lower than 30 and the humidity level above 70. If we transfer this scatter plot into a decision tree diagram, it should look like something below:<br>
![Pic](https://raw.githubusercontent.com/lilly-chen/Bite-sized-Machine-Learning/f19b826cf8bbd4164fbb433039eb50ffebb9de59/Decision%20Tree/Capture2.PNG)<br>
For this snow dataset, you can predict whether it is going to snow or not perfectly by asking two questions:

    Is Temperature below 30 ?
    Is Humidity above 70 ?
![2](https://user-images.githubusercontent.com/81442054/135796220-4032acf6-1d75-4c32-8222-7742dafcdb9d.png)


## Simple implementation

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

### result

![1](https://user-images.githubusercontent.com/81442054/135795904-2007b56a-7f8c-4d37-905e-01452824d8aa.png)

