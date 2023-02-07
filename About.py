
#2023-02-06 14:07:28 
import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns

st.set_page_config(page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded")
st.title('Pediatric Solid Tumor PDX Portal')

st.caption('Patient-Derived Xenografts (PDX) are an important tool for developing new therapies and understanding cancer biology in pediatric oncology. We have developed 68 PDXs from rare solid childhood cancers in a joint effort between Greehey Children’s Cancer Research Institute, UT Health San Antonio and UT Southwestern. These models have been profiled with one or more sequencing methods. ')

st.caption('We have created :blue[pstPDX] portal to share this resource with the community. On the portal users can query and request PDXs. The gene expression page also allows users to compare the expression of a gene across cancer types. ')

st.caption('The raw sequencing data are available at EGA (EGAS00001006710). The processed data, including deidentified clinical data, mutations, copy number, and gene expression can be found on synapse (syn35811916). ')

st.caption('Any questions about the portal should be directed to :blue[zhenglab@uthscsa.edu]. Request for PDX tissues should be directed to :blue[pdx@uthscsa.edu]. We will provide feedback in 3-5 business days upon receipt of the request. ')