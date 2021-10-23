#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:08:34 2020

@author: pma
"""

import pandas as pd
import sys



metadata_file_path = '~/cfm/platinum.tsv.gz'
fragged_list_path = '~/cfm/calculated_spectra.txt'
sep = '\t'
duplicated_field_header = 'structureCleaned_inchikey2D'
id_header = 'structureCleaned_inchikey2D'
smiles_header = 'structureCleaned_smiles2D'
for_frag_file_path = '~/cfm/cfm_input/sub_platinum_tofrag.tsv.gz'




df = pd.read_csv(metadata_file_path, sep=sep, error_bad_lines=False, low_memory=False)
df = pd.read_csv(metadata_file_path, compression='gzip', header=0, sep=sep, quotechar='"', error_bad_lines=False)


fragged_list = pd.read_csv(fragged_list_path,header = None, quotechar='"', error_bad_lines=False)


fragged_list[0]
type(fragged_list[0])


df.columns

df.info()

df = df.drop_duplicates(subset= duplicated_field_header )

df.info()


df = df[[id_header, smiles_header]]

# here we keep all entries which are not in the previously fragmented list 

df[~df[id_header].isin(fragged_list[0])]


df.to_csv(for_frag_file_path, sep=' ', index=False, compression='gzip', header=None)
