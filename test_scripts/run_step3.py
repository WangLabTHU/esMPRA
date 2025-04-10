import os



#the run_name of this test
name = 'ENCFF074MMO_A549_r1'
#the run_name of corresponding step1
name_step1 = 'ENCFF074MMO'
# multiple files can be processed together
os.system(f'step3_get_RNA_counts \
        --read_1 ./ENCFF074MMO/count_A549/ENCFF554OMB.fastq.gz \
        --run_name {name} --position_mode --run_name_step1 {name_step1}')
# run quality control for step3
os.system(f'qc_step3 --run_name {name}')


# a parallel experiment
name = 'ENCFF074MMO_A549_r2'
name_step1 = 'ENCFF074MMO'
os.system(f'step3_get_RNA_counts \
        --read_1 ./ENCFF074MMO/count_A549/ENCFF061UCM.fastq.gz \
        --run_name {name} --position_mode --run_name_step1 {name_step1}')