import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
x = np.arange(start=1, stop = 15, step= 1)
y_liner = x + 5 * np.random.randn(14)
y_quadratic = x**2 + 10 *np.random.randn(14)
fn_linear = np.poly1d(np.polyfit(x, y_liner, deg=1))
fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic,deg= 2))

fig = plt.figure()
axi = fig.add_subplot(1,1,1)

axi.plot(x, y_liner, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth = 2)

axi.xaxis.set_ticks_position('bottom')
axi.yaxis.set_ticks_position('left')
axi.set_title('Scatter plots regression lines')

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim((min(x)-1., max(x)+1.))
plt.ylim((min(y_quadratic)-10., max(y_quadratic)+10.))

plt.savefig(r'test.jpg', dpi = 400, bbox_inches = 'tight')
plt.show()