#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Hiwot Zewdie (hz196@duke.edu)
# Date:   Fall 2020
#------------------------------------------------------------
#Ask user for a search date
user_date = input("Specify a date to search for Sara [M/D/YYYY]: ")


# create a variable pointing to the data file 
file_name = './data/raw/sara.txt'

#create a file object from the file 
file_object = open(file_name,'r')

#read entire content of data file into lists 
line_list = file_object.readlines()

#close the file
file_object.close()

#create 2 empty dictionary objects 
date_dict = {}
coord_dict = {}


#Iterate through all lines in the lineList from line 17 on 
for lineString in line_list: 
    if lineString[0] in ("#","u"): continue

    #split the string into a line of data items 
    lineData = lineString.split()
  
    #extract items in list into variables 
    record_id = lineData[0]
    obs_date =  lineData[2]
    obs_lc = lineData[4]
    if obs_lc not in ("1", "2", "3"):
        continue 
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat , obs_lon)
    
#create empty list to hold matching keys 
matching_keys =[]

#loop through items in the date_dict and collect kets for matching ones
for date_item in date_dict.items():
    #get the key and date of the dictionary item
    the_key,the_date = date_item #tuple separates out into 2 values 
    #see if the date matches the user date
    if the_date == user_date: 
        #if so add the key to the list
        matching_keys.append(the_key)
    
#if no matching keys tell user 
if len(matching_keys) == 0:
    print(f"No observations on {user_date}")
    
        
#reveal locations for each key in matching_keys 
for matching_key in matching_keys :
    obs_lat, obs_lon = coord_dict[matching_key]
    the_date = date_dict[matching_key]
    #print location of sara
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon: {obs_lon} on {user_date}")