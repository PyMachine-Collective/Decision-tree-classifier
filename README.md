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

