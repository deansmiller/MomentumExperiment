__author__ = 'deansmiller'


data = open("data/GL/2013-14.csv").readlines()
x = []
for line in data:
    x.append(line.split(",")[:6])

print x


