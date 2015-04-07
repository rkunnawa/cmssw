//
// Jet Analyzer class for heavy ion jets. for DQM jet analysis monitoring 
// For CMSSW_7_5_X, especially reading background subtracted jets - jet matching 1 - 1 
// author: Raghav Kunnawalkam Elayavalli,
//         April 6th 2015 
//         Rutgers University, email: raghav.k.e at CERN dot CH 
//


#include "DQMOffline/JetMET/interface/JetAnalyzer_HeavyIons_matching.h"

using namespace edm;
using namespace reco;
using namespace std;

// declare the constructors:


JetAnalyzer_HeavyIons::JetAnalyzer_HeavyIons(const edm::ParameterSet& iConfig) :
  mInputJet1Collection           (iConfig.getParameter<edm::InputTag>       ("src_Jet1")),
  mInputJet2Collection           (iConfig.getParameter<edm::InputTag>       ("src_Jet2")),
  JetType1                       (iConfig.getUntrackedParameter<std::string>("JetType1")),
  UEAlgo1                        (iConfig.getUntrackedParameter<std::string>("UEAlgo1")),
  JetType2                       (iConfig.getUntrackedParameter<std::string>("JetType2")),
  UEAlgo2                        (iConfig.getUntrackedParameter<std::string>("UEAlgo2")),
  mRecoJetPtThreshold            (iConfig.getParameter<double>              ("recoJetPtThreshold"))
{
  std::string inputCollectionLabel(mInputCollection.label());

  //consumes
  caloJetsToken_  = consumes<reco::CaloJetCollection>(mInputCollection);
  jptJetsToken_   = consumes<reco::JPTJetCollection>(mInputCollection);
  if (isPFJet)   {
    if(std::string("Pu")==UEAlgo) basicJetsToken_    = consumes<reco::BasicJetCollection>(mInputCollection);
    if(std::string("Vs")==UEAlgo) pfJetsToken_    = consumes<reco::PFJetCollection>(mInputCollection);
  }

  pfCandToken_ = consumes<reco::PFCandidateCollection>(mInputPFCandCollection);
  pfCandViewToken_ = consumes<reco::CandidateView>(mInputPFCandCollection);
  caloCandViewToken_ = consumes<reco::CandidateView>(edm::InputTag("towerMaker"));
  backgrounds_ = consumes<edm::ValueMap<reco::VoronoiBackground> >(Background);  
  backgrounds_value_ = consumes<std::vector<float> >(Background);
  centralityToken_ = consumes<reco::Centrality>(centrality);
  hiVertexToken_ = consumes<std::vector<reco::Vertex> >(edm::InputTag("hiSelectedVertex"));

  // initialize the Jet matching histograms 

}
   
void JetAnalyzer_HeavyIons::bookHistograms(DQMStore::IBooker & ibooker, edm::Run const & iRun,edm::EventSetup const &) 
  {

    ibooker.setCurrentFolder("JetMET/JetValidation/"+mInputCollection.label());
    
    

    if (mOutputFile.empty ()) 
      LogInfo("OutputInfo") << " Histograms will NOT be saved";
    else 
      LogInfo("OutputInfo") << " Histograms will be saved to file:" << mOutputFile;


  }



//------------------------------------------------------------------------------
// ~JetAnalyzer_HeavyIons
//------------------------------------------------------------------------------
JetAnalyzer_HeavyIons::~JetAnalyzer_HeavyIons() {}


//------------------------------------------------------------------------------
// beginJob
//------------------------------------------------------------------------------
//void JetAnalyzer_HeavyIons::beginJob() {
//  std::cout<<"inside the begin job function"<<endl;
//}


//------------------------------------------------------------------------------
// endJob
//------------------------------------------------------------------------------
//void JetAnalyzer_HeavyIons::endJob()
//{
//  if (!mOutputFile.empty() && &*edm::Service<DQMStore>())
//    {
//      edm::Service<DQMStore>()->save(mOutputFile);
//    }
//}

