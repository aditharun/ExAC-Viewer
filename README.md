# ExAC Viewer

This is a tool that provides clean visualization of ExAC data (http://exac.broadinstitute.org/) that is easy to interpret and understand.

## Output

Returns an excel file stored in your current working directory, titled the same as you initial file but with the word FORMATTED inserted. The first sheet of the excel file is a neatly and cleanly organized table of pertinent information regarding each mutation of interest split by ethnicity. The second sheet is a table that shows percent frequency of mutations in the overall population and by ethnicity. This table condenses all the ExAC data into one tidy chart that is easy to interpret. 

## Functionality

- takes downloaded ExAC file for a gene
- removes all mutations with frequency 1
- user can specify a class of mutations to view (e.g missense, loss of function, splice)
- returns color coded chart of mutations with ethnic distribution and separate table of frequencies split by ethnicity

## How to Use This Tool

Package Dependencies: xlsxwriter, xlrd
Download python script, exacView.py, specify extra arguments as such and run in terminal

Which mutations to consider? Enter 1 to consider all types (default), 2 for missense only, 3 for non coding transcript exon, 4 for frameshift, 5 for 5'UTR, 6 for 3'UTR, 7 for synonymous, 8 for splice, 9 for intron. If you want to consider only frameshift and 5'UTR enter the numbers 46 or 64. 

#### Example Command Line Input for Program:: exacView.py FullPathToDownloadedExACFile TypesOfMutations
