Title: Align and estimate abundance
Date: 2018-03-07 12:00


If assembled transcriptome sequence set and RNA-seq reads for that are available for an organism, we can align reads and estimate transcript abundance by running the script (`align_and_estimate_abundance.pl`) in the Trinity software package. When the Trinity package was installed using Homebrew, that script is installed in `/usr/local/Cellar/trinity/2.5.1/util` where `2.5.1` is the version of Trinity.

For that process, we can now use  [`kallisto`](https://pachterlab.github.io/kallisto/) for transcript quantification in the latest version of Trinity (v2.5.1). It cannot be installed from bioconda now in macOS platform, and this version of Trinity was installed utilizing Homebrew.

Shell script to run that script is something like this.

```
#!/bin/sh
thre=4
transcript=IACV01.1.fsa_nt.gz
left=DRR118520_1_val_1.fq.gz
right=DRR118520_2_val_2.fq.gz
# parameters to run above
time /usr/local/Cellar/trinity/2.5.1/util/align_and_estimate_abundance.pl \
--thread_count $thre \
--transcripts $transcript \
--seqType fq \
--left  $left \
--right $right \
--est_method kallisto \
--kallisto_add_opts "-t $thre" \
--prep_reference --output_dir kallisto_out
```

This command above is for **paired-end** sequence.
