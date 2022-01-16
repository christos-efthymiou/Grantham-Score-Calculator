## Welcome to the Grantham Score Calculator

The Grantham score is a score ranging from 5 to 215 which predicts how likely a missense mutation is to be damaging. The score theorizes that the more distant two amino acids are in terms of their chemical characteristics, the more likely it is for a mutation to be damaging. Therefore, a higher score corresponds to a higher likelihood of damage caused by a mutation [Grantham, 1974](https://pubmed.ncbi.nlm.nih.gov/4843792/). 

The scores have been compiled in a table, shown here: 

![image](https://user-images.githubusercontent.com/97161093/149503335-1bade813-e9ef-4a3e-bd44-4bd5e74c36d0.png)

However, when dealing with hundreds or thousands of mutations, it is not feasible to find these scores manually. Therefore, you can use this site to automatically calculate the score for each of your missense mutations. In the textbox below, enter each mutation in the format Arg86Lys on a separate line. In other words, the three letter code of the original amino acid, followed by the number amino acid in your protein, and the three letter code of the mutated amino acid. 

<html>
   <head>
      <title>HTML textarea Tag</title>
   </head>

   <body>
      <form id="form" action = "/cgi-bin/hello_get.cgi" method = "get">
         Enter mutations on separate lines with format Arg86Lys
         <br>
         <textarea id="textareaId" rows = "5" cols = "60" name = "description"></textarea><br>
         <input type = "submit" value = "submit" />
      </form>
      <script>
      let form = document.getElementById("form");
let data = {"Arg Lys":100}; // store data like this
form.addEventListener("submit",function(e){
e.preventDefault();
var lines = document.getElementById('textareaId').value.split('\n');
document.getElementById('textareaId').value = '';
    for(var i = 0;i < lines.length;i++){
   let val = lines[i].substring(0,3);
   let lastval = lines[i].substring(lines[i].length - 3)
   document.getElementById('textareaId').value += val+' '+lastval + ' - ' +data[val+' '+lastval]+'\n';
}
})
   <\script>
   </body>
</html>

