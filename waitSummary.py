#Authors: Ashutosh Shivakumar, Sean Banerjee
#Purpose: Provide summary statistics (mean, min, max, standard deviation) of head, left-hand, right-hand, and eye gaze from the VR system. 

import os
import pandas as pd
import statistics
import math
from prettytable import PrettyTable

def process_csv_files(root_folder, timestamp_col_name='Timestamp(ns)'):
    samples_per_second_list = []

    #EyeGazeLog_NOTIFICATION, HeadPositionLog_NOTIFICATION, LeftHandLog_NOTIFICATION, RightHandLog_NOTIFICATION
    #EyeGazeLog_WITHOUT_NOTIFICATION, HeadPositionLog_WITHOUT_NOTIFICATION, LeftHandLog_WITHOUT_NOTIFICATION, RightHandLog_WITHOUT_NOTIFICATION
    modalities = ["EyeGazeLog_NOTIFICATION", "HeadPositionLog_NOTIFICATION", "LeftHandLog_NOTIFICATION", "RightHandLog_NOTIFICATION",
    "EyeGazeLog_WITHOUT_NOTIFICATION","HeadPositionLog_WITHOUT_NOTIFICATION", "LeftHandLog_WITHOUT_NOTIFICATION", "RightHandLog_WITHOUT_NOTIFICATION"]

    t = PrettyTable(['Treatment', 'Type of Data', 'Min', 'Max', 'Mean', 'SD'])

    for submodalities in modalities:
        print("")
        print("Processing..." + submodalities)
        samples_per_second_list.clear()
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:            
                if filename.endswith(submodalities+".csv"):
                    file_path = os.path.join(dirpath, filename)
                    
                    try:
                        df = pd.read_csv(file_path, delimiter=',(?![^\(]*[\)])', engine='python', index_col= False)

                        df[timestamp_col_name] = pd.to_datetime(df[timestamp_col_name], unit = 'ns')

                        df = df.set_index(timestamp_col_name)                        
                        df_resampled = df.resample('1s').size()

                        df_resampled_without_index = df_resampled.values
                        samples_per_second_list.append(df_resampled_without_index.mean())

                    except Exception as e:
                        print(f"  Error processing {filename}: {e}")
        
        #print("Number of Participants: ", len(samples_per_second_list))

        #Calculate minimum
        min_avg_value = min(samples_per_second_list)        
        #Calculate maximum
        max_avg_value = max(samples_per_second_list)
        #Calculate mean
        overall_mean = statistics.mean(samples_per_second_list)
        #Calculate standard deviation
        overall_standard_deviation = statistics.stdev(samples_per_second_list)
        
        if "WITHOUT_NOTIFICATION" in submodalities:
            if "Eye" in submodalities:
                row = ["Without Notification", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["Without Notification", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["Without Notification", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["Without Notification", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
        else:
            if "Eye" in submodalities:
                row = ["With Notification", "Eye", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Head" in submodalities:
                row = ["With Notification", "Head", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Left" in submodalities:
                row = ["With Notification", "Left", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
            if "Right" in submodalities:
                row = ["With Notification", "Right", "{:.2f}".format(min_avg_value),"{:.2f}".format(max_avg_value),"{:.2f}".format(overall_mean),"{:.2f}".format(overall_standard_deviation)]
        t.add_row(row)
        t.add_divider()
    print(t)

if __name__ == "__main__":
    #Data path is assumed to be 'VRData'
    root_folder_path = 'VRData'
    process_csv_files(root_folder_path)