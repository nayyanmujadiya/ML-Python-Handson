import matplotlib.pyplot as plt

#Pie chart, where the slices will be ordered and ploted counter-clockwise:

labels = 'Frogs','Hogs','Dogs','Logs'

sizes = [15,30,45,10]

explode = (0,0.1,0,0) # only "expload" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()

ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%')

ax1.axis('equal') # Equal aspect ration ensure that pie is drawn as a circle

plt.show()
