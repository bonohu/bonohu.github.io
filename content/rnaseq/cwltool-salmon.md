Title: Running salmon via CWL
Date: 2019-06-28 11:00

If a transcriptome sequence set is available for the organism, [salmon](https://combine-lab.github.io/salmon/) can be used for transcript quantification.
`cwltool` must be installed in advance by `conda install cwltool` or `pip install cwltool`.

```
#!/bin/sh
# number of threads to use
p=6
# workspace: Donwloads directory
cd ~/Downloads/
# git clone pitagora-cwl
git clone https://github.com/pitagora-network/pitagora-cwl
# retrieve human reference transcriptome
curl -O ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_30/gencode.v30.transcripts.fa.gz
# make salmon index
cwltool pitagora-cwl/tools/salmon/index/salmon_index.cwl \
--nthreads $p --index_name Human_gencode_salmon \
--transcript_fasta gencode.v30.transcripts.fa.gz 
# run salmon quant
for srr in DRR100656 DRR100657; do
  cwltool pitagora-cwl/tools/salmon/quant/paired_end/salmon_quant_pe.cwl \
  --fq1 ${srr}_1_val_1.fq.gz --fq2 ${srr}_2_val_2.fq.gz \
  --index_dir Human_gencode_salmon --nthreads $p \
  --quant_out_dir ${srr}_salmon_quant
  done
```

This command above is for **paired end** sequence.
