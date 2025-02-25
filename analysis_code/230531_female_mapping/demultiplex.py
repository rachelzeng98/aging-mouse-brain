from cemba_data.demultiplex.demultiplex import demultiplex_pipeline
import pathlib

fastq_dir = '/gale/netapp/seq12/illumina_runs/220616_A00280_0554_AH2G3CDSX5_220622111731888176493/Pool_AMB38_mm'
output_dir = '/ceph/gale-1/qzeng'

demultiplex_pipeline(
    fastq_pattern=f'{fastq_dir}/*.gz', 
    output_dir= f'{output_dir}/{pathlib.Path(fastq_dir).name}', 
    config_path='mm10.hisat-3n.mapping_config.ini', 
    cpu=10, 
    aligner='hisat-3n'
)
