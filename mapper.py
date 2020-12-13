import matplotlib.pyplot as plt

hfont = {'fontname':'Montserrat'}

# draw a simple line chart showing population growth over last 115 years

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960]
pops = [1, 6, 11, 2, 6, 4, 2, 19]

# plot our chart with the data above, and also format the line color and width

plt.plot(years, pops, color=(255/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("Gold Medals Won by USA in Winter Olympics", **hfont, labelpad=20)
plt.xlabel("Olympic Year", **hfont, labelpad=20)

# add title to chart

plt.title("Gold Medals Won by USA in Winter Olympics by Year", pad='20', **hfont)

# run the show method
# this generates graphic in new window
plt.show()