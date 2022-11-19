template = '{0}, {1} and {2}'                                   #по позиціях
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'                         #по ключовим словам
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'                            #по позиціях і ключових словах
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}'                                      #по відносним позиціям
print(template.format('spam', 'ham', 'eggs'))

print('{motto}, {0} and {food}'.format(42, motto = 3.14, food=[1,2]))

X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1,2])
print(X)

print(X.split(' and '))
Y = X.replace('and', 'but under no circumstances')
print(Y)