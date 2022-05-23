#!/usr/bin/env Rscript

suppressPackageStartupMessages (library(ggplot2))
suppressPackageStartupMessages (library(dplyr))
suppressPackageStartupMessages (library(tidyr))

source ("graph-style.R")


data=data.frame(SchemaType=factor(), NameLength=double(), NameComponent=double(), NumberofPublications=double(), SchemaSize=double())
t = read.csv(file="../non_repeated_result.csv")
data = rbind(data,t)
s = subset(data, Name_Length==2 & Name_Component_Length==2)

g <- ggplot (s, aes(x=Number_of_Publications, y=Schema_Size))+
	 theme_custom() +
	geom_line(aes(colour=Schema_Type)) 
	
g2 <- ggplot(s, aes(x=Number_of_Publications)) + geom_bar(stat="identity", aes(y=Schema_Size, colour=Schema_Type, fill=Schema_Type), position="dodge") + theme_custom()

ggsave("pdfs/exp_2.pdf", plot=g2, width=12, height=8, device=cairo_pdf)
