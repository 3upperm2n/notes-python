conda create -n tf_cpu python=3

source activate tf_cpu

conda install numpy pandas matplotlib jupyter notebook

conda install -c conda-forge tensorflow


## remove env
```
conda-env remove -n YourEnvName
```

## search avail env and activate
```
conda env list
source activate dlnd-tf-lab
```

## show all the installed packages

conda list

## upgrade all packages

conda upgrade --all

## install package

conda install packageName

## specify package version

conda install packageName=1.01

## unintall / update a package

conda remove packageName

conda update packageName

## search package

conda search packageName

## install a package from a channel

conda install -c channel_name packageName
