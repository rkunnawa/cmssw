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


JetAnalyzer_HeavyIons_matching::JetAnalyzer_HeavyIons_matching(const edm::ParameterSet& iConfig) :
  mInputJet1Collection           (iConfig.getParameter<edm::InputTag>       ("src_Jet1")),
  mInputJet2Collection           (iConfig.getParameter<edm::InputTag>       ("src_Jet2")),
  JetType1                       (iConfig.getUntrackedParameter<std::string>("Jet1")),
  JetType2                       (iConfig.getUntrackedParameter<std::string>("Jet2")),
  mRecoJetPtThreshold            (iConfig.getParameter<double>              ("recoJetPtThreshold")),
  mRecoDelRMatch                 (iConfig.getParameter<double>              ("recoDelRMatch")),
  mRecoJetEtaCut                 (iConfig.getParameter<double>              ("recoJetEtaCut"))
{
  std::string inputCollectionLabelJet1(mInputJet1Collection.label());
  std::string inputCollectionLabelJet2(mInputJet2Collection.label());
  
  //consumes

  if(std::string("VsCalo") == JetType1) caloJet1Token_ = consumes<reco::CaloJetCollection>(mInputJet1Collection);
  if(std::string("VsPF") == JetType1) pfJetsToken_ = consumes<reco::PFJetCollection>(mInputJet1Collection);
  if(std::string("PuCalo") == JetType1) caloJet2Token_ = consumes<reco::CaloJetCollection>(mInputJet1Collection);
  if(std::string("PuPF") == JetType1) basicJetsToken_ = consumes<reco::BasicJetCollection>(mInputJet1Collection);

  if(std::string("VsCalo") == JetType2) caloJet1Token_ = consumes<reco::CaloJetCollection>(mInputJet2Collection);
  if(std::string("VsPF") == JetType2) pfJetsToken_ = consumes<reco::PFJetCollection>(mInputJet2Collection);
  if(std::string("PuCalo") == JetType2) caloJet2Token_ = consumes<reco::CaloJetCollection>(mInputJet2Collection);
  if(std::string("PuPF") == JetType2) basicJetsToken_ = consumes<reco::BasicJetCollection>(mInputJet2Collection);

  // initialize the Jet matching histograms

  mpT_ratio_Jet1Jet2 = 0;
  mpT_Jet1_matched = 0;
  mpT_Jet2_matched = 0;
  mpT_Jet1_unmatched = 0;
  mpT_Jet2_unmatched = 0;
}
   
void JetAnalyzer_HeavyIons_matching::bookHistograms(DQMStore::IBooker & ibooker, edm::Run const & iRun,edm::EventSetup const &) 
  {

    ibooker.setCurrentFolder("JetMET/JetValidation/"+mInputJet1Collection.label()+mInputJet2Collection.label());
    
    mpT_ratio_Jet1Jet2 = ibooker.book1D("Ratio_Jet1pT_vs_Jet2pT","",100, 0, 20);
    mpT_Jet1_matched = ibooker.book1D("Jet1_matched_jet_Spectra","",1000, 0, 1000);
    mpT_Jet2_matched = ibooker.book1D("Jet2_matched_jet_Spectra","",1000, 0, 1000);
    mpT_Jet1_unmatched = ibooker.book1D("Jet1_unmatched_jet_Spectra","",1000, 0, 1000);
    mpT_Jet2_unmatched = ibooker.book1D("Jet2_unmatched_jet_Spectra","",1000, 0, 1000);

    if (mOutputFile.empty ()) 
      LogInfo("OutputInfo") << " Histograms will NOT be saved";
    else 
      LogInfo("OutputInfo") << " Histograms will be saved to file:" << mOutputFile;


  }



//------------------------------------------------------------------------------
// ~JetAnalyzer_HeavyIons
//------------------------------------------------------------------------------
JetAnalyzer_HeavyIons_matching::~JetAnalyzer_HeavyIons_matching() {}


//------------------------------------------------------------------------------
// beginJob
//------------------------------------------------------------------------------
//void JetAnalyzer_HeavyIons_matching::beginJob() {
//  std::cout<<"inside the begin job function"<<endl;
//}


//------------------------------------------------------------------------------
// endJob
//------------------------------------------------------------------------------
//void JetAnalyzer_HeavyIons_matching::endJob()
//{
//  if (!mOutputFile.empty() && &*edm::Service<DQMStore>())
//    {
//      edm::Service<DQMStore>()->save(mOutputFile);
//    }
//}


