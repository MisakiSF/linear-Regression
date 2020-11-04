import numpy as np
import matplotlib.pyplot as plot

from matplotlib import style
from statistics import mean

style.use("ggplot")


x_dataset = np.array([1,2,3,4,5,4,5,3,3,4,4,3,3,4,4,2,4,2,4,2,4,2,4,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4])
y_dataset = np.array([2,3,4,2,3,4,4,4,4,4,4,4,3,2,2,3,3,4,4,3,3,3,4,4,5,5,3,3,3,2,2,2,2,2,2,8,8,9,8,])


#y = mx +b
#b = mean(y)- m* mean(x)
#m = mean(X) * mean(y) - mean(x*y)/ (mean(x))^2 - mean(x^2)

def slope():
    m = (((mean(x_dataset) * mean(y_dataset)) - (mean(x_dataset*y_dataset))) / ((mean(x_dataset))^2 - mean(x_dataset^2)))
    return m

def intercept():
    b = mean(y_dataset) - (slope() * mean(x_dataset))
    return b

m = slope()
b = intercept()


regression_line = [((m*x)+b) for x in x_dataset]

plot.scatter(x_dataset,y_dataset)
plot.plot(x_dataset,regression_line)
plot.show()
