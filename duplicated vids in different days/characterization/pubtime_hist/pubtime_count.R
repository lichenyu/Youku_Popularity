workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/pubtime_hist/pubtime_count', sep = ''))
pubtime = data$V2



pdf(paste(workpath, "characterization/pubtime_hist/pubtime_count.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 0) + 0.1)
barpos = barplot(pubtime, axes = FALSE, 
                 main = '', sub = '', xlab = 'Publication Date', ylab = 'Video Count', border = 'grey')
axis(side = 1, at = barpos, labels = rep('', length(barpos)))
axis(side = 1, at = c(barpos[1], barpos[length(barpos) - 2]), labels = c('2015-12-06', '2016-01-04'), tck = 0)
axis(side = 2, at = c(0, 10000, 30000, 50000), 
     labels = expression('0', '1*10'^4, '3*10'^4, '5*10'^4), 
     las = 1, mgp = c(3, 0.75, 0))

dev.off()

