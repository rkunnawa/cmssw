from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config=config()

config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'RECO_pthat80_HCAL_Method2_test3'

config.section_('JobType')
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_PU_method2.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['step3_RAW2DIGI_L1Reco_RECO_PU.root']
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2
config.JobType.inputFiles = ['rssLimit']

config.section_('Data')
config.Data.splitting = 'FileBased' 
#config.Data.totalUnits = 5
config.Data.unitsPerJob = 1

config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/rkunnawa/Run2_PbPbpthat80_RECO_HCAL_Method2_test3/'
config.Data.primaryDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/bla/BLA'
config.Data.userInputFiles = ['/store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_100_1_2fl.root',
                              '/store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_101_2_AbU.root',
                              '/store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_102_1_KVX.root',
                              '/store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_103_1_koO.root',
                              '/store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_104_1_QHb.root']

config.Data.publishDataName = 'Run2_PbPBpthat80_RECO_HCAL_Method2_test3'

config.section_('Site')
config.Site.storageSite = 'T2_US_MIT'

