#!/usr/bin/python

import numpy as np
import os, errno, sys


# Import parameter
tmax  = 10**int( sys.argv[1] )   



# Do something
vecOut = np.arange(1,tmax+1,1)



# Export 
nameOut = "generated-by-first-tmax%08d.dat"%(tmax)
np.savetxt(nameOut, vecOut, delimiter = '  ' ,  fmt='%d')



# Lets see 
print("END of",nameOut, "   log10",np.log10(tmax) )

