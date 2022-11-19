import sys

print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

somelist = list('SPAM')
print(somelist)
print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, midle={2}'.format(*parts))