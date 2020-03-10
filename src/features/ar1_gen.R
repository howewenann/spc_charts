ar1 = arima.sim(model = list(ar=c(0.8)), n=1000000)
# write.csv(ar1, 'ar1.csv', row.names = FALSE)

arima(ar1, order = c(1,0,0))