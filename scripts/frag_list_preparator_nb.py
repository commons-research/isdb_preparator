#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:08:34 2020

@author: pma
"""

import pandas as pd
import sys



metadata_file_path = '/Users/pma/01_large_files/lotus/wetransfer_lotus_2021-10-15_0844/platinum.tsv.gz'
sep = '\t'
duplicated_field_header = 'structureCleaned_inchikey2D'
id_header = 'structureCleaned_inchikey2D'
smiles_header = 'structureCleaned_smiles2D'
for_frag_file_path = '/Users/pma/01_large_files/lotus/wetransfer_lotus_2021-10-15_0844/platinum_tofrag.tsv.gz'




df = pd.read_csv(metadata_file_path, sep=sep, error_bad_lines=False, low_memory=False)
df = pd.read_csv(metadata_file_path, compression='gzip', header=0, sep=sep, quotechar='"', error_bad_lines=False)

df.columns

df.info()

df = df.drop_duplicates(subset= duplicated_field_header )

df.info()


df = df[[id_header, smiles_header]]


df.to_csv(for_frag_file_path, sep=' ', index=False, compression='gzip', header=None)
