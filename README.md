# Molecular Similarity Analysis Workflow

Molecular similarity analysis stands as a cornerstone in the realm of drug discovery, offering a systematic approach to unveil compounds with therapeutic potential. This method, rooted in the comparison of molecular structures, plays a pivotal role in identifying potential drug candidates, optimizing lead compounds, and guiding the intricate processes of structure-activity relationship (SAR) studies. By harnessing the power of molecular similarity, researchers can efficiently explore chemical space, predict crucial pharmacological and pharmacokinetic properties, and strategically navigate the complex landscape of drug development. This approach not only enhances the cost and time efficiency of the drug discovery process but also empowers scientists with valuable insights for the rational design and selection of compounds with desired bioactivities. Molecular similarity analysis thus emerges as a fundamental and indispensable tool, contributing to the success and advancement of drug development programs worldwide.

The primary objective of this research project is to design a filtering process that eliminates unsuitable or less suitable molecules while preserving potential drug candidates in drug discovery process. This project executes a series of three processes, where the input for each subsequent process is the output of the previous one. The workflow aims to analyze the similarity between small molecules, specifically drug candidates, and known drugs based on their molecular structures using Nextflow. For this analysis, a set of molecules, that are known to be good candidates for a drug are compared to another dataset of molecules for similarity. If molecules from the second dataset are similar enough to known drug candidates, they may be added to the conventional drug discovery process. The workflow is described in the picture below in the square box as a part of a bigger process of drug discovery.

![Slide1](https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/3b790e4e-5773-41cc-83ce-b5dc655a4c8e)

## Process 1: Calculate Similarity
The first process, named "calculateSimilarity," operates on a dataset of small molecules represented by molecular smiles. The dataset contains two columns, "SMILES_RESULT" and "SMILES_QUERY," representing the molecular formulas of known drugs and drug candidates, respectively. The goal is to assess the similarity between these drug candidates (SMILES_QUERY) and known drugs (SMILES_RESULT). If drug candidates exhibit sufficient similarity to known drugs, they can be further explored for characteristics such as affinity with a target, ADME (Absorption, Distribution, Metabolism, Excretion), and more. 

The script for this process utilizes the RDKit library to calculate similarity scores between pairs of molecules. The output is a file with an additional column containing similarity scores ranked from 0 to 1. To complete this process, a script called runSimScore.py is executed. The input file is provided in the data folder and is called “CS_for_sim.csv”. Additionally, to columns with molecular smiles, there are also columns with information on Dataset, product type, price, supplier, and ID, because the data comes from similarity search from the real vendor database. The output file is called “output.csv” and contains an extra column with a similarity score calculated.

Input file:
<img width="468" alt="image" src="https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/45d33e4b-cb92-4b0a-a276-e19691a9d8c1">

Output file:
<img width="468" alt="image" src="https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/7582945c-f8ed-4f22-af1c-fa1035ae9866">


## Process 2: Extract Top 10%
The second process, "extractTop10," takes the calculated similarity scores from Process 1 and extracts the top 10% of values along with their corresponding molecule pairs. These pairs represent the most similar drug candidates to known drugs, which can be further investigated. The scrip is called extractTop10.py, the “output.csv” from process 1 is becoming an input for this process, the generated file is called “top_10_percent.csv”.
The script for this process identifies and extracts the top 10% of similarity scores, providing a subset of molecular pairs for downstream analysis.

<img width="468" alt="image" src="https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/c9d03d32-74c0-4fd6-b1f2-40d7640c6f0f">


## Process 3: Visualization
The third process, "visualization," generates a distribution plot based on the top 10% of molecular pairs obtained from Process 2. This visualization helps in understanding the distribution of similarity scores within the selected subset.
The scrip is called visualize_top_pairs.py, the “top_10_percent.csv” from process 2 is becoming an input for this process, the generated file is called “distribution_plot.png”
The script for this process creates a distribution plot using the molecular pairs identified as the top 10% in the previous step.
The plot is below

<img width="468" alt="image" src="https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/09758368-6e2c-4006-9594-7e2cfde56740">


## Workflow
The three processes are orchestrated in a workflow, where the output of each process serves as the input for the subsequent one. This ensures a seamless analysis of molecular similarity and facilitates the identification of promising drug candidates.

### Usage
To execute the workflow, follow these steps:

## Set up

Follow instructions to install [git](https://github.com/git-guides/install-git), [conda](https://www.anaconda.com/download#macos), [nextflow](https://www.nextflow.io/docs/latest/getstarted.html#installation) and [docker](https://www.docker.com/get-started/) before running this pipeline.
The full list of dependencies is below:

  - nextflow 23.10.0
  - python=3.10
  - rdkit=2023.9.1
  - seaborn
  - pandas=2.1.2

### Using Conda

#### 1.	Clone the repository in your root folder.

``` cd ``` #this will redirect you to the root directory

``` git clone https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity.git ``` 

#### 2. Navigate to the project directory
``` cd Nextflow_MBB659-G100_Similarity ```

#### 3.	Create the environment. In the root of the repository run:
``` conda env create --file environment.yml ```

### Running the Analysis

Activate the environment

``` conda activate similarity ``` 

From the root directory run

``` nextflow Manskaia_project.nf ``` 

### Using Docker
Note: Docker was not running on all the machines, but the Dockerfile is presented in the repository

#### 1.	Install and launch Docker on your computer.

#### 2.	Clone the repository
``` git clone https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity.git ``` 

#### 3. Navigate to the project directory
``` cd Nextflow_MBB659-G100_Similarity ```

#### 4. Running the analysis

``` docker compose up jupyter-lab ```

In the terminal, look for a URL that starts with http://127.0.0.1:8888/lab?token= (for an example, see the highlighted text in the terminal below). Copy and paste that URL into your browser.

<img width="468" alt="image" src="https://github.com/emanskaia/Nextflow_MBB659-G100_Similarity/assets/139388597/b8a1e55c-5a43-414e-8fef-8eedbc4328ee">


## References
1. Warr, W. A., Nicklaus, M. C., Nicolaou, C. A., & Rarey, M. (2022). Journal of Chemical Information and Modeling, 62(9), 2021-2034. (https://doi.org/10.1021/acs.jcim.2c00224).
2. Torab-Miandoab, A., Poursheikh Asghari, M., Hashemzadeh, N. et al. Analysis and identification of drug similarity through drug side effects and indications data. BMC Med Inform Decis Mak 23, 35 2023. (https://doi.org/10.1186/s12911-023-02133-3)

