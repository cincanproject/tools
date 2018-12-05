import pev
import sys

filu = sys.argv[1]
p = pev.Pev.pescan(filu)
pj = p.toJSON()
print(pj)
