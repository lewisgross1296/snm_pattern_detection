# Run the batching script with
`sbatch snm-submit.sh`
# Restart the simulation with 
`sbatch snm-restart-submit.sh`
# This is the command used to write data to CSV for each detector. This has 
# changed to become one command and have the write script loop over estimators 
# and entity IDS to write the results in each detector
`./snm-write-data.py --rendezvous_file="snm_rendezvous_8.xml" --NPS="6E10" --HEU_X="0" --HEU_Y="0" --HEU_Z="0"`
