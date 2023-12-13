import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

def calculate_similarity(smiles1, smiles2):
    # Convert SMILES to RDKit molecules
    mol1 = Chem.MolFromSmiles(smiles1)
    mol2 = Chem.MolFromSmiles(smiles2)

    # Generate Morgan fingerprints
    if mol1 and mol2:
        fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 2, nBits=1024)
        fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2, nBits=1024)

        # Calculate Tanimoto similarity
        similarity = DataStructs.TanimotoSimilarity(fp1, fp2)
        return similarity
    else:
        return None

# Read the CSV file containing pairs of SMILES
csv_file = "~/data/CS_for_sim.csv"
molecule_pairs = pd.read_csv(csv_file)

# Add a new column for similarity scores
molecule_pairs['Similarity'] = molecule_pairs.apply(lambda row: calculate_similarity(row['SMILES_QUERY'], row['SMILES_RESULT']), axis=1)

# Print the resulting DataFrame
print(molecule_pairs)

output_file = "output.csv"
molecule_pairs.to_csv(output_file, index=False)
