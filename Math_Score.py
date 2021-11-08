import csv;
import plotly.figure_factory as ff;
import plotly.graph_objects as o ;
import statistics;
import random;
import pandas as pd ; 

df = pd.read_csv("data.csv");
data = df["reading_time"].to_list();

'''
mean = statistics.mean(data);
std_dev = statistics.stdev(data);
print("Standard Devaition is :", std_dev)
print("Mean is :",mean);
'''


'''
fig = ff.create_distplot([data],["Math_score"],show_hist = False);
fig.show();
'''


def random_set_of_mean(counter):
    dataset = [];
    for i in range(0,counter):
        randInd = random.randint(0,len(data)-1)
        value = data[randInd]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean;


meanList = [];

for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    meanList.append(set_of_mean);

std_dev = statistics.stdev(meanList)
mean = statistics.mean(meanList)
#print("Mean is :",mean);


'''
fig = ff.create_distplot([meanList],["Students marks"],show_hist=False)
fig.add_trace(o.Scatter(x = [mean,mean] , y = [0,0.20],mode = "lines",name="mean"))
fig.show();
'''


firstStart , firstEnd = mean-std_dev,mean+std_dev;
secondStart , secondEnd = mean-(2*std_dev),mean+(2*std_dev);
thirdStart , thirdEnd = mean-(3*std_dev),mean+(3*std_dev);

print("1st Standard Deviation is : ",firstStart,firstEnd)
print("2nd Standard Deviation is : ",secondStart,secondEnd)
print("3rd Standard Deviation is : ",thirdStart,thirdEnd)

fig = ff.create_distplot([meanList], ["student marks"], show_hist=False) 
fig.add_trace(o.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(o.Scatter(x=[firstStart, firstStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(o.Scatter(x=[firstEnd, firstEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(o.Scatter(x=[secondStart, secondStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(o.Scatter(x=[secondEnd, secondEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(o.Scatter(x=[thirdStart, thirdStart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(o.Scatter(x=[thirdEnd, thirdEnd], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show();