import os

#####################################################################
#code for step1

#the run_name of this test
name = 'ENCFF074MMO'

# run step1 to map the oligo and barcode sequences
# multiple files can be processed together
# the order of the read_1 files and the read_2 files should correspond to each other
os.system(f'step1_oligo_barcode_map \
          --ref_fa ./ENCFF074MMO/fasta/ENCFF074MMO.fasta.gz \
          --read_1 ./ENCFF074MMO/oligo_barcode/ENCFF235LUE.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF708MPZ.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF381TUK.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF847HXK.fastq.gz \
          --read_2 ./ENCFF074MMO/oligo_barcode/ENCFF215NWC.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF317FNS.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF504ZPY.fastq.gz \
          ./ENCFF074MMO/oligo_barcode/ENCFF420UFL.fastq.gz \
          --run_name {name} --oligo_length 200')

# run quality control for step1
os.system(f'qc_step1 --run_name {name}')


#####################################################################
#code for step2

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


#####################################################################
#code for step3

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

#####################################################################
#code for step4

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

#####################################################################
#code for step5

#the run_name of this test
name = 'ENCFF074MMO_A549'
# the run_names of step4 for comparision
# multiple names can be processed together, and the program will automatically perform pairwise comparisons.
name_step4_r1 = 'ENCFF074MMO_A549_r1'
name_step4_r2 = 'ENCFF074MMO_A549_r2'
os.system(f'step5_compare_diff_rep  --run_name {name} \
          --run_name_step4 {name_step4_r1} {name_step4_r2}')



