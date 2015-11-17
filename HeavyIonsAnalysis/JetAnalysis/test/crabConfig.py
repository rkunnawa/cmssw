from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.section_('General')
config.General.transferOutputs = True
#config.General.requestName = 'HiForest_pthat15_MC_ECAL25nsMulti_50Kevents'
#config.General.requestName = 'HiForest_pthat80_MC_ECAL25nsMulti_50Kevents'
config.General.requestName = 'HiForest_pthat30_MC_ECAL25nsMulti_50Kevents'
config.section_('JobType')
config.JobType.psetName = 'runForest_ECALStudy_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.JobType.inputFiles = ['rssLimit', 'HI_PythiaCUETP8M1_5020GeV_753p1_v3.db']
config.JobType.outputFiles = ['HiForest.root']
config.section_('Data')
#config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet15_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
#config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet80_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-Pythia8_Dijet30_pp_TuneCUETP8M1_Hydjet_MinBias_5020GeV_RECODEBUG_PrivMC-4cccc1464606b0b9799122eb9219e36a/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'EventAwareLumiBased' 
NJOBS=550
config.Data.unitsPerJob = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
#config.Data.outputDatasetTag = 'Pythia8_Dijet_pthat15_TuneCUETP8M1_5020GeV_HYDJET_MINBIAS_HiForest_PrivMC_MultiFit25ns'
#config.Data.outputDatasetTag = 'Pythia8_Dijet_pthat80_TuneCUETP8M1_5020GeV_HYDJET_MINBIAS_HiForest_PrivMC_MultiFit25ns'
config.Data.outputDatasetTag = 'Pythia8_Dijet_pthat30_TuneCUETP8M1_5020GeV_HYDJET_MINBIAS_HiForest_PrivMC_MultiFit25ns'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_MIT'
