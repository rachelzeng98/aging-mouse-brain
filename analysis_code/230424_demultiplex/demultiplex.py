from cemba_data.demultiplex.demultiplex import demultiplex_pipeline
import pathlib

fastq_dir = '/gale/netapp/seq2/illumina_runs/retr/220824_A00280_0582_BHF7VGDSX5_220829141054712279014/Pool_AMB67'

demultiplex_pipeline(
    fastq_pattern=f'{fastq_dir}/*.gz', 
    output_dir=pathlib.Path(fastq_dir).name, 
    config_path='mm10.hisat-3n.mapping_config.ini', 
    cpu=10, 
    aligner='hisat-3n'
)
