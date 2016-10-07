
setwd("~/Desktop/Exercises/python-capstone")
library(plyr)
######################### Gun Laws Favor Opinion ##################################

data <- read.csv2("gunlaw_opinion.csv", sep = ",")
df <- data.frame(data)
View(df)
library(ggplot2)

year = df$Year
favor = df$GunLawFavor
ggplot(df, aes(x = year, y = favor, group=1)) + geom_line(aes(group=1))

mjdata <- read.csv2("mass_shootings_per_year.csv", sep =",")
mass <- data.frame(mjdata)
View(mjdata)

year = mass$Year
massshootings = mass$MassShootings
ggplot(mass, aes(x = year, y = massshootings, group=1)) + geom_line(aes(group=1))

############################## Mass Shootings vs Gun Control laws ##########################################

glms<- read.csv2("gunlaws_mass_shootings.csv", sep = ",")

View(glms)

year = glms$Year
favor = glms$GunLaw.Favor
mass = glms$MassShootings
yfavor <- as.numeric(as.character( favor ))

par(mar=c(5,4,4,5)+.1)
plot(year, mass, axes=F, ylim=c(0,max(mass)), xlab="", ylab="",type="l",
     col="red", main="Mass Shootings vs Favor of Gun laws")
axis(2, ylim=c(0,max(mass)),col="red",lwd=2)
mtext(2,text="No of Mass Shootings",line=2.5)

par(new=T)
plot(year, yfavor, axes=F, xlab="", ylab="",
     type="l",col='blue', main="",lwd=2)
axis(4, at=pretty(yfavor), paste0(pretty(yfavor) * 100, " %"),
     ylim=c(0,max(yfavor)), col="blue", lwd=2)
mtext(4,text="Favor", line=2)

axis(1,pretty(range(year),10))
mtext("Year",side=1,col="black",line=2)

par(xpd=TRUE)
legend("topleft", legend=c("Favor","M. Shootings"),
       lty=1, text.col=c("blue","red"),col=c("blue","red"), bty="n")

########################## Mother Jones Gun Mass Shootings ##############################

mjdata <- read.csv2("mj-1982-2016-US-mass-shootings.csv", sep = ",")
mjdf <- data.frame(mjdata)
View(mjdf)
mjyear <- mjdf$Year
victims <- mjdf$Total.victims

library(plotrix)
### Race
race <- mjdf$Race
levels(race)
levels(race) <- c("Asian", "Black", "Black", "Latino", "Native American", "Other & Unclear",
                  "Other & Unclear", "White", "White", "White" )
#### Plotting race
counts <- table(race)
lbls <- levels(race)
pct <- round(counts/sum(counts)*100)
lbls <- paste(lbls, pct)
lbls <- paste(lbls, "%", sep="")
pos <- pie3D(counts, labels=lbls, explode=0.1, main="Race")
pos[4] <- 4.8
pie3D(counts, labels=lbls, explode=0.1, main="Race", labelpos = pos)

prop.table(summary(race))
# Asian           Black          Latino Native American Other & Unclear           White
# 0.07228916      0.16867470      0.07228916      0.03614458      0.07228916      0.57831325

### bought legally vs illegally
gun.purchase <- mjdf$Weapons.obtained.legally
levels(gun.purchase)
levels(gun.purchase) <- c("Yes", "No", "Unknown", "Yes", "Yes", "Yes")

prop.table(summary(gun.purchase))
# Yes         No    Unknown
# 0.79518072 0.14457831 0.06024096


### prior mental health issues
mental <- mjdf$Prior.signs.of.possible.mental.illness
levels(mental)
levels(mental) <- c("No", "Unclear", "Unclear", "Unknown", "Unknown", "Yes")

prop.table(summary(mental))
# No    Unclear    Unknown        Yes
# 0.20481928 0.21686747 0.02409639 0.55421687

### Ploting
ggplot(mjdf, aes(x = mjyear, y = victims, group=1)) + geom_line(aes(group=1))

### total of gun shootings per year vs vicitms
table(xtabs(victims ~ mjyear, data = mjdf))
massfreq <- count(mjdf, "Year")
agmj <- aggregate(victims ~ mjyear, data=mjdf, FUN=sum)
agmj ['MassShootings'] <- massfreq$freq
colnames(agmj)[1] <- 'Year'
View(agmj)

#### Plotting Mass Shootings vs Amount of Victims

mjmass <- agmj$MassShootings
mjvict <- agmj$victims
mjyear <- agmj$Year

par(mar=c(5,4,4,5)+.1)
plot(mjyear, mjmass, axes=F, ylim=c(0,max(mjmass)), xlab="", ylab="",type="l",
     col="red", main="Mass Shootings vs No of Victims")
axis(2, ylim=c(0,max(mjmass)),col="red",lwd=2)
mtext(2,text="No of Mass Shootings",line=2.5)

par(new=T)
plot(mjyear, mjvict, axes=F, xlab="", ylab="",col='dark grey', type="l", lty=3, main="",lwd=2)
axis(4, at=pretty(mjvict),  ylim=c(0,max(mjvict)),
     ylim=c(0,max(mjvict)), col="dark grey", lwd=2)
mtext(4,text="No of Victims", line=2)

axis(1,pretty(range(year),10))
mtext("Year",side=1,col="black",line=2)

par(xpd=TRUE)
legend("topleft", legend=c("Victims","M. Shootings"),
       lty=c(3,1), text.col=c("dark grey","red"),col=c("dark grey","red"), bty="n")


########################### Correlation Gun laws vs Mass Shootings ################################
cor(mass, yfavor)

ran <- glms[glms$Year > 1988 & glms$Year < 2012,]
rfavor <-as.numeric(as.character( ran$GunLaw.Favor ))
cor(ran$MassShootings, rfavor)
