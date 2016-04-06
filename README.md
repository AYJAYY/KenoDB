#  Massachusetts KenoDB Logger

**Requirements:**
Python 2.*

**_In order to accurately track the day's data you must run this program nightly AFTER 1:05 AM EST. I reccomend using 1:20AM._**

This program is setup so you can easily track keno numbers. It outputs two files, a full log of the day's numbers in multiple formats and other draw info, as well as a list of the numbers drawn for the day in a single row to do pivot table analysis on the hot/coldness of numbers.

Included is an Access database file with a table that has the correct header titles and rows created to accept the data from the program.

*Note:* Using the task scheduler you can use the nightly.bat file as a cron job on windows PC's. Just download the zip file and edit the nightly.bat file to fit your file locations / Windows Username