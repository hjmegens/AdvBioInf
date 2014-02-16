import sys

line = sys.stdin.readline()[:-1]
coords = sys.stdin.readline()[:-1].split(' ')
print(coords)
print(line)
print(line[int(coords[0]):int(coords[1])+1],line[int(coords[2]):int(coords[3])+1])
