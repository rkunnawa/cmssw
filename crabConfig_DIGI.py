from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config=config()

config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'Run2_DIGI_HCALupdate_PbPbMBHydjet_753'

config.section_('JobType')
config.JobType.psetName = 'step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco.root']
config.JobType.maxMemoryMB = 2500
config.JobType.numCores = 1
config.JobType.inputFiles = ['rssLimit']

config.section_('Data')
config.Data.splitting = 'EventAwareLumiBased' 
NJOBS=100
config.Data.unitsPerJob = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.inputDBS = 'global'
config.Data.outLFNDirBase = '/store/user/rkunnawa/Run2_DIGI_HCALupdate_PbPbMBHydjet_753/'
config.Data.inputDataset = '/RelValHydjetQ_MinBias_5020GeV/CMSSW_7_5_0-75X_mcRun2_HeavyIon_v1-v2/GEN-SIM'

config.Data.publishDataName = 'Run2_DIGI_HCALupdate_PbPbMBHydjet_753'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

