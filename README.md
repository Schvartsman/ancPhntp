# ancPhntp

A lightweight command-line tool for extracting SNP data from aligned sequencing files and preparing input/output files for **HIrisPlex** phenotype prediction in archaeological genetics.

## Overview

Phenotype reconstruction is an important task in archaeological genetics. **HIrisPlex** is a widely used tool that predicts phenotypic traits based on a set of 42 SNPs. Extracting the required SNP information from aligned sequencing data (SAM files) can be time-consuming and error-prone, especially when working with large datasets.

`ancPhntp` automates this workflow by extracting SNP data and formatting results for downstream processing. The tool is designed to be simple and accessible, even for users with limited experience in Linux environments.

## Features

- Extraction of HIrisPlex SNP positions from aligned SAM files  
- Support for multiple reference genomes (hg19, hg38)  
- Generation of CSV files compatible with the HIrisPlex website  
- Conversion of HIrisPlex results into a DOCX report  
- Simple command-line interface  

## Workflow

The pipeline consists of two main steps:

1. **SNP extraction**  
   Extracts SNP data from an aligned SAM file and generates a CSV file in the required HIrisPlex format.

2. **Report generation**  
   Converts the HIrisPlex output file into a DOCX document containing phenotype predictions.

## Requirements

- Python 3.x  
- Linux or macOS  
- Aligned and sorted sequencing data in SAM format  

## Usage

### Step 1: SNP Extraction

Run the SNP extraction script with the following arguments:

- `--sam` — path to the aligned SAM file  
- `--id` — sample identifier (any string)  
- `--ref` — reference genome version (`19` or `38`)  

Example:

```bash
path_to_directory/ancPhntp/src/calling.py \
  --sam path_to_sam \
  --id S20 \
  --ref 38
```

The resulting CSV file is written to the user’s home directory.

### Step 2: HIrisPlex Processing

Upload the generated CSV file to the **HIrisPlex** website. The service returns a file containing phenotype predictions.

### Step 3: Report Generation

Convert the HIrisPlex output into a DOCX report:

- Use `table.py` for a single sample
- Use `table.mult.py` for multiple samples

Example:

```bash
path_to_directory/ancPhntp/src/table.py \
  --input path_to_file/Results.csv
```

The final DOCX report is saved in the home directory.

## Supported Reference Genomes

- hg19
- hg38

## Output

- **CSV** — intermediate file for HIrisPlex upload
- **DOCX** — final phenotype report

## Future Improvements

- Configurable output directories
- Ability to run scripts from the current working directory
- Support for additional reference genomes
