import matplotlib.pyplot as plt
import numpy as np

def gen_f_variable( N1, N2 ) : 
  samples1, samples2 = np.random.normal(size=N1), np.random.normal(size=N2)
  # Your code to generate the random variable described in the text goes here


  
# This code generates a 20 random variables using your function above and 
# plots them on a graph
xvals, yvals = np.linspace(0,20,20), np.zeros(20)
for i in range(20) : yvals[i] = gen_f_variable(5,6)

plt.plot( xvals, yvals, 'ko')
plt.savefig("variables.png")
