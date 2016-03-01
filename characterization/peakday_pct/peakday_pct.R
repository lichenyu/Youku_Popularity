workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct', sep = ''))

p1 = data$V2
p2 = data$V3
p3 = data$V4

cdf_p1 = ecdf(p1)
cdf_p2 = ecdf(p2)
cdf_p3 = ecdf(p3)


pdf(paste(workpath, "characterization/peakday_pct/peakday_pct.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(cdf_p3, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 1), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Percentage of Total View Count", ylab = "CDF", 
     col = "green", lwd = 2)
lines(cdf_p2, do.points = FALSE, verticals = TRUE, col.01line = 0, col = "red", lwd = 2)
lines(cdf_p1, do.points = FALSE, verticals = TRUE, col.01line = 0, col = "blue", lwd = 2)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("1st Peak Day", 
                                 "2nd Peak Day", 
                                 "3rd Peak Day"), 
       lwd = rep(2, 3), col = c("blue", "red", "green"), 
       bg="white", cex = 0.8)
box()

dev.off()



library(MASS)
library(fitdistrplus)
library(actuar)



pdf(paste(workpath, "characterization/longterm_distribution/longterm_fit.pdf", sep = ''), 
    width = 10, height = 4)
par(mfrow=c(1, 2))

data = read.table(paste(workpath, 'data/vci_files/vci_1-7', sep = ''))
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



# data = read.table(paste(workpath, 'data/vci_files/vci_8-14', sep = ''))
# n30 = rowSums(data[2:31])
# n30_p = n30[which(0 < n30)]
# 
# fp <- fitdist(n30_p, "pareto")
# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# ppcomp(fp, axes = FALSE, 
#        main = '', sub = '(b)', xlab = 'Theoretical Probabilities', ylab = 'Empirical Probabilities', 
#        lwd = 5)
# axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2))
# axis(side = 2, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), las = 1)
# abline(0, 1)
# box()



data = read.table(paste(workpath, 'data/vci_files/vci_15-21', sep = ''))
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



# data = read.table(paste(workpath, 'data/vci_files/vci_22-28', sep = ''))
# n30 = rowSums(data[2:31])
# n30_p = n30[which(0 < n30)]
# 
# fp <- fitdist(n30_p, "pareto")
# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# ppcomp(fp, axes = FALSE, 
#        main = '', sub = '(c)', xlab = 'Theoretical Probabilities', ylab = 'Empirical Probabilities', 
#        lwd = 5)
# axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2))
# axis(side = 2, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), las = 1)
# abline(0, 1)
# box()

dev.off()


# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# ppcomp(fp, fitcol = 'red', lwd = 4, 
#        main = "", sub = "", 
#        xlab = "Theoretical Probabilities", ylab = "Empirical Probabilities")
# legend("bottomright", legend = c("Whole Dataset"), pch = 19, col = "red", bg="white", cex = 0.8)
# abline(0, 1, lty = 2, lwd = 1, col = "grey")


