# Example Pipeline 

The example pipeline demos the standard way to use the script. This pipeline is run for Sig1R, the Sigma 1 Receptor. 

### Getting the ExAC file 

1) Visit http://exac.broadinstitute.org/ and use the identified OPRS1. 
2) Export the table to csv
        Downloaded File Name: exac_ENSG00000147955_2019_04_19_14_55_03.csv
        Open the csv file in Excel and save as xls file. 
3) Download the ExAC-Viewer repository by clicking "Download ZIP"
4) Unzip the file on your computer and find exacView.py
5) Move the xls ExAC file into the unzipped repository folder
6) cd into the unzipped repository and enter the command: 
         python3 exacView.py exac_ENSG00000147955_2019_04_19_14_55_03.xls 2
         
         The command considers only missense mutations becasue the second argument given was a '2'.
7) The outuput charts have now been created within the unzipped repository folder. 

        
