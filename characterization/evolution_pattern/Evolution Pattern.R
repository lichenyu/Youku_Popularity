workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data_demo = read.table(paste(workpath, 'characterization/evolution_pattern/demo', sep = ''))



pdf(paste(workpath, "characterization/evolution_pattern/demo.pdf", sep = ''), 
    width = 5, height = 4)



#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(seq(0, 30), data_demo[1, ], type = "l", 
     xlim = c(0, 30), ylim = c(0, 6000), 
     xlab = "Days Since Uploaded", ylab = "View Count", main = "", sub = "", 
     col = "red", lwd = 2, lty = 1)
lines(seq(0, 30), data_demo[2, ], type = "l", col = "cyan", lwd = 2, lty = 5)
lines(seq(0, 30), data_demo[3, ], type = "l", col = "blue", lwd = 2, lty = 4)
lines(seq(0, 30), data_demo[4, ], type = "l", col = "chartreuse", lwd = 2, lty = 2)
legend("topleft", legend = c("Video 1", "Video 2", "Video 3", "Video 4"), 
       lty = c(1, 5, 4, 2), lwd = rep(2, 4), col = c("red", "cyan", "blue", "chartreuse"), 
       bg="white", cex = 0.8)



dev.off()


