import collections
import time


def write_file(file_name, write_mode, file_text):
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


try:
    f = open("KenoFiles/kenodbfull-1column.csv")
    lines = f.readlines()
    counter = collections.Counter(lines)
    hot_list = counter.most_common(5)
    for x in hot_list:
    	hot_log = "KenoFiles/HOT-Numbers.csv"
		hot_numbers = x[0]
		hot_numbers_break = hot_numbers.replace('\n', '')
		hot_time = time.strftime("%Y-%m-%d")
		hot_writeout = hot_numbers_break + "," + hot_time + "\n"
		write_file(hot_log,"a+",hot_writeout)

except Exception as hot_error:
    print "An error has occured while calculating the HOT numbers."
    print hot_error

write_file(hot_log,"a+","HOT NUMBERS ABOVE")
raw_input("Success! Press any key to continue...")
