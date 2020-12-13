import matplotlib.pyplot as plt
import numpy

def absolute_value(val):
    a  = numpy.round(val/100.*sizes.sum(), 0)
    return a

labels = ['Gold', 'Silver', 'Bronze']
sizes = numpy.array([36,10,14])
colors = ['gold', 'silver', 'olive']
fig1, ax1 = plt.subplots()

ax1.pie(sizes, colors=colors, autopct=absolute_value,
        shadow=False, startangle=0)
        
plt.axis('equal')
plt.tight_layout()

plt.show()

