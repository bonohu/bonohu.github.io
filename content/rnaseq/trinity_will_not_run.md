Title: Trinity will not run
Date: 2018-06-06 17:00

After some software updates, Trinity ended with error below.

> dyld: Library not loaded: /usr/local/opt/gcc/lib/gcc/7/libgomp.1.dylib                                    
> Referenced from: /usr/local/Cellar/trinity/2.5.1/util/..//Inchworm/bin/fastaToKmerCoverageStats
> Reason: image not found

I checked the file `/usr/local/opt/gcc/lib/gcc/7/libgomp.1.dylib`, and found that there was no directory termed `7` in `/usr/local/opt/gcc/lib/gcc/`, only the directory termed `8`. And there was `libgomp.1.dylib` in old version of gcc library, thus I made a sim-link to that.

```
% cd /usr/local/opt/gcc/lib/gcc/
% ln -s ../../../7.3.0_1/lib/gcc/7 .
```

It is okay now, but I also found that Trinity version 2.5.1 is not the latest one as of June 2018 (the latest version is 2.6.6). I should try newer version of Trinity! 
