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
hard_cuts = False

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

#all_vars = [ 'Ev_nComp_ME11','Ev_nComp_ME12']

comp_vars = list(set(comp_var))
wire_vars = list(set(wire_var))

arrs_comp_sig = [None]*(len(input_sig)+1)
arrs_wire_sig = [None]*(len(input_sig)+1)

print "Opening input files"

print "Opening file: ", input_sig[0]
arrs_comp_sig[0] = uproot.open(input_sig[0])[comp_treename]
arrs_wire_sig[0] = uproot.open(input_sig[0])[wire_treename]
comp_sig = arrs_comp_sig[0].pandas.df(comp_vars)
wire_sig = arrs_wire_sig[0].pandas.df(wire_vars)
if normalize:
    comp_sig = comp_sig.head(130)
    wire_sig = comp_sig.head(130)
#print "Comp num events = %i" % (len(comp_sig.index))
#print "Wire num events = %i" % (len(wire_sig.index))

j=1
for i in range(1,len(input_sig)):
    print "Opening file: ", input_sig[i]
    arrs_comp_sig[j] = uproot.open(input_sig[i])[comp_treename]
    arrs_wire_sig[j] = uproot.open(input_sig[i])[wire_treename]
    temp_comp_sig = arrs_comp_sig[i].pandas.df(comp_vars)
    temp_wire_sig = arrs_wire_sig[i].pandas.df(wire_vars)
    if normalize:
        temp_comp_sig = temp_comp_sig.head(130)
        temp_wire_sig = temp_wire_sig.head(130)
    #print "Comp num events = %i" % (len(temp_comp_sig.index))
    #print "Wire num events = %i" % (len(temp_wire_sig.index))
    comp_sig = comp_sig.append(temp_comp_sig)
    wire_sig = wire_sig.append(temp_wire_sig)
    j=j+1


print "Opening file: ", input_bkg[0]
arrs_comp_bkg = uproot.open(input_bkg[0])[comp_treename]
arrs_wire_bkg = uproot.open(input_bkg[0])[wire_treename]
comp_bkg = arrs_comp_bkg.pandas.df(comp_vars)
wire_bkg = arrs_wire_bkg.pandas.df(wire_vars)
print "Number of bkg events: %i" % (len(wire_bkg))
print "Number of sig events: %i" % (len(wire_sig))



min_=0
max_=150
it_=1


## choice of shower
r1=1
r2=1

# loose
if options.showerChoice == 0:
    r1=3
    r2=4
# nominal
elif options.showerChoice == 1:
    r1=2
    r2=3
# tight
elif options.showerChoice == 2:
    r1=1
    r2=2

r = [r1,r2,r2,r1,r2,r1,r2,r1,r2]

l1=.12
l2=.2
rmin = [0.0,.02,.02,.02,.02,.02,.02,.02,.02]
rmax_t = [.02,l2,l2,l1,l2,l1,l2,l1,l2]
rmax = [i*1 for i in rmax_t]


compXX = [0,0,0,0,0,0,0,0,0]
wireXX = [0,0,0,0,0,0,0,0,0]

#hard_cuts = False

for inc in range(len(comp_var)):

    comp_efficiency=[0]
    comp_sig_tot = len(comp_sig)
    comp_rate=[0]
    comp_bkg_tot = len(comp_bkg)
    comp_limits=[0]
    best = 0.0
    best_cut = 149

    for limit in (xrange(min_,max_,it_)):
        comp_efficiency.append(len(comp_sig[(comp_sig[comp_var[inc]] > limit)])/comp_sig_tot*100)

        comp_rate.append(len(comp_bkg[(comp_bkg[comp_var[inc]] > limit)])/comp_bkg_tot*30*1000)

        comp_limits.append(limit)

    for i in range(len(comp_rate)):
        if comp_rate[i] > rmin[inc] and comp_rate[i] < rmax[inc]:
            if np.power(comp_efficiency[i],r[inc])/np.sqrt(comp_rate[i]) > best:
                best = np.power(comp_efficiency[i],r[inc])/np.sqrt(comp_rate[i])
                best_cut = comp_limits[i]

    if hard_cuts:
        #compXX = [98, 56, 30, 49, 42, 49, 35, 42, 31] #nominal
        #compXX = [149, 64, 21, 33, 34, 33, 25, 32, 31] #tight
        compXX = [99, 57, 25, 45, 36, 43, 29, 43, 32] #loose
        best_cut = compXX[inc]
    print "For " + comp_var[inc] + ":"
    print "Best threshold > %i" %(best_cut)
    print 'rate =', comp_rate[best_cut+1], 'kHz and efficiency =', comp_efficiency[best_cut+1], '% for threshold >', comp_limits[best_cut+1]
    print "-----------------------------------------------------------------------"
    compXX[inc] = best_cut+1

