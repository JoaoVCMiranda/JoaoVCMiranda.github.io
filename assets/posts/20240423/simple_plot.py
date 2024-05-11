import numpy as np
import matplotlib.pyplot as plt

X = [x for x in range(10)]
Sa = [2*x for x in range(10)]
St = [5+x for x in range(10)]

#plt.style.use('dark_background')

fig = plt.figure(figsize = (10, 10))

plt.axis('off')

plt.plot(X, Sa, label='Achilles')
plt.plot(X, St, label='Tortoise')
plt.legend()
plt.show()
