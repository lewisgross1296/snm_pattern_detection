import os
import sys
from datetime import date
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager

def writeSNMSimulationSpectrum(   rendezvous_file,
                                  NPS,
                                  HEU_X,
                                  HEU_Y,
                                  HEU_Z):

    # Activate just-in-time initialization to prevent automatic loading of the
    # geometry and data tables
    Utility.activateJustInTimeInitialization()

    # Reload the simulation
    manager = Manager.ParticleSimulationManagerFactory( rendezvous_file ).getManager()

    # estimator id to location map for printing results
    # this convention puts the origin and axes the same as in Treils
    detectors = {1:"NE" , 2:"NW", 3:"CC",4:"SE",5:"SW"}

    # create CSV output file
    file_name = "snm_results_"
    today = date.today().strftime("%b-%d-%Y")
    file = open(file_name + NPS + "_" + today + ".csv","w+")
    # Write the HEU position at the top of the file
    file.write("HEU X" + "," + "HEU Y" + "," + "HEU Z" "\n")
    file.write(HEU_X + "," + HEU_Y + "," +  HEU_Z + "\n")
    # index est corresponds to estimator ID
    # entity ID is just the estimator ID plus 3 due to the way the geometry is generated
    for est_idx in range(1,6):
        file.write("detector location: " + detectors.get(est_idx) + "\n")
        # Extract the estimator of interest from FRENSIE
        estimator = manager.getEventHandler().getEstimator( est_idx )
        entity_bin_data = estimator.getEntityBinProcessedData( est_idx + 3 )
        entity_bin_data["t_bins"] = estimator.getTimeDiscretization()
        file.write("time bin upper bound" + "," + "flux mean" + "," + "flux RE"+ "\n")
        # Write FRENSIE results to CSV forrmat
        for i in range(0,len(entity_bin_data["mean"])):
            file.write(str(entity_bin_data["t_bins"][i+1]) + "," +  str(entity_bin_data["mean"][i]) + "," + str(entity_bin_data["re"][i]) +"\n")
    
    file.close()
