workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/duration_hist/durations', sep = ''), fileEncoding = 'utf-8')
duration = data$V1
category = data$V2



#brks = seq(0, ceiling(max(duration)), 1)
h = hist(duration, breaks = 5000, plot = FALSE)
h$counts = h$counts / 50000



pdf(paste(workpath, "characterization/duration_hist/duration_hist.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 4) + 0.1)
plot(h, 
     xlim = c(0, 1800), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Video Duration (seconds)", ylab = "Video Count", 
     col = 'grey')
e = ecdf(duration)
lines(e, do.points = FALSE, verticals = TRUE, col.01line = NULL, col = "blue", lwd = 2)
axis(side = 1, at = seq(0, 1800, 300), labels = seq(0, 1800, 300))
axis(side = 2, at = seq(0, 1, .2), 
     labels = expression('0', '1*10'^4, '2*10'^4, '3*10'^4, '4*10'^4, '5*10'^4), 
     las = 1, mgp = c(3, 0.75, 0))
#mgp=c(axis.title.position, axis.label.position, axis.line.position), The default is c(3, 1, 0)
axis(side = 4, at = seq(0, 1, .2), labels = seq(0, 1, .2), las = 1)
mtext("CDF", side = 4, las = 0, line = 2.5)

dev.off()


