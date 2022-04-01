#!/usr/bin/python
import sys, os
from optparse import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from snm_write_data_simulation import writeSNMSimulationSpectrum

if __name__ == "__main__":

    # Parse the command line arguments
    parser = OptionParser()
    parser.add_option("--rendezvous_file", type="string", dest="rendezvous_file",
                      help="the rendezvous file to load")
    parser.add_option("--NPS",type="string",dest="NPS",
                      help="the number of particles corresponding to the results")
    parser.add_option("--HEU_X", type="string", dest="X",
                      help="the position of HEU in the geometry [cm]")
    parser.add_option("--HEU_Y", type="string", dest="Y",
                      help="the position of HEU in the geometry [cm]")
    parser.add_option("--HEU_Z", type="string", dest="Z",
                      help="the position of HEU in the geometry [cm]")
    options,args = parser.parse_args()

    # Plot the spectrum
    writeSNMSimulationSpectrum(   options.rendezvous_file,
                                  options.NPS,
                                  options.X,
                                  options.Y,
                                  options.Z)