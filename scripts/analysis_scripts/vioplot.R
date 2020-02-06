library(vioplot)

#vioplot(paper_dataset$Interface, paper_dataset$Inheritance, paper_dataset$Exception, paper_dataset$JVMS, paper_dataset$Threading, paper_dataset$Complexity, paper_dataset$ATDx, names=c("Interface", "Inheritance", "Exception", "JVMS", "Threading", "Complexity", "ATDx"), col = c("#51B0FA", "#51B0FA", "#51B0FA","#51B0FA","#51B0FA","#51B0FA", "blue"))
vioplot(paper_dataset$interface, paper_dataset$inheritance, paper_dataset$exception,
        paper_dataset$vmsmell, paper_dataset$threading, paper_dataset$complexity,
        paper_dataset$ATDx, 
        # names=c("Interface", "Inheritance", "Exception", "JVMS", 
                # "Threading", "Complexity", "ATDx"), 
        col = c("#51B0FA", "#51B0FA", "#51B0FA","#51B0FA","#51B0FA",
                 "#51B0FA", "#2F6798")
        )
title(ylab="Value", xlab="ATDD")
grid(NULL, lty = 20, col = "grey", nx=0)