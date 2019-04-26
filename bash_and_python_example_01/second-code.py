#!/usr/bin/python

import numpy as np
import os, errno, sys


# Import parameter
tmax  = 10**int( sys.argv[1] )   



# Import data
nameIn = "generated-by-first-tmax%08d.dat"%(tmax)
vecin  = np.loadtxt( nameIn )



# Do something
vecOut = np.array( [ np.log10(tmax), len(vecin), np.mean(vecin), np.std(vecin)  ] )



#Export data
nameOut = "generated-by-second-tmax%08d.dat"%(tmax)
np.savetxt(nameOut, vecOut, delimiter = '  ' ,  fmt='%d')



# Lets see 
print("END of  nameIn:",nameIn, "   nameOut:",nameOut, "   log10",np.log10(tmax) )









