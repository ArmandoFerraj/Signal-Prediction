import numpy
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix

#Import Dataset
filename = "SonarData.csv"
dataset = read_csv(filename, names=None)

#Dimensions of our Dataset
print('Dimensions =',dataset.shape)
print()

#Datatypes For Our Attributes
#set_option('display.max_rows', 500) #REMOVE COMMENT TO VIEW ALL 60
print(dataset.dtypes)
print()

#Descriptive Statistics For Our Attributes
#set_option('display.max_columns', None) #REMOVE COMMENT TO VIEW ALL 60
print(dataset.describe())

#Histogram Plots
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
pyplot.show()

#Density Plots
dataset.plot(kind='density', subplots=True, layout=(8,8), sharex=False, legend=False, fontsize=1)
pyplot.show()

# correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(dataset.corr(), vmin=-1, vmax=1, interpolation='none')
fig.colorbar(cax)
pyplot.show()

