import os
import sys

root = os.path.dirname(__file__)
pythonpath = os.path.join(root, "python")
sys.path.insert(0, pythonpath)

from rezutil import _rezbuild
_rezbuild.main([root])
