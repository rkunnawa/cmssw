# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run2_mc_HIon -s RAW2DIGI,L1Reco,RECO -n 2 --eventcontent RECODEBUG --scenario HeavyIons --pileup HiMix --datatier GEN-SIM-RECO --beamspot NominalHICollision2015 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/user/mnguyen/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/PyquenUnquenched_Dijet_pthat80_740pre8_MCHI2_74_V3_DIGI-RAW_v2/ee815b27030c232e2e0a7be48a50a463/step2_DIGI_L1_DIGI2RAW_RAW2DIGI_L1Reco_PU_100_1_2fl.root'),
                            secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:2'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
                                           dataset = cms.untracked.PSet(
                                               dataTier = cms.untracked.string('GEN-SIM-RECO'),
                                               filterName = cms.untracked.string('')
                                           ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           fileName = cms.untracked.string('step3_RAW2DIGI_L1Reco_RECO_PU.root'),
                                           outputCommands = process.RECODEBUGEventContent.outputCommands,
                                           splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_HIon', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1_HI 

#call to customisation function customisePostLS1_HI imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1_HI(process)
# End of customisation functions

