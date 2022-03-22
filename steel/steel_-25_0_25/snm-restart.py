#!/usr/bin/python
import sys, os
from optparse import *
import PyFrensie.Geometry as Geometry
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.Utility.MPI as MPI
import PyFrensie.Utility.Prng as Prng
import PyFrensie.Utility.Coordinate as Coordinate
import PyFrensie.Utility.Distribution as Distribution
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Collision as Collision
import PyFrensie.MonteCarlo.ActiveRegion as ActiveRegion
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager
import PyFrensie.Data as Data
import PyFrensie.Data.Native as Native

if __name__ == "__main__":

        # Parse the command line options
    parser = OptionParser()
    parser.add_option("--rendezvous_file", type="string", dest="rendezvous_file",
                      help="the rendezvous file to restart")
    parser.add_option("--threads", type="int", dest="threads", default=1,
                      help="the number of threads to use")
    options,args = parser.parse_args()

    rendezvous_file = options.rendezvous_file
    threads = options.threads


##---------------------------------------------------------------------------##
## Initialize the MPI Session
##---------------------------------------------------------------------------##
    
    session = MPI.GlobalMPISession( len(sys.argv), sys.argv )
    
    # Suppress logging on all procs except for the master (proc=0)
    Utility.removeAllLogs()
    session.initializeLogs( 0, True )


##---------------------------------------------------------------------------##
##  Set up the simulation manager
##---------------------------------------------------------------------------##

    #Create the paricle simulatiom manager from the rendezvous file
    manager = Manager.ParticleSimulationManagerFactory( rendezvous_file , threads ).getManager()

    # Turn on multiple rendezvous files
    manager.useMultipleRendezvousFiles()

    # Allow logging on all procs
    session.restoreOutputStreams()

    # Resume the simulation
    manager.runSimulation()