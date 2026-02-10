# ancPhntp

A containerized bioinformatics command-line tool for extracting HIrisPlex SNPs from aligned sequencing data and preparing standardized inputs and reports for phenotype prediction in archaeogenetics.

## Overview

Phenotype reconstruction from ancient DNA is a common task in archaeogenetics and forensic genomics. The HIrisPlex system predicts pigmentation traits based on a defined panel of SNPs, but preparing the required input from aligned sequencing files can be repetitive and error-prone.

ancPhntp automates this process by extracting the required SNPs from aligned sequencing data and producing standardized outputs suitable for downstream HIrisPlex analysis. The tool is designed as a reproducible, containerized CLI application that can be executed locally or in cloud environments.

## Key Features

- Extraction of HIrisPlex SNP positions from aligned sequencing files (SAM)
- Support for human reference genomes hg19 and hg38
- Generation of CSV files compatible with the HIrisPlex web service
- Conversion of HIrisPlex output into structured DOCX phenotype reports
- Docker-based execution for reproducibility and portability
- Simple and explicit command-line interface

## Typical Workflow

1. SNP Extraction  
   Extracts HIrisPlex SNP information from an aligned SAM file and generates a CSV file in the required HIrisPlex format.

2. HIrisPlex Prediction  
   The generated CSV file is uploaded to the HIrisPlex web service, which returns phenotype prediction results.

3. Report Generation  
   Converts HIrisPlex output files into human-readable DOCX reports for single or multiple samples.

## Project Structure

ancPhntp/
├── src/                Source code  
├── data/               Reference SNP tables (hg19 / hg38)  
├── input_output/       User-provided input and output files (mounted at runtime)  
├── requirements.txt  
├── Dockerfile  
└── README.md  

## Requirements

Recommended:
- Docker

For non-containerized execution:
- Python 3.9+
- Linux or macOS

## Running with Docker

Build the image:

docker build -t ancphntp .

Run the pipeline:

docker run --rm \
  -v $(pwd)/input_output:/data \
  ancphntp \
  --sam /data/sample.sam \
  --id S20 \
  --ref 38

Input sequencing files are provided via a mounted volume.  
Reference SNP tables are bundled inside the container to ensure reproducible execution.

## Command-Line Arguments

--sam   Path to aligned SAM file  
--id    Sample identifier  
--ref   Reference genome version (19 or 38)

## Outputs

- CSV  Intermediate file formatted for HIrisPlex upload
- DOCX Final phenotype report generated from HIrisPlex results

## Design Decisions

- Docker-first design to ensure reproducibility and simplify deployment
- Clear separation of code, reference data, and user input/output
- Reference data bundled with the container image to guarantee consistent SNP coordinates
- Volume-mounted input/output to support large sequencing files efficiently

## Intended Use

This tool is intended for research and educational purposes in archaeogenetics, forensic genomics, and related bioinformatics workflows.

## Future Improvements

- Support for BAM and CRAM input formats
- Configurable output directories
- Batch processing of multiple samples
- Automated execution of HIrisPlex predictions

## Author

Developed by Daniil Shvartsman
