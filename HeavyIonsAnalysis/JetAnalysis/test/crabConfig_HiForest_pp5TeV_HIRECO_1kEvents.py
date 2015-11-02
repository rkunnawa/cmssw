#from WMCore.Configuration import Configuration
#config = Configuration()
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config=config()

config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'Run2_pp5TeV_HiForest_HIRECO'
#config.General.failureLimit = 1000

config.section_('JobType')
config.JobType.psetName = 'runForest_pp_MIX_75X.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['HiForest.root']
#config.JobType.maxJobRuntimeMin = 1900
config.JobType.maxMemoryMB = 2500
config.JobType.numCores = 1

config.section_('Data')
####Test Job###
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 100
NJOBS=10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#####Actual Job###
#config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 500
#NJOBS=1000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

#config.Data.publication = True
config.Data.inputDBS = 'global'
config.Data.outLFNDirBase = '/store/user/rkunnawa/Run2_pp5TeV_HiForest_HIRECO/'
#config.Data.inputDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/istaslis-PyquenUnquenched_Dijet_NcollFilt_pthat80_753patch1_RECODEBUG-fc27ae3aaa1b75922ce282ddc77e17de/USER'
config.Data.inputDataset = '/PYTHIA_QCD_TuneCUETP8M1_cfi_GEN_SIM_5020GeV/dgulhan-PYTHIA_QCD_80_TuneCUETP8M1_cfi_HI_RECODEBUG_5020GeV_patch3_20151010-5a929d7059f4b993e3119764421f52bf/USER'
#config.Data.primaryDataset = '/BJet_STEP2_RECO_TEST'
#config.Data.publishDataName = 'Run2_pthat120_RECO_HCAL_Method0'

config.section_('Site')
#config.Site.whitelist = ["*US*"]
config.Site.storageSite = 'T2_US_MIT'

