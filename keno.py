# Keno Data Logging - Full Data
# KDL v1.5
# AYJAY@programmer.net
# Last Edit Date: 4/11/16

import urllib2
import json
import time

def write_file(file_name, write_mode, file_text):
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


#get the keno json file
f = urllib2.urlopen("http://www.masslottery.com/data/json/search/dailygames/todays/15.json")
#read from the json file
json_string = f.read()
#parse the json file so we can work with it
parsed_json = json.loads(json_string)
#get the min and max game and subtract them
#so we can get total number of games to iterate over
min_game = int(parsed_json['min'])
max_game = int(parsed_json['max'])
games = max_game - min_game

#program loop
while games > 0:
    #get info from "draws" section in json file + Create error log
    try:
        orgOrder = parsed_json['draws'][games]['winning_num_org']
        sortedOrder = parsed_json['draws'][games]['winning_num']
        multiplier = parsed_json['draws'][games]['bonus']
        multi_value = parsed_json['draws'][games]['bonus_value']
        draw = parsed_json['draws'][games]['draw_id']
        #split on dashes 19 times to split up the 20 numbers
        orgOrder_split = orgOrder.split('-', 19)
        #join the 20 numbers with commas to accomodate the csv
        orgOrder_join = ",".join(orgOrder_split)
        orgOrder_column = "\n".join(orgOrder_split)
    except Exception as e:
        logfile = "KenoFiles/LOG.csv"
        error_date = time.strftime("%Y-%m-%d-%I:%M %p")
        error_text =  str(e) + "," + "Number of Games Error" + "," + error_date + "\n"
        write_file(logfile, "a+", error_text)
        print "Too Few Games Played So Far. Currently at: " + str(games)
        games = games - 1
        continue

    #a way to string together the data using my "write file" function, this
    #also turns everything into a string format so I can concatenate them.
    long_text = str(orgOrder_join + "," + orgOrder + "," + sortedOrder + "," + multiplier + "," + multi_value + "," + draw) + "\n"
    #also put the numbers in a single row for alternate file
    single_row = str(orgOrder_column + "\n")

    #write out to the files individually
    try:
        #format today's date for the filename and set it
        date = time.strftime("%Y-%m-%d")
        kenodbfile = "KenoFiles/Daily/kenodb" + str(date) + ".csv"
        #write a new daily file
        write_file(kenodbfile, "a+", long_text)
        #append to the master file
        write_file("KenoFiles/kenodbfull.csv", "a+", long_text)
        #append to the single column file
        write_file("KenoFiles/kenodbfull-1column.csv", "a+", single_row)
        #incase the user is running on demand, give success messages
        print "Succesfully logged game #" + draw
    except Exception as eW:
        logfile_eW = "KenoFiles/LOG.csv"
        error_date_eW = time.strftime("%Y-%m-%d-%I:%M %p")
        error_text_eW =  str(eW) + "," + "File Write Error" + "," + error_date_eW + "\n"
        write_file(logfile_eW, "a+", error_text_eW)
        print "An error has occured while writing to the file. Check the log in KenoFiles/LOG.csv"
        break

    games = games - 1
    #wait for a bit to limit amount of hits to the MA-KENO servers
    time.sleep(0.25)
    print "Sleeping...."

#success
logfile_success = "KenoFiles/LOG.csv"
success_date = time.strftime("%Y-%m-%d-%I:%M %p")
success_text = "KenoDB completed successfully" + "," + success_date + "," + min_game + "," + max_game + "\n"
write_file(logfile_success, "a+", success_text)
