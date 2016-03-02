workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'data/vci_files/vci', sep = ''))

n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 100000)
n7 = n7[idx]
n30 = n30[idx]


plot(n7, n30)



data = read.table(paste(workpath, 'characterization/early_longterm/early_longterm_pattern10', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 1000000)
n7 = n7[idx]
n30 = n30[idx]
plot(n7, n30, xlim = c(0, 1000000), ylim = c(0, 1000000))

data = read.table(paste(workpath, 'characterization/early_longterm/early_longterm_pattern0', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 1000000)
n7 = n7[idx]
n30 = n30[idx]
plot(n7, n30, xlim = c(0, 1000000), ylim = c(0, 1000000))


#pdf(paste(workpath, "characterization/early_longterm/early_longterm.pdf", sep = ''), 
#    width = 5, height = 4)

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

#dev.off()