//------------------------------------------------------------------------------
// analyze
//------------------------------------------------------------------------------
void JetAnalyzer_HeavyIons_matching::analyze(const edm::Event& mEvent, const edm::EventSetup& mSetup)
{

  // Get the Jet collection
  //----------------------------------------------------------------------------
  
  std::vector<Jet> recoJet1;
  recoJet1.clear();
  std::vector<Jet> recoJet2;
  recoJet2.clear();
  
  edm::Handle<CaloJetCollection>  caloJet1;
  edm::Handle<CaloJetCollection>  caloJet2;
  edm::Handle<JPTJetCollection>   jptJets;
  edm::Handle<PFJetCollection>    pfJets;
  edm::Handle<BasicJetCollection> basicJets;

  //std::cout<<"Jet1 = "<<JetType1<<" and Jet 2 = "<<JetType2<<std::endl;

  if(std::string("VsCalo") == JetType1) {
    mEvent.getByToken(caloJet1Token_, caloJet1);
    for (unsigned ijet=0; ijet<caloJet1->size(); ijet++) recoJet1.push_back((*caloJet1)[ijet]);
  }
  if(std::string("PuCalo") == JetType1) {
    mEvent.getByToken(caloJet2Token_, caloJet1);
    for (unsigned ijet=0; ijet<caloJet1->size(); ijet++) recoJet1.push_back((*caloJet1)[ijet]);
  }
  if(std::string("VsPF") == JetType1) {
    mEvent.getByToken(pfJetsToken_, pfJets);
    for (unsigned ijet=0; ijet<pfJets->size(); ijet++) recoJet1.push_back((*pfJets)[ijet]);
  }
  if(std::string("PuPF") == JetType1) {
    mEvent.getByToken(basicJetsToken_, basicJets);
    for (unsigned ijet=0; ijet<basicJets->size(); ijet++) recoJet1.push_back((*basicJets)[ijet]);
  }

  if(std::string("VsCalo") == JetType2) {
    mEvent.getByToken(caloJet1Token_, caloJet2);
    for (unsigned ijet=0; ijet<caloJet2->size(); ijet++) recoJet2.push_back((*caloJet2)[ijet]);
  }
  if(std::string("PuCalo") == JetType2) {
    mEvent.getByToken(caloJet2Token_, caloJet2);
    for (unsigned ijet=0; ijet<caloJet2->size(); ijet++) recoJet2.push_back((*caloJet2)[ijet]);
  }
  if(std::string("VsPF") == JetType2) {
    mEvent.getByToken(pfJetsToken_, pfJets);
    for (unsigned ijet=0; ijet<pfJets->size(); ijet++) recoJet2.push_back((*pfJets)[ijet]);
  }
  if(std::string("PuPF") == JetType2) {
    mEvent.getByToken(basicJetsToken_, basicJets);
    for (unsigned ijet=0; ijet<basicJets->size(); ijet++) recoJet2.push_back((*basicJets)[ijet]);
  }

  // start to perform the matching - between recoJet1 and recoJet2.

  Int_t Jet1_nref = recoJet1.size();
  Int_t Jet2_nref = recoJet2.size();

  //std::cout<<"Jet1_nref = "<<recoJet1.size()<<std::endl;
  //std::cout<<"Jet2_nref = "<<recoJet2.size()<<std::endl;

  //if(Jet1_nref==0 || Jet2_nref==0) return;

  int jet1 = 0;
  int jet2 = 0; 
  
  std::vector <MyJet> vJet1, vJet2;
  std::vector <int> Jet1_ID(Jet1_nref), Jet2_ID(Jet2_nref);
  
  
  for(unsigned ijet1 = 0; ijet1 < recoJet1.size(); ++ijet1){

    //std::cout<<" pt of jet "<< ijet1 <<" in jet collection1 = "<<recoJet1[ijet1].pt()<<std::endl;
    //std::cout<<" eta of jet "<< ijet1 <<" in jet collection1 = "<<recoJet1[ijet1].eta()<<std::endl;
    //std::cout<<" phi of jet "<< ijet1 <<" in jet collection1 = "<<recoJet1[ijet1].phi()<<std::endl;

    if(recoJet1[ijet1].pt() < mRecoJetPtThreshold) continue;
    if(fabs(recoJet1[ijet1].eta()) < mRecoJetEtaCut) continue;

    MyJet JET1;
    JET1.eta = recoJet1[ijet1].eta();
    JET1.phi = recoJet1[ijet1].phi();
    JET1.pt  = recoJet1[ijet1].pt();
    JET1.id  = ijet1; 

    vJet1.push_back(JET1);
    jet1++;

  }// first jet loop

  for(unsigned ijet2 = 0; ijet2 < recoJet2.size(); ++ijet2){
    
    //std::cout<<" pt of jet "<< ijet2 <<" in jet collection2 = "<<recoJet2[ijet2].pt()<<std::endl;
    //std::cout<<" eta of jet "<< ijet2 <<" in jet collection2 = "<<recoJet2[ijet2].eta()<<std::endl;
    //std::cout<<" phi of jet "<< ijet2 <<" in jet collection2 = "<<recoJet2[ijet2].phi()<<std::endl;

    if(recoJet2[ijet2].pt() < mRecoJetPtThreshold) continue;
    if(fabs(recoJet2[ijet2].eta()) < mRecoJetEtaCut) continue;

    MyJet JET2;
    JET2.eta = recoJet1[ijet2].eta();
    JET2.phi = recoJet1[ijet2].phi();
    JET2.pt  = recoJet1[ijet2].pt();
    JET2.id  = ijet2; 

    vJet2.push_back(JET2);
    jet2++;

  }// second jet loop

  bool onlyJet1     = (jet1>0  && jet2==0)  ? true : false;
  bool onlyJet2     = (jet1==0 && jet2 >0)  ? true : false;
  bool bothJet1Jet2 = (jet1>0  && jet2 >0)  ? true : false;
  
  int matchedJets   = 0;
  int unmatchedJet1 = 0;
  int unmatchedJet2 = 0;  

  std::vector < MyJet >::const_iterator iJet, jJet;

  if(onlyJet1) {

    for(iJet = vJet1.begin(); iJet != vJet1.end(); ++iJet){

      int pj = (*iJet).id;
      
      mpT_Jet1_unmatched->Fill(recoJet1[pj].pt());
      //std::cout<<"first unmatched Jet = "<<recoJet1[pj].pt()<<std::endl;

    }

  }else if(onlyJet2) {

    for(iJet = vJet2.begin(); iJet != vJet2.end(); ++iJet){

      int cj = (*iJet).id;

      mpT_Jet2_unmatched->Fill(recoJet2[cj].pt());
      //std::cout<<"second unmatched Jet = "<<recoJet2[cj].pt()<<std::endl;
    }
    
  }else if (bothJet1Jet2){

    ABMatchedJets mABMatchedJets; 

    for(iJet = vJet1.begin(); iJet != vJet1.end(); ++iJet){
      for(jJet = vJet2.begin(); jJet != vJet2.end(); ++jJet){
	mABMatchedJets.insert(std::make_pair(*iJet, *jJet));	
      }
    }

    ABItr itr;
    // matched Jets matching Jet 1 to Jet 2 
    for(itr = mABMatchedJets.begin(); itr != mABMatchedJets.end(); ++itr){

      ABJetPair jetpair = (*itr);
      MyJet Aj = jetpair.first;
      MyJet Bj = jetpair.second;

      float delr = JetAnalyzer_HeavyIons_matching::deltaRR(Bj.eta, Bj.phi, Aj.eta, Aj.phi);

      if( delr < mRecoDelRMatch && Jet1_ID[Aj.id] == 0){

	mpT_ratio_Jet1Jet2->Fill((Float_t) recoJet2[Bj.id].pt()/recoJet1[Aj.id].pt());

	mpT_Jet1_matched->Fill(recoJet1[Aj.id].pt());
	mpT_Jet2_matched->Fill(recoJet2[Bj.id].pt());
	
	Jet1_ID[Aj.id] = 1;
	Jet2_ID[Bj.id] = 1;

	matchedJets++; 

	//std::cout<<"matched Jet 1 pT = "<<recoJet1[Aj.id].pt()<<std::endl;
	//std::cout<<"matched Jet 2 pT = "<<recoJet2[Bj.id].pt()<<std::endl;

      }

    }

    // for unmatched Jets 
    for(itr = mABMatchedJets.begin(); itr != mABMatchedJets.end(); ++itr){

      ABJetPair jetpair = (*itr);

      MyJet Aj = jetpair.first;
      MyJet Bj = jetpair.second;

      if(Jet1_ID[Aj.id] == 0) {

	mpT_Jet1_unmatched->Fill(recoJet1[Aj.id].pt());
	unmatchedJet1++;
	Jet1_ID[Aj.id] = 1; 
       
      }

      if(Jet2_ID[Bj.id] == 0) {

	mpT_Jet2_unmatched->Fill(recoJet2[Bj.id].pt());
	unmatchedJet2++;
	Jet2_ID[Bj.id] = 1; 
       
      }
      
    }
    

  }// both Jet1 and Jet2 in the event. 


}


  
