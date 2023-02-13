import numpy
from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt

filename = "SonarData.csv"
dataset = read_csv(filename, names=None)

array = dataset.values
X = array[:,0:60].astype(float)
Y = array[:,60]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size, random_state=seed)


seed = 10
scoring = 'accuracy'

# prepare the model
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
model = SVC(C=1.7)
model.fit(rescaledX, Y_train)
# estimate accuracy on validation dataset
rescaledValidationX = scaler.transform(X_validation)
predictions = model.predict(rescaledValidationX)
print('Accuracy Score =',accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
cm = confusion_matrix(Y_validation, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp = disp.plot(cmap="Purples")
plt.show()


    

 
