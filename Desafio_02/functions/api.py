import pandas as pd
import numpy as np
import csv
import json
import sys

def createDataframeConfig():
    data = [{"info": "co2", "unit": "PPM", "env": "activity-room", "val_ini": "-1000000", "val_end": "500"}, {"info": "co2", "unit": "PPM", "env": "refectory", "val_ini": "-1000000", "val_end": "400"}, {"info": "co2", "unit": "PPM", "env": "room-1", "val_ini": "-1000000", "val_end": "300"}, {"info": "co2", "unit": "PPM", "env": "bathroom-main", "val_ini": "-1000000", "val_end": "500"}, {"info": "co2", "unit": "PPM", "env": "garden", "val_ini": "-1000000", "val_end": "500"}, {"info": "temperature", "unit": "C", "env": "activity-room", "val_ini": "19", "val_end": "22"}, {"info": "temperature", "unit": "C", "env": "refectory", "val_ini": "20", "val_end": "23"}, {"info": "temperature", "unit": "C", "env": "room-1", "val_ini": "21", "val_end": "23"}, {"info": "temperature", "unit": "C", "env": "bathroom-main", "val_ini": "22", "val_end": "25"}, {"info": "temperature", "unit": "C", "env": "garden", "val_ini": "15", "val_end": "22"}, {"info": "humidity", "unit": "%", "env": "activity-room", "val_ini": "50", "val_end": "60"}, {"info": "humidity", "unit": "%", "env": "refectory", "val_ini": "50", "val_end": "70"}, {"info": "humidity", "unit": "%", "env": "room-1", "val_ini": "50", "val_end": "60"}, {"info": "humidity", "unit": "%", "env": "bathroom-main", "val_ini": "60", "val_end": "75"}, {"info": "humidity", "unit": "%", "env": "garden", "val_ini": "50", "val_end": "80"}, {"info": "sound", "unit": "dB", "env": "activity-room", "val_ini": "0", "val_end": "40"}, {"info": "sound", "unit": "dB", "env": "refectory", "val_ini": "20", "val_end": "35"}, {"info": "sound", "unit": "dB", "env": "room-1", "val_ini": "10", "val_end": "30"}, {"info": "sound", "unit": "dB", "env": "bathroom-main", "val_ini": "20", "val_end": "35"}, {"info": "sound", "unit": "dB", "env": "garden", "val_ini": "10", "val_end": "35"}, {"info": "illumination", "unit": "Lux", "env": "activity-room", "val_ini": "300", "val_end": "750"}, {"info": "illumination", "unit": "Lux", "env": "refectory", "val_ini": "200", "val_end": "500"}, {"info": "illumination", "unit": "Lux", "env": "room-1", "val_ini": "100", "val_end": "200"}, {"info": "illumination", "unit": "Lux", "env": "bathroom-main", "val_ini": "100", "val_end": "200"}, {"info": "illumination", "unit": "Lux", "env": "garden", "val_ini": "-1000000", "val_end": "1000000"}]
    df = pd.DataFrame(data)  
    return df  
    
def main(dict):
    try:
        if dict:
            config = createDataframeConfig()
            df = pd.DataFrame.from_dict(dict).reset_index()
            merged_df = df.merge(config, how='inner', left_on=["index", "room"], right_on=["info","env"])
        
            merged_df["values"]  = pd.to_numeric(merged_df["values"])
            merged_df["val_ini"] = pd.to_numeric(merged_df["val_ini"])
            merged_df["val_end"] = pd.to_numeric(merged_df["val_end"])
        
            alert_df = merged_df[~(merged_df['values'].between(merged_df['val_ini'], merged_df['val_end']))][['info']]
        
            result = alert_df.values.flatten().tolist()
        
        else:    
            result = []
    except:
        result = []
        
    return { 'alerts': result }
        

if __name__ == "__main__":
    dict = {
            "room": "bathroom-main",
            "values": {
                        "co2": 4000,
                        "temperature": 220,
                        "humidity": 70,
                        "sound": 30,
                        "illumination": 150
                       }
            }
    result = main(dict)    
    print(result)