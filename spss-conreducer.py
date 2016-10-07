# This programs reads the GSS data in SPSS and converts in a smaller file in CSV format for analysis.

# This program also has an option to return a cleaner data without missing values.
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro


print "\nHello!\n\n This program reads the General Social Survey(GSS) data in SPSS format\n and converts into csv file with the variables you want for analysis.\n\n As it might take a while to load the data, please take this time\n and consult the codebook that comes along with this program\n and choose the variables you want for your file.\n"

print "Reading file... \n"

gssfile = "GSS7214_R6a.sav"

ro.r('data <- foreign::read.spss("%s", to.data.frame=TRUE)' % gssfile)

print "Done!\n"


def spss_converter():
    variables = []
    done = False
    while not done:
        variable = raw_input("Enter a variable specified in the code book\n or hit 'enter' when you're done: ")
        if variable != "":
            variables.append(variable.lower())
        elif variable == "" or len(variables) == 0:
            done = True

    filename = raw_input("\nPlease enter the name of the output file: ")

    complete_cases = raw_input("Would you like a tidier data (no empty values)?\n ** That might affect the final of results ** (yes or no)? ")

    num = len(variables)
    ro.r('vector <- c()')
    for value in variables:
        ro.r('''
            for (i in 1:length("%s"))
            vector <- c(vector, "%s")''' % (num, value))

    done = False
    while not done:
        complete_cases = complete_cases.lower()
        if complete_cases == "yes":
            ro.r('data <- data[,vector]')
            ro.r('data <- data[complete.cases(data),]')
            ro.r('"%s" <- data' % filename)
            done = True
        elif complete_cases == "no" or vale == "":
            ro.r('"%s" <- data[,vector]' % filename)
            done = True
        else:
            "Please answer yes or no"

    print "\n Writing the csv file...\n"
    ro.r('write.csv(%s, "%s.csv")' %(filename, filename))
    print "Done!\n"
    print "Look for the file in the directory.\n\n"

spss_converter()

again = raw_input("Would you like to produce another file?\n Yes or No? ")
done = False
while not done:
    again = again.lower()
    if again == "yes":
        spss_converter()
    elif again == "no" or vale == "":
        print "\n\n Bye!"
        done = True
    else:
        "Please answer yes or no"
