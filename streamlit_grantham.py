#Import Python Libraries
import pandas as pd
import streamlit as st
import numpy as np
import io
import matplotlib.pyplot as plt
import py3Dmol
from stmol import showmol
import re

#Add sidebar title
st.sidebar.markdown("### Histogram of Grantham Scores")

#Add title and subtitle to the main interface of the app
st.title("Grantham Score Calculator")
st.markdown("To get the grantham score for your mutations, enter your mutations in the input box in the format A987E R47K L1009V (format is first aa_residue location_mutated aa SPACE repeat.). If you copy and paste from a column in Excel, it should automatically convert your mutations to be separated by a space (as is needed!). That's it!")

#Input box for mutations to be entered 
mutations = st.text_input("Mutations separated by a space", '')
#Remove the residue numbers as they do not factor in the Grantham model 
no_digits = ''.join([i for i in mutations if not i.isdigit()])
#Split the string into a list
mutations_list = no_digits.split()
#Dictionary containing all Grantham scores 
dict = {'AA':'0','AC':'195','AD':'126','AE':'107','AF':'113','AG':'60','AH':'86','AI':'94','AK':'106','AL':'96','AM':'84','AN':'111','AP':'27','AQ':'91','AR':'112','AS':'99','AT':'58','AV':'64','AW':'148','AY':'112','CA':'195','CC':'0','CD':'154','CE':'170','CF':'205','CG':'159','CH':'174','CI':'198','CK':'202','CL':'198','CM':'196','CN':'139','CP':'169','CQ':'154','CR':'180','CS':'112','CT':'149','CV':'192','CW':'215','CY':'194','DA':'126','DC':'154','DD':'0','DE':'45','DF':'177','DG':'94','DH':'81','DI':'168','DK':'101','DL':'172','DM':'160','DN':'23','DP':'108','DQ':'61','DR':'96','DS':'65','DT':'85','DV':'152','DW':'181','DY':'160','EA':'107','EC':'170','ED':'45','EE':'0','EF':'140','EG':'98','EH':'40','EI':'134','EK':'56','EL':'138','EM':'126','EN':'42','EP':'93','EQ':'29','ER':'54','ES':'80','ET':'65','EV':'121','EW':'152','EY':'122','FA':'113','FC':'205','FD':'177','FE':'140','FF':'0','FG':'153','FH':'100','FI':'21','FK':'102','FL':'22','FM':'28','FN':'158','FP':'114','FQ':'116','FR':'97','FS':'155','FT':'103','FV':'50','FW':'40','FY':'22','GA':'60','GC':'159','GD':'94','GE':'98','GF':'153','GG':'0','GH':'98','GI':'135','GK':'127','GL':'138','GM':'127','GN':'80','GP':'42','GQ':'87','GR':'125','GS':'56','GT':'59','GV':'109','GW':'184','GY':'147','HA':'86','HC':'174','HD':'81','HE':'40','HF':'100','HG':'98','HH':'0','HI':'94','HK':'32','HL':'99','HM':'87','HN':'68','HP':'77','HQ':'24','HR':'29','HS':'89','HT':'47','HV':'84','HW':'115','HY':'83','IA':'94','IC':'198','ID':'168','IE':'134','IF':'21','IG':'135','IH':'94','II':'0','IK':'102','IL':'5','IM':'10','IN':'149','IP':'95','IQ':'109','IR':'97','IS':'142','IT':'89','IV':'29','IW':'61','IY':'33','KA':'106','KC':'202','KD':'101','KE':'56','KF':'102','KG':'127','KH':'32','KI':'102','KK':'0','KL':'107','KM':'95','KN':'94','KP':'103','KQ':'53','KR':'26','KS':'121','KT':'78','KV':'97','KW':'110','KY':'85','LA':'96','LC':'198','LD':'172','LE':'138','LF':'22','LG':'138','LH':'99','LI':'5','LK':'107','LL':'0','LM':'15','LN':'153','LP':'98','LQ':'113','LR':'102','LS':'145','LT':'92','LV':'32','LW':'61','LY':'36','MA':'84','MC':'196','MD':'160','ME':'126','MF':'28','MG':'127','MH':'87','MI':'10','MK':'95','ML':'15','MM':'0','MN':'142','MP':'87','MQ':'101','MR':'91','MS':'135','MT':'81','MV':'21','MW':'67','MY':'36','NA':'111','NC':'139','ND':'23','NE':'42','NF':'158','NG':'80','NH':'68','NI':'149','NK':'94','NL':'153','NM':'142','NN':'0','NP':'91','NQ':'46','NR':'86','NS':'46','NT':'65','NV':'133','NW':'174','NY':'143','PA':'27','PC':'169','PD':'108','PE':'93','PF':'114','PG':'42','PH':'77','PI':'95','PK':'103','PL':'98','PM':'87','PN':'91','PP':'0','PQ':'76','PR':'103','PS':'74','PT':'38','PV':'68','PW':'147','PY':'110','QA':'91','QC':'154','QD':'61','QE':'29','QF':'116','QG':'87','QH':'24','QI':'109','QK':'53','QL':'113','QM':'101','QN':'46','QP':'76','QQ':'0','QR':'43','QS':'68','QT':'42','QV':'96','QW':'130','QY':'99','RA':'112','RC':'180','RD':'96','RE':'54','RF':'97','RG':'125','RH':'29','RI':'97','RK':'26','RL':'102','RM':'91','RN':'86','RP':'103','RQ':'43','RR':'0','RS':'110','RT':'71','RV':'96','RW':'101','RY':'77','SA':'99','SC':'112','SD':'65','SE':'80','SF':'155','SG':'56','SH':'89','SI':'142','SK':'121','SL':'145','SM':'135','SN':'46','SP':'74','SQ':'68','SR':'110','SS':'0','ST':'58','SV':'124','SW':'177','SY':'144','TA':'58','TC':'149','TD':'85','TE':'65','TF':'103','TG':'59','TH':'47','TI':'89','TK':'78','TL':'92','TM':'81','TN':'65','TP':'38','TQ':'42','TR':'71','TS':'58','TT':'0','TV':'69','TW':'128','TY':'92','VA':'64','VC':'192','VD':'152','VE':'121','VF':'50','VG':'109','VH':'84','VI':'29','VK':'97','VL':'32','VM':'21','VN':'133','VP':'68','VQ':'96','VR':'96','VS':'124','VT':'69','VV':'0','VW':'88','VY':'55','WA':'148','WC':'215','WD':'181','WE':'152','WF':'40','WG':'184','WH':'115','WI':'61','WK':'110','WL':'61','WM':'67','WN':'174','WP':'147','WQ':'130','WR':'101','WS':'177','WT':'128','WV':'88','WW':'0','WY':'37','YA':'112','YC':'194','YD':'160','YE':'122','YF':'22','YG':'147','YH':'83','YI':'33','YK':'85','YL':'36','YM':'36','YN':'143','YP':'110','YQ':'99','YR':'77','YS':'144','YT':'92','YV':'55','YW':'37','YY':'0'}
values = []
#For every value in the mutations entered by user, if the value is found in teh dictionary 
for i in mutations_list: 
    if i in dict: 
        value = dict.get(i)
        values.append(value)

