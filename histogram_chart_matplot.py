import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(1000)
x2 = mu2 + sigma*np.random.randn(1000)

fig = plt.figure()
axi = fig.add_subplot(1,1,1)
n, bins, batches = axi.hist(x1, bins = 50, normed=False, color='darkgreen')
n, bins, batches = axi.hist(x2, bins = 50, normed = False, color='orange', alpha = 0.3)
#bins = 50 means the value shoud be binned into 50 bins, alpha = 0,5 means the second histogram should be more transparent
#so we can see the dark green bars where the two histogras overlap

axi.xaxis.set_ticks_position('bottom')
axi.yaxis.set_ticks_position('left')

plt.xlabel('bins')
plt.ylabel('Number of value in bin')

fig.suptitle('Histogram', fontsize = 14, fontweight = 'bold')
axi.set_title('Two frequency distributions')

plt.savefig(r'histogram.jpg', dpi = 400, bbox_inches = 'tight')
plt.show()