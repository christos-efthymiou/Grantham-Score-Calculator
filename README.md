# Grantham Score Calculator for Missense Mutations
## Overview
This [Streamlit application](https://grantham-score-calculator-by-christos-efthymiou.streamlit.app/) calculates the Grantham score for missense mutations in proteins. The Grantham score quantifies the chemical similarity between different amino acids and is widely used to predict the effects of point mutations on protein stability and function. However, since the publication of the amino acid substitution scores in 1974, no automated way to calculate the scores had been developed. This left individuals (including myself!) to search in a table to find the score for each amino acid substitution manually. This is extremely time consuming and impossible when evaluating hundreds of mutations. Therefore, I have created a Streamlit app so anyone can easily calculate the Grantham scores for missense mutations which can be accessed here: https://grantham-score-calculator-by-christos-efthymiou.streamlit.app/

## Features
- Grantham Score Calculation: Enter mutations in a specified format to compute their Grantham scores quickly.
- Histogram Visualization: View a histogram of computed Grantham scores directly in the app.
- Interactive 3D Visualization: Explore mutations on protein structures using an interactive 3D viewer.
- Downloadable Results: Easily download the results as CSV or TXT files, as well as the histogram plot as a PNG file.
- Dynamic Mutation Highlighting: Highlight and label specific mutations on the 3D structure of a protein by entering PDB codes and selecting residues.

## Usage
Upon launching the app, you will be greeted with an interface that guides you through the process of inputting your mutations, viewing results, and exploring protein structures. Here's a quick guide:

- Input Mutations: Enter your mutations in the input box in the format A987E R47K L1009V. The app can process mutations copied directly from an Excel column.
- View Histogram: The sidebar includes a histogram of the Grantham scores, providing a visual distribution of the scores.
- Download Results: Use the download buttons to save your results as CSV or TXT files, or download the histogram plot as a PNG file.
- 3D Visualization: Enter a PDB code and select residues to visualize mutations on the protein structure. Adjust visual settings such as color and transparency to enhance your view.

## Contributing
Contributions to this project are welcome. You can contribute in several ways:

- Enhance the computational efficiency of the score calculations.
- Extend the functionality to include more mutation types.
- Improve the user interface for a more seamless experience.

Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Christos Efthymiou](https://www.linkedin.com/in/christos-efthymiou/)

## Acknowledgments
Thanks to the developers of Streamlit and RDKit for providing the tools that power this application.