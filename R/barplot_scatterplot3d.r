library("scatterplot3d")
my.mat <- matrix(runif(25), nrow = 5)
dimnames(my.mat) <- list(LETTERS[1:5], letters[11:15])
s3d.dat <- data.frame(columns = c(col(my.mat)),
rows = c(row(my.mat)), value = c(my.mat))
scatterplot3d(s3d.dat, type = "h", lwd = 5, pch = " ",
x.ticklabs = colnames(my.mat), y.ticklabs = rownames(my.mat),
color = grey(25:1 / 40), main = "3D barplot")
