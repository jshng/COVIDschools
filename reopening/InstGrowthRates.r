library(mgcv)

DataFile <- function(country){
  if(country=="DK"){filename <- "denmark_data.csv"}
  else if(country=="DKcase"){filename <- "denmark_cases.csv"}
  else if(country=="NO"){filename <- "norway_data.csv"}
  else if(country=="DE"){filename <- "germany_data_hosp.csv"}
  else if(country=="DEstaff"){filename <- "germany_data_raw.csv"}
  else if(country=="DEstudents"){filename <- "germany_data_raw.csv"}
  filename
}

GrowthRate <- function(raw, country, plotfig=TRUE, printrates=TRUE){
  
  if(country=="DK"){raw <- raw$Hospital}
  else if(country=="DKcase"){raw <- raw$Confirmed}
  else if(country=="NO"){raw <- raw$Confirmed}
  else if(country=="DE"){raw <- raw$Hospital}
  else if(country=="DEstaff"){raw <- raw$Staff}
  else if(country=="DEstudents"){raw <- raw$Students}
  #By default, the fit goes over as many data points as the length of the raw data, but N can bee changed here is desired
  N <- length(raw)
  
  #Prepare data structures
  rates<- data.frame(rate=rep(0,N),rateub=rep(0,N),ratelb=rep(0,N))
  ndays <- seq(1,length(raw),1)
  #Time t
  dt<-seq(1,length(raw), length=N)
  newdays <- data.frame(ndays=dt)
  #Time t + epsilon
  epsilon <- 1e-7
  dteps <- seq(1,length(raw), length=N) + epsilon
  newdayseps <- data.frame(ndays=dteps)
  
  #Define GAM function
  GAMfit <- gam(raw~s(ndays), family=quasipoisson())
  #Estimated fits for times (t, t+epsilon)
  Fitt <- predict(GAMfit, newdays, type="lpmatrix")
  Fitteps <- predict(GAMfit, newdayseps, type="lpmatrix")
  
  #Approximation of the derivative of the fit. This derivative will give us the instantaneous rate.
  Grad <- (Fitteps-Fitt)/epsilon
  #Apply the GAM fit to the raw derivatives to smooth them out
  rateval <- Grad%*%coef(GAMfit)
  #Multiply our rates by the GAM covariance matrix to obtain the variance of the rates
  #Square root to determine the standard deviation
  rateval.stdev <- sqrt(rowSums(Grad%*%GAMfit$Vp*Grad))
  
  #Save the mean and confidence intervals
  rates$rate <- rateval
  rates$rateub <- rateval+2*rateval.stdev
  rates$ratelb <- rateval-2*rateval.stdev
  
  if(printrates==TRUE){
    if(country=="DK"){
      write.csv(rates$rate, 'DK.csv')
      write.csv(rates$rateub, 'DK-ub.csv')
      write.csv(rates$ratelb, 'DK-lb.csv')
    }
    else if(country=="DKcase"){
      write.csv(rates$rate, 'DKcases.csv')
      write.csv(rates$rateub, 'DKcases-ub.csv')
      write.csv(rates$ratelb, 'DKcases-lb.csv')
    }
    else if(country=="NO"){
      write.csv(rates$rate, 'NO.csv')
      write.csv(rates$rateub, 'NO-ub.csv')
      write.csv(rates$ratelb, 'NO-lb.csv')
    }
    else if(country=="DE"){
      write.csv(rates$rate, 'DE.csv')
      write.csv(rates$rateub, 'DE-ub.csv')
      write.csv(rates$ratelb, 'DE-lb.csv')
    }
    else if(country=="DEstaff"){
      write.csv(rates$rate, 'DEstaff.csv')
      write.csv(rates$rateub, 'DEstaff-ub.csv')
      write.csv(rates$ratelb, 'DEstaff-lb.csv')
    }
    else if(country=="DEstudents"){
      write.csv(rates$rate, 'DEstudents.csv')
      write.csv(rates$rateub, 'DEstudents-ub.csv')
      write.csv(rates$ratelb, 'DEstudents-lb.csv')
    }
  }
}

#Choose which country to analyse (DK, DKcase, NO, DE, DEstaff, or DEstudents):
CountryCode <- "NO"
InputData<-data.frame(read.csv(DataFile(CountryCode)))
#Toggle printrates if you want to save the instantaneous growth rates
#Evaluates the instantaneous growth rate
GrowthRate(InputData, CountryCode, printrates=FALSE)
#These growth rates are visualised in Python (see other enclosed scripts)


