workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct', sep = ''))

p1 = data$V2
p2 = data$V3
p3 = data$V4

cdf_p1 = ecdf(p1)
cdf_p2 = ecdf(p2)
cdf_p3 = ecdf(p3)


pdf(paste(workpath, "characterization/peakday_pct/peakday_pct.pdf", sep = ''), 
    width = 20, height = 4)

par(mfrow=c(1, 4), cex=1)



#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(cdf_p3, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 1), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(a)", xlab = "Percentage of Total View Count", ylab = "CDF", 
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



data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct_level1', sep = ''))
p1_level1 = data$V2
p2_level1 = data$V3
p3_level1 = data$V4
cdf_p1_level1 = ecdf(p1_level1)
cdf_p2_level1 = ecdf(p2_level1)
cdf_p3_level1 = ecdf(p3_level1)

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct_level2', sep = ''))
p1_level2 = data$V2
p2_level2 = data$V3
p3_level2 = data$V4
cdf_p1_level2 = ecdf(p1_level2)
cdf_p2_level2 = ecdf(p2_level2)
cdf_p3_level2 = ecdf(p3_level2)

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct_level3', sep = ''))
p1_level3 = data$V2
p2_level3 = data$V3
p3_level3 = data$V4
cdf_p1_level3 = ecdf(p1_level3)
cdf_p2_level3 = ecdf(p2_level3)
cdf_p3_level3 = ecdf(p3_level3)

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct_level4', sep = ''))
p1_level4 = data$V2
p2_level4 = data$V3
p3_level4 = data$V4
cdf_p1_level4 = ecdf(p1_level4)
cdf_p2_level4 = ecdf(p2_level4)
cdf_p3_level4 = ecdf(p3_level4)

data = read.table(paste(workpath, 'characterization/peakday_pct/peakday_pct_level5', sep = ''))
p1_level5 = data$V2
p2_level5 = data$V3
p3_level5 = data$V4
cdf_p1_level5 = ecdf(p1_level5)
cdf_p2_level5 = ecdf(p2_level5)
cdf_p3_level5 = ecdf(p3_level5)



#d,l,u,r
par(mar=c(5, 4, 1, 2))
cols = rainbow(5)
plot(cdf_p1_level1, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 1), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(b)", xlab = "Percentage of Total View Count", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(cdf_p1_level2, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(cdf_p1_level3, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(cdf_p1_level4, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(cdf_p1_level5, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8)
box()

#d,l,u,r
par(mar=c(5, 4, 1, 2))
cols = rainbow(5)
plot(cdf_p2_level1, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 1), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(c)", xlab = "Percentage of Total View Count", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(cdf_p2_level2, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(cdf_p2_level3, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(cdf_p2_level4, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(cdf_p2_level5, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8)
box()

#d,l,u,r
par(mar=c(5, 4, 1, 2))
cols = rainbow(5)
plot(cdf_p3_level1, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 1), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "(d)", xlab = "Percentage of Total View Count", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(cdf_p3_level2, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(cdf_p3_level3, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(cdf_p3_level4, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(cdf_p3_level5, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 1, 0.2), labels = seq(0, 1, 0.2), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8)
box()



dev.off()
