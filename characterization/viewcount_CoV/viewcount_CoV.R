workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/viewcount_CoV/viewcount_CoV', sep = ''))

cov = data$V4

h = hist(cov, breaks = 50, plot = FALSE)
max(h$counts)
h$counts = h$counts / 75000



pdf(paste(workpath, "characterization/viewcount_CoV/viewcount_CoV.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar = c(5, 4, 1, 4) + 0.1)
plot(h, 
     xlim = c(0, 6), ylim = c(0, 1), 
     axes = FALSE, xaxs="i", yaxs="i", 
     main = "", sub = "", xlab = "Coefficient of Variation", ylab = "Video Count", 
     col = 'grey')
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

dev.off()
