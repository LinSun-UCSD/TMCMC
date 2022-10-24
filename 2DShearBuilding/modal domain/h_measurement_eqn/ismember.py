from typing import List

import numpy as np


def ismember(d, k):
    return [True if (i in k) else False for i in d]
