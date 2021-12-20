import statistics
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean of the population:", population_mean)
print("Standard Deviation of the population:", stdev)

def random_samples_and_their_mean(count):
  dataset = []
  for i in range(0,count):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  
  mean = statistics.mean(dataset)
  return mean

def show_fig(mean_list):
  df = mean_list
  fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
  fig.show()

mean_list = []

for i in range(0,100):
  set_of_means = random_samples_and_their_mean(30)
  mean_list.append(set_of_means)
sampling_mean = statistics.mean(mean_list)
sampling_stdev = statistics.stdev(mean_list)

first_stdev_start, first_stdev_end = sampling_mean-sampling_stdev, sampling_mean+sampling_stdev
second_stdev_start, second_stdev_end = sampling_mean-(2*sampling_stdev), sampling_mean+(2*sampling_stdev)
third_stdev_start, third_stdev_end = sampling_mean-(3*sampling_stdev), sampling_mean+(3*sampling_stdev)

fig = ff.create_distplot([mean_list],["Reading Time"],show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,1],mode='lines',name="Standard Deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,1],mode='lines',name="Standard Deviation 1 end"))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,1],mode='lines',name="Standard Deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,1],mode='lines',name="Standard Deviation 2 end"))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,1],mode='lines',name="Standard Deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,1],mode='lines',name="Standard Deviation 3 end"))
fig.show()

z_score = (sampling_mean-population_mean)/sampling_stdev
print(f"Z score of the sample: {z_score}")