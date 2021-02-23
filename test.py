import pandas as pd
import plotly.express as px
import csv
import math

with open('data.csv','r') as f:
  reader = csv.reader(f)
  filedata = list(reader)

data = filedata.pop(0)
newData = []
for i in range(len(filedata)):
  newNumber = filedata[i][1]
  newData.append(float(newNumber))

n = len(newData)
total = 0
for x in newData:
  total+=x

mean = total/n
print(newData)

df = pd.read_csv('data.csv')
fig = px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes = [dict(
    type = "line",
    y0 = mean,
    y1 = mean,
    x0 = 0,
    x1 = n
)])
fig.show()

def mean(data):
  n = len(data)
  total = 0
  for x in data:
    total+= int(x)
  mean = total/n
  return mean

squaredList = []
for number in newData:
  a = float(number)-mean(newData)
  a = a**2
  squaredList.append(a)

sum = 0
for i in squaredList:
  sum = sum+i

result = sum/(len(newData)-1)
standardDaviation = math.sqrt(result)
print(standardDaviation)