from ROOT import TFile, TTree, TChain
from ROOT import gROOT, AddressOf
import uproot
from array import array
from tqdm import tqdm
import numpy as np
from helpers import signal_samples, data_samples, timeBinChoice, test_sample, get_R
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", dest="sampleChoice",  type=int, default=0, help='0:signal; 1: data')
parser.add_option("-t", dest="timeChoice",  type=int, default=3, help='0 through 6')
(options,args) = parser.parse_args()

TimeChoice = options.timeChoice

box = False
#Setting box=True will only consider signal events that decay right in front of a chamber to be in acceptance

def processSingleSample(dataset, sample_dict, runTest=False):

    print("Processing dataset", dataset)

    comp_ME11 = array('f', [0.])
    comp_ME12 = array('f', [0.])
    comp_ME13 = array('f', [0.])
    comp_ME21 = array('f', [0.])
    comp_ME22 = array('f', [0.])
    comp_ME31 = array('f', [0.])
    comp_ME32 = array('f', [0.])
    comp_ME41 = array('f', [0.])
    comp_ME42 = array('f', [0.])

    wire_ME11 = array('f', [0.])
    wire_ME12 = array('f', [0.])
    wire_ME13 = array('f', [0.])
    wire_ME21 = array('f', [0.])
    wire_ME22 = array('f', [0.])
    wire_ME31 = array('f', [0.])
    wire_ME32 = array('f', [0.])
    wire_ME41 = array('f', [0.])
    wire_ME42 = array('f', [0.])

    if box:
        out_path = "trees_TimeChoice" + str(TimeChoice) + "/box_selected/MaxDigis_tree_" + dataset + ".root"
    else:
        out_path = "trees_TimeChoice" + str(TimeChoice) + "/MaxDigis_tree_" + dataset + ".root"

    f = TFile.Open( out_path, 'RECREATE' )
    if not f:
        print("Failed to open output file:", f)

    comp_tree = TTree( 'comparator', 'Max Comparator digis in a single chamber in each ring per event' )
    wire_tree = TTree( 'wire', 'Max Comparator digis in a single chamber in each ring per event' )
    # tree.Branch( 'digis', digis, 'Ev_max_nComp_ME11/I:Ev_max_nComp_ME12:Ev_max_nComp_ME13:Ev_max_nComp_ME21:Ev_max_nComp_ME22:Ev_max_nComp_ME31:Ev_max_nComp_ME32:Ev_max_nComp_ME41:Ev_max_nComp_ME42:Ev_max_nWire_ME11:Ev_max_nWire_ME12:Ev_max_nWire_ME13:Ev_max_nWire_ME21:Ev_max_nWire_ME22:Ev_max_nWire_ME31:Ev_max_nWire_ME32:Ev_max_nWire_ME41:Ev_max_nWire_ME42',0 )
    comp_tree.Branch( 'Ev_max_nComp_ME11', comp_ME11, 'comp_ME11/F')
    comp_tree.Branch( 'Ev_max_nComp_ME12', comp_ME12, 'comp_ME12/F')
    comp_tree.Branch( 'Ev_max_nComp_ME13', comp_ME13, 'comp_ME13/F')
    comp_tree.Branch( 'Ev_max_nComp_ME21', comp_ME21, 'comp_ME21/F')
    comp_tree.Branch( 'Ev_max_nComp_ME22', comp_ME22, 'comp_ME22/F')
    comp_tree.Branch( 'Ev_max_nComp_ME31', comp_ME31, 'comp_ME31/F')
    comp_tree.Branch( 'Ev_max_nComp_ME32', comp_ME32, 'comp_ME32/F')
    comp_tree.Branch( 'Ev_max_nComp_ME41', comp_ME41, 'comp_ME41/F')
    comp_tree.Branch( 'Ev_max_nComp_ME42', comp_ME42, 'comp_ME42/F')

    wire_tree.Branch( 'Ev_max_nWire_ME11', wire_ME11, 'wire_ME11/F')
    wire_tree.Branch( 'Ev_max_nWire_ME12', wire_ME12, 'wire_ME12/F')
    wire_tree.Branch( 'Ev_max_nWire_ME13', wire_ME13, 'wire_ME13/F')
    wire_tree.Branch( 'Ev_max_nWire_ME21', wire_ME21, 'wire_ME21/F')
    wire_tree.Branch( 'Ev_max_nWire_ME22', wire_ME22, 'wire_ME22/F')
    wire_tree.Branch( 'Ev_max_nWire_ME31', wire_ME31, 'wire_ME31/F')
    wire_tree.Branch( 'Ev_max_nWire_ME32', wire_ME32, 'wire_ME32/F')
    wire_tree.Branch( 'Ev_max_nWire_ME41', wire_ME41, 'wire_ME41/F')
    wire_tree.Branch( 'Ev_max_nWire_ME42', wire_ME42, 'wire_ME42/F')

    if dataset=="Data_pre-selected":
        comp_pass_list = open("passlists/comp_pass_list.txt","w")
        wire_pass_list = open("passlists/wire_pass_list.txt","w")
        comp_last_text = ""
        wire_last_text = ""
        compXX = [98, 56, 30, 49, 42, 49, 35, 42, 31]
        wireXX = [104, 92, 32, 133, 83, 130, 74, 127, 88]
        comp_pass_count = 0
        wire_pass_count = 0

    MC = True
    if "ZeroBias" in dataset:
        MC = False
        print(">>Sample is ZeroBias")

    print("Declaring TChains")

    ## declare the chains
    alctChain = TChain("lctreader/Ev_alcttree")
    clctChain = TChain("lctreader/Ev_clcttree")
    llpChain = TChain("lctreader/llp")

    prefix = "root://cmseos.fnal.gov/"
    userdir = "/store/user/dildick/"
    directory = prefix + userdir + sample_dict[dataset]
    if runTest:
        directory = sample_dict[dataset]
    print("Adding Files")

    print("directory",directory)
    if runTest:
        llpChain.Add(directory + "TPEHists*.root")
        alctChain.Add(directory + "TPEHists*.root")
        clctChain.Add(directory + "TPEHists*.root")
    else:
        if MC:
            llpChain.Add(directory + "TPEHists*.root")
            alctChain.Add(directory + "TPEHists*.root")
            clctChain.Add(directory + "TPEHists*.root")
        else:
            llpChain.Add(directory + "TPEHists_data_10*.root")
            alctChain.Add(directory + "TPEHists_data_10*.root")
            clctChain.Add(directory + "TPEHists_data_10*.root")

    print("Entries in ALCT Chain", alctChain.GetEntries())
    print("Entries in CLCT Chain", clctChain.GetEntries())
    print("Entries in LLP Chain", llpChain.GetEntries())

    clct = clctChain
    alct = alctChain
    llp = llpChain

    nEntries_clct = clctChain.GetEntries()
    nEntries_alct = alctChain.GetEntries()
    if MC:
      nEntries_llp = llpChain.GetEntries()

    llp_accept = []
    #max_nComp = np.array([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
    max_nComp = np.zeros((5,4))
    max_nWire = np.zeros((5,4))
    lastEventclct = 0
    lastEventalct = 0
    n_big = 0

    passed=0
    if MC:
        print "Finding LLP Acceptance"
        for i in range(0, nEntries_llp):
            llp.GetEntry(i)

            if(llp.llp_in_acceptance[0]==1 or llp.llp_in_acceptance[1]==1):
                if box:
                    for nlp in range(0,2):
                        R = get_R((llp.llp_decay_x[nlp]/100),(llp.llp_decay_y[nlp]/100))
                        for cut in range(0,len(zMin)):
                            if(abs(llp.llp_decay_z[nlp]/100) > zMin[cut] and abs(llp.llp_decay_z[nlp]/100) < zMax[cut] and R > rMin[cut] and R < rMax[cut]):
                                llp_accept.append(llp.event)
                                passed+=1
                                break
                else:
                    llp_accept.append(llp.event)
                    passed+=1

    print "# passed = " + str(passed)



    print "Starting CLCT Analysis"
    for i in tqdm(range(0, nEntries_clct)):
        clct.GetEntry(i)

        if MC:
            if clct.t_Event not in llp_accept:
                continue

        ## number of in-time comparators
        nComp = clct.t_compTimes[TimeChoice]

        ## ignore event if no in-time comparators
        if nComp == 0:
            continue

        if(clct.t_Event!=lastEventclct):
            lastEventclct = clct.t_Event

            comp_ME11[0] = max_nComp[1][1]
            comp_ME12[0] = max_nComp[1][2]
            comp_ME13[0] = max_nComp[1][3]
            comp_ME21[0] = max_nComp[2][1]
            comp_ME22[0] = max_nComp[2][2]
            comp_ME31[0] = max_nComp[3][1]
            comp_ME32[0] = max_nComp[3][2]
            comp_ME41[0] = max_nComp[4][1]
            comp_ME42[0] = max_nComp[4][2]
            max_nComp = np.zeros((5,4))

            comp_tree.Fill()


        if nComp > max_nComp[clct.t_station][clct.t_ring]:
            max_nComp[clct.t_station][clct.t_ring] = nComp

        if dataset=="Data_pre-selected":
            if (max_nComp[1][1]>compXX[0] or max_nComp[1][2]>compXX[1] or max_nComp[1][3]>compXX[2] or
                max_nComp[2][1]>compXX[3] or max_nComp[2][2]>compXX[4] or
                max_nComp[3][1]>compXX[5] or max_nComp[3][2]>compXX[6] or
                max_nComp[4][1]>compXX[7] or max_nComp[4][2]>compXX[8]):

                comp_pass_text = "%i:%i:%d\n" % (clct.t_Run,clct.t_Lumi,clct.t_Event)
                if comp_pass_text!=comp_last_text:
                    comp_pass_list.write(comp_pass_text)
                    comp_pass_count+=1
                comp_last_text = comp_pass_text

    if dataset=="Data_pre-selected":
        print "%i events passed cut" %(comp_pass_count)


    print "Starting ALCT Analysis"
    for i in tqdm(range(0, nEntries_alct)):
        alct.GetEntry(i)

        if MC:
            if alct.t_Event not in llp_accept:
                continue

        ## number of in-time wires
        nWire = alct.t_wireTimes[TimeChoice]

        ## ignore event if no in-time wires
        if nWire == 0:
            continue

        if(alct.t_Event!=lastEventalct):
            lastEventalct = alct.t_Event

            wire_ME11[0] = max_nWire[1][1]
            wire_ME12[0] = max_nWire[1][2]
            wire_ME13[0] = max_nWire[1][3]
            wire_ME21[0] = max_nWire[2][1]
            wire_ME22[0] = max_nWire[2][2]
            wire_ME31[0] = max_nWire[3][1]
            wire_ME32[0] = max_nWire[3][2]
            wire_ME41[0] = max_nWire[4][1]
            wire_ME42[0] = max_nWire[4][2]
            max_nWire = np.zeros((5,4))

            wire_tree.Fill()


        if nWire > max_nWire[alct.t_station][alct.t_ring]:
            max_nWire[alct.t_station][alct.t_ring] = nWire

        if dataset=="Data_pre-selected":
            if (max_nWire[1][1]>wireXX[0] or max_nWire[1][2]>wireXX[1] or max_nWire[1][3]>wireXX[2] or
                max_nWire[2][1]>wireXX[3] or max_nWire[2][2]>wireXX[4] or
                max_nWire[3][1]>wireXX[5] or max_nWire[3][2]>wireXX[6] or
                max_nWire[4][1]>wireXX[7] or max_nWire[4][2]>wireXX[8]):

                wire_pass_text = "%i:%i:%d\n" % (alct.t_Run,alct.t_Lumi,alct.t_Event)
                if wire_pass_text!=wire_last_text:
                    wire_pass_list.write(wire_pass_text)
                    wire_pass_count+=1
                wire_last_text = wire_pass_text

    if dataset=="Data_pre-selected":
        print "%i events passed cut" %(wire_pass_count)



    f.Write()
    f.Close()
    if dataset=="Data_pre-selected":
        comp_pass_list.close()
        wire_pass_list.close()
    print("Finished analysis")


def runTest():
    processSingleSample('Test', test_sample, runTest=True)


## make a choice
runSamples = {}
if options.sampleChoice == 0:
    runSamples = signal_samples

if options.sampleChoice == 1:
    runSamples = data_samples

#runTest()

for dataset in tqdm(runSamples):
    print(dataset)

for dataset in tqdm(runSamples):
    processSingleSample(dataset, runSamples)
