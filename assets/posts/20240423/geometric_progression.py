import numpy as np
import matplotlib.pyplot as plt



rang = 6

X = [x for x in range(rang)]
Sa = [2*x for x in range(rang)]
St = [5+x for x in range(rang)]

SaI = [x/2 for x in range(rang)]
StI = [x-5 for x in range(rang)]

#plt.style.use('dark_background')

fig = plt.figure(figsize = (10, 10))

#plt.axis('off')

plt.plot(X, Sa, label='Achilles')
plt.plot(X, St, label='Tortoise')

for i,x in enumerate(X):
  # Vertical Lines
  plt.plot((x,Sa[i]),(x,St[i]), color='red')
  print((x,Sa[i]),(x,St[i]))
  # Horizontal Lines
  plt.plot((SaI[i],St[i]),(StI[i],St[i]), color='black')
  print((SaI[i],St[i]),(StI[i],St[i]))


plt.legend()
plt.show()

