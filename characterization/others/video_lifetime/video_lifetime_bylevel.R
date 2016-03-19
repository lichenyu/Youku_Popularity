workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime_level1', sep = ''))
lifetime_l1 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime_level2', sep = ''))
lifetime_l2 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime_level3', sep = ''))
lifetime_l3 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime_level4', sep = ''))
lifetime_l4 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime_level5', sep = ''))
lifetime_l5 = data$V2

lifetime_l1_cdf = ecdf(lifetime_l1)
lifetime_l2_cdf = ecdf(lifetime_l2)
lifetime_l3_cdf = ecdf(lifetime_l3)
lifetime_l4_cdf = ecdf(lifetime_l4)
lifetime_l5_cdf = ecdf(lifetime_l5)

pdf(paste(workpath, "characterization/video_lifetime/video_lifetime_bylevel.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2.5) + 0.1)
cols = rainbow(5)
plot(lifetime_l1_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 30), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Lifetime (days)", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(lifetime_l2_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(lifetime_l3_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(lifetime_l4_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(lifetime_l5_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
box()
par(xpd = TRUE)
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8, inset = c(-0.12, 0))
par(xpd = FALSE)

dev.off()



data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime_level1', sep = ''))
first_lifetime_l1 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime_level2', sep = ''))
first_lifetime_l2 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime_level3', sep = ''))
first_lifetime_l3 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime_level4', sep = ''))
first_lifetime_l4 = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime_level5', sep = ''))
first_lifetime_l5 = data$V2
first_lifetime_l1_cdf = ecdf(first_lifetime_l1)
first_lifetime_l2_cdf = ecdf(first_lifetime_l2)
first_lifetime_l3_cdf = ecdf(first_lifetime_l3)
first_lifetime_l4_cdf = ecdf(first_lifetime_l4)
first_lifetime_l5_cdf = ecdf(first_lifetime_l5)

pdf(paste(workpath, "characterization/video_lifetime/video_first_lifetime_bylevel.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2.5) + 0.1)
cols = rainbow(5)
plot(first_lifetime_l1_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 30), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Lifetime (days)", ylab = "CDF", 
     col = cols[1], lwd = 2)
lines(first_lifetime_l2_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[2], lwd = 2)
lines(first_lifetime_l3_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[3], lwd = 2)
lines(first_lifetime_l4_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[4], lwd = 2)
lines(first_lifetime_l5_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = cols[5], lwd = 2)
axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
box()
par(xpd = TRUE)
legend("bottomright", legend = c("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"), 
       lwd = rep(2, 5), col = cols, 
       bg="white", cex = 0.8, inset = c(-0.12, 0))
par(xpd = FALSE)

dev.off()


