## Welcome to the Grantham Score Calculator

The Grantham score is a score ranging from 5 to 215 which predicts how likely a missense mutation is to be damaging. The score theorizes that the more distant two amino acids are in terms of their chemical characteristics, the more likely it is for a mutation to be damaging. Therefore, a higher score corresponds to a higher likelihood of damage caused by a mutation [Grantham, 1974](https://pubmed.ncbi.nlm.nih.gov/4843792/). 

The scores have been compiled in a table, shown here: 

![image](https://user-images.githubusercontent.com/97161093/149503335-1bade813-e9ef-4a3e-bd44-4bd5e74c36d0.png)

However, when dealing with hundreds or thousands of mutations, it is not feasible to find these scores manually. Therefore, you can use this site to automatically calculate the score for each of your missense mutations. In the textbox below, enter each mutation in the format Arg86Lys on a separate line. In other words, the three letter code of the original amino acid, followed by the number amino acid in your protein, and the three letter code of the mutated amino acid. 

<input type="text" id="name" name="name"/>

```python
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
  
  
root = tk.Tk()
  
root.title("ScrolledText Widget Example")
  
ttk.Label(root, text="ScrolledText Widget Example",
          font=("Times New Roman", 15)).grid(column=0, row=0)
ttk.Label(root, text="Enter your comments :", font=("Bold", 12)).grid
(column=0, row=1)
  
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                      width=40, height=8,
                                      font=("Times New Roman", 15))
  
text_area.grid(column=0, row=2, pady=10, padx=10)
  
# placing cursor in text area
text_area.focus()
root.mainloop()
```
