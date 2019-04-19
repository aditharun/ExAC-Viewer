# ExAC Viewer: Clean visualization of ExAC Data 

This script generates a summary of the ExAC Data for a gene of interest. The summary consists of an ethnic breakdown and allele frequency percentage. It takes in raw downloaded data for a gene, and creates charts that are easy to understand and interpret. 

These charts look nice, and can be made into manuscript-ready tables with relative ease. 

An example pipeline of this script is shown for the gene Sig1R, under the folder examplePipeline. 

### Input

Choose a gene from the ExAC portal (http://exac.broadinstitute.org/). 
Download the csv file with all the data. 
Save the csv file as an xls file. 
Store the xls file in the same directory as this script.

### Dependencies 

Make sure python3 is installed (https://www.python.org/downloads/). 
  Check python version: 
    on Mac --> python --version   
    on Windows --> python
Install xlrd and xlsxwriter packages by the following command in the terminal: 
  pip3 install xlrd
  pip3 install xlsxwriter

### Runnning the Script

1) download the script
2) follow the directions in the above section (Dependencies)
2) store the script in the same directory as the xls ExAC file
3) run the command as such:
        python3 scriptname.py filenameofExAC mutations
        
        scriptname.py is the name of the python script that you downloaded from this repository
        filenameofExAC is the file name for the xls ExAC file
        mutations is the parameter that specifies which mutations to consider
        
        mutations LEGEND
        
        Which mutations to consider? 
        1 to consider all types (default parameter)
        2 for missense only
        3 for non coding transcript exon
        4 for frameshift
        5 for 5'UTR
        6 for 3'UTR
        7 for synonymous
        8 for splice
        9 for intron
        
        If you want to consider a combination of mutation types, such as frameshift and 5'UTR enter the numbers 46 or 64. 

### Output

The script returns an Excel file outputted to the directory from which you ran the program. The output file will be titled SummaryChart.xlsx. 

Only mtations with allele count greater than 1 are considered. This is to ensure that only "relatively frequent" mutations are considered, and so the visualizaiton of the data is meaningful. This parameter can be changed easily within the script. 

There are two charts that are created: 
  1) Ethnic Breakdown -- reports allele count, total allele number, and number of homozygotes for each mutation
  2) Allele Frequency Percentage -- reports allele frequency percentage affected by each mutation, and it is broken down by ethnic subgroup
