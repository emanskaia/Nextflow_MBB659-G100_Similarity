import pandas as pd

def extract_top_10_percent(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Sort the DataFrame based on the "similarity" column
    df_sorted = df.sort_values(by='Similarity', ascending=False)

    # Calculate the index to get the top 10%
    top_10_percent_index = int(0.1 * len(df_sorted))

    # Extract the top 10%
    top_10_percent_df = df_sorted.head(top_10_percent_index)

    # Write the result to the output CSV file
    top_10_percent_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Input and output file paths
    input_file = "output.csv"
    output_file = "top_10_percent.csv"

    # Call the function to extract the top 10%
    extract_top_10_percent(input_file, output_file)
