# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_mc_HIon --scenario HeavyIons --pileup_input das:/RelValHydjetQ_MinBias_5020GeV/CMSSW_7_5_0-75X_mcRun2_HeavyIon_v1-v2/GEN-SIM -n 2 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --beamspot NominalHICollision2015 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_HIon_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

# Input source
process.source = cms.Source("PoolSource",
                            dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
                            fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/user/dgulhan/HydjetNcoll_Pyquen_DiJet_pt120to9999_5020GeV_cfi_GEN_SIM_750_run2_mc_HIon_BS_v2/HydjetNcoll_Pyquen_DiJet_pt120to9999_5020GeV_cfi_GEN_SIM_750_run2_mc_HIon_BS_v2/bf872ec8e105dc07c9b7ab12cc7f57a7/step1_1000_1_zPJ.root'),
                            inputCommands = cms.untracked.vstring('keep *', 
                                                                  'drop *_genParticles_*_*', 
                                                                  'drop *_genParticlesForJets_*_*', 
                                                                  'drop *_kt4GenJets_*_*', 
                                                                  'drop *_kt6GenJets_*_*', 
                                                                  'drop *_iterativeCone5GenJets_*_*', 
                                                                  'drop *_ak4GenJets_*_*', 
                                                                  'drop *_ak7GenJets_*_*', 
                                                                  'drop *_ak8GenJets_*_*', 
                                                                  'drop *_ak4GenJetsNoNu_*_*', 
                                                                  'drop *_ak8GenJetsNoNu_*_*', 
                                                                  'drop *_genCandidatesForMET_*_*', 
                                                                  'drop *_genParticlesForMETAllVisible_*_*', 
                                                                  'drop *_genMetCalo_*_*', 
                                                                  'drop *_genMetCaloAndNonPrompt_*_*', 
                                                                  'drop *_genMetTrue_*_*', 
                                                                  'drop *_genMetIC5GenJs_*_*'),
                            secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:2'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
                                              dataset = cms.untracked.PSet(
                                                  dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
                                                  filterName = cms.untracked.string('')
                                              ),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
                                              fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.root'),
                                              outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
                                              splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/001C72B7-C72E-E511-A02F-02163E012031.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/06E46846-C42E-E511-9B3B-02163E01340C.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/18722542-C62E-E511-9442-02163E0140E1.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/1874F9EA-C92E-E511-9338-02163E012934.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/24B37CCF-CB2E-E511-AAB5-02163E0133CA.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/3E609093-D22E-E511-B02D-02163E013918.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/4AE5B5C6-CF2E-E511-8463-02163E014576.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/5A52AAEE-172F-E511-B7D8-02163E014543.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/84975BA6-0D2F-E511-9CA6-02163E01457B.root', '/store/relval/CMSSW_7_5_0/RelValHydjetQ_MinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v1-v2/00000/92598EB1-CD2E-E511-A65D-02163E011836.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.FEVTDEBUGHLToutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1_HI 

#call to customisation function customisePostLS1_HI imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1_HI(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

