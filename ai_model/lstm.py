import matplotlib.pyplot as plt
import pandas
frame = pandas.read_csv('sales_per_day.csv')
model_id = frame['model_id']
frame['random_date'] = pandas.to_datetime(frame['random_date'], format = '%Y-%M-%d')
frame = frame.sort_values(by=['random_date'])
nExamples = 39586
train, test = frame[0:2*nExamples//3], frame[2*nExamples//3:]
from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot
# load dataset
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')
# walk-forward validation
history = [x for x in train]
predictions = list()
for i in range(len(test)):
	# make prediction
	predictions.append(history[-1])
	# observation
	history.append(test[i])
# report performance
rmse = sqrt(mean_squared_error(test, predictions))
print('RMSE: %.3f' % rmse)
# line plot of observed vs predicted
pyplot.plot(test)
pyplot.plot(predictions)
pyplot.show()