# Machine Learning Sonar Project: Binary Classification Problem

Project Overwiew:
-	The task is to train a model that can discriminate metal and rock objects from sonar signals.
-	We explore 6 machine learning algorthms for our model. 
-	Logistic regression, linear discriminant analysis, naïve bayes, classification and regression trees, k nearest negihbors and support vector machines (LR, LDA, NB, CART, LNN, SVM).
-	We evaluated and compared models using 10 fold cross validation and classification accuracy. 
-	It was found that transforming the data then using SVM produced the best results achieving 92.8% accuracy.
-	The libraries used were sci-kit learn, numpy, scipy, pandas and matplotlib.

Objectives:
-	Analyze data
-	Evaluate algorithms
-	Improve accuracy 
-	Finalize model

Analyze Data:
- We analyzed our data with statistics and visualizations.
-	Histogram & Density Plot: Some attributes resemble a gaussian distribution, others an exponential.


![HistoPlot](https://user-images.githubusercontent.com/108841153/218567137-4c72208d-b6c9-47a7-8c22-33221e215e09.png)
![DensityPlot](https://user-images.githubusercontent.com/108841153/218567430-22b0e496-6559-4c1e-8cba-f9f46ec8aecb.png)


-	Box and whisker plot: The attributes appear to have a differing mean. Standardizing the data may provide benefit.


![BoxAndWhisker](https://user-images.githubusercontent.com/108841153/218568211-c0b62501-6314-412a-95f9-2b0969fc664e.png)


-	Correlation Matrix: The patches around the diagonal suggest attributes next to each other are in general, more positively correleated with one another.


![CorrMat](https://user-images.githubusercontent.com/108841153/218568311-4379d90d-2ef6-424c-8d64-dc1032f68425.png)

Evaluate Algorithms:
- We evaluated the 6 algorithms and compared their performances.
-	LR had the best results with a mean accuracy of 77.9%. 
- Distribution of accuracy: 
![CompareAlgs](https://user-images.githubusercontent.com/108841153/218569040-5e37bd14-1cf8-4bcf-ac20-6ece7a30e2cc.png)

Improve Accuracy:
- To improve accuracy we standardized the dataset. Pipelines were implemented to avoid data leakage.
-	KNN and SVM had the best results with a mean accuracy of 80.8% and 82.6%  respectively.
- Distribution of accuracy:
![CompareScaledAlg](https://user-images.githubusercontent.com/108841153/218569653-8ca2eb03-1129-48fe-b5a9-865f0d4010fa.png)

Finalize Model:
- KNN and SVM show the most promise for a model. Thus we experimented with these two candidates.
- We tuned the parameters for KNN and SVM to find the most optimal configuration.
-	It was found that SVM with radial basis function as the kernel and C= 1.7 scored the best with 85.0% accuracy.
- To finalize the model 80% of the dataset is used to train, 20% to make predictions.

Results:
- The final model achieved an accuracy of 92.8% on unseen data. This surpasses our estimate of 85.0%. The predictions made by our model are depicted below.
-	confusion matrix:

![ConfusionMatrix](https://user-images.githubusercontent.com/108841153/218570407-92f52dfa-61ff-4b3d-9ba1-4b18a5aba5be.png)


Refrences:
http://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks)#:~:text=mines%22%20contains%20111%20patterns%20obtained,modulated%20chirp%2C%20rising%20in%20frequency.

