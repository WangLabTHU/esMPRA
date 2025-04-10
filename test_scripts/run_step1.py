import os

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
          --run_name {name} --use_flash')


# run quality control for step1
os.system(f'qc_step1 --run_name {name}')



#nohup time python run_step1_1.py > step1.log 2>&1 &