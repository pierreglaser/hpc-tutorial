# Instructions to launch `Python` experiences on a `slurm` cluster

This file contains the necessary bash commands to setup an environment where
`joblib`/`dask`/`jupyter` are installed so that you can run the tutorial
notebooks.

## Install miniconda on your machine

```bash
mkdir -p "$HOME/.local"
# Download and run the miniconda installer. Skip this part if conda is already
# installed on your system.
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/.local/miniconda3

# Activate for every login shell:
echo 'source $HOME/.local/miniconda3/etc/profile.d/conda.sh
conda activate
' >> $HOME/.profile
source $HOME/.profile
```

## Create a conda environment

```bash
# Create an isolated conda environment for this tutorial
conda create -y -n slurm-tutorial python=3.7
conda activate slurm-tutorial

# Side note: conda is great because it is more than a python package manager:
# it is a binary package manager - you can for example install gcc using:
# `conda install gcc`. Very helpful when you're not root on the machine you're
# using.

# Install jupyter
conda install -y jupyter
```

### Install the requirements fot the "joblib on your local machine" tutorial

To run the "joblib on your local machine" tutorial, you simply need to install
joblib
```bash
conda install -y joblib
bash
```

### Install the requirements fot the "joblib on your local machine" tutorial
To run the "joblib+dask on slurm" tutorial, you need distributed and
dask-jobqueue.
```bash
conda install -y distributed dask-jobqueue joblib
```

## Clone the tutorial and launch the notebooks

```bash
cd $HOME
git clone https://github.com/pierreglaser/hpc-tutorial
cd hpc-tutorial
jupyter-notebook joblib_tutorial.ipynb
```
