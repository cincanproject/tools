import sys
#sys.path.append('/home/raulik/cincan/tools')
import pytest
from .. import cincan_tools

def test_image():
    cincan_tools.hello_world()
