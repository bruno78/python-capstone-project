# Capstone: Retrieving, Processing, and Visualizing Data with Python
## "America's Views on Gun Permits" project

### Introduction

This project is the final assignment of [*Capstone: Retrieving, Processing, and Visualizing Data with Python*](https://www.coursera.org/learn/python-capstone) which is the last course of 5 from the Python for Everybody Specialization series offered by University of Michigan on Coursera.

The final project was divided into three assignments:

*Exploring Data Sources* assignment has the goal to let you select, process and visualize the data of your choice and make a small presentation. The data chosen was the General Social Survey (GSS) data by NORC at University of Chicago. It's a very complex and broad data which according to the [GSS.NORC](http://gss.norc.org/About-The-GSS) website:

>for more than four decades, the General Social Survey (GSS) has studied the growing complexity of American society. It is the only full-probability, personal-interview survey designed to monitor changes in both social characteristics attitudes currently being conducted in the United States.

With this data, the question posed was, "How have Americans views changed regarding gun control through the years?"

*Accessing New Data Sources* the task for this assignment is to make a presentation that reflects the progress to date in retrieving and cleaning your data source to perform your analysis.

For this process, a few scripts were created to make calculations on the data. Instead of numbers, proportions were calculated to show the percentage of people in 'FAVOR' or 'OPPOSE' to gun control laws. The overall average age were computed as well as for each case favor/oppose. The data on Mass Shootings from the [Mother Jones](http://www.motherjones.com/politics/2012/07/mass-shootings-map) news website was added for comparison. A script for that data was created where it calculated the total of mass shootings per year and was then grouped in a new and smaller CSV file containing only the year and number of mass shootings per year.

*Vizualizing new Data Sources* the third and the last part of the Project assignment is presenting the analysis of the data visually.

The final result of this project was presented in a blog post available for reading [America's View on Gun Permits](http://brunogtavares.com/2016/09/16/gun-control-laws.html). Graphs were created in D3js and R for data visualization.


**NOTE:** The work showed here is for educational purposes only.

### This project contains:

1. GSS7214_R6a.sav - GSS main data set (not for public display)
2. GSScodebook.pdf - GSS codebook in pdf format for consultation
3. spss-conreducer.py - A Python program that takes the variables needed from the GSS data, and asks the user if they want it without NA values to create a smaller CSV file for analysis
4. tdgunlaw.csv - Tidy data in CSV format on Gun Control Laws
5. table-viewer.py - A Python script that transforms the tidy date in sqlite file for visualization
6. tdgunlaws.sqlite - Tidy data in sqlite format
7. mj-1982-2016-US-mass-shootings.csv - Data set on mass shootings from Mother Jones website
8. mass_shootings.py - A Python script for taking data out of Mother Jones data set
9. mass_shootings_per_year.csv - Data set containing the total mass shottings per year
10. gunlaw-script.py - A Python script that makes calculations on tdgunlaw
11. gunlaw_opinion.csv - Data set on gun law opinions and average age per year from tdgunlaw
12. age_frequency.csv - Data set on age frequency from tdgunlaw  
13. twodatasets.py - A script to combine gunlaw_opinion and mass_shootings_per_year data sets
14. gunlaws_mass_shootings.csv - Data set containing gun law opinions and mass shootings per year
15. graph.html - html file containing a line graph for data visualization
16. gun-control-script.R - R script plotting comparative graphs Mass Shootings vs Gun Control, Plotting Mass Shootings vs Amount of Victims laws, and correlation calculations on Gun Control laws vs Mass Shootings
17. mass_shootings-vs-gunlaws.svg - graph in svg format
18. README.md - read me file in markdown format explaining the process
19. codebook.md - codebook in markdown format containing information about the scripts and different data variables

### Process

#### *Exploring Data Sources* assignment

For this assignment I created a generic program spss-conreducer.py that would read the GSS data in SPSS format and ask to input variables (listed in the gss codebook.pdf), to produce a smaller CSV file. To try to answer the question "How have Americans views changed regarding gun control through the years?", the variables "year","id","sex","race","age","region","gunlaw" were chosen. Even though I could only have chosen "year" and "gunlaw", the others were included in case further questions came up along the way. The result of this process is the tdgunlaw.csv file, a tidy data (with no missing values).

#### *Accessing New Data Sources*

For the second part of this process, I decided to take the tdgunlaw.csv data and calculate the proportions as well as the average age for easy visualizing and broader understanding of the data. The script gunlaw-script.py takes tdgunlaw.csv and calculates the overall average age of the the population, the average age of people who are in favor, as well as, of people who oppose gun control laws per year. It also returns the total of people interviewed per year. The result of this process is the file gunlaw_opinion.csv where it contains the variables "Year", "Total", "AverageAge", "GunLawFavor", "GLFAvgAge", "GunLawOppose", "GLOAvgAge".

The gunlaw_opinion.csv shows 3 major peaks for favorable opinions, one in 1974 with 76.14%, another in 1993 with 82.5%, and the third in 1998 with 83.54%. Considering that between 1985 and 1990 we have an increase of 10%, my next questions were "Why do we have these three major peaks?", "why the sudden increase?", and "why after 1998 does favorability decrease, despite more mass shootings?". From 1998 to 2014, basically we have a decrease of 10%. To try to answer these questions, I considered the following possibilities:

1. Who were the presidents?
2. What major crimes occurred, such as mass shootings and/or serial killing sprees?
3. What terrorists threats or attacks occurred?
4. What was the media influence (such as Fox News) on the gun control issue?

So, I looked into Mother Jones data on US Mass Shootings but unfortunately the data covered was only from 1982 to 2016; however, that would still shed some light on my question number 2. The script mass_shootings.py was created to calculate the total number of mass shootings per year and create a smaller file mass_shootings_per_year.csv, containing the variables "Year" and "MassShootings". That gave me a clearer idea on the numbers. The Mother Jones data divides mass shootings in two categories "mass shootings" and "spree", but I decided to calculate them together since both involve killings of more than one person.  

To consolidate the data, I created another script twodatasets.py where I used mass_shootings_per_year.csv and gunlaw_opinion.csv and added them together. This way I could put them on the same graph to see possible correlations.

#### *Visualizing new Data Sources*

The last part of the process involves creating graphs and reporting the results. For graphs, I decided to use D3js which gave me the flexibility to insert the data into HTML format and manipulate it however I wanted. I also used R's ggplot for the Mother Jones data for speed. The data report was published on my own personal blog and it can be found [America's View on Gun Permits](http://brunogtavares.com/2016/09/16/gun-control-laws.html).

### Programs and Scripts

#### spss-conreducer.py

* reads the GSS file gss7214_R6a.sav in SPSS format
* asks the user to enter the variables from the file that are listed in the gss codebook
* asks if the user wants the data free from NA (missing values)
* creates a new file in CSV format with the set of variables chosen by the user

#### gunlaw-script.py

* reads the tdgunlaw.csv file
* calculates the total of respondents per year
* calculates the total average age of respondents per year
* calculates the proportion of respondents in 'FAVOR' per year
* calculates the average age of respondents in 'FAVOR' per year
* calculates the proportion of respondents in 'OPPOSE' per year
* calculates the average age of respondents in 'OPPOSE' per year
* creates a new file in CSV format with a new set of variables based on calculations

#### mass_shootings.py

* reads the mj-1982-2016-US-mass-shootings.csv file
* calculates the total mass shooting incidents per year
* creates a new file in CSV format with year and total mass shootings per year

#### twodatasets.py

* reads two files: gunlaw_opinion.csv and mass_shootings_per_year.csv
* merges two files
* creates a new merged file in CSV format

### Data files

See [codebook](https://github.com/bruno78/python-capstone-project/blob/master/codebook.md) for more details

*Note:* To see the version control process ask me to see the bitbucket account. There are files such as GSS data set that is not available for public display.

### Sources

The General Social Survey data:

<http://gss.norc.org/About-The-GSS>

Mother Jones:

<http://www.motherjones.com/politics/2012/07/mass-shootings-map>

Bruno G. Tavares's page:

<http://brunogtavares.com>

For Github repo:

<http://github.org/bruno78>

Coursera:

<https://www.coursera.org>

Python for Everybody Specialization:

<https://www.coursera.org/specializations/python>
