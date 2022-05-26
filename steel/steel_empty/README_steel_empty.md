# Run the batching script with
`sbatch snm-submit.sh`
# Restart the simulation with 
`sbatch snm-restart-submit.sh`
# This is the command used to write data to CSV for each detector. This has 
# changed to become one command and have the write script loop over estimators 
# and entity IDS to write the results in each dls -etector
`./snm-write-data.py --rendezvous_file="snm_rendezvous_78.xml" --NPS="55E10" --HEU_X="empty" --HEU_Y="" --HEU_Z=""`