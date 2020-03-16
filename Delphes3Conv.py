import sys
import ROOT, array
from math import *
import random
import math
import argparse



from ROOT import TRandom, TFile, TLorentzVector
from ROOT.std import vector
from array import array




Delphes_Path="/home/tomas/Documentos/MG5_aMC_v2_6_6/Delphes/"
ROOT.gSystem.AddDynamicPath(Delphes_Path)
ROOT.gSystem.Load("libDelphes.so");

def GlobalAnalysisParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--DIR', help='Directory to read input')
    parser.add_argument('--XS', help='Sample cross section')
    parser.add_argument('--LUMI', help='Luminosity [pb-1]')
    parser.add_argument('--MLL', help='Minimum mll')
    parser.add_argument('--MET', help='Minimum met')
    parser.add_argument('--OUT', help='ROOT output file')
    parser.add_argument('--ANA', help='Analysis selector')
    parser.add_argument('--DELPHES', help='Delphes libraries location')
    return parser.parse_args()

args = GlobalAnalysisParser()








ER_Path="/home/tomas/Documentos/MG5_aMC_v2_6_6/ExRootAnalysis/"
ROOT.gSystem.AddDynamicPath(ER_Path)
ROOT.gSystem.Load("libExRootAnalysis.so");

try:
    ROOT.gInterpreter.Declare('#include "/home/tomas/Documentos/MG5_aMC_v2_6_6/Delphes/classes/DelphesClasses.h"')
    ROOT.gInterpreter.Declare('#include "/home/tomas/Documentos/MG5_aMC_v2_6_6/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')
    print "Delphes classes imported"
except:
    pass


#def BasketFile(FileName=args.OUT, OpenOption="RECREATE"):
    #try:
    #    if args.OUT is None: raise NameError('No file name was declared, please do!')
    #except NameError:
    #    raise
    #return ROOT.TFile(FileName, OpenOption)



inFileName = sys . argv [1]


fs = ROOT.TFile(inFileName)
#fs = ROOT.TFile("/home/tomas/Documentos/MG5_aMC_v2_6_6/pp2w+w-_13TeV/Events/run_01/tag_1_delphes_events.root")
s = fs.Get("Delphes")
otree = ROOT.ExRootTreeReader(s)
#Numero de eventos
ns = s.GetEntries()
#Carga las Ramas de Jets, Electrones y Muones del arbol de Delphes
jet = otree.UseBranch("Jet")
electron = otree.UseBranch("Electron")
muon = otree.UseBranch("Muon")
met = otree.UseBranch("MissingET")

myfile = TFile( "/home/tomas/Documentos/Python Notebooks/NewTree3.root", 'RECREATE' )
NewTree1 = ROOT.TTree( 'SystemTree', 'Arbol Deshojado' )

                
Jet1 = ROOT.TLorentzVector(0,0,0,0)
Jet2 = ROOT.TLorentzVector(0,0,0,0)
Jet3 = ROOT.TLorentzVector(0,0,0,0)
Jet4 = ROOT.TLorentzVector(0,0,0,0)

Elec1 = ROOT.TLorentzVector(0,0,0,0)
Elec2 = ROOT.TLorentzVector(0,0,0,0)

Muon1 = ROOT.TLorentzVector(0,0,0,0)
Muon2 = ROOT.TLorentzVector(0,0,0,0)

METNRGT = array( 'f', [ 0 ] )
METPhi= array( 'f', [ 0 ] )
METEta= array( 'f', [ 0 ] )

b_Jet1 = array( 'f', [ 0 ] )
b_Jet2 = array( 'f', [ 0 ] )
b_Jet3 = array( 'f', [ 0 ] )
b_Jet4 = array( 'f', [ 0 ] )

Tau_Jet1 = array( 'f', [ 0 ])
Tau_Jet2 = array( 'f', [ 0 ])
Tau_Jet3 = array( 'f', [ 0 ])
Tau_Jet4 = array( 'f', [ 0 ])




