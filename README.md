# Soil Moisture Sensor Calibration — Raspberry Pi Pico

This repository contains a mini-project to **calibrate a capacitive soil moisture sensor** using a **Raspberry Pi Pico** and **MicroPython**.  
The objective is to build a calibration curve that accurately converts the analog readings from the sensor into **soil moisture percentage (%)**.

## 🗒️ Overview

Capacitive soil moisture sensors provide an analog voltage proportional to the water content in soil.  
However, this relationship depends on several factors.

This project aims to experimentally determine the calibration curve that maps **ADC readings** from the Raspberry Pi Pico to real **soil moisture values**.

## ⚙️ Components & Materials

| Component | Description |
|------------|--------------|
| **Raspberry Pi Pico** | Microcontroller used for reading analog signals |
| **Capacitive soil moisture sensor** | v2.0.0 |
| **Breadboard + jumper wires** | For connections |
| **Power supply** | 3.3V from Pico |
| **Soil sample** | From dry to saturated |
| **Scale** | To determine water content gravimetrically |


## 📊 Calibration Procedure

1. **Prepare the soil sample**
   - Start by drying the soil sample in an oven at **95–100°C for 10 minutes**. This will be the **dry reference sample**.
   - Measure the dry soil mass using a scale to determine the weight that corresponds to **0% humidity**.

2. **Insert the sensor**
   - Place the capacitive soil moisture sensor into the soil sample, ensuring consistent depth.

3. **Record sensor data**
   - Record the **ADC value** and the **corresponding voltage** from the Raspberry Pi Pico.  
     *(Use the script `get_measurements.py` for data collection.)*

4. **Water the soil sample until saturation**
   - Gradually add water until the soil is completely wet.  
   - Wait for the sample to expel excess water before taking the next readings. This process may take some time, so ensure that all soil is uniformly moistened. 

5. **Repeat measurements for 5 to 8 days**
   - Take daily readings to observe variations. 
   - **Don't forget to measure the soil mass each day!**

6. **Build the calibration curve**
   - Use your preferred analysis tool to plot the relationship between **ADC readings** and **soil moisture percentage (%).**
   - Fit the data using a **linear** or **polynomial regression** to obtain the **calibration equation**.



