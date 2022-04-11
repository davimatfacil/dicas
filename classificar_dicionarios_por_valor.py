
#Como classificar um dict Python por valor

# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

#Forma 1
sorted(xs.items(), key=lambda x: x[1])



#Forma 2
import operator
sorted(xs.items(), key=operator.itemgetter(1))
