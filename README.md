# ExAC Viewer

This is a tool that provides clean visualization of ExAC data (http://exac.broadinstitute.org/) that is easy to interpret and understand.

## Functionality

- takes downloaded ExAC file for a gene
- removes all mutations with frequency 1
- user can specify a class of mutations to view (e.g missense, loss of function, splice)
- returns color coded chart of mutations with ethnic distribution and separate table of frequencies split by ethnicity

## How to Use This Tool

Package Dependencies: xlsxwriter, xlrd
Download python script, exacView.py, and run in terminal. 
Enter the full path for the downloaded ExAC file when prompted by the script. 


#### Other Things To Add
- enter gene name and get initial ExAC file
- allow for multiple genes to be inputted
- generate pysch versus nonpsych data, cancer versus noncancer data
