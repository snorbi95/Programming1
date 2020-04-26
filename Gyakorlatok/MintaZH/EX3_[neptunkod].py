import numpy as np

vec = np.random.randint(1,101,size=10)
avg = np.average(vec)
dist = np.abs(vec - avg)
dist[dist < 10] = 0

print("Vektor: {}".format(vec))
print("Vektor atlaga: {}".format(avg))
print("Eredmeny vektor: {}".format(dist))