import json
from collections import defaultdict


class PeFile:
    """
    This class is a collection of features for a single PE file.

    It is intended for curating the outputs of various tools, and
    if necessary enable swapping of the underlying implementation
    without breaking the rest of the script.

    """

    def __init__(self):
        # Hashes
        self.md5 = None
        self.sha1 = None
        self.sha256 = None
        self.ssdeep = None
        self.imphash = None

        # PEscan stuff
        self.file_entropy = None
        self.entropy_class = None
        self.fpu_anti_disas = None
        self.imagebase = None
        self.entrypoint = None
        self.DOS_stub = None
        self.TLS_dir = None
        self.timestamp = None
        self.section_count = None
        self.sections = []

        # readpe stuff
        self.function_imports = defaultdict(list)
        # self.full_analysis_raw_xml = None

        return

    def __repr__(self):
        return "{}:{}".format(self.__class__.__name__, self.md5)

    def sethashes(self, md5, sha1, sha256, ssdeep, imphash):
        """
        Sets the hashes for this PE feature collection.
        :param md5:
        :param sha1:
        :param sha256:
        :param ssdeep:
        :param imphash:
        :return:
        """

        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256
        self.ssdeep = ssdeep
        self.imphash = imphash

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
