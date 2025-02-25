#!/usr/bin/env Rscript

suppressPackageStartupMessages({
	library(data.table)
	library(DSS)
	require(bsseq)
})

args = commandArgs(trailingOnly=TRUE)
dmltest_path = args[1]
out_path = args[2]

dmltest = fread(dmltest_path,sep='\t')

#dmr = callDMR(dmltest, p.threshold=0.05, minlen = 0, minCG = 0)
dmr = callDMR(dmltest, p.threshold=0.01, minlen = 1, minCG = 1, pct.sig=0.5)
dmr = dmr[order(dmr$chr, dmr$start),]

write.table(dmr, file = out_path, quote = FALSE, sep = '\t', na = '', dec = ".", row.names = FALSE, col.names = FALSE, )


