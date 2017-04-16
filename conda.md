conda create -n tea_facts python=3

source activate tea_facts

conda install numpy pandas matplotlib

conda install jupyter notebook
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
