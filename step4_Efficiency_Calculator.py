from __future__ import division
import pandas as pd
import numpy as np
import uproot
import matplotlib
from matplotlib import pyplot as plt
from tqdm import tqdm

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-t", dest="timeChoice",  type=int, default=3, help='0 through 6')
parser.add_option("-l", dest="showerChoice",  type=int, default=1, help='0:loose; 1:nominal; 2:tight')
(options,args) = parser.parse_args()

normalize = False
hard_cuts = True
cut = 'tight'

in_dir = "trees_TimeChoice" + str(options.timeChoice) + "/"

input_bkg = [in_dir + 'MaxDigis_tree_ZeroBias_2018D.root']

input_sig = [
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_10000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_500mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm.root',

              in_dir+'MaxDigis_tree_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm.root',
              in_dir+'MaxDigis_tree_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm.root',
             ]

comp_treename = 'comparator'
wire_treename = 'wire'

comp_var = [ 'Ev_max_nComp_ME11','Ev_max_nComp_ME12','Ev_max_nComp_ME13','Ev_max_nComp_ME21','Ev_max_nComp_ME22',
             'Ev_max_nComp_ME31','Ev_max_nComp_ME32','Ev_max_nComp_ME41','Ev_max_nComp_ME42']
wire_var = [ 'Ev_max_nWire_ME11','Ev_max_nWire_ME12','Ev_max_nWire_ME13','Ev_max_nWire_ME21','Ev_max_nWire_ME22',
             'Ev_max_nWire_ME31','Ev_max_nWire_ME32','Ev_max_nWire_ME41','Ev_max_nWire_ME42']

comp_vars = list(set(comp_var))
wire_vars = list(set(wire_var))

arrs_comp_sig = [None]*(len(input_sig)+1)
arrs_wire_sig = [None]*(len(input_sig)+1)

comp_thresholds = [
    [100, 54, 20, 35, 29, 35, 24, 36, 26],
    [100, 55, 20, 35, 29, 35, 25, 40, 30],
    [100, 61, 30, 35, 35, 40, 30, 40, 30]
]

wire_thresholds = [
    [105, 93, 33, 134, 80, 118, 75, 128, 87], #loose
    [104, 99, 32, 133, 83, 130, 74, 127, 88], #nominal
    [105, 102, 48,  134, 84,  131, 87,  128, 94] #tight
]

def calculate_efficiency(comp_sig, wire_sig):

    compXX = comp_thresholds[options.showerChoice]
    wireXX = wire_thresholds[options.showerChoice]

    comp_sig_tot = len(comp_sig)
    wire_sig_tot = len(wire_sig)

    efficiency_comp_final = len(comp_sig[(comp_sig['Ev_max_nComp_ME11'] > compXX[0]) |
                                         (comp_sig['Ev_max_nComp_ME12'] > compXX[1]) |
                                         (comp_sig['Ev_max_nComp_ME13'] > compXX[2]) |
                                         (comp_sig['Ev_max_nComp_ME21'] > compXX[3]) |
                                         (comp_sig['Ev_max_nComp_ME22'] > compXX[4]) |
                                         (comp_sig['Ev_max_nComp_ME31'] > compXX[5]) |
                                         (comp_sig['Ev_max_nComp_ME32'] > compXX[6]) |
                                         (comp_sig['Ev_max_nComp_ME41'] > compXX[7]) |
                                         (comp_sig['Ev_max_nComp_ME41'] > compXX[8])])/comp_sig_tot*100
    efficiency_wire_final = len(wire_sig[(wire_sig['Ev_max_nWire_ME11'] > wireXX[0]) |
                                         (wire_sig['Ev_max_nWire_ME12'] > wireXX[1]) |
                                         (wire_sig['Ev_max_nWire_ME13'] > wireXX[2]) |
                                         (wire_sig['Ev_max_nWire_ME21'] > wireXX[3]) |
                                         (wire_sig['Ev_max_nWire_ME22'] > wireXX[4]) |
                                         (wire_sig['Ev_max_nWire_ME31'] > wireXX[5]) |
                                         (wire_sig['Ev_max_nWire_ME32'] > wireXX[6]) |
                                         (wire_sig['Ev_max_nWire_ME41'] > wireXX[7]) |
                                         (wire_sig['Ev_max_nWire_ME41'] > wireXX[8])])/wire_sig_tot*100
    #print "Loose cut"
    print "Comparator Efficiency = %f%%" %(efficiency_comp_final)
    #print "Wire Efficiency = %f%%" %(efficiency_wire_final)


for i in range(0,len(input_sig)):
    print "Opening file: ", input_sig[i]
    arrs_comp_sig[i] = uproot.open(input_sig[i])[comp_treename]
    arrs_wire_sig[i] = uproot.open(input_sig[i])[wire_treename]
    comp_sig = arrs_comp_sig[i].pandas.df(comp_vars)
    wire_sig = arrs_wire_sig[i].pandas.df(wire_vars)

    calculate_efficiency(comp_sig, wire_sig)
