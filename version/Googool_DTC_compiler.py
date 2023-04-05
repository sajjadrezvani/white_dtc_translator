# from google.colab import drive 
# drive.mount('/content/drive')
import io
import os

dir_root_folder = os.getcwd()

dir_en_folder = os.path.join( dir_root_folder , 'dtc_en')
dir_faset_folder =  os.path.join( dir_root_folder , 'dtc_fa_dataset')
# print('>>>>' , dir_en_folder)

result_path = os.path.join( dir_root_folder , 'Googool_translated' )
missing_path = os.path.join( dir_root_folder , 'Googool_NOTtranslated')

try:
    os.mkdir(result_path) 
    os.mkdir(missing_path) 
except:
    None


list_en_files = os.listdir(dir_en_folder)
list_en_files = list( map(lambda x: (x.split('.')[0].upper() + '.' + x.split('.')[1]) , list_en_files) )

list_faset_ecufolders = os.listdir(dir_faset_folder)

dic_dtc = {}
for enfiles_name in list_en_files:      # loop over input english files 
    list_fafolders_names = []
    for fafolder_name in list_faset_ecufolders: # searching for a DTC code between farsi dataset folders 

        dir_ecufolders = os.path.join(dir_faset_folder , fafolder_name)
        list_faset_files = os.listdir(dir_ecufolders)
        # list_faset_files = list( map( lambda x: (x.split('.')[0].upper() + '.' + x.split('.')[1]) , list_faset_files) )

        if enfiles_name in list_faset_files:        # check if specific DTC code is among every folders files 
            list_fafolders_names.append(fafolder_name)

    print(enfiles_name,list_fafolders_names,'\n')
    dic_dtc.update({ enfiles_name : list_fafolders_names }) # collect in a dictionary

# -------------------------------------------------------------------------------------------------------------------------------------

print("total number of Dtc files: " , len(list(dic_dtc.values())) )
print("number of missing Dtc files in folder: " , list(dic_dtc.values()).count([]) ) 

# -------------------------------------------------------------------------------------------------------------------------------------

for i in list(dic_dtc.keys()):  # loop over all DTC codes 
    newStr = ''
    originStr = 'origin folders: '

    for j in dic_dtc[i]:           # loop over every DTC code folders 
        fafile_path = dir_faset_folder + '/' + j + '/' + i 
        print('*input: ', fafile_path)
        fa = io.open( fafile_path , mode="r", encoding="utf-16-le")
        onefile_txt = fa.read()       
        originStr += j + ' - '          # collect every string origin folder name to find impure english files in dataset later
        newStr += onefile_txt + '\n'    # collect whole strings related an specific DTC code 
    
    if newStr == '' :                   # DTC codes that are not found any in dataset 
        newfile_path = os.path.join(missing_path,i)
        dir_self_file =os.path.join(dir_en_folder , i)

        self_txt = io.open( dir_self_file , mode="r", encoding="utf-16-le")
        newStr = self_txt.read()
    else: 
        newfile_path = os.path.join(result_path,i)
        newStr += '\n' + originStr

    new = io.open( newfile_path , mode= 'w' , encoding="utf-16-le") # Write in result file 
    new.write(newStr)

    print('>>>>>out: ',newfile_path , '\n>>>>>txt:\n', newStr, '\n-----------------------------------------------------------------------------------------------------\n')

