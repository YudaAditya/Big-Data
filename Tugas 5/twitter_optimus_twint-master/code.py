# from IPython import get_ipython
# ipython = get_ipython()

# if '__IPYTHON__' in globals():
#     ipython.magic('load_ext autoreload')
#     ipython.magic('autoreload 2')

    
import sys
sys.path.append("twint/")

import twint

from optimus import Optimus
op = Optimus()

# Set up TWINT config
c = twint.Config()

# Solve compatibility issues with notebooks and RunTime errors.

c.Search = "data science"
# Custom output format
c.Format = "Username: {username} |  Tweet: {tweet}"
c.Limit = 1
c.Pandas = True
twint.run.Search(c)
