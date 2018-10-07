# ExAC Viewer

This is a tool that provides clean visualization of ExAC data (http://exac.broadinstitute.org/) that is easy to interpret and understand.

## Functionality

- takes downloaded ExAC file for a gene
- removes all mutations with frequency 1
- user can specify a class of mutations to view (e.g missense, loss of function, splice)
- returns color coded chart of mutations with ethnic distribution and separate table of frequencies split by ethnicity

## How to Use This Tool

Package Dependencies: xlsxwriter, xlrd
Download python script, exacView.py, specify extra arguments as such and run in terminal

Which mutations to consider? Enter 1 to consider all types (default), 2 for missense only, 3 for non coding transcript exon, 4 for frameshift, 5 for 5'UTR, 6 for 3'UTR, 7 for synonymous, 8 for splice, 9 for intron. If you want to consider onlt frameshift and 5'UTR enter the numbers 46 or 64. 

#### exacView.py FullPathToDownloadedExACFile TypesOfMutations


#### Other Things To Add
- enter gene name and get initial ExAC file
- allow for multiple genes to be inputted
- generate pysch versus nonpsych data, cancer versus noncancer data
