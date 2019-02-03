Title: fasterq-dump
Date: 2019-02-02 21:00

I noticed the announcement in [NCBI's sra-tools GitHub wiki](https://github.com/ncbi/sra-tools/wiki)

> With release 2.9.1 of sra-tools we have finally made available the tool `fasterq-dump`, a replacement for the much older `fastq-dump` tool. 

So I tested the speed from my home.

1. Just specify a run ID of SRA.

```
# Just fasterq-dump
% fasterq-dump DRR100656
142.09s user 78.79s system 10% cpu 33:32.82 total
```
It takes about 33min.

2. Download SRA-formatted file from DDBJ DRA and dump it.

```
# Download SRA from DDBJ and then fasterq-dump
% curl -O ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/sra/ByExp/sra/DRX/DRX094/DRX094089/DRR100656/DRR100656.sra
% fasterq-dump DRR100657.sra
162.76s user 47.46s system 242% cpu 1:26.76 total
```

It takes around 5 min to download the file.
And the conversion from SRA to FASTQ takes 1.5 min.

It was much faster to fetch SRA and then dump it while we have to get the URLs to do so.
I regularly get the URLs for that from SRA download links in [DBCLS SRA](http://sra.dbcls.jp/).