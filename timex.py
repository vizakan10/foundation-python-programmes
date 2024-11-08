#import packages and modules created
import random
from datetime import datetime

#variable output is used to gather everything which are printed to display in text file

#to get the name for text file with the format of yyyy_mm_dd_hr_min_sec_random 4 didgt number
def time(output):
    current_datetime = datetime.now()
    year = str(current_datetime.year)
    month = str(current_datetime.month).zfill(2)
    day = str(current_datetime.day).zfill(2)
    hour = str(current_datetime.hour).zfill(2)
    minute = str(current_datetime.minute).zfill(2)
    second = str(current_datetime.second).zfill(2)

    random_number = random.randint(0, 9999)
    random_number_str = str(random_number).zfill(4)

    name = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second + "_" + random_number_str + ".txt"
    return name,output#it will return the name to mainx file and from there name will be given to text file
