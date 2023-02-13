# ML Sonar Project: Binary Classification Problem

Project Overwiew:
-	The task is to train a model that can discriminate metal and rock objects from sonar signals
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
-	Histogram & Density Plot: Some attributes resemble a gaussian distribution, others an exponential.
![HistoPlot](https://user-images.githubusercontent.com/108841153/218567137-4c72208d-b6c9-47a7-8c22-33221e215e09.png)
![DensityPlot](https://user-images.githubusercontent.com/108841153/218567430-22b0e496-6559-4c1e-8cba-f9f46ec8aecb.png)
-	Box and whisker plot: The attributes appear to have a differing mean. Standardizing the data may provide benefit.
![BoxAndWhisker](https://user-images.githubusercontent.com/108841153/218568211-c0b62501-6314-412a-95f9-2b0969fc664e.png)
-	Correlation Matrix: The patches around the diagonal suggest attributes next to each other are generally more positively correleated with one another.
![CorrMat](https://user-images.githubusercontent.com/108841153/218568311-4379d90d-2ef6-424c-8d64-dc1032f68425.png)







Source:http://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks)#:~:text=mines%22%20contains%20111%20patterns%20obtained,modulated%20chirp%2C%20rising%20in%20frequency.

