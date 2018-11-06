Title: CellFishing
Date: 2018-11-06 21:00

I tried to use [CellFishing](https://doi.org/10.1101/374462) written in [Julia](https://julialang.org). 
It was my first time to use Julia, so I started from the installation of Julia with Homebrew.

```
# Install Julia
brew cask install julia
# Install CellFishing
julia -e 'using Pkg; Pkg.add(PackageSpec(url="git://github.com/bicycle1885/CellFishing.jl.git"))'
# Run test for CellFishing
julia -e 'using Pkg; Pkg.test("CellFishing")'
```

After installing julia, I followed the instruction in [CellFishing](https://github.com/bicycle1885/CellFishing.jl) website, but the test code was failed. 
According to CellFishing developer, the reason for that failure was that `zstd` was missing. So I installed `zstd`.

```
# Install zstd via Homebrew
brew install -v zstd
```

And I tried command-line interface for CellFishing.
Some packages (`HDF5` and `DocOpt`) were requred to run `cellfishing build` command.

```
# Install required packages in julia
julia -e 'using Pkg; Pkg.add("HDF5")'
julia -e 'using Pkg; Pkg.add("DocOpt")'
```

Of course, data for the search was required. It could be downloaded from 
http://bimsbstatic.mdc-berlin.de/rajewsky/PSCA/all_sgete_4GU75.loom.gz liked from [Planaria Single Cell Atlas website](https://shiny.mdc-berlin.de/psca/).

```
# Getting data for the search
curl -O http://bimsbstatic.mdc-berlin.de/rajewsky/PSCA/all_sgete_4GU75.loom.gz 
gzip -dc all_sgete_4GU75.loom.gz > Plass2018.dge.loom
```

After getting the file, I successfully ran the code!

```
# Run CellFishing
./bin/cellfishing build Plass2018.dge.loom
./bin/cellfishing search Plass2018.dge.loom.cf Plass2018.dge.loom >neighbors.tsv
```