#Get residue numbers from the input of the user 
int_values = [ int(i) for i in values ]
values_array = np.array(int_values)

#Create two columns 
col1, col2 = st.columns(2)
#Create button to download results as CSV
with col1:
   with io.BytesIO() as buffer:
    # Write array to buffer
        np.savetxt(buffer, values_array, delimiter=",", fmt='%i')
        st.download_button(
            label="Download results as CSV",
            data = buffer, # Download buffer
            file_name = 'grantham_scores.csv',
            mime='text/csv'
        )
#Create button to download results as .txt 
with col2: 
    with io.BytesIO() as buffer2:
    # Write array to buffer
        np.savetxt(buffer2, values_array, delimiter=",", fmt='%i')
        st.download_button(
            label="Download results as txt",
            data = buffer2, # Download buffer
            file_name = 'grantham_scores.txt',
            mime='text/csv'
        )    

#Also print all the scores on the screen so users can copy and paste from there 
for i in values: 
    st.text(i)

#Histogram Plot
with st.sidebar:
    fig, ax = plt.subplots()
    ax.hist(values_array, bins=10, edgecolor="black")
    plt.xlabel('Grantham Score')
    plt.ylabel('Counts')
    plt.title('Grantham Score Histogram', fontsize = 18)
    plt.xlim(5, 215)

