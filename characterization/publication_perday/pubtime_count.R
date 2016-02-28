workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/publication_perday/pubtime_count', sep = ''))
pubtime = data$V2



pdf(paste(workpath, "characterization/publication_perday/pubtime_count.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 0) + 0.1)
barpos = barplot(pubtime, 
                 main = '', sub = '', xlab = 'Publication Date', ylab = 'Count', border = 'grey')
axis(side = 1, at = barpos, labels = seq(0, 23))

dev.off()

