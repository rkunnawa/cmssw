import FWCore.ParameterSet.Config as cms

#--------------------------------------------------------------------------
# LOCAL RECO

# Tracker
from RecoVertex.BeamSpotProducer.BeamSpot_cfi import *
from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *

# Ecal
from RecoLocalCalo.Configuration.ecalLocalRecoSequence_cff import *
from RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi import *

# Hcal
from RecoLocalCalo.Configuration.hcalLocalReco_cff import *
from RecoLocalCalo.Configuration.hcalLocalRecoNZS_cff import *

#castor
from RecoLocalCalo.CastorReco.CastorSimpleReconstructor_cfi import *

# Muons
from RecoLocalMuon.Configuration.RecoLocalMuon_cff import *

from RecoLuminosity.LumiProducer.lumiProducer_cff import *

#--------------------------------------------------------------------------
# HIGH LEVEL RECO

from RecoHI.Configuration.Reconstruction_HI_cff import *
from RecoHI.Configuration.Reconstruction_hiPF_cff import *
from RecoLocalCalo.Castor.Castor_cff import *
from RecoHI.HiEgammaAlgos.HiElectronSequence_cff import *

#--------------------------------------------------------------------------

caloReco = cms.Sequence(ecalLocalRecoSequence*hcalLocalRecoSequence)
hbhereco = hbheprereco.clone()
hcalLocalRecoSequence.replace(hbheprereco,hbhereco)
muonReco = cms.Sequence(trackerlocalreco+muonlocalreco+lumiProducer)
localReco = cms.Sequence(offlineBeamSpot*muonReco*caloReco*castorreco)

#hbherecoMB = hbheprerecoMB.clone()
#hcalLocalRecoSequenceNZS.replace(hbheprerecoMB,hbherecoMB)
caloRecoNZS = cms.Sequence(caloReco+hcalLocalRecoSequenceNZS)
localReco_HcalNZS = cms.Sequence(offlineBeamSpot*muonReco*caloRecoNZS)

#--------------------------------------------------------------------------
# Main Sequences

reconstructionHeavyIons = cms.Sequence(localReco*globalRecoPbPb*CastorFullReco)
reconstructionHeavyIons_wConformalPixel = cms.Sequence(localReco*globalRecoPbPb_wConformalPixel*CastorFullReco)
reconstructionHeavyIons_HcalNZS = cms.Sequence(localReco_HcalNZS*globalRecoPbPb)

reconstructionHeavyIonsStep1 = cms.Sequence(localReco*globalRecoPbPbStep1)
reconstructionHeavyIonsStep2 = cms.Sequence(globalRecoPbPbStep2*CastorFullReco)



#--------------------------------------------------------------------------
