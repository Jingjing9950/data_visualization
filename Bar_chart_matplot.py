import matplotlib.pyplot as plt
plt.style.use('ggplot')

customers = ['ad','df','fg','rt']
customer_index = range(len(customers))
amount = ['10','25','15','5']
bar_width = 0.4

fig = plt.figure()
axi = fig.add_subplot(2,1,1)
axi.bar(customer_index,amount,bar_width,align='center',color='black')
axi.xaxis.set_ticks_position('bottom')
axi.yaxis.set_ticks_position('left')
plt.xticks(customer_index,customers,rotation =0, fontsize='20')
plt.xlabel('customer Name')
plt.ylabel('Sales Amount')
plt.title('Sales amount per customer')
plt.savefig(r'test.jpg', dpi = 400, bbox_inches = 'tight')
plt.show()