# Consume -- Just HOW Do?

Front end template taken from [Dash apps](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-financial-report) for [code.jam(2019)](https://devpost.com/software/consume-just-how-do), see link for a more detailed explanation of the project.

## Data Imbalance
We observed early on an issue with the data we were given: less than 5% of the data provided could be used a target. 	

## Built With

- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots

The following are screenshots for the app in this repo:

![animated](screenshots/demo.gif)

![screenshot](screenshots/p1-overview.png)

![screenshot](screenshots/p2-dashboard.png)

![screenshot](screenshots/p3-eval.png)

## The Model
The model used by our website is Random Forest, implented using SKlearn. We tried KNN, Logistic Regression, and also Deep Neural Networks using Keras([link](fasterboi.ipynb)). For the Deep Neural Network, we tried a 7 layer neural network using ReLU, sigmoid, Leaky ReLU and linear activation functions. We also have batch normalization between every layer.
We realized that accuracy is not a suitable metric for our data set: a more fitting metric would be the f1 score which calculates the false postive _rate_ and false negative _rate_. However, our highest f1 score was 0.09.
