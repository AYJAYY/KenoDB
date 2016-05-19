#  Massachusetts Keno Numbers Logger
#### QuickKeno - http://ayjayy.github.io/KenoDB/

[![Python 2.*](https://img.shields.io/badge/python-2.7-blue.svg)](http://python.org) [![Version 1.5](https://img.shields.io/badge/version-1.5.1-brightgreen.svg)](https://github.com/AYJAYY/KenoDB) [![Updated FREQUENTLY](https://img.shields.io/badge/Live%20Project-Beta-red.svg)](#)

**_~In order to track the whole day's data you must run this nightly AFTER 1:05 AM EST. Reccomended: 1:20AM EST~_**

This script outputs several files to the /KenoFiles directory, a full log of the day's numbers and other draw info, as well as a list of the numbers drawn for the day in a single column to do pivot table analysis on the hot/coldness of numbers. For troubleshooting it logs all successes and failures into two HTML log files.

Also included is an Access database file with a table that has the correct header titles and rows created to import the data from the kenodbfull.csv file.

******NEW******
The file "HOT.py" is an on-demand file that will calculate the hottest 5 numbers from the data collected from the main program.

*Windows Users Note:* Using the task scheduler you can use the nightly.bat file to create a nightly task. Just edit the nightly.bat file to fit your file locations / Windows Username. Then you can add a nightly task to run the nightly.bat file. For more information on scheduling a task click the link below.

[_Microsoft Schedule a Task Guide_](https://technet.microsoft.com/en-us/library/cc748993.aspx)

[![Contact AYJAY](https://img.shields.io/badge/contact-AYJAY-orange.svg)](mailto:ayjay@programmer.net)



