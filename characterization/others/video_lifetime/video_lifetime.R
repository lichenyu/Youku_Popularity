workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/video_lifetime/video_lifetime', sep = ''))
lifetime = data$V2
data = read.table(paste(workpath, 'characterization/video_lifetime/video_first_lifetime', sep = ''))
first_lifetime = data$V2



lifetime_cdf = ecdf(lifetime)
first_lifetime_cdf = ecdf(first_lifetime)
plot(lifetime_cdf)
plot(first_lifetime_cdf)



pdf(paste(workpath, "characterization/video_lifetime/video_lifetime.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(first_lifetime_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, 
     xlim = c(0, 30), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Lifetime (days)", ylab = "CDF", 
     col = "red", lwd = 2)
lines(lifetime_cdf, do.points = FALSE, verticals = TRUE, col.01line = 0, col = "blue", lwd = 2)
axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5), tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 2, tck = 1, lty = 2, col = 'grey')
legend("bottomright", legend = c("Video Lifetime (Backward Checking)", 
                                 "Video Lifetime (Forward Checking)"), 
       lwd = rep(2, 2), col = c("blue", "red"), 
       bg="white", cex = 0.8)
box()

dev.off()


