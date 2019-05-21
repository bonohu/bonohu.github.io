Title: Running ikra
Date: 2019-05-21 18:00

Tried to use [ikra](https://github.com/yyoshiaki/ikra/).
SRR mode which directly fetches SRA file from NCBI worked fine, but FASTQ mode
was failed after trimming with the error below.
It seems that the file setting for salmon was incorrect.

```
Exception : [
The following errors were detected with the read files
======================================================
ERROR: file [fq/ERRxxxxxx_trimmed.fq.gz] does not appear to exist!

]
salmon quant was invoked improperly.
For usage information, try salmon quant --help
Exiting.
```

So, I made symlinks.

```
% cd fq
% ln -s ../*trimmed.fq.fz .
```

After this command,　I can continue ikra workflow.
 
