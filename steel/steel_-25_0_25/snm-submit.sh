#!/bin/sh
#SBATCH --partition=pre
#SBATCH --time=1-00:00:00 
#SBATCH --nodes=16
#SBATCH --ntasks-per-node=5
#SBATCH --cpus-per-task=4
#SBATCH --mem=120000
#SBATCH --error=snm_%J.err
#SBATCH --output=snm_%J.out
#SBATCH --constrain=avx2


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
mpirun -np $SLURM_NTASKS singularity exec --bind ${BIND_PATH}:${BIND_PATH} frensie_hpc.simg python snm.py --sim_name="snm" --num_particles=11e10 --threads=$SLURM_CPUS_PER_TASK --db_path=${BIND_PATH}/database.xml

# -np $SLURM_NTASKS has mpi create $SLURM_NTASKS copies of the program and MPI handles the data
# transfering between nodes and the process 0 node 

###############################################################################
# RESOURCE EXPLANATION
# --nodes=2 #how many nodes, each containing 20 cpus do you want
# --ntasks-per-node=5 # number of tasks(threads) per cpu
# --cpus-per-task=4 # need cpus per task * ntasks per node needs to be 20 (or as close but under 20 as possible) so that we don't waste any threads in a node