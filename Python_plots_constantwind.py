# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:30:15 2024

@author: toon4
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path = "C:/Users/toon4/OneDrive - Delft University of Technology/Attachments/Desktop/THESIS/Simulations/SIMA_Simulations/Constant_Wind_Sim/Constant_Wind_Sim_15MW.xlsx"
excel_data = pd.ExcelFile(file_path)

rated_wind_speed = 10.59
# Rotor diameter and radius
rotor_diameter = 240  # in meters
rotor_radius = rotor_diameter / 2  # in meters

# Initialize lists to store results
wind_speeds = []
mean_rotor_speeds = []
mean_aero_forces_x = []
mean_pitch_angles = []
mean_generator_torques = []
mean_generator_outputs = []
tip_speed_ratios = []

# Iterate through each sheet (each wind speed)
for sheet_name in excel_data.sheet_names:
    # Extract wind speed from the sheet name (e.g., "Wind_4", "Wind_6")
    wind_speed = float(sheet_name.split("_")[1])  # Extracts the number after "Wind_"
    wind_speeds.append(wind_speed)
    
    # Load the data from the sheet
    data = excel_data.parse(sheet_name, header=1)
    data = data[1:].reset_index(drop=True)  # Drop the units row
    
    
    
    # Compute mean values for each variable
    mean_rotor_speed = data['Rotor speed (rpm)'].mean()  # Store in a variable for reuse
    mean_rotor_speeds.append(mean_rotor_speed)
    mean_aero_forces_x.append(data['Aero force X-dir in shaft system'].mean())
    mean_pitch_angles.append(data['Pitch angle blade 1, Line: bl1foil'].mean())
    mean_generator_torques.append(data['Mechanical generator torque on LSS'].mean())
    mean_generator_outputs.append(data['Electrical generator output'].mean())
    

    # Compute rotor speed in radians per second
    angular_velocity = mean_rotor_speed * (2 * np.pi / 60)  # Convert RPM to rad/s

    # Compute TSR
    tsr = (angular_velocity * rotor_radius) / wind_speed
    tip_speed_ratios.append(tsr)
    
# Sort the results by wind speed
sorted_data = sorted(zip(wind_speeds, mean_rotor_speeds, mean_aero_forces_x, mean_pitch_angles, mean_generator_torques, mean_generator_outputs))
wind_speeds, mean_rotor_speeds, mean_aero_forces_x, mean_pitch_angles, mean_generator_torques, mean_generator_outputs = zip(*sorted_data)




# Plot Mean Rotor Speed vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, mean_rotor_speeds, '-', label="Mean Rotor Speed", color='b')
plt.axvline(rated_wind_speed, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Mean Rotor Speed (RPM)")
plt.grid(True)
plt.legend()
plt.show()

# Plot Mean Aerodynamic Force in X-Direction vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, mean_aero_forces_x, '-', label="Mean Thrust Force", color='r')
plt.axvline(rated_wind_speed, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Mean Thrust Force (N)")
plt.grid(True)
plt.legend()
plt.show()

# Plot Mean Pitch Angle vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, mean_pitch_angles, '-', label="Mean Pitch Angle", color='g')
plt.axvline(rated_wind_speed, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Mean Pitch Angle (degrees)")
plt.grid(True)
plt.legend()
plt.show()

# Plot Mean Generator Torque vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, mean_generator_torques, '-', label="Mean Generator Torque", color='m')
plt.axvline(rated_wind_speed, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Mean Generator Torque (Nm)")
plt.grid(True)
plt.legend()
plt.show()

# Plot Mean Electrical Generator Output vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, mean_generator_outputs, '-', label="Mean Generator Output", color='c')
plt.axvline(rated_wind_speed, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Mean Electrical Generator Output (W)")
plt.grid(True)
plt.legend()
plt.show()

# Plot Tip Speed Ratio vs Wind Speed
plt.figure(figsize=(8, 6))
plt.plot(wind_speeds, tip_speed_ratios, '-', label="Tip Speed Ratio (TSR)", color='b')
plt.axvline(10.59, color='k', linestyle='--', label="Rated Wind Speed (10.59 m/s)")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Tip Speed Ratio (TSR)")
plt.grid(True)
plt.legend()
plt.show()