efficiency_comp_final = len(comp_sig[(comp_sig['Ev_max_nComp_ME11'] > compXX[0]) | (comp_sig['Ev_max_nComp_ME12'] > compXX[1]) | (comp_sig['Ev_max_nComp_ME13'] > compXX[2]) |
                           (comp_sig['Ev_max_nComp_ME21'] > compXX[3]) | (comp_sig['Ev_max_nComp_ME22'] > compXX[4]) |
                           (comp_sig['Ev_max_nComp_ME31'] > compXX[5]) | (comp_sig['Ev_max_nComp_ME32'] > compXX[6]) |
                           (comp_sig['Ev_max_nComp_ME41'] > compXX[7]) | (comp_sig['Ev_max_nComp_ME41'] > compXX[8])])/comp_sig_tot*100

rate_comp_final       = len(comp_bkg[(comp_bkg['Ev_max_nComp_ME11'] > compXX[0]) | (comp_bkg['Ev_max_nComp_ME12'] > compXX[1]) | (comp_bkg['Ev_max_nComp_ME13'] > compXX[2]) |
                           (comp_bkg['Ev_max_nComp_ME21'] > compXX[3]) | (comp_bkg['Ev_max_nComp_ME22'] > compXX[4]) |
                           (comp_bkg['Ev_max_nComp_ME31'] > compXX[5]) | (comp_bkg['Ev_max_nComp_ME32'] > compXX[6]) |
                           (comp_bkg['Ev_max_nComp_ME41'] > compXX[7]) | (comp_bkg['Ev_max_nComp_ME42'] > compXX[8])])/comp_bkg_tot*30*1000

print "Combined Result:"
print "rate =", rate_comp_final, "kHz, efficiency =", efficiency_comp_final, "%"

rate_num_final       = len(comp_bkg[(comp_bkg['Ev_max_nComp_ME11'] > compXX[0]) | (comp_bkg['Ev_max_nComp_ME12'] > compXX[1]) | (comp_bkg['Ev_max_nComp_ME13'] > compXX[2]) |
                           (comp_bkg['Ev_max_nComp_ME21'] > compXX[3]) | (comp_bkg['Ev_max_nComp_ME22'] > compXX[4]) |
                           (comp_bkg['Ev_max_nComp_ME31'] > compXX[5]) | (comp_bkg['Ev_max_nComp_ME32'] > compXX[6]) |
                           (comp_bkg['Ev_max_nComp_ME41'] > compXX[7]) | (comp_bkg['Ev_max_nComp_ME42'] > compXX[8])])

print "Number of events that pass:", rate_num_final, " out of", comp_bkg_tot

for inc in range(len(wire_var)):

    wire_efficiency=[0]
    wire_sig_tot = len(wire_sig)
    wire_rate=[0]
    wire_bkg_tot = len(wire_bkg)
    wire_limits=[0]
    best = 0.0
    best_cut = 149

    for limit in (xrange(min_,max_,it_)):
        wire_efficiency.append(len(wire_sig[(wire_sig[wire_var[inc]] > limit)])/wire_sig_tot*100)

        wire_rate.append(len(wire_bkg[(wire_bkg[wire_var[inc]] > limit)])/wire_bkg_tot*30*1000)

        wire_limits.append(limit)

    for i in range(len(wire_rate)):
        if wire_rate[i] > rmin[inc] and wire_rate[i] < rmax[inc]:
            if np.power(wire_efficiency[i],r[inc])/np.sqrt(wire_rate[i]) > best:
                best = np.power(wire_efficiency[i],r[inc])/np.sqrt(wire_rate[i])
                best_cut = wire_limits[i]

    if hard_cuts:
        #wireXX = [104, 92, 32, 133, 83, 130, 74, 127, 88] #nominal
        #wireXX = [149, 108, 27,  75, 44,  83, 34,  83, 40] #tight
        wireXX = [105, 93, 33, 134, 80, 118, 75, 128, 87] #loose
        best_cut = wireXX[inc]
    print "For " + wire_var[inc] + ":"
    print "Best threshold > %i" %(best_cut)
    print 'rate =', wire_rate[best_cut+1], 'kHz and efficiency =', wire_efficiency[best_cut+1], '% for threshold >', wire_limits[best_cut+1]
    print "-----------------------------------------------------------------------"
    wireXX[inc] = best_cut+1

