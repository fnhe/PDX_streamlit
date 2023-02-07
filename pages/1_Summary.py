#2023-02-06 14:07:28 
# Add every font at the specified location
from matplotlib import font_manager
font_dir = ['/home/UTHSCSA/hef/Tools/miniconda3/fonts']
for font in font_manager.findSystemFonts(font_dir):
    font_manager.fontManager.addfont(font)
# Set font family globally
import matplotlib as mpl
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns

indir = './raw_data'
info = pd.read_table(indir + '/sample_info.txt')
st.title('Data summary')

info_sel = 'Cancer type'
info_sel = st.selectbox(
    'Clincal information you interested',
    ['Cancer type', 'Sex', 'Race', 'Ethnicity','Treatment']
)

if info_sel == 'Cancer type' :
    col = 'Disease Code level 1'
elif info_sel == 'Sex' :
    col = 'Gender'
elif info_sel == 'Race' :
    col = 'Race'
elif info_sel == 'Ethnicity' :
    col = 'Ethnicity'
elif info_sel == 'Treatment' :
    col = 'Therapy prior to PDX collection'

info2show = info.fillna('NA').groupby(col).count()[['PatientID']]

#define Seaborn color palette to use
colors = sns.color_palette('Set2')[0:len(info2show)]

#create pie chart
sns.set_context('notebook', font_scale = 1.0, rc = {'lines.linewidth':1}) #设置文本
fig = plt.figure(figsize=(8,6))
plt.pie(info2show['PatientID'], labels = info2show.index, colors = colors, autopct='%.0f%%', radius=1, labeldistance=1.3)
#st.pyplot(fig, figsize=(3, 3))
from io import BytesIO

buf = BytesIO()
fig.savefig(buf, format="png")
st.image(buf)