NewTree1.Branch( 'Jet1', Jet1 )
NewTree1.Branch( 'Jet2', Jet2 )
NewTree1.Branch( 'Jet3', Jet3 )
NewTree1.Branch( 'Jet4', Jet4 )

NewTree1.Branch( 'Elec1', Elec1 )
NewTree1.Branch( 'Elec2', Elec2 )

NewTree1.Branch( 'Muon1', Muon1 )
NewTree1.Branch( 'Muon2', Muon2 )

NewTree1.Branch( 'METNRGT', METNRGT,'METNRGT/F' )
NewTree1.Branch( 'METPhi', METPhi, 'METPhi/F' )
NewTree1.Branch( 'METEta', METEta, 'METEta/F')

NewTree1.Branch( 'b-Jet1' , b_Jet1, 'b-Jet1/F')
NewTree1.Branch( 'b-Jet2' , b_Jet2, 'b-Jet2/F')
NewTree1.Branch( 'b-Jet3' , b_Jet3, 'b-Jet3/F')
NewTree1.Branch( 'b-Jet4' , b_Jet4, 'b-Jet4/F')






NewTree1.Branch( 'Tau-Jet1' , Tau_Jet1, 'Tau-Jet1/F')
NewTree1.Branch( 'Tau-Jet2' , Tau_Jet2, 'Tau-Jet2/F')
NewTree1.Branch( 'Tau-Jet3' , Tau_Jet3, 'Tau-Jet3/F')
NewTree1.Branch( 'Tau-Jet4' , Tau_Jet4, 'Tau-Jet4/F')


