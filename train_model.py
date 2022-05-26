#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import Sequential
from keras.layers import *
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

# Load training dataset and scale and export to a new csv file
training_data_df = pd.read_csv("ML_data_chosen.csv")
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_training = scaler.fit_transform(training_data_df)
scaled_training_df = pd.DataFrame(scaled_training, columns=training_data_df.columns.values)
scaled_training_df.to_csv("ML_data_scaled.csv", index=False)
mult_val = scaler.scale_[9:]
add_val = scaler.min_[9:]


# Building the model
training_data_df = pd.read_csv("ML_data_scaled.csv")
# Input
X = training_data_df[['m0','m12','A0','tanbeta','tanbetaR','VR','signmuR','Ys','Yv']].values
# Output
Y = training_data_df[['neutralino_mass','sneutrino_mass','gluino_mass','Cha1_mass','Mzp_mass','stau_mass','selectron_mass','stop_mass','sbottom_mass','smuon_mass','h1_mass','BtoXsgamma','Bstomumu','BRBtotaunu','DD','relic_density']].values
# Define the model
model = Sequential()
model.add(Dense(100, input_dim=9, activation='linear'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(16, activation='linear'))
model.compile(loss="mean_squared_error", optimizer="adam")

# Train the model
model.fit(
    X,
    Y,
    epochs=50,
    shuffle=True,
    verbose=2
)

# Save the model to disk
model.save("BLRSSM.h5")
print("Model saved to disk.")


