#2023-02-06 14:07:28 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns

a,b,c,d,e,f,g,h,i = [plt.cm.winter, plt.cm.cool, plt.cm.spring, plt.cm.copper, plt.cm.bone, plt.cm.gist_heat, plt.cm.pink, plt.cm.summer, plt.cm.autumn]
cancer_ranking_all = [ 'Osteosarcoma', 'Clear Cell Sarcoma', 'Other Sarcoma',   'Wilms Tumor', 'Hepatoblastoma','Germ Cell Tumor',   'Neuroblastoma', 'Other Tumor']
color_ranking_palette = [ f(.6), f(.8), f(.3), h(.6), b(.6), a(.6), h(.2), e(.6)]
color_ranking_dict = {'Osteosarcoma':  f(.6),  'Clear Cell Sarcoma':f(.8), 'Other Sarcoma':f(.3),  'Wilms Tumor': h(.6), 'Hepatoblastoma':b(.6),
                     'Germ Cell Tumor': a(.6),   'Neuroblastoma':h(.2), 'Other Tumor': e(.6)}
def plot_box_with_ax_datatype1(dt, X, Y, ax):
    cancer_ranking1 = dt.groupby(X).median().sort_values(Y, ascending=False).index
    color_ranking1 = [color_ranking_palette[cancer_ranking_all.index(i)]  for i in cancer_ranking1 ]


    p = sns.boxplot(data = dt, x = X, y = Y,  order = cancer_ranking1,  palette=color_ranking1, ax = ax,
            fliersize=0,
                boxprops={'edgecolor': 'black', 'alpha':1,'linewidth':0, },  
                medianprops={'color':'black', 'alpha':1, 'linewidth':1.5},
                whiskerprops={'linewidth':1, 'color':'black','alpha' : 1},
           )
    plt.setp(p.collections, alpha=.7, linewidth=0)

    p = sns.stripplot(data = dt[dt['Datatype'] == 'PT'], x = X, y = Y,  ax =ax, jitter=0.1,
              color='steelblue', marker = 'o', size = 9, alpha = 0.9,  linewidth=0.5, edgecolor = '.2',
             order =cancer_ranking1)
    p = sns.stripplot(data = dt[dt['Datatype'] == 'PDX'],  x = X, y = Y,  ax = ax,jitter=0.1,
              color='orange', marker = '^', size = 9, alpha = 0.9, linewidth=0.5, edgecolor = '.2',
             order =cancer_ranking1)
    
    p.set_xticklabels(cancer_ranking1,  ha='right', rotation_mode='anchor', rotation = 45)
    p.set_xlabel('')
    sns.despine()
    p.legend(bbox_to_anchor = (1,1), frameon=False)
    
def plot_box_with_ax_datatype2(dt, X, Y, ax):
    cancer_ranking1 = dt.groupby(X).median().sort_values(Y, ascending=False).index
    color_ranking1 = [color_ranking_palette[cancer_ranking_all.index(i)]  for i in cancer_ranking1 ]


    p = sns.boxplot(data = dt, x = X, y = Y,  order = cancer_ranking1,  palette=color_ranking1, ax = ax,
            fliersize=0,
                boxprops={'edgecolor': 'black', 'alpha':1,'linewidth':0, },  
                medianprops={'color':'black', 'alpha':1, 'linewidth':1.5},
                whiskerprops={'linewidth':1, 'color':'black','alpha' : 1},
           )
    plt.setp(p.collections, alpha=.7, linewidth=0)

    p = sns.stripplot(data = dt[dt['Datatype'] == 'PDX'],  x = X, y = Y,  ax = ax,jitter=0.1,
              color='orange', marker = '^', size = 9, alpha = 0.9, linewidth=0.5, edgecolor = '.2',
             order =cancer_ranking1)
    
    p.set_xticklabels(cancer_ranking1,  ha='right', rotation_mode='anchor', rotation = 45)
    p.set_xlabel('')
    sns.despine()
    p.legend(bbox_to_anchor = (1,1), frameon=False)

indir = './raw_data'
exp = pd.read_table(indir + '/exp.tpm.txt', index_col = 0)
exp = exp.drop('1853_PDX', axis = 1) 
exp = exp.drop('1947_PDX', axis = 1) 
exp = exp.round(2)

exp.columns = exp.columns.str.replace('875194','1939-Dup',regex = True) 

info = pd.read_table(indir + '/sample_info.txt')
info_dict = dict(info[['PatientID', 'Disease Code level 1']].values)

gene_ranking = sorted(exp.index)
gene_sel = 'PDGFRA'
gene_sel = st.selectbox(
    'Gene you interested',
    gene_ranking
)

info2plot = exp.loc[[gene_sel]].T
info2plot['PatientID'] = info2plot.index.str.split('_').str[0]
info2plot['Datatype'] = info2plot.index.str.split('_').str[1]
info2plot['Cancer'] = info2plot.PatientID.map(info_dict)

sns.set_context('notebook',font_scale = 1.6, rc = {'lines.linewidth':1}) #设置文本
fig = plt.figure(figsize=(15,5))

gs = gridspec.GridSpec(1, 2, hspace=2 , width_ratios=[1,1]) 
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])

X = 'Cancer'
Y = gene_sel
g1 = plot_box_with_ax_datatype1(info2plot, X, Y, ax1)
ax1.set_title('PT and PDX samples')
g2 = plot_box_with_ax_datatype2(info2plot[info2plot['Datatype'] == 'PDX'], X, Y, ax2)
ax2.set_title('PDX samples')

ylim = st.slider(
    'Select a TPM range of y-axis',
    0.0, 100.0, (0.0, round(float(ax1.get_ylim()[1]), 1)) )
ax1.set_ylim(ylim)
ax2.set_ylim(ylim)

st.pyplot(fig)
# Download
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
csv = convert_df(info2plot)
st.download_button("Download", csv, "exp.csv", "text/csv", key='download-csv')