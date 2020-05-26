#!/usr/bin/env Rscript
args = commandArgs(TRUE)

xmax = 4*as.numeric(args[1])

nameIN = sprintf('sequence_with_xmax%02d.dat',xmax)
array  = as.vector( data.matrix(read.table(nameIN)) )

print( array )
print( sprintf( 'mean value:%1.2f',mean(array)  )  )

