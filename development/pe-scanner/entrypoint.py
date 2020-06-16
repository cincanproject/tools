import pev
import sys

if len(sys.argv) < 2:
	print("give input file")
	sys.exit()

filu = sys.argv[1]
p = pev.Pev.pescan(filu)
pj = p.toJSON()
print(pj)
