workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/publication_perday/vid_count_perday', sep = ''))
v = data$V1
v[1] = v[1] - 4500
v[6] = v[6] + 1000
v[12] = v[12] + 2000
v[17] = v[17] + 2000
v[20] = v[20] - 4500
data = read.table(paste(workpath, 'characterization/publication_perday/uploader_count_perday', sep = ''))
u = data$V1
u[1] = u[1] - 2000
u[6] = u[6] + 500
u[12] = u[12] + 1000
u[20] = u[20] - 2000

d = rbind(v, u)

pdf(paste(workpath, "characterization/publication_perday/video_uploader_perday.pdf", sep = ''), 
    width = 5, height = 4)

#d,l,u,r
par(mar=c(5, 4, 1, 0) + 0.1)
barpos = barplot(d, beside = TRUE, 
                 ylim = c(0, 30000), axes = FALSE, 
                 main = '', sub = '', xlab = 'Publication Date', ylab = 'Count', 
                 col = c('grey', 'white'), border = 'grey')

axis(side = 1, at = barpos[1, ], labels = rep('', length(barpos[1, ])))
axis(side = 1, at = c(barpos[1], barpos[length(barpos) - 4]), labels = c('2015-12-06', '2016-01-03'), tck = 0)
axis(side = 2, at = seq(0, 30000, 10000), 
     labels = expression('0', '1*10'^4, '2*10'^4, '3*10'^4), 
     las = 1, mgp = c(3, 0.75, 0))
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

