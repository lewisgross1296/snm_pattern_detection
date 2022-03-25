# Run the batching script with
`sbatch snm-submit.sh`
# Restart the simulation with 
`sbatch snm-restart-submit.sh`
# These are the commands used to write data to CSV for each detector. The estimator id corresponds to the ID attached during the problem definition. The entity id corresonds to the volume number in the geometry model that the estimator lives in
`./snm-write-data.py --rendezvous_file="snm_rendezvous_1.xml" --estimator_id=1 --entity_id=4 --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`
`./snm-write-data.py --rendezvous_file="snm_rendezvous_1.xml" --estimator_id=2 --entity_id=5 --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`
`./snm-write-data.py --rendezvous_file="snm_rendezvous_1.xml" --estimator_id=3 --entity_id=6 --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`
`./snm-write-data.py --rendezvous_file="snm_rendezvous_1.xml" --estimator_id=4 --entity_id=7 --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`
`./snm-write-data.py --rendezvous_file="snm_rendezvous_1.xml" --estimator_id=5 --entity_id=8 --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`