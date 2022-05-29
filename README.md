# CONCA
## Copy Number By Coverage Analysis

Script for the Microbial Metagenomics laboratory, A.Y. 2021/2022.

#### NOTICE
This code was developed as part of a project carried out during the course of Microbial Metagenomics (Molecular Biology master degree) at the University of Padova. The project was supervised by Prof. Stefano Campanaro, Dr. Maria Silvia Morlino, Dr. Edoardo Bizzotto, and Dr. Gabriele Ghiotto. The project was made by Anna Tanada, Carmen de Ancos Jimeno, Chiara Rebagliati, and Roberto Merlo.

#### INTRODUCTION
The objective of the CONCA script is to investigate whether the copy number of a gene varies under different experimental conditions within a Metagenome-Assembled Genome (MAG). Copy number variants (CNVs) are a mechanism by which gene expression can be regulated, and can be approximated by comparing the sequencing coverage of a gene to the median coverage of each gene in an experiment. Furthermore, CNVs can be calculated under different experimental conditions to make inferences about genetic and functional changes in the genome.

#### USING CONCA
##### 1. Input Files
 The input file should be a folder that contains .txt files with MAG data organized as a table. The number of input files can vary depending on the number of experiments performed, but the first .txt file should be the one containing the information from the control conditions.
 
 Within each table, each row should contain a gene (which should be in the same order for each table). Each table should also contain columns titled “Information” and “COVERAGE” for each gene. The “Information” column should contain a label and information for the contig (such as the ID, db_xref, Name, etc.), with the information separated by a semicolon (;) and label separated from the information with an equal sign (=). The “COVERAGE” column should contain a numerical value reporting the coverage of that gene for the given experiment.
 
 Example of “Information” formatting: ``ID=JHFGFCBP_00001;db_xref=COG:COG0419;inference=ab …``
 
 ##### 2. Running The Script
 Ensure that all .txt files with the experimental condition tables are together in a folder, with the control table as the first file in the folder. Then run the following command in the terminal:
``
python CONCA_script.py folder_name outputfile_name
``
##### 3. Output Files
After running the command, the user should receive 2 output files as .txt files, which can be visualized as a table.
The first table, titled “output_filename.txt”, contains the original information from the tables plus the average copy number of each gene under each experimental condition (designated as Expt_1, Expt_2, etc.) in the order the experiments were provided in the input folder.
The second table, titled “information.txt”, contains the information provided for each gene separated by label for easy viewing.

##### 4. Heatmaps
After producing the first two output tables, the program will ask the user if they would like to generate a heatmap for a given COG or KEGG code. 
Entering a code after the prompt will generate a heatmap that shows the changes in CNVs under different conditions for genes identified with that code in the “Information” section of the original input tables.
