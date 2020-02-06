library(readr)

# Patterns for manual removal
patterns <- c("demo", "course", "thesis", "exam", "tool",
              "util", "helper", "plugin", "plug-in",
              "homework", "sonarcloud", "sonarqube")

# ncloc_java and files repo filtering 
final_df <- subset(df, df$ncloc_java > 99 & df$files > 9)

# select projects for manual inspection
to_inspect <- filter(final_df, grepl(paste(patterns, collapse="|"), projectKey))

write_csv(to_inspect, "manual_repo_inspection.csv")

# load manual inspection results
manual_repo_inspection <- read_csv("manual_repo_inspection.csv")
View(manual_repo_inspection)

# filter out projects to be removed according to one granularity
final_df <- subset(final_df, !(final_df$X1 %in% manual_repo_inspection$X1 &
                     manual_repo_inspection$to_be_removed == 1))

# remove outliers according to iqr * 1.5
lowerq = quantile(final_df$ncloc_java)[2]
upperq = quantile(final_df$ncloc_java)[4]
iqr = upperq - lowerq
mild_threshold_lower = lowerq - (iqr * 1.5)
mild_threshold_upper = (iqr * 1.5) + upperq

final_df <- subset(final_df, final_df$ncloc_java >= mild_threshold_lower 
                   & final_df$ncloc_java <= mild_threshold_upper)


