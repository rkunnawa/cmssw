from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config=config()

config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'RECO_pthat120_HCAL_Method0_40kevents'

config.section_('JobType')
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PU_method0.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['step3_RAW2DIGI_L1Reco_RECO_PU.root']
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2
config.JobType.inputFiles = ['rssLimit']

config.section_('Data')
config.Data.splitting = 'EventAwareLumiBased' 
NJOBS=500
config.Data.unitsPerJob = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/rkunnawa/Run2_PbPbpthat120_RECO_HCAL_Method0_40kevents/'
#config.Data.inputDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/mnguyen-PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2-ee815b27030c232e2e0a7be48a50a463/USER'
config.Data.inputDataset = '/HydjetNcoll_Pyquen_DiJet_pt120to9999_5020GeV_cfi_GEN_SIM_750_run2_mc_HIon_BS_v2/dgulhan-HydjetNcoll_Pyquen_DiJet_pt120to9999_5020GeV_cfi_DIGI_RAW_750_run2_mc_HIon_BS-04dd99eee2d0be43bf0c03571f470b50/USER'
config.Data.publishDataName = 'Run2_PbPbpthat120_RECO_HCAL_Method0_40kevents'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'
#config.Site.whitelist = ['T2_US_MIT']

