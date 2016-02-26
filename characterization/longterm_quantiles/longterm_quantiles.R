workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/longterm_quantiles/quantiles', sep = ''))

q25 = data$V1
q50 = data$V2
q75 = data$V3

mean(q25)
mean(q50)
mean(q75)



pdf(paste(workpath, "characterization/longterm_quantiles/quantiles.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(q25, type = 'l', 
     xlim = c(0, 30), ylim = c(1, 1000), 
     axes = FALSE, xaxs="i", 
     main = '', sub = '', xlab = 'Publication Date', ylab = 'View Count', 
     lwd = 2, col = 'blue', log = 'y')
lines(q50, type = 'l', lwd = 2, col = 'red')
lines(q75, type = 'l', lwd = 2, col = 'green')
lines(c(0, 30), c(mean(q25), mean(q25)), lty = 2, col = 'grey')
lines(c(0, 30), c(mean(q50), mean(q50)), lty = 2, col = 'grey')
lines(c(0, 30), c(mean(q75), mean(q75)), lty = 2, col = 'grey')
axis(side = 1, at = c(1, 29), 
     labels = c('2015-12-06', '2016-01-04'))
axis(side = 2, at = c(10, 30, 80, 100, 400, 500), labels = c(10, 30, '', '', '', ''), las = 2)
axis(side = 2, at = c(60, 120, 300, 600), labels = c(80, 100, 400, 500), las = 2, tck = 0)
legend("bottomright", legend = c("0.25 Quantiles", "0.50 Quantiles", "0.75 Quantiles"), 
       lwd = rep(2, 3), col = c("blue", "red", "green"), 
       bg="white", cex = 0.8)
box()

dev.off()
