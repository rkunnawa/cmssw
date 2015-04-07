#ifndef JetAnalyzer_HeavyIons_matching_H
#define JetAnalyzer_HeavyIons_matching_H


//
// Jet Tester class for heavy ion jets. for DQM jet analysis monitoring 
// For CMSSW_7_5_X, especially reading background subtracted jets 
// author: Raghav Kunnawalkam Elayavalli,
//         April 6th 2015 
//         Rutgers University, email: raghav.k.e at CERN dot CH 
//
// this class will be very similar to the class available in the validation suite under RecoJets/JetTester_HeavyIons 
//


#include <memory>
#include <fstream>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "CommonTools/TriggerUtils/interface/GenericTriggerEventFlag.h"
#include "FWCore/Utilities/interface/EDGetToken.h"

#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/JetReco/interface/JPTJet.h"
#include "DataFormats/JetReco/interface/JPTJetCollection.h"
#include "DataFormats/JetReco/interface/PFJet.h"

#include "DataFormats/CaloTowers/interface/CaloTower.h"
#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/CandidateWithRef.h"

// include the basic jet for the PuPF jets. 
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/BasicJetCollection.h"
// include the pf candidates 
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
// include the voronoi subtraction
#include "DataFormats/HeavyIonEvent/interface/VoronoiBackground.h"
#include "RecoHI/HiJetAlgos/interface/UEParameters.h"
// include the centrality variables
#include "DataFormats/HeavyIonEvent/interface/Centrality.h"

#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "RecoJets/JetProducers/interface/JetIDHelper.h"
#include "DQMOffline/JetMET/interface/JetMETDQMDCSFilter.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/DetId/interface/DetId.h"

#include "DataFormats/Scalers/interface/DcsStatus.h" 
#include "PhysicsTools/SelectorUtils/interface/JetIDSelectionFunctor.h"
#include "PhysicsTools/SelectorUtils/interface/PFJetIDSelectionFunctor.h"
#include "DQMServices/Core/interface/DQMEDAnalyzer.h"
#include <map>
#include <string>


const Int_t MAXPARTICLE = 10000;

class MonitorElement;

class JetAnalyzer_HeavyIons_matching : public DQMEDAnalyzer {
 public:

  explicit JetAnalyzer_HeavyIons_matching (const edm::ParameterSet&);
  virtual ~JetAnalyzer_HeavyIons_matching();
  
  void analyze(const edm::Event&, const edm::EventSetup&) override; 
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;
  
 private:
  
  edm::InputTag   mInputCollection;
  edm::InputTag   mInputPFCandCollection;
  edm::InputTag   centrality;
  
  std::string     mOutputFile;
  std::string     JetType;
  std::string     UEAlgo;
  edm::InputTag   Background;
  double          mRecoJetPtThreshold;
  double          mReverseEnergyFractionThreshold;
  double          mRThreshold;
  std::string     JetCorrectionService;

  //Tokens
  edm::EDGetTokenT<std::vector<reco::Vertex> > pvToken_;
  edm::EDGetTokenT<CaloTowerCollection > caloTowersToken_;
  edm::EDGetTokenT<reco::CaloJetCollection> caloJetsToken_;
  edm::EDGetTokenT<reco::PFJetCollection> pfJetsToken_;
  edm::EDGetTokenT<reco::BasicJetCollection> basicJetsToken_;
  edm::EDGetTokenT<reco::JPTJetCollection> jptJetsToken_;
  edm::EDGetTokenT<reco::PFCandidateCollection> pfCandToken_; 
  edm::EDGetTokenT<reco::CandidateView> pfCandViewToken_;
  edm::EDGetTokenT<reco::CandidateView> caloCandViewToken_;

  //edm::EDGetTokenT<reco::VoronoiMap> backgrounds_;
  edm::EDGetTokenT<edm::ValueMap<reco::VoronoiBackground>> backgrounds_;
  edm::EDGetTokenT<std::vector<float>> backgrounds_value_;
  edm::EDGetTokenT<reco::Centrality> centralityToken_;
  edm::EDGetTokenT<std::vector<reco::Vertex> > hiVertexToken_;



};


#endif 
