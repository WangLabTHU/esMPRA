import os

os.system(f'generate_data_for_MPRAnalyse \
          --step1_dir  ./ENCFF074MMO_step1 \
          --step2_dir  ./ENCFF074MMO_r1_step2 \
          --step3_dir  ./ENCFF074MMO_A549_r1_step3 \
          --run_tag rep1')

os.system(f'generate_data_for_MPRAnalyse \
          --step1_dir  ./ENCFF074MMO_step1 \
          --step2_dir  ./ENCFF074MMO_r2_step2 \
          --step3_dir  ./ENCFF074MMO_A549_r2_step3 \
          --run_tag rep2')
