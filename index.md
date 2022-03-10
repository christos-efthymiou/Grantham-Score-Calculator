## Welcome to the Grantham Score Calculator

To calculate Grantham scores, visit the [Google Colab notebook here](https://colab.research.google.com/drive/19Qavi2gFNx9YF085CS7CGptR-BxEY70T?usp=sharing)

The Grantham score is a score ranging from 5 to 215 which predicts how likely a missense mutation is to be damaging. The score theorizes that the more distant two amino acids are in terms of their chemical characteristics, the more likely it is for a mutation to be damaging. Therefore, a higher score corresponds to a higher likelihood of damage caused by a mutation [Grantham, 1974](https://pubmed.ncbi.nlm.nih.gov/4843792/). 

The scores have been compiled in a table, shown here: 

![image](https://user-images.githubusercontent.com/97161093/149503335-1bade813-e9ef-4a3e-bd44-4bd5e74c36d0.png)

However, when dealing with hundreds or thousands of mutations, it is not feasible to find these scores manually. Therefore, you can use the google colab notebook https://colab.research.google.com/drive/19Qavi2gFNx9YF085CS7CGptR-BxEY70T?usp=sharing to automatically calculate the score for each of your missense mutations. In the input box, enter each mutation in the format A86K with a space separating each mutation. In other words, the one letter code of the original amino acid, followed by the number amino acid in your protein, and the one letter code of the mutated amino acid. 
