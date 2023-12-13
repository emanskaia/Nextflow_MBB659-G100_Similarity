# Use Jupyter's minimal-notebook as base image
FROM quay.io/jupyter/minimal-notebook:notebook-7.0.6

RUN pip install scikit-learn==1.3.2 
RUN pip install pandas==2.1.2
RUN pip install rdkit==2023.9.1
RUN pip install seaborn==0.11.2