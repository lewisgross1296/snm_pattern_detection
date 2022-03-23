import numpy
import math as m
import matplotlib.pyplot as plt
import os
import sys
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager

def plotSNMSimulationSpectrum( rendezvous_file,
                                  estimator_id,
                                  entity_id):

    # Activate just-in-time initialization to prevent automatic loading of the
    # geometry and data tables
    Utility.activateJustInTimeInitialization()

    # Reload the simulation
    manager = Manager.ParticleSimulationManagerFactory( rendezvous_file ).getManager()
    
    # Extract the estimator of interest from FRENSIE
    estimator = manager.getEventHandler().getEstimator( estimator_id )

    entity_bin_data = estimator.getEntityBinProcessedData( entity_id )
    entity_bin_data["e_bins"] = estimator.getTimeDiscretization()

    # TODO print FRENSIE results to CSV forrmat
    for i in range(0,len(entity_bin_data["mean"])):
        print entity_bin_data["e_bins"][i+1], entity_bin_data["mean"][i], entity_bin_data["re"][i]