workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'data/vci_files/vci', sep = ''))

n1 = data$V2
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])



cdf1 = ecdf(n1)
cdf7 = ecdf(n7)
cdf30 = ecdf(n30)



pdf(paste(workpath, "characterization/longterm_distribution/longterm_cdf.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(cdf1, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(1, 100000), ylim = c(0, 1), log = "x", 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "View Count", ylab = "CDF", 
     col = "green", lwd = 2)
lines(cdf7, do.points = FALSE, verticals = TRUE, col.01line = 0, col = "red", lwd = 2)
lines(cdf30, do.points = FALSE, verticals = TRUE, col.01line = 0, col = "blue", lwd = 2)
axis(side = 1, at = c(1, 10, 100, 1000, 10000, 100000), 
     labels = expression('10'^0, '10'^1, '10'^2, '10'^3, '10'^4, '10'^5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("View Count after a Day", 
                                 "View Count after a Week", 
                                 "View Count after a Month"), 
       lwd = rep(2, 3), col = c("green", "red", "blue"), 
       bg="white", cex = 0.8)
box()

dev.off()



library(MASS)
library(fitdistrplus)
library(actuar)



pdf(paste(workpath, "characterization/longterm_distribution/longterm_fit.pdf", sep = ''), 
    width = 15, height = 4)
par(mfrow=c(1, 3))

data = read.table(paste(workpath, 'data/vci_files/vci_1-10', sep = ''))
n30 = rowSums(data[2:31])
n30_p = n30[which(0 < n30)]

fp <- fitdist(n30_p, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, axes = FALSE, 
       main = '', sub = '(a)', xlab = 'Theoretical Probabilities', ylab = 'Empirical Probabilities', 
       lwd = 5)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2))
axis(side = 2, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), las = 1)
abline(0, 1)
box()



data = read.table(paste(workpath, 'data/vci_files/vci_11-20', sep = ''))
n30 = rowSums(data[2:31])
n30_p = n30[which(0 < n30)]

fp <- fitdist(n30_p, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, axes = FALSE, 
       main = '', sub = '(b)', xlab = 'Theoretical Probabilities', ylab = 'Empirical Probabilities', 
       lwd = 5)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2))
axis(side = 2, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), las = 1)
abline(0, 1)
box()



data = read.table(paste(workpath, 'data/vci_files/vci_21-29', sep = ''))
n30 = rowSums(data[2:31])
n30_p = n30[which(0 < n30)]

fp <- fitdist(n30_p, "pareto")
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
ppcomp(fp, axes = FALSE, 
       main = '', sub = '(c)', xlab = 'Theoretical Probabilities', ylab = 'Empirical Probabilities', 
       lwd = 5)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2))
axis(side = 2, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), las = 1)
abline(0, 1)
box()

dev.off()


# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# ppcomp(fp, fitcol = 'red', lwd = 4, 
#        main = "", sub = "", 
#        xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
# legend("bottomright", legend = c("Whole Dataset"), pch = 19, col = "red", bg="white", cex = 0.8)
# abline(0, 1, lty = 2, lwd = 1, col = "grey")


