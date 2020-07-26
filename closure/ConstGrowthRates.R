library(ggplot2)
library(MASS)

DataFile <- function(country){
  if(country=="BY"){filename <- "Bavaria_results.csv"}
  else if(country=="BW"){filename <- "Baden_results.csv"}
  else if(country=="BE"){filename <- "Berlin_results.csv"}
  else if(country=="HE"){filename <- "Hesse_results.csv"}
  else if(country=="NI"){filename <- "LSaxony_results.csv"}
  else if(country=="NW"){filename <- "NRW_results.csv"}
  else if(country=="RP"){filename <- "Rhineland_results.csv"}
  filename
}

ConstGrowthRate <- function(tmp, country,double=FALSE){
  #Read in from date of school closure
  #Determine the lag time per country
  #Fit pre-response and post-response over the same time window (if available)
  if(country=="BY"){
    startwindow <- 11
    window <- 10+startwindow-1
    endwindow <- 10}
  else if(country=="BW"){
    startwindow <- 14
    window <- 8+startwindow-1
    weekendwindow <- 5+startwindow-1#A shorter fitting window to account for the weekend effect
    endwindow <- 8}
  else if(country=="BE"){
    startwindow <- 11
    window <- 9+startwindow-1
    endwindow <- 9}
  else if(country=="HE"){
    startwindow <- 5
    window <- 8+startwindow-1
    endwindow <- 8}
  else if(country=="NI"){
    startwindow <- 9
    window <- 9+startwindow-1
    endwindow <- 9}
  else if(country=="NW"){
    startwindow <- 9
    window <- 9+startwindow-1
    weekendwindow <- 7+startwindow-1#A shorter fitting window to account for the weekend effect
    endwindow <- 9}
  else if(country=="RP"){
    startwindow <- 11
    window <- 6+startwindow-1
    endwindow <- 6}

#Define the time steps (in days), and the fitting weights
tmp$Day <- seq(1,length(tmp$Sum),1)
tmp$wpts <- tmp$Weights/mean(tmp$Weights)
tmp$projwpts <- tmp$ProjWeights/mean(tmp$ProjWeights)

#Apply the fits to the data (choose between default negative binomial fit and quasi-Poisson)
#Observed pre-response 
preobsGLM <- glm.nb(Sum[c(startwindow:window)] ~ (Day[c(startwindow:window)]), data=tmp, weights=wpts[c(startwindow:window)])
#preobsGLM <- glm(Sum[c(startwindow:window)] ~ (Day[c(startwindow:window)]), data=tmp, family=quasipoisson(), weights=wpts[c(startwindow:window)])
#Observed post-response 
postobsGLM <- glm.nb(Sum[c(window+1:endwindow)] ~ (Day[c(window+1:endwindow)]), data=tmp, weights=wpts[c(window+1:endwindow)])
#postobsGLM <- glm(Sum[c(window+1:endwindow)] ~ (Day[c(window+1:endwindow)]), data=tmp, family=quasipoisson(), weights=wpts[c(window+1:endwindow)])
#Modelled post-response 
postmodGLM <- glm.nb(Projection[c(window+1:endwindow)] ~ (Day[c(window+1:endwindow)]), data=tmp, weights=projwpts[c(window+1:endwindow)])
#postmodGLM <- glm(Projection[c(window+1:endwindow)] ~ (Day[c(window+1:endwindow)]), data=tmp, family=quasipoisson(), weights=projwpts[c(window+1:endwindow)])
#Observed pre-response, corrected for the weekend effect
  if(country=="BW" || country=="NW"){
    weekpreobsGLM <- glm.nb(Sum[c(startwindow:weekendwindow)] ~ (Day[c(startwindow:weekendwindow)]), data=tmp, weights=wpts[c(startwindow:weekendwindow)])
    #weekpreobsGLM <- glm(Sum[c(startwindow:weekendwindow)] ~ (Day[c(startwindow:weekendwindow)]), data=tmp, family=quasipoisson(), weights=wpts[c(startwindow:weekendwindow)])
  }

#Growth rates and doubling times
preobsrate <- c(preobsGLM$coefficients[2],confint(preobsGLM)[2,1],confint(preobsGLM)[2,2])
postobsrate <- c(postobsGLM$coefficients[2],confint(postobsGLM)[2,1],confint(postobsGLM)[2,2])
postmodrate <- c(postmodGLM$coefficients[2],confint(postmodGLM)[2,1],confint(postmodGLM)[2,2])
if(country=="BW" || country=="NW"){
  weekpreobsrate <- c(weekpreobsGLM$coefficients[2],confint(weekpreobsGLM)[2,1],confint(weekpreobsGLM)[2,2])
}

  if(double){
    print(log(2)/preobsrate)
    if(country=="BW" || country=="NW"){print(log(2)/weekpreobsrate)}
    print(log(2)/postobsrate)
    print(log(2)/postmodrate)
  }
  else{
    print(preobsrate)
    if(country=="BW" || country=="NW"){print(weekpreobsrate)}
    print(postobsrate)
    print(postmodrate)
  }
}

#Choose which German state to analyse: Baden-Wurttemberg (BW), Bavaria (BY), Berlin (BE)
#     Hesse (HE), Lower Saxony (NI), North Rhine-Westphalia (NW), Rhineland-Palatinate (RP)
CountryCode <- "BW"
InputData<-data.frame(read.csv(DataFile(CountryCode)))
#Call functions which determines the growth rates...toggle if want to print doubling times instead
ConstGrowthRate(InputData,CountryCode,FALSE)