for event in range(ns):
    otree.ReadEntry(event)
    
    if jet.GetEntries() == 0:
        Jet1.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet2.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet3.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet4.SetPtEtaPhiM(-10, -10,-10,-10)
	b_Jet1[0] = -3
	b_Jet2[0] = -3
	b_Jet3[0] = -3
	b_Jet4[0] = -3
	Tau_Jet1[0] = -3
	Tau_Jet2[0] = -3
	Tau_Jet3[0] = -3
	Tau_Jet4[0] = -3
        
        
    if jet.GetEntries() == 1:
        Jet1.SetPtEtaPhiM(jet.At(0).PT,jet.At(0).Eta,jet.At(0).Phi,jet.At(0).Mass)
        Jet2.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet3.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet4.SetPtEtaPhiM(-10, -10,-10,-10)
	b_Jet1[0] = jet.At(0).BTag
	b_Jet2[0] = -3
	b_Jet3[0] = -3
	b_Jet4[0] = -3
	Tau_Jet1[0] = jet.At(0).TauTag
	Tau_Jet2[0] = -3
	Tau_Jet3[0] = -3
	Tau_Jet4[0] = -3
    
    if jet.GetEntries() == 2:
        Jet1.SetPtEtaPhiM(jet.At(0).PT,jet.At(0).Eta,jet.At(0).Phi,jet.At(0).Mass)
        Jet2.SetPtEtaPhiM(jet.At(1).PT,jet.At(1).Eta,jet.At(1).Phi,jet.At(1).Mass)
        Jet3.SetPtEtaPhiM(-10, -10,-10,-10)
        Jet4.SetPtEtaPhiM(-10, -10,-10,-10)
	b_Jet1[0] = jet.At(0).BTag
	b_Jet2[0] = jet.At(1).BTag
	b_Jet3[0] = -3
	b_Jet4[0] = -3
	Tau_Jet1[0] = jet.At(0).TauTag
	Tau_Jet2[0] = jet.At(1).TauTag
	Tau_Jet3[0] = -3
	Tau_Jet4[0] = -3
        
    if jet.GetEntries() == 3:
        Jet1.SetPtEtaPhiM(jet.At(0).PT,jet.At(0).Eta,jet.At(0).Phi,jet.At(0).Mass)
        Jet2.SetPtEtaPhiM(jet.At(1).PT,jet.At(1).Eta,jet.At(1).Phi,jet.At(1).Mass)
        Jet3.SetPtEtaPhiM(jet.At(2).PT,jet.At(2).Eta,jet.At(2).Phi,jet.At(2).Mass)
        Jet4.SetPtEtaPhiM(-10, -10,-10,-10)
	b_Jet1[0] = jet.At(0).BTag
	b_Jet2[0] = jet.At(1).BTag
	b_Jet3[0] = jet.At(2).BTag
	b_Jet4[0] = -3
	Tau_Jet1[0] = jet.At(0).TauTag
	Tau_Jet2[0] = jet.At(1).TauTag
	Tau_Jet3[0] = jet.At(2).TauTag
	Tau_Jet4[0] = -3        

    if jet.GetEntries() >= 4:
        Jet1.SetPtEtaPhiM(jet.At(0).PT,jet.At(0).Eta,jet.At(0).Phi,jet.At(0).Mass)
        Jet2.SetPtEtaPhiM(jet.At(1).PT,jet.At(1).Eta,jet.At(1).Phi,jet.At(1).Mass)
        Jet3.SetPtEtaPhiM(jet.At(2).PT,jet.At(2).Eta,jet.At(2).Phi,jet.At(2).Mass)
        Jet3.SetPtEtaPhiM(jet.At(3).PT,jet.At(3).Eta,jet.At(3).Phi,jet.At(3).Mass)
	b_Jet1[0] = jet.At(0).BTag
	b_Jet2[0] = jet.At(1).BTag
	b_Jet3[0] = jet.At(2).BTag
	b_Jet4[0] = jet.At(3).BTag
	Tau_Jet1[0] = jet.At(0).TauTag
	Tau_Jet2[0] = jet.At(1).TauTag
	Tau_Jet3[0] = jet.At(2).TauTag
	Tau_Jet4[0] = jet.At(3).TauTag
    
    
    if muon.GetEntries() == 0:
        Muon1.SetPtEtaPhiM(-10, -10,-10,-10)
        Muon2.SetPtEtaPhiM(-10, -10,-10,-10)
    
    if muon.GetEntries() == 1:
        Muon1.SetPtEtaPhiM(muon.At(0).PT,muon.At(0).Eta,muon.At(0).Phi,0.10566)
        Muon2.SetPtEtaPhiM(-10, -10,-10,-10)
    
    if muon.GetEntries() >= 2:
        Muon1.SetPtEtaPhiM(muon.At(0).PT,muon.At(0).Eta,muon.At(0).Phi,0.10566)
        Muon2.SetPtEtaPhiM(muon.At(1).PT,muon.At(1).Eta,muon.At(1).Phi,0.10566)
    
    
    
    
    if electron.GetEntries() == 0:
        Elec1.SetPtEtaPhiM(-10, -10,-10,-10)
        Elec2.SetPtEtaPhiM(-10, -10,-10,-10)
        
    if electron.GetEntries() == 1:
        Elec1.SetPtEtaPhiM(electron.At(0).PT,electron.At(0).Eta,electron.At(0).Phi,0.0005110)
        Elec2.SetPtEtaPhiM(-10, -10,-10,-10)
    
    if electron.GetEntries() >= 2:
        Elec1.SetPtEtaPhiM(electron.At(0).PT,electron.At(0).Eta,electron.At(0).Phi,0.0005110)
        Elec2.SetPtEtaPhiM(electron.At(1).PT,electron.At(1).Eta,electron.At(1).Phi,0.0005110)
    
    
    METNRGT[0] = met.At(0).MET
    METPhi[0] = met.At(0).Phi
    METEta[0] = met.At(0).Eta
    
    
    
    NewTree1.Fill()

NewTree1.Write()
args.OUT.Close()
