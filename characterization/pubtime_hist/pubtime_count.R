workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/pubtime_hist/pubtime_count', sep = ''))
pubtime = data$V2



pdf(paste(workpath, "characterization/pubtime_hist/pubtime_count.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 0) + 0.1)
barpos = barplot(pubtime, axes = FALSE, 
                 main = '', sub = '', xlab = 'Publication Time', ylab = 'Video Count', border = 'grey')
axis(side = 1, at = c(barpos - (barpos[2] - barpos[1]) / 2, barpos[length(barpos)] + (barpos[2] - barpos[1]) / 2), 
     labels = c('0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'), 
     las = 2, mgp = c(3, 0.7, 0))
axis(side = 2, at = c(0, 10000, 30000, 50000), 
     labels = expression('0', '1*10'^4, '3*10'^4, '5*10'^4), 
     las = 1, mgp = c(3, 0.75, 0))

dev.off()

