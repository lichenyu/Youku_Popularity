workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/publication_perday/collected_count_perday', sep = ''))
c = data$V1
c[12] = c[12] + 2000
data = read.table(paste(workpath, 'characterization/publication_perday/uploader_count_perday', sep = ''))
u = data$V1
u[12] = u[12] + 1500

d = rbind(c, u)

pdf(paste(workpath, "characterization/publication_perday/video_uploader_perday.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 0) + 0.1)
barpos = barplot(d, beside = TRUE, 
                 ylim = c(0, 35000), axes = FALSE, 
                 main = '', sub = '', xlab = 'Publication Date', ylab = 'Count', 
                 col = c('grey', 'white'), border = 'grey')
axis(side = 1, at = c(barpos[1], barpos[length(barpos)]), labels = c('2015-12-06', ''))
axis(side = 1, at = barpos[length(barpos) - 4], labels = '2016-01-04', tck = 0)
axis(side = 2, at = seq(0, 30000, 10000), labels = seq(0, 30000, 10000))
legend("topright", inset = c(0, 0), 
       pch = c(15, 0), col = c("grey", "grey"), 
       legend = c("Video Count","Uploader Count"), bg = "white", cex = 0.8)

dev.off()

# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# barpos = barplot(c, 
#                  ylim = c(0, 30000), 
#                  main = '', sub = '', xlab = 'Publication Date', ylab = 'Publication Count', 
#                  space = 2, col = 'grey', border = 'grey')
# axis(side = 1, at = c(barpos[1], barpos[29]), labels = c('2015-12-06', '2016-01-04'))

