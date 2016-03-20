#workpath = 'F:/Youku_Popularity/Youku_Popularity/'
workpath = '/Users/ouyangshuxin/Documents/Youku_Popularity/Youku_Popularity/'

data = read.table(paste(workpath, 'characterization/publication/cat_rank_perday', sep = ''))


pdf(paste(workpath, "characterization/publication/cat_rank_perday.pdf", sep = ''), 
    width = 10, height = 4)

cols = rainbow(24)
#d,l,u,r
par(mar=c(5, 4, 1, 13))
plot(data$V1, type = 'l', 
     ylim = c (0, 24), axes = FALSE, 
     main = '', sub = '', xlab = 'Published Date', ylab = 'Category Rank', 
     col = cols[24]
     )
points(data$V1, pch = 20, col = cols[24], cex = 0.5)
for(i in seq(2, 24)){
  var = paste()
  lines(eval(parse(text = paste('data$V', i, sep = ''))), 
        type = 'l', col = cols[24 - i + 1])
  points(eval(parse(text = paste('data$V', i, sep = ''))), 
         pch = 20, col = cols[24 - i + 1], cex = 0.5)
}
par(xpd = TRUE)
axis(side = 1, at = seq(1, 29), labels = rep('', 29))
axis(side = 1, at = c(1, 29), labels = c('2015-12-06', '2016-01-03'), tck = 0)
axis(side = 2, at = seq(0, 24, 4), labels = seq(25, 1, -4), las = 2)
cats = c('life', 'game', 'education', 'music', 'tv episode', 'family', 'sport', 'creativity', 'news', 'entertainment', 'amateur', 'variety show', 'advertisement', 'humor', 'auto', 'blog', 'animation', 'film', 'fashion', 'technology', 'travel', 'minishow', 'documentary', 'netshow')
legend("right", legend = cats, col = cols, ncol = 2, 
       lty = rep(1, 24), lwd = rep(1, 24), 
       bg="white", cex = 0.75, inset = c(-0.375, 0))
par(xpd = FALSE)

dev.off()


