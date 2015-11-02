#from WMCore.Configuration import Configuration
#config = Configuration()
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config=config()

config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'Run2_pthat120_HiForest_HCAL_Method0_19KEvents'
#config.General.failureLimit = 1000

config.section_('JobType')
config.JobType.psetName = 'runForest_PbPb_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForest.root']
#config.JobType.maxJobRuntimeMin = 1900
config.JobType.maxMemoryMB = 2500
config.JobType.numCores = 1

config.section_('Data')
####Test Job###
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 200
NJOBS=95
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#####Actual Job###
#config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 500
#NJOBS=1000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

#config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/rkunnawa/Run2_pthat120_HiForest_HCAL_Method0_19KEvents/'
#config.Data.inputDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/istaslis-PyquenUnquenched_Dijet_NcollFilt_pthat80_753patch1_RECODEBUG-fc27ae3aaa1b75922ce282ddc77e17de/USER'
config.Data.inputDataset = '/HydjetNcoll_Pyquen_DiJet_pt120to9999_5020GeV_cfi_GEN_SIM_750_run2_mc_HIon_BS_v2/rkunnawa-Run2_PbPbpthat120_RECO_HCAL_Method0_40kevents-8464e7c32dba41b93ae62574ea53b62c/USER'
#config.Data.primaryDataset = '/BJet_STEP2_RECO_TEST'
#config.Data.publishDataName = 'Run2_pthat120_RECO_HCAL_Method0'

config.section_('Site')
#config.Site.whitelist = ["*US*"]
config.Site.storageSite = 'T2_US_MIT'

