#!/bin/sh
#SBATCH --partition=cnerg
#SBATCH --time=7-00:00:00 
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=5
#SBATCH --cpus-per-task=4
#SBATCH --mem=128000
#SBATCH --error=snm_%J.err
#SBATCH --output=snm_%J.out
#SBATCH --constrain=avx2
#SBATCH --begin=00:47:00


# build command
# FIRST LOG INTO AN INTERACTIVE NODE: srun -n1 -N1 -p int --pty bash
# may possibly need to unset the two below environemnt variables
# unset HTTPS_PROXY
# unset http_proxy

# BUILD SINGULARITY IMAGE FROM DOCKERHUB IMAGE
# singularity build frensie_hpc.simg docker://ligross/frensie_hpc:frensie_stable 

#BIND path to shared data in dagmc group
BIND_PATH=/software/groups/dagmc/opt/misc/MCNP/MCNP_DATA
module load openmpi
mpirun -np $SLURM_NTASKS singularity exec --bind ${BIND_PATH}:${BIND_PATH} frensie_hpc.simg python snm-restart.py --threads=$SLURM_CPUS_PER_TASK --rendezvous_file="snm_rendezvous_17.xml"
