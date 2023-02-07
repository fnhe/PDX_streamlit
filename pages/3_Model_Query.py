

#2023-02-06 14:07:28 
import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns


indir = './raw_data'
exp = pd.read_table(indir + '/exp.tpm.txt', index_col = 0)
exp = exp.filter(regex = 'PDX')
exp = exp.drop('1853_PDX', axis = 1) 
exp.columns = exp.columns.str.replace('875194','1939-Dup',regex = True)

mut = pd.read_table(indir + '/Final_mut.maf')
mut['PatientID'] = mut['Tumor_Sample_Barcode'].str.split('_').str[0]
mut['m'] = mut['Tumor_Sample_Barcode'].str.split('_').str[1] 
mut = mut[mut['m'] == 'PDX'].fillna('NA')

info = pd.read_table(indir + '/sample_info.txt')

st.title('Download curated table:')



def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def check_wes_sample(data, col):
    p = []
    for i,x in enumerate(data[col]):
        if ((x=='WT') & (data.index[i] in ['1853','1796','707','512','560-SM'] )):
            p.append(np.nan)
        else :
            p.append(x)
    return p

cancer_ranking = sorted(info['Disease Code level 1'].unique() )
gene_ranking = sorted(exp.index)
ct_sel = st.multiselect(
    'Cancer types you interested',
    cancer_ranking
)
gene_sel = st.selectbox(
    'Gene you interested',
    gene_ranking
)

clinical_col2show = ['PatientID',  'Disease Code level 1', 'Disease Code level 2', 'Gender', 'Age(year)', 'Race', 'Ethnicity','Therapy prior to PDX collection', 
           'Tumor Collected (Primary or Met)', 'Primary Tumor Site', 'Site of Tumor Collection']
mut_col2show = ['Variant_Classification', 'HGVSp_Short']

if len(ct_sel) == 0:
    ct_sel = ['Hepatoblastoma']
else:
    info2show = pd.DataFrame()
    for ct in ct_sel:
        a = info[info['Disease Code level 1'] == ct]
        info2show = pd.concat([info2show, a ], axis = 0, ignore_index=True)
    info2show = info2show[clinical_col2show].set_index('PatientID').fillna(np.nan)
    if len(gene_sel) == 0:
        st.dataframe(info2show)
    else:
        try:
            b = mut[(mut['Hugo_Symbol'] == gene_sel)].set_index('Tumor group2').T[ct_sel].T.reset_index().set_index('PatientID')[mut_col2show]
        except KeyError:
            b = pd.DataFrame(index = info2show.index)
            b['HGVSp_Short'] = ['WT'] * len(info2show)
            b['Variant_Classification'] = ['WT'] * len(info2show)
        else:
            b = mut[(mut['Hugo_Symbol'] == gene_sel)].set_index('Tumor group2').T[ct_sel].T.reset_index().set_index('PatientID')[mut_col2show]
            b = b.reset_index().groupby(['PatientID']).first()            
        b.index = b.index.astype(str)
        info2show.index = info2show.index.astype(str)
        info2show = pd.concat([info2show,b], axis = 1)
        info2show[mut_col2show] = info2show[mut_col2show].fillna('WT')
        #change WT 2 NA
        info2show['HGVSp_Short'] = check_wes_sample(info2show, 'HGVSp_Short')
        info2show['Variant_Classification'] = check_wes_sample(info2show, 'Variant_Classification')

        c = exp[[ i + '_PDX' for i in info2show.index if i + '_PDX' in list(exp.columns)]].loc[[gene_sel]].T
        c.index = c.index.str.split('_').str[0]
        c.index = c.index.astype(str)
        c = c.round(2)


        info2show = pd.concat([info2show,c], axis = 1)
        info2show = info2show.fillna(np.nan)
        #info2show['Age(year)'] =[str(round(i,1)) for i in info2show['Age(year)']]
        info2show = info2show.reset_index()
        info2show.columns = ['PatientID'] + list(info2show.columns[1:])
        st.dataframe( info2show.style.format({'Age(year)': '{:.1f}', gene_sel: '{:.1f}'}))
        # Download
        csv = convert_df(info2show.fillna('NA'))
        st.download_button("Download", csv, "file.csv", "text/csv", key='download-csv')