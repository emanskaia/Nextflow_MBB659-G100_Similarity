#!/usr/bin/env nextflow

nextflow.enable.dsl=2

// Process 1: Calculate Similarity
process calculateSimilarity {

    // Specify input and output
    input:
    path input_csv, name: 'CS_for_sim.csv'

    output:
    path 'output.csv'

    // Specify the script to run
    script:
    """
    python ~/Nextflow_MBB659-G100_Similarity/src/runSimScore.py ${input_csv} ${'output.csv'}
    """
}

// Process 2: Extract Top 10%
process extractTop10 {

    // Specify input and output
    input:
    path 'output.csv'

    output:
    path 'top_10_percent.csv'

    // Specify the script to run
    script:
    """
    python ~/Nextflow_MBB659-G100_Similarity/src/extractTop10.py ${'output.csv'} ${'top_10_percent.csv'}
    """
}

// Process 3: Visualization
process visualization {

    // Specify input
    input:
    path 'top_10_percent.csv'

    output:
    path 'distribution_plot.png'

    // Specify the script to run
    script:
    """
    python ~/Nextflow_MBB659-G100_Similarity/src/visualize_top_pairs.py ${'top_10_percent.csv'} ${'distribution_plot.png'}
    """
}

// Define the workflow structure
workflow {

    // Execute processes in order
    
    data = channel.fromPath('~/Nextflow_MBB659-G100_Similarity/data/CS_for_sim.csv')
    calculateSimilarity(data) \
        | extractTop10 \
        | visualization
    
}
