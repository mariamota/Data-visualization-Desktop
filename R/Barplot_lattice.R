library(package = "lattice")
counts <- table(mtcars$gear)
barchart(counts, main="Car Distribution", xlab="Number of Gears", horizontal="false", col="yellow")