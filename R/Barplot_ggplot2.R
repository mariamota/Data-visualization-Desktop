library("ggplot2")
g <- ggplot(mpg, aes(class))
  	g + geom_bar()
  	g + geom_bar(fill = "gray", colour = "green")