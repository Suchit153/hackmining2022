import pandas as pd
import csv
import serial
import time

s = serial.Serial("/dev/ttyACM0", 115200)

fieldnames = ["Time", "Anchor", "Distance"]

with open("data_output.csv", 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    while(True):
       
        try:
            read =  s.readline()
            
            substr = read.split()
            print(substr)
            info = {
                "Time": substr[0],
                "Anchor": substr[1],
                "Distance": substr[2]
            }
            
            csv_writer.writerow(info)
        
        except KeyboardInterrupt:
            break

        time.sleep(0.5)