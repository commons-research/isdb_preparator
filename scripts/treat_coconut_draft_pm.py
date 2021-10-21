#%%
### This script fetch info from a metadattable and populates mgf headers accordingly


#|   Be careful !!! use python2 and not python3 to launch this script !!! |
# ---------------------------------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#               ||----w |
#               ||     ||




import csv
import sys
import glob

tsv_filename = '/Users/pma/is_fragmentation/scripts/COCONUT4MetFrag_adducted.tsv'



# This will contain the tsv data
data = {}
header = False  # Was header red?

# Read the tsv file and store data in data
with open(tsv_filename, 'r') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t', quotechar='"') #or dialect=csv.excel_tab 

    try:
        for row in tsv_reader:
            # Set the header if it wasn't yet
            if header is False:
                header = row
                continue  # Go to the next row
            if row != []:  # Take care of shitty windows format
                data[row[header.index('Identifier')]] = row
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(tsv_filename,
                                               tsv_reader.line_num,
                                               e))

done = 0
skipped = 0

# Iterate over all files
for pos, row in data.items():
    # This will contain the mgf data
    content = ''
    print(row[header.index('Identifier')])
    filename = row[header.index('Identifier')]
    if ".mgf" not in filename:
        filename = "%s.mgf" % filename
    # Create content
    # To access a row of a specific name:
    #   row[header.index('NAMEOFTHEROW')]
    # Careful, as the program will crash if the row doesn't
    # exist (left as an exercise ;) )

    content += "BEGIN IONS\n"
    content += "PEPMASS={}\n".format(row[header.index('protonated_emass')])
    content += "CHARGE=1+\n"
    # MSLEVEL=xxx
    #content += "SOURCE_INSTRUMENT={}-{}\n".format(
        #row[header.index('INSTRUMENT')],
       # row[header.index('IONSOURCE')])
    content += "FILENAME={}\n".format(row[header.index('Identifier')])
#    content += "InChIKey={}\n".format(row[header.index('InChIKey')])
    content += "MOLECULAR_FORMULA={}\n".format(row[header.index('MolecularFormula')])
    content += "SEQ=*..*\n"
    #content += "NOTES={}:{}:{}:{}:{}:{}\n".format(
        #row[header.index('PI')],
        #row[header.index('DATACOLLECTOR')],
        # "N/A",  # Change that
#         "N/A",  # Change that
#         row[header.index('ACQUISITION')],
#         "N/A"  # Change that
#     )
# 
    content += "IONMODE=POSITIVE\n"
    content += "EXACTMASS={}\n".format(row[header.index('MW')])
#     # Change that
    # ORGANISM=xxx
    content += "NAME={}\n".format(row[header.index('Identifier')])
    content += "SMILES={}\n".format(row[header.index('SMILES')])
    content += "INCHI={}\n".format(row[header.index('InChI')])
    #content += "Synonyms={}\n".format(row[header.index('Syn_list')])
    #content += "LIB={}\n".format(row[header.index('LIB')])    
#    content += "INCHIAUX={}\n".format(row[header.index('INCHI_KEY')])
    content += "LIBRARYQUALITY=In Silico Fragmented CFM-ID\n"



    # Change that
    # SPECTRUMID=xxx
    # ACTIVATION=xxx
    # INSTRUMENT=xxx
    # TITLE=xxx

#    content += "SCANS={}\n".format(row[header.index('EXTRACTSCAN')])
    content += "SCANS=1\n"

    # Try to open the file
    


    
    try:
        path = glob.glob('../coconut_data/bacasable/**/{}'.format(filename), recursive=True)
        if path != []:
            with open(path[0], 'r') as mzxml_file:
                for line in mzxml_file:
                    content += line.strip() + "\n"
                content += '\n'.join(list(mzxml_file))
                content += "END IONS\n"
                # Write the output file
                
                with open(filename.split('.')[0]+'.mgf', 'w') as mgf_file:
                    mgf_file.write(content)
                done += 1
        
        
    except IOError:
        print('File {} not found, skipped'.format(filename))
        skipped += 1
        continue
        


print('Treated {} files, skipped {}.'.format(done, skipped))


#%%

filename = 'CNP0000001.mgf'

open(glob.iglob('../coconut_data/bacasable/**/CNP00001.mgf', recursive=True)[0])

path = glob.glob('../coconut_data/bacasable/**/{}'.format(filename), recursive=True)

open('../coconut_data/bacasable/coconut_0000/CNP0000001.mgf', 'r')

open(path[0], 'r')
path = glob.glob('../coconut_data/bacasable/**/{}'.format(filename), recursive=True)

df = pd.read_csv("/Users/pma/is_fragmentation/scripts/COCONUT4MetFrag_adducted.tsv", sep="\t")
