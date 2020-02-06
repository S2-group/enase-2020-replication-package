drs <- architectural_rules$squid
granularities <- 
      architectural_rules$granularity_level

for (i in 1:length(drs)){
  dr = drs[i]
  granularity = granularities[i]
  newCol = paste("AVG", dr, sep = "")
  filtered_dataset[, newCol] <- (filtered_dataset[, dr] / filtered_dataset[, granularity])*1000
} 

filtered_dataset[is.na(filtered_dataset)] <- 0

categories <- 
      architectural_rules$atd_dimension[architectural_rules$squid==dr]

for (i in 1:length(drs)){
  dr = drs[i]
  newCol = paste("outlier", dr, sep = "")
  filtered_dataset <- as.data.frame(filtered_dataset)
  filtered_dataset[, newCol] <- 
  ifelse(filtered_dataset[, dr]
    %in% boxplot.stats(filtered_dataset[,dr])$out, 1, 0)
}

filtered_dataset$inheritance <- ((filtered_dataset$`outliersquid:ObjectFinalizeOverridenCheck` + filtered_dataset$`outliersquid:S1161`
                                 + filtered_dataset$`outliersquid:S1182` + filtered_dataset$`outliersquid:S1185`
                                 + filtered_dataset$`outliersquid:S1210` + filtered_dataset$`outliersquid:S2062` 
                                 + filtered_dataset$`outliersquid:S2157` + filtered_dataset$`outliersquid:S2638` +
                                 + filtered_dataset$`outliersquid:S2975`)/9)*5

filtered_dataset$exception <- ((filtered_dataset$`outliersquid:RedundantThrowsDeclarationCheck` + filtered_dataset$`outliersquid:S1160`
                                 + filtered_dataset$`outliersquid:S1165` + filtered_dataset$`outliersquid:S1166`
                                 + filtered_dataset$`outliersquid:S1194` + filtered_dataset$`outliersquid:S2166` 
                                 + filtered_dataset$`outliersquid:S2221` + filtered_dataset$`outliersquid:S00112`)/8)*5


filtered_dataset$vmsmell <- ((filtered_dataset$`outliersquid:S1194` + filtered_dataset$`outliersquid:S1210`
                               + filtered_dataset$`outliersquid:S1217` + filtered_dataset$`outliersquid:S2059`
                               + filtered_dataset$`outliersquid:S2157` + filtered_dataset$`outliersquid:S2638` 
                               + filtered_dataset$`outliersquid:S2975`)/7)*5

filtered_dataset$interface <- ((filtered_dataset$`outliersquid:S00107` + filtered_dataset$`outliersquid:ClassVariableVisibilityCheck`
                               + filtered_dataset$`outliersquid:S1118` + filtered_dataset$`outliersquid:S1133`
                               + filtered_dataset$`outliersquid:S1160` + filtered_dataset$`outliersquid:S1609` 
                               + filtered_dataset$`outliersquid:S1610`)/7)*5

filtered_dataset$threading <- ((filtered_dataset$`outliersquid:S2134` + filtered_dataset$`outliersquid:S2222`
                               + filtered_dataset$`outliersquid:S2236` + filtered_dataset$`outliersquid:S2273`
                               + filtered_dataset$`outliersquid:S2276` + filtered_dataset$`outliersquid:S2693` 
                               + filtered_dataset$`outliersquid:S2885`)/7)*5

filtered_dataset$complexity <- ((filtered_dataset$`outliersquid:S00104` + filtered_dataset$`outliersquid:MethodCyclomaticComplexity`
                               + filtered_dataset$`outliersquid:S1133` + filtered_dataset$`outliersquid:S1188`
                               + filtered_dataset$`outliersquid:S1199` + filtered_dataset$`outliersquid:ClassCyclomaticComplexity`)/6)*5

filtered_dataset$ATDx <- (filtered_dataset$inheritance + filtered_dataset$exception + filtered_dataset$vmsmell + 
                          filtered_dataset$interface + filtered_dataset$threading + filtered_dataset$complexity)/6