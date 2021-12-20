import statistics
import random
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print("Mean of the population is {}".format(population_mean))
print("Standard Deviation of the population is {}".format(population_stdev))

fig = ff.create_distplot([data], ["Reading Time"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
  df = mean_list
  fig = ff.create_distplot([df], ["Means"], show_hist=False)
  fig.show()

def setup(count):
  mean_list = []
  for i in range(0,count):
    mean = random_set_of_mean(30)
    mean_list.append(mean)
  show_fig(mean_list)
  mean_of_mean_list = statistics.mean(mean_list)
  stdev_of_mean_list = statistics.stdev(mean_list)
  print("Mean of the sample is {}".format(mean_of_mean_list))
  print("Standard Deviation of the sample is {}".format(stdev_of_mean_list))

setup(100)