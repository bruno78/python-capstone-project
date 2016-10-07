## Gunlaws Mass Shootings (gunlaws_mass_shootings.csv)
Bruno G. Tavares

### Introduction
Gunlaws Mass Shootings is a data set that has been cleaned, filtered and merged from two bigger data sets comprised of 3 subsets


### Source Data

* 'GSS7214_R6a.sav': List of the years from 1972 to 2014, the variable "gunlaw" which contains opinions on gun control laws. It also contains the variables race, sex, age and region of the respondents (not for public display).

* 'mj-1982-2016-US-mass-shootings.csv': List of the years from 1982-2016 and each observation corresponds to a mass shooting incident.

The General Social Survey data can be found and downloaded at:

<http://gss.norc.org/About-The-GSS>

The Mother Jones investigation on mass shootings data can be found and downloaded at:

<http://www.motherjones.com/politics/2012/07/mass-shootings-map>


### Subsets

gunlaws_mass_shootings.csv consists data from mass_shootings_per_year.csv and gunlaws_opinions.csv

mass_shootings_per_year.csv consists data from mj-198202016-US-mass-shootings.csv

gunlaw_opinion.csv consists data from tdgunlaw.csv

age_frequency.csv consists data from tdgunlaw.csv

tdgunlaw.csv consists data from GSS7214_R6a.sav


### Process

* Step1: Run spss-conreducer.py to read GSS7214_R6a.csv file and input the variables, year, id, sex, race, age, region, gunlaw. Give a name to the file input 'yes' for complete cases. In this case, it creates tdgunlaw.csv

* Step2: The script gunlaw-cript.py uses tdgunlaw.csv to calculate the total of respondents per year, the average age of the respondents per year, the proportion of answers in favor of gun permits per year, the average age of respondents in favor, the proportion of answers in opposition to gun permits per year, the average age of respondents in opposition. It creates a new file: gunlaw_opinion.csv and age_frequency.csv

* Step3: Use mass_shootings.py script to read mj-1982-2016-US-mass-shootings.csv and calculate how many mass shoots per year. it creates mass_shootings_per_year.csv

* Step4: the script twodatasets.py will take mass_shootings_per_year.csv and gunlaw_opinion.csv and it merges both files returning gunlaws_mass_shootings.csv


### Variables


#### TDGUNLAW.CSV

**year** - respective year of the survey

**id** - id of the respondent

**sex** - gender of the respondent

**race** - race of the respondent

**age** - age of the respondent

**region** - region of the interview

**gunlaw** - favor or oppose gun permits


#### GUNLAW_OPINION.CSV

**Year** - respective year of the survey

**Total** - total of respondents on respective year

**AverageAge** - average age of total respondents per year

**GunLawFavor** - proportion of respondents who answered 'FAVOR' per year

**GLFAvgAge** - average age of respondents who answered 'FAVOR' per year

**GunLawOppose** - proportion of respondents who answered 'OPPOSE' per year

**GLOAvgAge** - average age of respondents who answered 'OPPOSE' per year


#### GUNLAWS_MASS_SHOOTINGS.CSV

**Year** - year

**Total** - total of respondents per year

**AverageAge** - average age of total respondents per year

**GunLawFavor** - proportion of respondents who answered 'FAVOR' per year

**GLFAvgAge** - average age of respondents who answered 'FAVOR' per year

**GunLawOppose** - proportion of respondents who answered 'OPPOSE' per year

**GLOAvgAge** - average age of respondents who answered 'OPPOSE' per year

**MassShootings** - total of mass shootings registered per year


#### AGE_FREQUENCY.CSV

**Year** - respective year of the survey

**Age_Frequency** - age frequency of the respondents per year

**FavorAgeFrquency** - age frequency of the respondents who answered 'FAVOR' per year

**OpposeAgeFrequency** - age frequency of the respondents who answered 'FAVOR' per year


#### MASS_SHOOTINGS_PER_YEAR.CSV

**Year** - respective year of mass shootings

**MassShootings** - total of mass shootings registered per year