efficiency_wire_final = len(wire_sig[(wire_sig['Ev_max_nWire_ME11'] > wireXX[0]) | (wire_sig['Ev_max_nWire_ME12'] > wireXX[1]) | (wire_sig['Ev_max_nWire_ME13'] > wireXX[2]) |
                           (wire_sig['Ev_max_nWire_ME21'] > wireXX[3]) | (wire_sig['Ev_max_nWire_ME22'] > wireXX[4]) |
                           (wire_sig['Ev_max_nWire_ME31'] > wireXX[5]) | (wire_sig['Ev_max_nWire_ME32'] > wireXX[6]) |
                           (wire_sig['Ev_max_nWire_ME41'] > wireXX[7]) | (wire_sig['Ev_max_nWire_ME41'] > wireXX[8])])/wire_sig_tot*100

rate_wire_final       = len(wire_bkg[(wire_bkg['Ev_max_nWire_ME11'] > wireXX[0]) | (wire_bkg['Ev_max_nWire_ME12'] > wireXX[1]) | (wire_bkg['Ev_max_nWire_ME13'] > wireXX[2]) |
                           (wire_bkg['Ev_max_nWire_ME21'] > wireXX[3]) | (wire_bkg['Ev_max_nWire_ME22'] > wireXX[4]) |
                           (wire_bkg['Ev_max_nWire_ME31'] > wireXX[5]) | (wire_bkg['Ev_max_nWire_ME32'] > wireXX[6]) |
                           (wire_bkg['Ev_max_nWire_ME41'] > wireXX[7]) | (wire_bkg['Ev_max_nWire_ME42'] > wireXX[8])])/wire_bkg_tot*30*1000

print "Combined Result:"
print "rate =", rate_wire_final, "kHz, efficiency =", efficiency_wire_final, "%"

rate_num_final       = len(wire_bkg[(wire_bkg['Ev_max_nWire_ME11'] > wireXX[0]) | (wire_bkg['Ev_max_nWire_ME12'] > wireXX[1]) | (wire_bkg['Ev_max_nWire_ME13'] > wireXX[2]) |
                           (wire_bkg['Ev_max_nWire_ME21'] > wireXX[3]) | (wire_bkg['Ev_max_nWire_ME22'] > wireXX[4]) |
                           (wire_bkg['Ev_max_nWire_ME31'] > wireXX[5]) | (wire_bkg['Ev_max_nWire_ME32'] > wireXX[6]) |
                           (wire_bkg['Ev_max_nWire_ME41'] > wireXX[7]) | (wire_bkg['Ev_max_nWire_ME42'] > wireXX[8])])

print "Number of events that pass:", rate_num_final, " out of", wire_bkg_tot


if hard_cuts:
    #compXX = [ 98, 56, 30, 49, 42, 49, 35, 42, 31] #nominal
    #compXX = [149, 64, 21, 33, 34, 33, 25, 32, 31] #tight
    compXX = [99, 57, 25, 45, 36, 43, 29, 43, 32] #loose
    #wireXX = [104,  92, 32, 133, 83, 130, 74, 127, 88] #nominal
    #wireXX = [149, 108, 27,  75, 44,  83, 34,  83, 40] #tight
    wireXX = [105, 93, 33, 134, 80, 118, 75, 128, 87] #loose


print "Optimal Comparator Thresholds:"
print "ME11: %i, ME12: %i, ME13: %i," %(compXX[0],compXX[1],compXX[2])
print "ME21: %i, ME22: %i," %(compXX[3],compXX[4])
print "ME31: %i, ME32: %i," %(compXX[5],compXX[6])
print "ME41: %i, ME42: %i," %(compXX[7],compXX[8])
print "With rate and efficiency:"
print "rate = %f kHz, efficiency = %f%%" %(rate_comp_final,efficiency_comp_final)
print
print "Optimal Wire Thresholds:"
print "ME11: %i, ME12: %i, ME13: %i," %(wireXX[0],wireXX[1],wireXX[2])
print "ME21: %i, ME22: %i," %(wireXX[3],wireXX[4])
print "ME31: %i, ME32: %i," %(wireXX[5],wireXX[6])
print "ME41: %i, ME42: %i," %(wireXX[7],wireXX[8])
print "With rate and efficiency:"
print "rate = %f kHz, efficiency = %f%%" %(rate_wire_final,efficiency_wire_final)
