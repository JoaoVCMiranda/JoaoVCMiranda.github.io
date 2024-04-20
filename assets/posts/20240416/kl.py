import math
import matplotlib.pyplot as plt
import numpy as np

def char_dist(arq):
  # Modelo de distribuição
  D = [0]*(ord('Z')-ord('A')+1 + ord('z')-ord('a')+1 + ord('ƿ')-ord('À')+1)

  # Leitura do arquivo
  with open(arq, 'r') as p:
    for x,line in enumerate(p):
      for y,c in enumerate(line):
        # Capital
        if ('A'<=c<='Z'):
          D[ord(c)-ord('A')]+=1
        # Lowercase
        if('a'<=c<='z'):
          D[ord('Z')-ord('A')+1 +ord(c)-ord('a')]+=1
        # Latim Extended + European Latim
        if('À'<=c<='ƿ'):
          D[ord('Z')-ord('A')+1+ord('z')-ord('a')+1 +ord(c)-ord('À')]+=1

    # Normalização
    cte = sum(D)
    for i,x in enumerate(D):
      D[i] = x/cte
  return D

def entropia_relativa(Q,R):
  er = 0
  for i,q in enumerate(Q):
    if(q==0):
      er += 0
    elif(R[i]!=0):
      er += q*math.log2(q/R[i])

    else:
      return math.inf
  return er

def bin_dist(arq):
  D = [0,0]

  with open(arq, 'r') as p:
    for x,line in enumerate(p):
      for y,c in enumerate(line):
        # Capital + Lowercase
        if (('a'<=c<='z') or ('A'<=c<='Z')):
          # 0xxxxxxx
          D[0]+=1
          for x in format(ord(c),'b'):
            if(x == '0'):
              D[0]+=1
            else:
              D[1]+=1
        # Latim Extended + European Latim
        if ('À'<=c<='ƿ'):
          # 110xxxxx 10xxxxxx
          b = format(ord(c), 'b')

          D[0]+=2 + (11 - len(b))
          D[1]+=3
          for x in format(ord(c),'b'):
            if(x == '0'):
              D[0]+=1
            else:
              D[1]+=1
    # Normalização
    cte = sum(D)
    for i,x in enumerate(D):
      D[i] = x/cte
  return D

def plots(P, E,chars):

  plt.style.use('seaborn-v0_8-deep')
  #plt.style.use('dark_background')


  lw =0.25
  barP = np.arange(len(P))
  barP = [x+lw/2 for x in barP]
  barE = [x+lw for x in barP]

  fig = plt.figure(figsize = (10,5))
  plt.bar(barP,P,color='blue', width=0.25, label='alencar')
  plt.bar(barE,E,color='red',width=0.25, label='doyle')

  plt.xticks([x+lw for x in range(len(chars))], chars)

  plt.legend()
  plt.show()

if __name__ == "__main__":

  P = bin_dist('P.txt')
  E = bin_dist('E.txt')

  doyle = bin_dist('scarlet.txt')
  alencar = bin_dist('gazela.txt')
  #chars = []
  #for x in range(ord('A'), ord('Z')+1):
  #  chars.append(chr(x))
  #for x in range(ord('a'), ord('z')+1):
  #  chars.append(chr(x))
  #for x in range(ord('À'), ord('ƿ')+1):
  #  chars.append(chr(x))

  #limite = 52

  #P = P[:limite]
  #E = E[:limite]
  #chars = chars[:limite]
  #doyle = doyle[:limite]
  #alencar = alencar[:limite]




  print('D(P||E)=', entropia_relativa(P, E), 'bits')
  print('D(E||P)=', entropia_relativa(E, P), 'bits')

  print('D(doyle||alencar)=', entropia_relativa(doyle, alencar), 'bits')
  print('D(alencar||doyle)=', entropia_relativa(alencar, doyle), 'bits')

  print(doyle, alencar)



  plots(alencar,doyle,['0', '1'])
