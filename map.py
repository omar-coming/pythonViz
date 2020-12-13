import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4
silver_usa = (10, 4, 38, 31)
gold_usa = (1, 19, 11, 10)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, gold_usa, bar_width,
alpha=opacity,
color='r',
label='Gold')

rects2 = plt.bar(index + bar_width, silver_usa, bar_width,
alpha=opacity,
color='b',
label='Silver')

plt.xlabel('Year')
plt.ylabel('Medal Count')
plt.title('Count by Year')
plt.xticks(index + bar_width, ('1924', '1960', '2002', '2014'))
plt.legend()

plt.tight_layout()
plt.show()