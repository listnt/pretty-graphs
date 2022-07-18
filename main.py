import numpy as np

def dropPercentile(q,a):
    l= int(len(a) /100  *(((100-q)/2)))
    r = int(len(a)-1-len(a)/100 * ((100-q)/2))
    return a[l:r:1]

mu, sigma = 2, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
s.sort()
s95 = dropPercentile(95,s)
s99 = dropPercentile(99,s)

e=np.array([x for x in s if x > 0.5])
e95 = dropPercentile(95,e)
e99 = dropPercentile(99,e)

x = np.array([t for t in s if t >1])
x95 = dropPercentile(95,x)
x99 = dropPercentile(99,x)

datas=[
    (s,100,0),
    (s95,95,0),
    (s99,99,0),
    (e,100,0.5),
    (e95,95,0.5),
    (e99,99,0.5),
    (x,100,1),
    (x95,95,1),
    (x99,99,1)]
colors = ['y','tab:orange','r','k']


import matplotlib.pyplot as plt
fig,axs = plt.subplots(3,3)

for i in range(0,3):
    for j in range(0,3):
        axs[j,i].set_facecolor('xkcd:turquoise')
        count, bins, ignored = axs[j,i].hist(datas[i*3+j][0], 20,edgecolor=colors[3],fc=colors[i])
        label = axs[j,i].set_xlabel(
            "cutout " + '%.1f'%datas[i*3+j][2]+"\n"+
            "confident "+'%d'%datas[i*3+j][1]+"\n"+
            "std " + '%.3f'%np.std(datas[i*3+j][0])+"\n"+
            "median "+ '%.3f'%np.mean(datas[i*3+j][0])+"\n"+
            "sum " + '%.3f'%np.sum(datas[i*3+j][0]),
            fontsize = 9, c='xkcd:plum'
            )
        axs[j,i].xaxis.set_label_coords(0.1, 1)


plt.show()
