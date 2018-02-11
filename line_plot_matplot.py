import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

plot_data1= np.random.randn(50).cumsum()
plot_data2= np.random.randn(50).cumsum()
plot_data3= np.random.randn(50).cumsum()
plot_data4= np.random.randn(50).cumsum()

fig = plt.figure()
axi = fig.add_subplot(1,1,1)

axi.plot(plot_data1, marker = r'o', color=u'blue', linestyle = '-', label= 'Blue Solid')
axi.plot(plot_data2, marker = r'+', color=u'red', linestyle = '--', label= 'Red Dashed')
axi.plot(plot_data3, marker = r'*', color=u'green', linestyle = '-.', label= 'Green Dash Dot')
axi.plot(plot_data4, marker = r's', color=u'orange', linestyle = ':', label= 'Orange Dotted')
#label arguments ensure the lines are properly labeled in the legend

axi.xaxis.set_ticks_position('bottom')
axi.yaxis.set_ticks_position('left')
axi.set_title('Line plots: Markers, Colors, and Linestyles')

plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc = 'best') #place the legend in the best location based on the open space in the plot

plt.savefig(r'test.jpg', dpi = 400, bbox_inches = 'tight')
plt.show()

