
import sys
import requests
import json

if len(sys.argv) > 1:
        url = 'https://www.pdfexaminer.com/pdfapi.php'
        file_to_send = sys.argv[1]
        files = {'sample[]': open(file_to_send, 'rb')}
        print ("Sending >> " + file_to_send + " <<")

        # Summary (-s) or set output format
        if len(sys.argv) > 2:
                if sys.argv[2] != '-s':
                        datatype = {'type':sys.argv[2]}
                else:
                        datatype = {'type':'json'}
        else:
                datatype = {'type':'json'}

        # Post request
        r = requests.post(url, files=files, data=datatype)

        # If -s set, show only summary
        if len(sys.argv) > 2 and sys.argv[2] == '-s':
                j = json.loads(r.text.strip())
                print ("\nSummary: " + j['summary'] + "\nIs malware:" + j['is_malware'])
        else:
                print(r.text.strip())
else:
        print ("Usage:    [pdf file] [options]\nOptions:\n json\n xml \n ioc\n php\n severity\n rating\n is_malware\n text\n summary (-s)\n ")

