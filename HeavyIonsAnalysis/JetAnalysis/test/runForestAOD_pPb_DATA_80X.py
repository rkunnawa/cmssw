### HiForest Configuration
# Collisions: pp
# Type: MC
# Input: AOD

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process('HiForest')
options = VarParsing.VarParsing ('analysis')
options.outputFile = 'HiForestAOD-Data.root'
options.inputFiles = 'file:/afs/cern.ch/user/r/rkunnawa/eoscms/cms/tier0/store/hidata/PARun2016C/PAEGJet1/AOD/PromptReco-v1/000/285/956/00000/D0D90241-88B5-E611-8B58-02163E0125F4.root'
options.parseArguments()

process.options = cms.untracked.PSet()

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()

if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
				options.inputFiles
				)
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("CondCore.DBCommon.CondDBCommon_cfi")
 
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_miniAODv2_v1', '')
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag


# Customization
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_pPb8TeV
process = overrideJEC_pPb8TeV(process)

process.GlobalTag.toGet.extend([
	cms.PSet(record = cms.string("HeavyIonRcd"),
		 tag = cms.string("CentralityTable_HFtowersPlusTrunc200_EPOS8TeV_v80x01_mc"),
                 #tag = cms.string("CentralityTable_HFtowersPlusTrunc200_EPOS5TeV_v80x01_mc"),
                 connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
                 label = cms.untracked.string("HFtowersPlusTruncEpos")
             ),
	cms.PSet(record = cms.string("L1TGlobalPrescalesVetosRcd"),
                tag = cms.string("L1TGlobalPrescalesVetos_Stage2v0_hlt"),
                connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                )
])

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(options.outputFile))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################

process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_DataPPb")

#####################################################################################

############################
# Event Analysis
############################

## temporary centrality bin
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("pACentrality")
process.centralityBin.centralityVariable = cms.string("HFtowersPlusTrunc")
#process.centralityBin.nonDefaultGlauberModel = cms.string("Hydjet_Drum")
process.centralityBin.nonDefaultGlauberModel = cms.string("Epos")

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_pPb_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi') #use data version to avoid PbPb MC
process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVertices")
process.hiEvtAnalyzer.doCentrality = cms.bool(True)
process.hiEvtAnalyzer.CentralitySrc = cms.InputTag("pACentrality")
process.hiEvtAnalyzer.CentralityBinSrc = cms.InputTag("centralityBin","HFtowersPlusTrunc")
process.hiEvtAnalyzer.doEvtPlane = cms.bool(True)
process.hiEvtAnalyzer.doMC = cms.bool(True) #general MC info
process.hiEvtAnalyzer.doHiMC = cms.bool(False) #HI specific MC info

process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.pfcandAnalyzer.pfPtMin = 0
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
process.pfcandAnalyzer.doUEraw_ = cms.untracked.bool(False)

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')

# Use this instead for track corrections
## process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_Corr_cff')

#####################################################################################

#####################
# photons
######################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerpp')
process.ggHiNtuplizer.VtxLabel           = cms.InputTag("offlinePrimaryVertices")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso            = cms.bool(False)
process.ggHiNtuplizer.doElectronVID      = cms.bool(True)
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerppGED'))

####################################################################################
#####################
# Electron ID
#####################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format to be processed
# DataFormat.AOD or DataFormat.MiniAOD
dataFormat = DataFormat.AOD
switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce. Check here https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Recipe_for_regular_users_for_7_4
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
#####################################################################################
#####################
# Rechit analyzer
#####################
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_pp_cfi')
process.rechitanalyzer.doVS = cms.untracked.bool(False)
process.rechitanalyzer.doEcal = cms.untracked.bool(False)
process.rechitanalyzer.doHcal = cms.untracked.bool(False)
process.rechitanalyzer.doHF = cms.untracked.bool(False)
process.rechitanalyzer.JetSrc = cms.untracked.InputTag("ak4CaloJets")
process.pfTowers.JetSrc = cms.untracked.InputTag("ak4CaloJets")

#####################
# New rho analyzer
#####################
process.load('HeavyIonsAnalysis.JetAnalysis.hiFJRhoAnalyzer_cff')

#####################
# Muon Analyzer
#####################
process.load('HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi')
process.hltMuTree.vertices = cms.InputTag("offlinePrimaryVertices")

#########################
# Main analysis list
#########################
process.ana_step = cms.Path(process.hltanalysis *
			    process.hltobject *
                            process.centralityBin *
			    process.hiEvtAnalyzer *
                            process.jetSequences +
                            #process.egmGsfElectronIDSequence + #Should be added in the path for VID module
                            #process.ggHiNtuplizer +
                            #process.ggHiNtuplizerGED +
                            process.hiFJRhoAnalyzer +
			    process.pfcandAnalyzer +
			    #process.hltMuTree +
                            process.HiForest +
			    process.trackSequencesPP +
                            process.runAnalyzer +
                            process.rechitanalyzer
)

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25)
)

process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
