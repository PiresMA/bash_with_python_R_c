#!/usr/bin/env Rscript
args  = commandArgs(TRUE)

xmax = 4*as.numeric(args[1])

# generate a sequence from 0 to xmax
myseq = seq(0,xmax,by=1)
print(myseq)

nameOUT=sprintf('sequence_with_xmax%02d.dat',xmax)
write.table( myseq, file=nameOUT,row.names=F,col.names=F)
