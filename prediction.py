#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import Sequential
from keras.layers import *
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import random


prediction_titles_ordered = [['neutralino_mass','sneutrino_mass','gluino_mass','Cha1_mass','Mzp_mass','stau_mass','selectron_mass','stop_mass','sbottom_mass','smuon_mass','h1_mass','BtoXsgamma','Bstomumu','BRBtotaunu','DD','relic_density']]
# Set the scaling parameters
mult_val = np.array([9.64908727e-04, 4.73685698e-04, 2.30138710e-04, 5.37714945e-04,
       3.75301260e-04, 4.46914704e-04, 5.04319865e-04, 2.85537134e-04,
       2.75480785e-04, 4.94999590e-04, 2.72952806e-01, 5.37006169e+04,
       4.86812898e+08, 1.36259772e+01, 3.49170469e+10, 1.04297038e+00])

add_val = np.array([-4.46924849e-01, -2.57956141e-01, -5.43897372e-01, -4.72026495e-01,
       -1.69261191e+00, -3.82271338e-01, -2.45129124e-01, -6.98028651e-01,
       -5.98451594e-01, -4.22871698e-01, -3.33002443e+01, -1.61360960e+01,
       -1.56489790e+00, -1.26259405e+01, -2.42219554e-05, -4.29703796e-02])

# Building the sample
m0 = np.random.uniform(0,3000,1000000)
m12 = np.random.uniform(0,3000,1000000)
A0 = np.random.uniform(-9000, 9000,1000000)
tanbeta = np.random.uniform(0.,60.,1000000)
tanbetaR = np.random.uniform(1.,1.2,1000000)
signmuR = []
for i in range(1000000):
    signmuR.append(random.choice((1,-1)))
VR = np.random.uniform(6500,20000,1000000)
Ys = np.random.uniform(0.001,0.99,1000000)
Yv = np.random.uniform(0.001,0.99,1000000)
sample = pd.DataFrame({
                'm0': m0,
                'm12': m12,
                'A0': A0,
                'tanbeta': tanbeta,
                'tanbetaR': tanbetaR,
                'VR': VR,
                'signmuR': signmuR,
                'Ys': Ys,
                'Yv': Yv})
sample.to_csv('sample.csv', index=False)

# Scale the sample
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_sample = scaler.fit_transform(sample)
scaled_sample_df = pd.DataFrame(scaled_sample, columns=sample.columns.values)
scaled_sample_df.to_csv("sample_scaled.csv", index=False)
# finding the parameters of scaling
#print("Note: sample values are scaled by multiplying by {:.10f} and adding {:.6f}".format(scaler.scale_, scaler.min_))

# Load the model
model = load_model('BLRSSM.h5')

# Prediction
X_prediction = pd.read_csv("sample_scaled.csv").values
prediction = model.predict(X_prediction)


# Re-scale the data from the 0-to-1 range back to dollars
# These constants are from when the data was originally scaled down to the 0-to-1 range
prediction = prediction - add_val
prediction = prediction / mult_val

# Export prediction as a csv file
#title = np.array(['neutralino_mass','sneutrino_mass','gluino_mass','Cha1_mass','Mzp_mass','stau_mass','selectron_mass','stop_mass','sbottom_mass','smuon_mass','h1_mass','BtoXsgamma','Bstomumu','BRBtotaunu','DD','relic_density'])
#title.reshape(1,16)
pred = pd.DataFrame({'neutralino_mass': prediction[:,0],
                     'sneutrino_mass': prediction[:,1],
                     'gluino_mass': prediction[:,2],
                     'Cha1_mass': prediction[:,3],
                     'Mzp_mass': prediction[:,4],
                     'stau_mass': prediction[:,5],
                     'selectron_mass': prediction[:,6],
                     'stop_mass': prediction[:,7],
                     'sbottom_mass': prediction[:,8],
                     'smuon_mass': prediction[:,9],
                     'h1_mass': prediction[:,10],
                     'BtoXsgamma': prediction[:,11],
                     'Bstomumu': prediction[:,12],
                     'BRBtotaunu': prediction[:,13],
                     'DD': prediction[:,14],
                     'relic_density': prediction[:,15]})
#pred_final = pred.combine_first(title)
pred.to_csv('Prediction.csv', index=False)
# Concatenate two csv files
prediction = pd.read_csv('Prediction.csv')
sample = pd.read_csv('sample.csv')
(pd.concat([sample,prediction], axis=1)).to_csv('Master_prediction.csv', index=False)

# Put the constraints to elicit benchmarks
mp = pd.read_csv('Master_prediction.csv')
Benchmarks = mp[(mp["h1_mass"]>=122) & (mp["h1_mass"]<=128) & (mp["gluino_mass"]>1750) & (mp["Cha1_mass"]>103.5) & (mp["Mzp_mass"]>4500) & (mp["Mzp_mass"]<10000) &  (mp["stau_mass"]>=105) & (mp["selectron_mass"]>107) & (mp["stop_mass"]>=730) & (mp["sbottom_mass"]>=222) & (mp["smuon_mass"]>94) & (mp["relic_density"]>=0.09) & (mp["relic_density"]<=0.14) & (mp["selectron_mass"]>mp["neutralino_mass"]) & (mp["BtoXsgamma"]>=0.000299) & (mp["BtoXsgamma"]<=0.000387) & (mp["Bstomumu"]<=6.4e-09) & (mp["Bstomumu"]>=1.1e-09) & (mp["BRBtotaunu"]>=0.15) & (mp["BRBtotaunu"]<=2.41)]
Benchmarks.to_csv('Benchmarks.csv', index=False)















