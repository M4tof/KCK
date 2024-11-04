from pylab import *
from numpy import *
import math
from ipywidgets import *

labels = []

t = np.arange(0, 1*1/2, 1/50) # Momenty, w których pobieramy próbki (oś OX)
n = len(t)                 # Liczba próbek

labels = np.linspace(0,50,25)

print(labels)