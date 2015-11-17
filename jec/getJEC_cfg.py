import FWCore.ParameterSet.Config as cms
process = cms.Process("jectxt")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# define your favorite global tag
process.GlobalTag.globaltag = '75X_mcRun2_HeavyIon_v5'
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.readAKPu3Calo = cms.EDAnalyzer('JetCorrectorDBReader',  
                                      # below is the communication to the database 
                                      payloadName    = cms.untracked.string('AK4Calo_offline'),
                                      # this is used ONLY for the name of the printed txt files. You can use any name that you like, 
                                      # but it is recommended to use the GT name that you retrieved the files from.
                                      globalTag      = cms.untracked.string('75X_mcRun2_HeavyIon_v5'),#GR_R_52_V9'),  
                                      printScreen    = cms.untracked.bool(False),
                                      createTextFile = cms.untracked.bool(True)
                                  )
from HeavyIonsAnalysis.Configuration.CommonFunctionsLocalDB_cff import *
overrideGT_PbPb2760(process)

#process.readAK5Calo = process.readAK5PF.clone(payloadName = 'AK5Calo')
#process.readAK5JPT = process.readAK5PF.clone(payloadName = 'AK5JPT')
#process.p = cms.Path(process.readAK5PF * process.readAK5Calo * process.readAK5JPT)
#process.readAKPu3Calo = process.readAKPu3PF.clone(payloadName = 'AKVs3Calo_HI')
#process.readAKPu3PF   = process.readAKPu3PF.clone(payloadName = 'AKVs3PF_hiIterativeTracks')
process.p = cms.Path(process.readAKPu3Calo)