#Allow users to download plot as a png 
    st.pyplot(fig)
    image_name = 'histogram.png'
    plt.savefig(image_name,dpi=300)
    with open(image_name, "rb") as img:
        btn = st.download_button(
            label="Download plot as png",
            data=img,
            file_name=image_name,
            mime="image/png"
        )

#Visualize mutations on PDB files
st.sidebar.markdown("### Visualize Mutations on PDB File")

#Allow users to select a PDB code, but provide default value of 7KXY
pdb_code = st.sidebar.text_input(
        label="PDB Code",
        value="7KXY",
    )

#Extract residue numbers from the mutations list entered by users previously 
only_digits = re.findall(r'\d+', mutations)

#Add the word All to the beginning of the residue numbers list to create 
#an option to select all the residues at once 
only_digits.insert(0,"All")

#Provide ability to select one or more residues at a time, as well as All
hl_resi_list = st.sidebar.multiselect("Select the residue numbers to highlight:",only_digits)

#If a user selects the All option from multiselect, all residue numbers will be used 
if "All" in hl_resi_list:
    hl_resi_list = only_digits

#Tell user to specify which chain from the PDB file should have its residues highlighted 
hl_chain = st.sidebar.text_input(label="Select the relevant chain from the PDB file",value="A")
#Provide user with option to have labels on residues or not 
label_resi = st.sidebar.checkbox(label="Label Selected Residues", value=True)
#Allow user to show the protein as a surface representation 
surf_transp = st.sidebar.slider("Surface Transparency", min_value=0.0, max_value=1.0, value=0.0)
#Allow user to select the color for highlighting mutants 
hl_color = st.sidebar.text_input(label="Highlight Color of Mutants",value="red")
#Allow user to select backbone color 
bb_color = st.sidebar.text_input(label="Protein Backbone Color",value="lightgrey")
#Allow user to select ligand color 
lig_color = st.sidebar.text_input(label="Ligand Color",value="white")

st.markdown(f"## PDB [{pdb_code.upper()}](https://www.rcsb.org/structure/{pdb_code}) (Chain {hl_chain})")

### Step 3) Py3Dmol
#Set dimensions for py3dmol visualization box 
width = 700
height = 700

#remaining code in this section was found here https://github.com/napoles-uach/stmol
cartoon_radius = 0.2
stick_radius = 0.2

view = py3Dmol.view(query=f"pdb:{pdb_code.lower()}", width=width, height=height)

view.setStyle({"cartoon": {"style": "oval","color": bb_color,"thickness": cartoon_radius}})

view.addSurface(py3Dmol.VDW, {"opacity": surf_transp, "color": bb_color},{"hetflag": False})

view.addStyle({"elem": "C", "hetflag": True},
                {"stick": {"color": lig_color, "radius": stick_radius}})

view.addStyle({"hetflag": True},
                    {"stick": {"radius": stick_radius}})

for hl_resi in hl_resi_list:
    view.addStyle({"chain": hl_chain, "resi": hl_resi, "elem": "C"},
                    {"stick": {"color": hl_color, "radius": stick_radius}})

    view.addStyle({"chain": hl_chain, "resi": hl_resi},
                        {"stick": {"radius": stick_radius}})

if label_resi:
    for hl_resi in hl_resi_list:
        view.addResLabels({"chain": hl_chain,"resi": hl_resi},
        {"backgroundColor": "lightgray","fontColor": "black","backgroundOpacity": 0.5})

### Step 4) Stmol

showmol(view, height=height, width=width)

#Info
st.sidebar.markdown("Welcome to my first app. I built this app using Streamlit to make it easier to obtain the Grantham amino acid mutation score. I hope you enjoy!")
st.sidebar.markdown("created by [Christos Efthymiou](https://www.linkedin.com/in/christos-efthymiou/)")
