workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'



pdf(paste(workpath, "characterization/early_longterm/early_longterm_earlyburst.pdf", sep = ''), 
    width = 5, height = 4)

data = read.table(paste(workpath, 'characterization/early_longterm/early_longterm_earlyburst_filter', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 1000000)
n7_plot = n7[idx]
n30_plot = n30[idx]
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(n7_plot, n30_plot, 
     xlim = c(0, 1000000), ylim = c(0, 1000000), 
     axes = FALSE, #xaxs = "i", yaxs = "i", 
     main = "", sub = "", xlab = "Early View Count", ylab = "Long-term View Count")
axis(side = 1, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6))
axis(side = 2, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6), 
     las = 2, mgp = c(3, 0.7, 0))
abline(0, 1)
fit = lm(n30_plot ~ n7_plot)
abline(fit, lwd = 2, lty = 2, col = "red")
box()

dev.off()



pdf(paste(workpath, "characterization/early_longterm/early_longterm_pattern0.pdf", sep = ''), 
    width = 5, height = 4)

data = read.table(paste(workpath, 'characterization/early_longterm/early_longterm_pattern0_filter', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 1000000)
n7_plot = n7[idx]
n30_plot = n30[idx]
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(n7_plot, n30_plot, 
     xlim = c(0, 1000000), ylim = c(0, 1000000), 
     axes = FALSE, #xaxs = "i", yaxs = "i", 
     main = "", sub = "", xlab = "Early View Count", ylab = "Long-term View Count")
axis(side = 1, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6))
axis(side = 2, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6), 
     las = 2, mgp = c(3, 0.7, 0))
abline(0, 1)
fit = lm(n30_plot ~ n7_plot)
abline(fit, lwd = 2, lty = 2, col = "red")
box()

dev.off()



pdf(paste(workpath, "characterization/early_longterm/early_longterm_futureburst.pdf", sep = ''), 
    width = 5, height = 4)

data = read.table(paste(workpath, 'characterization/early_longterm/early_longterm_futureburst', sep = ''))
n7 = rowSums(data[2:8])
n30 = rowSums(data[2:31])
idx = which(n30 <= 1000000)
n7_plot = n7[idx]
n30_plot = n30[idx]
#d,l,u,r
par(mar=c(5, 4, 1, 2) + 0.1)
plot(n7_plot, n30_plot, 
     xlim = c(0, 1000000), ylim = c(0, 1000000), 
     axes = FALSE, #xaxs = "i", yaxs = "i", 
     main = "", sub = "", xlab = "Early View Count", ylab = "Long-term View Count")
axis(side = 1, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6))
axis(side = 2, at = c(0, 200000, 400000, 600000, 800000, 1000000), labels = expression('0', '2*10'^5, '4*10'^5, '6*10'^5, '8*10'^5, '1*10'^6), 
     las = 2, mgp = c(3, 0.7, 0))
abline(0, 1)
box()

dev.off()


