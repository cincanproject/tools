import exiftool
import subprocess,json
from xml.dom import minidom
import magic
import sys
import ssdeep
import hashlib

outdict = {}


filu = sys.argv[1]
ef = exiftool.ExifTool() 
try:
	ef.start()
	js = ef.get_metadata(filu)
	ef.terminate()
	outdict["exiftool"] = js


except:
	pass


try:
	mag = magic.from_file(filu)
	outdict["magic"] = mag
except:
	pass

try:
	p = subprocess.Popen(["trid", filu], stdout=subprocess.PIPE)
	(output, err) = p.communicate()
	p_status = p.wait()
	lines = output.split('\n')[6:]
	preds = []
	for l in lines:
		if len(l.strip()) > 0:
			preds.append(l.strip())

	outdict["trid"]=preds
except:
	pass

try:
	outdict["hashes"]=[{"ssdeep":ssdeep.hash_from_file(filu)}]
except:
	pass

try:	
	print(json.dumps(outdict))
except:
	pass



