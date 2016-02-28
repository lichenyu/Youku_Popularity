workpath = 'F:/Youku_Popularity/Youku_Popularity/'
#workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/publication_perday/cat_rank_perday', sep = ''))


cols = rainbow(24)
#d,l,u,r
par(mar=c(5, 4, 1, 5) + 0.1)
plot(data$V1, type = 'l', 
     ylim = c (0, 24), axes = FALSE, 
     main = '', sub = '', xlab = 'Publication Date', ylab = 'Category Rank', 
     col = cols[24]
     )
for(i in seq(2, 24)){
  var = paste()
  lines(eval(parse(text = paste('data$V', i, sep = '')))
        , type = 'l', col = cols[24 - i + 1])
}
axis(side = 1, at = c(1, 29), labels = c('2015-12-06', '2016-01-04'))
axis(side = 2, at = seq(0, 24, 4), labels = seq(25, 1, -4), las = 2)
legend("right", inset = c(5, 0), 
       pch = c(15, 0), col = c("grey", "grey"), 
       legend = c("Video Count","Uploader Count"), bg = "white", cex = 0.8)






d = rbind(c, u)

pdf(paste(workpath, "characterization/publication_perday/video_uploader_perday.pdf", sep = ''), 
    width = 5, height = 4)






for(i in seq(2, 24)){
  print(i)
  var = paste('V', i, sep = '')
  print(var)
  lines(data$var, type = 'l', col = cols[24 - i])
}










dev.off()

# #d,l,u,r
# par(mar=c(5, 4, 1, 2) + 0.1)
# barpos = barplot(c, 
#                  ylim = c(0, 30000), 
#                  main = '', sub = '', xlab = 'Publication Date', ylab = 'Publication Count', 
#                  space = 2, col = 'grey', border = 'grey')
# axis(side = 1, at = c(barpos[1], barpos[29]), labels = c('2015-12-06', '2016-01-04'))

