"""Path hack to make tests work."""

import os
import sys

base_path = os.path.dirname(os.path.realpath('.')).split(os.sep)
module_path = os.sep.join(base_path + ['utils'])
sys.path.insert(0, module_path)
