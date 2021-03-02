#Used for box selection
zMin = [4.5,5.7,5.8,7,7,8,8,9,9]
zMax = [5.5,6.7,6.8,8,8,9,9,10,10]
rMin = [1.0,2.5,4.7,1.4,3.5,1.6,3.5,1.8,3.5]
rMax = [2.8,4.5,6.8,3.5,7.0,3.5,7.0,3.5,7.0]


signal_samples = {
    'HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm' :
    'HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm_ANA_20210226_v2/210227_043020/0000/',

    'HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm' :
    'HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm_ANA_20210226_v2/210227_043029/0000/',


    'HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-12_CTau-9000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm_ANA_20210226_v2/210227_043039/0000/',

    'HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm_ANA_20210226_v2/210227_043051/0000/',

    'HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-25_CTau-15000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm_ANA_20210226_v2/210227_043101/0000/',

    'HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm_ANA_20210226_v2/210227_043111/0000/',

    'HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-50_CTau-30000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm_ANA_20210226_v2/210227_043122/0000/',

    'HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm' :
    'HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm_ANA_20210226_v2/210227_043132/0000/',


    'HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-120_CTau-10000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_10000mm_ANA_20210226_v2/210227_043143/0000/',

    'HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-120_CTau-1000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm_ANA_20210226_v2/210227_043154/0000/',

    'HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-120_CTau-500mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm_ANA_20210226_v2/210227_043204/0000/',

    'HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-60_CTau-10000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm_ANA_20210226_v2/210227_043217/0000/',

    'HTo2LongLivedTo4b_MH_250_MFF_60_CTau_1000mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-60_CTau-1000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_60_CTau_1000mm_ANA_20210226_v2/210227_043229/0000/',

    'HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm' :
    'HTo2LongLivedTo4b_MH-250_MFF-60_CTau-500mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm_ANA_20210226_v2/210227_043239/0000/',


    'HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-160_CTau-10000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm_ANA_20210226_v2/210227_043251/0000/',

    'HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-160_CTau-1000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm_ANA_20210226_v2/210227_043301/0000/',

    ## this is 500, not 5000!
    'HTo2LongLivedTo4b_MH_350_MFF_160_CTau_500mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-160_CTau-500mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_160_CTau_5000mm_ANA_20210226_v2/210227_043311/0000/',


    'HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-80_CTau-10000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm_ANA_20210226_v2/210301_211628/0000/',

    'HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-80_CTau-1000mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm_ANA_20210226_v2/210227_043331/0000/',

    'HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm' :
    'HTo2LongLivedTo4b_MH-350_MFF-80_CTau-500mm_TuneCP5_14TeV_pythia8/crab_HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm_ANA_20210226_v2/210227_043342/0000/',


    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm' :
    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/crab_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_ANA_20210226_v2/210227_042450/0000/',

    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm' :
    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia/crab_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_ANA_20210226_v2/210227_042502/0000/',

    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm' :
    'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia/crab_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_ANA_20210226_v2/210301_211644/0000/'
}


data_samples = {
    'ZeroBias_2018D_0000' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0000/',

    'ZeroBias_2018D_0001' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0001/',

    'ZeroBias_2018D_0002' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0002/',

    'ZeroBias_2018D_0003' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0003/',

    'ZeroBias_2018D_0004' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0004/',

    'ZeroBias_2018D_0005' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0005/',

    'ZeroBias_2018D_0006' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0006/',

    'ZeroBias_2018D_0007' :
    'ZeroBias/crab_ZeroBias_Run2018D_ANA_20210226_v2/210227_043750/0007/'
}

test_sample = {
    'Test' :
'root://cmseos.fnal.gov//store/user/dildick/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia/crab_HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_ANA_20210226_v2/210227_042502/0000/'
#'/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_11_1_0_pre6/src/'
}

def timeBinChoice(TimeChoice):
    if TimeChoice == 0:
        good_times_ano = [8]
        good_times_cat = [7]
    elif TimeChoice == 1:
        good_times_ano = [8,9]
        good_times_cat = [7,8]
    elif TimeChoice == 2:
        good_times_ano = [7,8]
        good_times_cat = [6,7]
    elif TimeChoice == 3:
        good_times_ano = [7,8,9]
        good_times_cat = [6,7,8]
    elif TimeChoice == 4:
        good_times_ano = [7,8,9,10]
        good_times_cat = [6,7,8,9]
    elif TimeChoice == 5:
        good_times_ano = [6,7,8,9]
        good_times_cat = [5,6,7,8]
    elif TimeChoice == 6:
        good_times_ano = [6,7,8,9,10]
        good_times_cat = [5,6,7,8,9]
    return good_times_ano, good_times_cat

def get_R(x,y):
    R = np.sqrt(np.square(x) + np.square(y))
    return R
