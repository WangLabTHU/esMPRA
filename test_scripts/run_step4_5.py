import os


#the run_name of this test
name = 'ENCFF074MMO_A549_r1'
#the run_names of previous steps
name_step1 = 'ENCFF074MMO'
name_step2 = 'ENCFF074MMO_r1'
name_step3 = 'ENCFF074MMO_A549_r1'
os.system(f'step4_get_result --ref_fa ./ENCFF074MMO/fasta/ENCFF074MMO.fasta.gz \
            --run_name_step1 {name_step1} \
            --run_name_step2 {name_step2} \
            --run_name_step3 {name_step3} \
            --run_name {name}')

# run quality control for step4
os.system(f'qc_step4 --run_name {name}')


# a parallel experiment
name = 'ENCFF074MMO_A549_r2'
name_step1 = 'ENCFF074MMO'
name_step2 = 'ENCFF074MMO_r2'
name_step3 = 'ENCFF074MMO_A549_r2'
os.system(f'step4_get_result --ref_fa ./ENCFF074MMO/fasta/ENCFF074MMO.fasta.gz \
            --run_name_step1 {name_step1} \
            --run_name_step2 {name_step2} \
            --run_name_step3 {name_step3} \
            --run_name {name}')


#the run_name of this test
name = 'ENCFF074MMO_A549'
# the run_names of step4 for comparision
# multiple names can be processed together, and the program will automatically perform pairwise comparisons.
name_step4_r1 = 'ENCFF074MMO_A549_r1'
name_step4_r2 = 'ENCFF074MMO_A549_r2'
os.system(f'step5_compare_diff_rep  --run_name {name} \
          --run_name_step4 {name_step4_r1} {name_step4_r2}')

