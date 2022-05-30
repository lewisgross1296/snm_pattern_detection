#!/bin/sh
#SBATCH --partition=pre
#SBATCH --time=1-00:00:00 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=128000
#SBATCH --error=snm_%J.err
#SBATCH --output=snm_%J.out
#SBATCH --constrain=avx2

unset HTTPS_PROXY
unset http_proxy
export TMPDIR=/home/ligross/tmp_scratch
singularity build frensie_hpc_at_N.simg docker://ligross/frensie_start_n:frensie_start_n