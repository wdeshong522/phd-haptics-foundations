import numpy as np

x = np.array([1,2,3,4])
h = np.array([1,0,-1])

# Manual Method
y=[]
for n in range(len(x)+len(h)-1):
    conv_sum = 0
    
    for k in range(n+1):
        if k<=len(h) and n-k>=0 and n-k < len(h):
            conv_sum = conv_sum+x[k]*h[n-k]
    y.append(conv_sum)
y = np.array(y)
print(y)

# Np Convolve Method
print(np.convolve(x,h))