Molecular Similarity Analysis Workflow
This project executes a series of three processes, where the input for each subsequent process is the output of the previous one. The workflow aims to analyze the similarity between small molecules, specifically drug candidates, and known drugs based on their molecular structures using Nextflow.

Process 1: Calculate Similarity
The first process, named "calculateSimilarity," operates on a dataset of small molecules represented by molecular smiles. The dataset contains two columns, "Smiles1" and "Smiles2," representing the molecular formulas of known drugs and drug candidates, respectively. The goal is to assess the similarity between these drug candidates and known drugs. If drug candidates exhibit sufficient similarity to known drugs, they can be further explored for characteristics such as affinity with a target, ADME (Absorption, Distribution, Metabolism, Excretion), and more.

Implementation
The script for this process utilizes the RDKit library to calculate similarity scores between pairs of molecules. The output is a file with an additional column containing similarity scores ranked from 0 to 1.

Process 2: Extract Top 10%
The second process, "extractTop10," takes the calculated similarity scores from Process 1 and extracts the top 10% of values along with their corresponding molecule pairs. These pairs represent the most similar drug candidates to known drugs, which can be further investigated.

Implementation
The script for this process identifies and extracts the top 10% of similarity scores, providing a subset of molecular pairs for downstream analysis.

Process 3: Visualization
The third process, "visualization," generates a distribution plot based on the top 10% of molecular pairs obtained from Process 2. This visualization helps in understanding the distribution of similarity scores within the selected subset.

Implementation
The script for this process creates a distribution plot using the molecular pairs identified as the top 10% in the previous step.

Workflow
The three processes are orchestrated in a workflow, where the output of each process serves as the input for the subsequent one. This ensures a seamless analysis of molecular similarity and facilitates the identification of promising drug candidates.

Usage
To execute the workflow, follow these steps:

Set up
Docker:

1.	Clone the repository.
git clone https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity.git

2.	Install and launch Docker on your computer.

Virtual Environment:

1.	Clone the repository. https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity.git

2.	Create the environment. In the root of the repository run:

conda env create --file environment.yml

Running the Analysis

  [conda activate similarity-env]

From root directory run

  [nextflow Manskaia_project.nf]

