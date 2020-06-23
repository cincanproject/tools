import subprocess
from xml.dom import minidom

import pefile


class Pev:

    def __init__(self):
        return

    def __repr__(self):
        return None

    @staticmethod
    def version():
        p = subprocess.Popen("pescan -v", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print("Command output : ", output)
        print("Command exit status/return code : ", p_status)

    @staticmethod
    def pescan(path):
        pf = pefile.PeFile()

        p = subprocess.Popen(["pehash", path, "-f", "xml"], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        p_status = p.wait()

        xmldoc = minidom.parseString(output)
        attr = xmldoc.getElementsByTagName("attribute")
        hashes = [a.childNodes[0].nodeValue for a in attr]
        pf.sethashes(hashes[1], hashes[2], hashes[3], hashes[4], hashes[5])

        p = subprocess.Popen(["pescan", "-v", path, "-f", "xml"], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        p_status = p.wait()
        xmldoc = minidom.parseString(output)
        attr = xmldoc.getElementsByTagName("attribute")
        for a in attr:
            key = a.attributes['name'].value
            val = a.childNodes[0].nodeValue
            if key == u'file entropy':
                pf.entropy_class = val[val.find("(") + 1:val.find(")")]
                pf.file_entropy = val.split(" ")[0]

            elif key == u'fpu anti-disassembly':
                pf.fpu_anti_disas = val
            elif key == u'imagebase':
                pf.imagebase = val
            elif key == u'entrypoint':
                pf.entrypoint = val
            elif key == u'DOS stub':
                pf.DOS_stub = val
            elif key == u'TLS directory':
                pf.TLS_dir = val
            elif key == u'timestamp':
                pf.timestamp = val
            elif key == u'section count':
                pf.section_count = val

        attr = xmldoc.getElementsByTagName("object")
        sections = []
        for neighbor in attr:
            title = neighbor.getElementsByTagName("attribute")[0]
            sections.append((title.attributes['name'].value, title.childNodes[0].nodeValue))
        pf.sections = sections

        p = subprocess.Popen(["readpe", path, "-f", "xml"], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        p_status = p.wait()

        xmldoc = minidom.parseString(output)

        attr = xmldoc.getElementsByTagName("object")
        for obj in attr:
            sect = obj.attributes['name'].value
            if sect == u'Library':
                libs = obj.getElementsByTagName("attribute")
                fuc = libs
                for l in fuc[1:]:
                    pf.function_imports[libs[0].childNodes[0].nodeValue].append(l.childNodes[0].nodeValue)
        return pf
