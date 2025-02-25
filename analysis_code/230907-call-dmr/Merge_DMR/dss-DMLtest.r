#!/usr/bin/env Rscript

suppressPackageStartupMessages({
    library(data.table)
    library(DSS)
    require(bsseq)
    })
    
    
args = commandArgs(trailingOnly=TRUE)
meta_path = args[1]
out_prefix = args[2]

meta = fread(meta_path, header=TRUE)

dfs = list()
for (i in seq_along(meta$allc_path)) {
    dfs[[i]] = fread(meta$allc_path[i], select = c(1,2,6,5), col.names=c('chr','pos','N','X'), showProgress = FALSE)
}

BSobj = makeBSseqData( dfs, meta$sample )


if(any(grepl("Rep", colnames(meta)))){
	design = meta[, c('CellType','Age','Rep')]
}else{
	design = meta[, c('CellType','Age')]
}

print(colnames(design))

DMLfit = DMLfit.multiFactor(BSobj, design=design, formula=~Age)
DMLtest.age = DMLtest.multiFactor(DMLfit, term='Age')

print('fitting finished')

print('writing results')
write.table(DMLtest.age, file = paste(out_prefix,'DMLtest.bed',sep='.'), quote = FALSE, sep = '\t',
            na = '', dec = ".", row.names = FALSE, )
print('done')
