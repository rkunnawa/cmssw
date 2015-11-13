// -*- C++ -*-
//
// Package:    hltanalyzer/testAnalyzer
// Class:      testAnalyzer
// 
/**\class testAnalyzer testAnalyzer.cc hltanalyzer/testAnalyzer/plugins/testAnalyzer.cc

   Description: [one line class summary]

   Implementation:
   [Notes on implementation]
*/
//
// Original Author:  Raghav Kunnawalkam Elayavalli
//         Created:  Fri, 13 Nov 2015 16:12:33 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"

#include "TTree.h"
#include "TROOT.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

using namespace std;
using namespace reco;
using namespace edm;


class testAnalyzer : public edm::EDAnalyzer{
public:
  explicit testAnalyzer(const edm::ParameterSet&);
  ~testAnalyzer();
  
private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  void clearAllGlobalVectors();
  
  // ----------member data ---------------------------

  edm::InputTag mInputCollection;
  edm::EDGetTokenT<reco::CaloJetCollection> caloJetsToken_;

  edm::Service<TFileService> fout;
  TTree * jetTree;
  int event, run, lumi, hiBin;
  double vz, vx, vy;
  std::vector <float> jet_pt;  
  std::vector <float> jet_eta;  
  std::vector <float> jet_phi;  

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
testAnalyzer::testAnalyzer(const edm::ParameterSet& iConfig):
  mInputCollection               (iConfig.getParameter<edm::InputTag>       ("src"))
  // //now do what ever initialization is needed
  // usesResource("TFileService");
{
  caloJetsToken_  = consumes<reco::CaloJetCollection>(mInputCollection);

}


testAnalyzer::~testAnalyzer()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

void testAnalyzer::clearAllGlobalVectors()
{

  jet_pt.clear();
  jet_eta.clear();
  jet_phi.clear();

}

// ------------ method called for each event  ------------
void testAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  clearAllGlobalVectors();

  cout<<"In the analyze function"<<endl;

  event = iEvent.id().event();
  run = iEvent.id().run();
  lumi = iEvent.id().luminosityBlock();
  
  // edm::Handle< vector<reco::Vertex> > vertex;
  // iEvent.getByLabel(tagVtx,vertex);
  // if(vertex->size() > 0){
  //   vx = vertex->begin()->x();
  //   vy = vertex->begin()->y();
  //   vz = vertex->begin()->z();
  // } else {
  //   vx = -1;
  //   vy = -1;
  //   vz = -1;
  // }


  std::vector<Jet> recoJets;
  recoJets.clear();
  
  edm::Handle<CaloJetCollection>  caloJets;
  iEvent.getByToken(caloJetsToken_, caloJets);

  if (!caloJets.isValid()) {
    return;
  }
  
  for (unsigned ijet=0; ijet<caloJets->size(); ijet++) {
    recoJets.push_back((*caloJets)[ijet]);
  } 

  for (unsigned ijet=0; ijet<recoJets.size(); ijet++) {

    // if(fabs(recoJets[ijet].eta()) > 2.0) continue;
    jet_pt.push_back(recoJets[ijet].pt());
    jet_eta.push_back(recoJets[ijet].eta());
    jet_phi.push_back(recoJets[ijet].phi());
    
  }// jet loop

  jetTree->Fill();
  
}


// ------------ method called once each job just before starting event loop  ------------
void  testAnalyzer::beginJob()
{

  cout<<"In the begin job function"<<endl;

  jetTree = fout->make<TTree>("jetTree","hltPuAK4CaloJetsCorrectedIDPassed");
  
  jetTree->Branch("event", &event, "event/I");
  jetTree->Branch("run", &run, "run/I");
  jetTree->Branch("lumi", &lumi, "lumi/I");
  // jetTree->Branch("vx", &vx, "vx/I");
  // jetTree->Branch("vy", &vy, "vy/I");
  // jetTree->Branch("vz", &vz, "vz/I");
  jetTree->Branch("jet_pt",&jet_pt);
  jetTree->Branch("jet_eta",&jet_eta);
  jetTree->Branch("jet_phi",&jet_phi);

}

// // ------------ method called once each job just after ending the event loop  ------------
// void 
// testAnalyzer::endJob() 
// {
// }

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
// void
// testAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
//   //The following says we do not know what parameters are allowed so do no validation
//   // Please change this to state exactly what you do use, even if it is no parameters
//   edm::ParameterSetDescription desc;
//   desc.setUnknown();
//   descriptions.addDefault(desc);
// }

//define this as a plug-in
DEFINE_FWK_MODULE(testAnalyzer);
