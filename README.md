#  Massachusetts KenoDB Logger

**Requirements:**
Python 2.*

**_~In order to track the whole day's data you must run this nightly AFTER 1:05 AM EST. Reccomended: 1:20AM~_**

This program is setup so you can easily track Keno numbers. It outputs two files, a full log of the day's numbers in multiple formats and other draw info, as well as a list of the numbers drawn for the day in a single row to do pivot table analysis on the hot/coldness of numbers.

Included is an Access database file with a table that has the correct header titles and rows created to accept the data from the program.

*Windows Users Note:* Using the task scheduler you can use the nightly.bat file to create a nightly task. Just edit the nightly.bat file to fit your file locations / Windows Username.