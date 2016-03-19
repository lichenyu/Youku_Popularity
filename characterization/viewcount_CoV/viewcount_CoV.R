workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV', sep = ''))

cov = data$V4

max(cov)
brks = seq(0, 5.5, 0.1)
h = hist(cov, breaks = brks, plot = FALSE)
max(h$counts)
h$counts = h$counts / 75000



pdf(paste(workpath, "characterization/viewcount_CoV/viewcount_CoV.pdf", sep = ''), 
    width = 10, height = 4)

par(mfrow=c(1, 2), cex=1)

#d,l,u,r
par(mar = c(5, 4, 1, 5))
plot(h, 
     xlim = c(0, 6), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(a)", xlab = "Coefficient of Variation", ylab = "", 
     col = 'grey', border = 'grey')
e = ecdf(cov)
lines(e, do.points = FALSE, verticals = TRUE, col.01line = NULL, col = "blue", lwd = 2)
axis(side = 1, at = seq(0, 6, 1), labels = seq(0, 6, 1))
axis(side = 2, at = seq(0, 1, .2), 
     labels = seq(0, 75000, 15000), 
     #labels = expression('0', '1.5*10'^4, '3.0*10'^4, '4.5*10'^4, '6.0*10'^4, '7.5*10'^4), 
     las = 1, mgp = c(3, 0.55, 0))
#mgp=c(axis.title.position, axis.label.position, axis.line.position), The default is c(3, 1, 0)
axis(side = 4, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 1)
mtext("CDF", side = 4, las = 0, line = 2.5, col = 'blue')
mtext("Video Count", side = 2, las = 0, line = 3.0, col = 'darkgrey')



data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV_level1', sep = ''))
cov_l1 = data$V4
data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV_level2', sep = ''))
cov_l2 = data$V4
data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV_level3', sep = ''))
cov_l3 = data$V4
data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV_level4', sep = ''))
cov_l4 = data$V4
data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV_level5', sep = ''))
cov_l5 = data$V4

cov_l1_cdf = ecdf(cov_l1)
cov_l2_cdf = ecdf(cov_l2)
cov_l3_cdf = ecdf(cov_l3)
cov_l4_cdf = ecdf(cov_l4)
cov_l5_cdf = ecdf(cov_l5)



#d,l,u,r
par(mar = c(5, 4, 1, 2))
cols = rainbow(5)
plot(cov_l1_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 6), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(b)", xlab = "Coefficient of Variation", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(cov_l2_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(cov_l3_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(cov_l4_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(cov_l5_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 6, 1), labels = seq(0, 6, 1), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8)
box()



dev.off()