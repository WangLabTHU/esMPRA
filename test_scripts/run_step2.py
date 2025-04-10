import os



#the run_name of this test
name = 'ENCFF074MMO_r1'
#the run_name of corresponding step1
name_step1 = 'ENCFF074MMO'
# multiple files can be processed together
os.system(f'step2_get_plasmid_counts \
          --read_1  ./ENCFF074MMO/plasmid/ENCFF850RIY.fastq.gz \
          --run_name {name} --position_mode --run_name_step1 {name_step1}')
# run quality control for step2
os.system(f'qc_step2 --run_name {name}')


# a parallel experiment
name = 'ENCFF074MMO_r2'
name_step1 = 'ENCFF074MMO'
os.system(f'step2_get_plasmid_counts \
          --read_1  ./ENCFF074MMO/plasmid/ENCFF944CEQ.fastq.gz \
          --run_name {name} --position_mode --run_name_step1 {name_step1}')



