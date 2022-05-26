#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
from pandas import Series, DataFrame
import sys
import pyslha
import xslha

# Input file
m0=[]
m12=[]
A0=[]
signmuR=[]
tanbeta=[]
tanbetaR=[]
VR=[]
Ys=[]
Yv=[]

# Output file
selectron=[]
mneutralino=[]
msneutrino=[]
DD_SI=[]
relic_density=[]
Mmh1=[]
gluino=[]
cha1=[]
zp=[]
stau=[]
stop=[]
sbottom=[]
smuon=[]
BtoXsgamma=[]
Bstomumu=[]
BRBtotaunu=[]



n_runs = len(os.listdir('/home/Universe/Research/BLRSSM/Cluster_run/Primary_run'))
n_runs1 = len(os.listdir('/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run'))

for i in range(1,n_runs+1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Primary_run/SPhenoOutputs'+str(i)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(i,file)
            content = pyslha.read(path + '/' + file)
        
            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino<sneutrino


            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128

            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
    
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
        	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
       
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
       	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
                #LHC constraints and BPhysics
                cha1.append(content.blocks["MASS"][1000024])
                zp.append(content.blocks["MASS"][99])
                stau.append(content.blocks["MASS"][1000015])
                selectron.append(content.blocks["MASS"][1000011])
                stop.append(content.blocks["MASS"][1000006])
                sbottom.append(content.blocks["MASS"][1000005])
                smuon.append(content.blocks["MASS"][1000013])
                mneutralino.append(neutralino)
                msneutrino.append(sneutrino)
                Mmh1.append(mh1)
                gluino.append(content.blocks["MASS"][1000021])
                BtoXsgamma.append(content.blocks["FLAVORKITQFV"][200])
                Bstomumu.append(content.blocks["FLAVORKITQFV"][4006])
                BRBtotaunu.append(content.blocks["FLAVORKITQFV"][503])
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])

for j in range(0,n_runs1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run/SPhenoOutputs'+str(j)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(j,file)
            content = pyslha.read(path + '/' + file)
        
            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino<sneutrino


            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128

            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
    
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
        	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
       
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
       	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
                #LHC constraints and BPhysics
                cha1.append(content.blocks["MASS"][1000024])
                zp.append(content.blocks["MASS"][99])
                stau.append(content.blocks["MASS"][1000015])
                selectron.append(content.blocks["MASS"][1000011])
                stop.append(content.blocks["MASS"][1000006])
                sbottom.append(content.blocks["MASS"][1000005])
                smuon.append(content.blocks["MASS"][1000013])
                mneutralino.append(neutralino)
                msneutrino.append(sneutrino)
                Mmh1.append(mh1)
                gluino.append(content.blocks["MASS"][1000021])
                BtoXsgamma.append(content.blocks["FLAVORKITQFV"][200])
                Bstomumu.append(content.blocks["FLAVORKITQFV"][4006])
                BRBtotaunu.append(content.blocks["FLAVORKITQFV"][503])
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])



df1 = pd.DataFrame({
                'm0': m0,
                'm12': m12,
                'A0': A0,
                'tanbeta': tanbeta,
                'tanbetaR': tanbetaR,
                'VR': VR,
                'signmuR': signmuR,
                'Ys': Ys,
                'Yv': Yv,
                'neutralino_mass': mneutralino,
                'sneutrino_mass': msneutrino,
                'gluino_mass': gluino,
                'Cha1_mass': cha1,
                'Mzp_mass':zp,
                'stau_mass': stau,
                'selectron_mass': selectron,
                'stop_mass':stop,
                'sbottom_mass': sbottom,
                'smuon_mass': smuon,
                'h1_mass': Mmh1,
                'BtoXsgamma': BtoXsgamma,
                'Bstomumu': Bstomumu,
                'BRBtotaunu': BRBtotaunu,
                'DD': DD_SI,
                'relic_density': relic_density})
df1.to_csv('ML_data.csv')

