# Keno Data Logging - QuickKeno
# KDL v1.5.1
# aj@ayjayy.com
# Last Edit Date: 4/20/16

import urllib2
import json
import time


def write_file(file_name, write_mode, file_text):
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


#get the keno json file
ma_keno_json = urllib2.urlopen("http://www.masslottery.com/data/json/search/dailygames/todays/15.json")
#read from the json file
json_string = ma_keno_json.read()
#parse the json file so we can work with it
parsed_json = json.loads(json_string)
#get the min and max game and subtract them...
#...so we can get total number of games to iterate over
min_game = int(parsed_json['min'])
max_game = int(parsed_json['max'])
games = max_game - min_game

#script loop
while games > 0:
    #get info from "draws" section in json file + create error log
    orgOrder = parsed_json['draws'][games]['winning_num_org']
    sortedOrder = parsed_json['draws'][games]['winning_num']
    multiplier = parsed_json['draws'][games]['bonus']
    multi_int = parsed_json['draws'][games]['bonus_value']
    draw = parsed_json['draws'][games]['draw_id']
    #split on dashes 19 times to split up the 20 numbers
    orgOrder_split = orgOrder.split('-', 19)
    #join the 20 numbers with commas to accomodate the csv
    orgOrder_join = ",".join(orgOrder_split)
    orgOrder_column = "\n".join(orgOrder_split)
    #a way to string together the data using my "write file" function, this
    #also turns everything into a string format so I can concatenate them.
    long_text = str(orgOrder_join + "," + orgOrder + "," + sortedOrder + "," + multiplier + "," + multi_int + "," + draw) + "\n"
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
        #in case the user is running on demand, give success messages & log them
        print "Succesfully logged game #" + draw
        vlog_string = "<font size='1px'><strong>Succesfully logged game:</strong> " + draw + " <strong>|</strong> </font>" + "\n"
        sys_log = "KenoFiles/SYSLOG.html"
        write_file(sys_log,"a+",vlog_string)
    except Exception as eW:
        error_date_eW = time.strftime("%Y-%m-%d-%I:%M %p")
        error_text_eW =  str(eW) + " | " + "File Write Error" + " | " + error_date_eW + "<br \>" + "\n"
        sys_log = "KenoFiles/SYSLOG.html"
        log_html = "KenoFiles/LOG.html"
        html_text = """<button type="button" class="btn btn-danger">An error has occured while writing to one of the files. Check the log in /KenoFiles</button><br \>""" + "\n"
        write_file(sys_log,"a+",error_text_eW)
        write_file(log_html,"a+",html_text)
        print "An error has occured while writing to one of the files. Check the logs in /KenoFiles"
        break

    games = games - 1

#success - write to logs and print out in case this is an on demand run
games = max_game - min_game
success_date = time.strftime("%Y-%m-%d-%I:%M %p")
log_html = "KenoFiles/LOG.html"
sys_log = "KenoFiles/SYSLOG.html"
success_html = "<center><div class='bg-success' style='border:1px solid green;'><strong><font color='green'> KenoDB completed successfully" + " | " + success_date + " | Min Game: " + str(min_game) + " | Max Game: " + str(max_game) + " | Total Games: " + str(games) + "</font></strong></div></center><br \>" + "\n"
sys_success_html = """<button type="button" class="btn btn-success">KenoDB completed successfully""" + " | Date: " + success_date + " | Min Game: " + str(min_game) + " | Max Game: " + str(max_game) + " | Number Of Games: " + str(games) + "</button><br \>" + "\n"
write_file(log_html,"a+",sys_success_html)
write_file(sys_log,"a+",success_html)
print "KenoDB completed successfully"


