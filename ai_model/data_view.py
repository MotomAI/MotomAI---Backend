import matplotlib.pyplot as plt
import pandas
frame = pandas.read_csv('sales_per_day.csv')
model_id = frame['model_id']
frame['random_date'] = pandas.to_datetime(frame['random_date'], format = '%Y-%M-%d')

frame = frame[model_id == 30516 ].sort_values('random_date')
plt.plot(frame['random_date'], frame['times_sell'], label = 'Air temperature at Frankfurt Int. Airport in 2015')
print(frame)
plt.show()
# frame[model_id == 17883].sort_values('random_date')['random_date'].plot(use_index=False, label="Model 17883")
# frame[model_id == 15325].sort_values('random_date')['random_date'].plot(use_index=False, label="Model 15325")




plt.show()