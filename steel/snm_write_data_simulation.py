import os
import sys
from datetime import date
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager

def writeSNMSimulationSpectrum( rendezvous_file,
                                  estimator_id,
                                  entity_id,
                                  HEU_X,
                                  HEU_Y,
                                  HEU_Z):

    # Activate just-in-time initialization to prevent automatic loading of the
    # geometry and data tables
    Utility.activateJustInTimeInitialization()

    # Reload the simulation
    manager = Manager.ParticleSimulationManagerFactory( rendezvous_file ).getManager()
    
    # Extract the estimator of interest from FRENSIE
    estimator = manager.getEventHandler().getEstimator( estimator_id )

    entity_bin_data = estimator.getEntityBinProcessedData( entity_id )
    entity_bin_data["e_bins"] = estimator.getTimeDiscretization()


    # create CSV output file
    file_name = "snm_results_"
    today = date.today().strftime("%b-%d-%Y")
    file = open(file_name + today + ".csv","w+")
    # Write the HEU position at the top of the file
    file.write("HEU X" + "," + "HEU Y" + "," + "HEU Z" "\n")
    file.write(HEU_X + "," + HEU_Y + "," +  HEU_Z + "\n")
    file.write("time bin upper bound" + "," + "flux mean" + "," + "flux RE"+ "\n")
    # Write FRENSIE results to CSV forrmat
    for i in range(0,len(entity_bin_data["mean"])):
        file.write(str(entity_bin_data["e_bins"][i+1]) + "," +  str(entity_bin_data["mean"][i]) + "," + str(entity_bin_data["re"][i]) +"\n")
    file.close()
