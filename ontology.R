# Web Ontology

# Author: Danilo Ré
# Date: 20/08/2014

# Loading Data:

setwd("C:\\Users\\she2040\\Desktop\\Python\\WebOntology")
data <- read.table("saida_ESPORTE_2.txt", sep = "|", head=F, 
                   col.names=c("CATEGORIA","URL","P"), fileEncoding="utf8")

head(data)

# Text Mining Analysis

corpus <- Corpus(VectorSource(data$P),
                 readerControl = list(language="pt_BR"))


tdm = TermDocumentMatrix(corpus,
                         control = list(removePunctuation = TRUE,
                                        stopwords = c(stopwords("portuguese")),
                                        removeNumbers = TRUE, tolower = TRUE))

inspect(tdm)
m <- as.matrix(tdm)

# Getting word counts in decreasing order

word_freqs <- sort(rowSums(m), decreasing = TRUE)

# Create dataframe with words and their frequencies

dm <- data.frame(word = names(word_freqs), freq = word_freqs)

# Plotting the WordCloud

wordcloud(dm$word[1:50], dm$freq[1:50], random.order = F, colors = brewer.pal(8, "Dark2"))

cbind(dm$word[1:50], dm$freq[1:50])
