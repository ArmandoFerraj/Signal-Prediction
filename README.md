# ML Sonar Project: Binary Classification Problem

Project Overwiew:
-	The task is to train a model that can discriminate metal and rock objects from sonar signals (dataset was downloaded from UCI ML repository).
-	We explore 6 machine learning algorthms for our model. 
-	Logistic regression, linear discriminant analysis, naïve bayes, classification and regression trees, k nearest negihbors and support vector machines (LR, LDA, NB, CART, LNN, SVM).
-	We evaluated and compared models using 10 fold cross validation and classification accuracy. 
-	It was found that transforming the data, then using SVM produced the best results for this problem.
-	The libraries used were sci-kit learn, numpy, scipy, pandas and matplotlib

Objectives:
-	Analyze data.
-	Evaluate algorithms
-	Improve accuracy 
-	Finalize model

Analyze Data:
We analyzed the data with statistics and visualizations.
-	Histogram & Density: Some attributes resemble a gaussian distribution, others an exponential.
[HistoPlot.pdf](https://github.com/ArmandoFerraj/MLSonarProject/files/10725665/HistoPlot.pdf)
[DensityPlot.pdf](https://github.com/ArmandoFerraj/MLSonarProject/files/10725669/DensityPlot.pdf)






Source:http://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks)#:~:text=mines%22%20contains%20111%20patterns%20obtained,modulated%20chirp%2C%20rising%20in%20frequency.

