# from google.colab import drive 
# drive.mount('/content/drive')

import io
import os

# dir_root_folder = '/content/drive/Other computers/MyLaptop/FlyDrive/python/White_DTC_compiler/'
dir_root_folder = os.getcwd()


def ensemble(inList):

    inList = list ( filter( lambda x : not x[1:].isascii() , inList))       # remove all English texts

    Ulist= list(set( inList ))

    mydic = dict(zip( Ulist , [inList.count(txt) for txt in Ulist] ))
    print( mydic )
    majority_keys_num = max(mydic.values()) 

    majority_keys = list( filter( lambda x: mydic[x] == majority_keys_num , mydic) )

    lens = list (map( lambda x: len(x) , majority_keys ))        # if there is several majority choose the longest one
    index_best = lens.index(max(lens))
    best_of_majority = majority_keys[index_best]

    return best_of_majority


wel = "\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> White DTC Compiler <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
hint = 'HINT: -Put **dtc_fa_dataset** and **dtc_en** folders next to this program .exe file \n \
      -**White_translated** and **White_NOTfound** \n\
       **White_NOTtranslated** and **White_ensemble** folders will be given as result  \n\
           -The searching results will be shown below...\n' 
warn = 'Warning: if you have these folders next to program the result files will be overwrited in these folders!\n\n'

print(wel,"\nHi! welcome to TNM White compiler by Sajjad Rezvani.K ... \n\n",hint,warn)
password = input("\nEnter your password:")

while True:
    if password == '308':
        break
    else: 
        print( 'The password is wrong! Fuck off!!! :)')



dir_en_folder = os.path.join( dir_root_folder , 'dtc_en')
dir_faset_folder =  os.path.join( dir_root_folder , 'dtc_fa_dataset')

result_path = os.path.join( dir_root_folder , 'White_translated' )
missing_path = os.path.join( dir_root_folder , 'White_NOTfound')
shit_path = os.path.join( dir_root_folder , 'White_NOTtranslated')
ensemble_path = os.path.join( dir_root_folder , 'White_ensemble') # directory to gather majority report of out texts of translated files

try:
    os.mkdir(dir_en_folder) 
    os.mkdir(dir_faset_folder) 
except:
    None

try:
    os.mkdir(result_path) 
    os.mkdir(missing_path) 
    os.mkdir(shit_path) 
    os.mkdir(ensemble_path)
except: None


try:
    list_en_files = os.listdir(dir_en_folder)
    list_en_files = list( map(lambda x: (x.split('.')[0].upper() + '.' + x.split('.')[1]) , list_en_files) )
    list_faset_ecufolders = os.listdir(dir_faset_folder)

except Exception as e:     # print any error that could happen durting the run time 
    print(e)
    input('\nShit Happend! :) See you soon!')



dic_dtc = {}
dic_fa_shit_found = {}
for enfiles_name in list_en_files:                           # loop over input english files 
    list_fafolders_names = []
    fafolder_shit_found = []
    fa_flag = 0
    for fafolder_name in list_faset_ecufolders:              # searching for a DTC code between farsi dataset folders 

        dir_ecufolders = os.path.join(dir_faset_folder , fafolder_name)
        list_faset_files = os.listdir(dir_ecufolders)
        # list_faset_files = list( map( lambda x: (x.split('.')[0].upper() + '.' + x.split('.')[1]) , list_faset_files) )

        if enfiles_name in list_faset_files:                 # check if specific DTC code is among every folders files 
            context_txt = ''
            enfiles_name_path = os.path.join(dir_ecufolders,enfiles_name)
            context = io.open( enfiles_name_path , mode="r", encoding="utf-16-le")
            context_txt = context.read()[1:]
            # print('>-----',context_txt,'------<')
            if context_txt.isascii()  :                 # totally english 
                fafolder_shit_found.append(fafolder_name) 
                # print('shit')
            else:     
                fa_flag = 1                                  # not totally english
                list_fafolders_names.append(fafolder_name)
                # print('good')

    print(enfiles_name,list_fafolders_names,'---> shit found: ',fafolder_shit_found,'\n')
    dic_dtc.update( { enfiles_name : list_fafolders_names } ) # collect in a dictionary

    if fa_flag==0 and not fafolder_shit_found == []:
        dic_fa_shit_found.update( { enfiles_name : fafolder_shit_found } )

#-----------------------------------------------------------------------------------------------------------------------------------

for i in list(dic_dtc.keys()):          # loop over all DTC codes 
    txt_list = []
    newStr = ''
    selfStr = '' 
    originalFoldersStr = 'origin folders: '

    for j in dic_dtc[i]:                # loop over every DTC code folders 
        fafile_path = dir_faset_folder + '/' + j + '/' + i 
        print('*input: ', fafile_path)
        fa = io.open( fafile_path , mode="r", encoding="utf-16-le")
        onefile_txt = fa.read()       
        originalFoldersStr += j + ' - '          # collect every string origin folder name to find impure english files in dataset later
        newStr += onefile_txt + '\n'    # collect whole strings related an specific DTC code 
        txt_list.append( onefile_txt )
    
    dir_self_file =os.path.join(dir_en_folder , i)
    self_txt = io.open( dir_self_file , mode="r", encoding="utf-16-le")
    # print(f'******* debuge:{self_txt} \n ')

    selfStr = 'origin txt: ' + self_txt.read()
    
    if newStr == '' and i in list(dic_fa_shit_found.keys()) :                   # DTC codes that are not found any in dataset 
        newfile_path = os.path.join(shit_path,i)
        newStr = ':'.join(selfStr.split(':')[1:])
    elif newStr == '' and not i in list(dic_fa_shit_found.keys()) :
        newfile_path = os.path.join(missing_path,i)
        newStr = ':'.join(selfStr.split(':')[1:])
    else: 
        newfile_path = os.path.join(result_path,i)      # get majority_report from function to save in new folder White_ensemble
        majority_report = str(ensemble(txt_list)).replace('\\ufeff','').replace('\\n','')
        print(f'***********debuge: ***{str(ensemble(txt_list))}*** \n' )
        newStr += '\n' + originalFoldersStr + '\n' + selfStr + '\n' + 'majority report: ' + majority_report

        majority_path = os.path.join(ensemble_path,i)
        majority_file = io.open( majority_path , mode= 'w' , encoding="utf-16-le") # Write in result file 
        majority_file.write(majority_report)

    new = io.open( newfile_path , mode= 'w' , encoding="utf-16-le") # Write in result file 
    new.write(newStr)

    print('>>>>>out: ',newfile_path , '\n>>>>>txt:\n', newStr, '\n----------------------------------------------------------------------------------------------------------\n')

print("***"*35)
a= len(list(dic_dtc.keys()))
b= list(dic_dtc.values()).count([])
c= len(list(dic_fa_shit_found.keys()))
print("total number of DTC files: " , a )
print("number of successful translate:" , a-b)
print("number of notfound DTC files in folder: " , b-c ) 
print("number of found but not translated DTC files in folder: " , c ,'\n') 

print( 'found but not translated DTC files:   ' ,dic_fa_shit_found)

path_log_shit_found = os.path.join(dir_root_folder, 'log_shit_found.txt')
log_shit_found = io.open( path_log_shit_found , mode= 'w' , encoding="utf-16-le") # Write in result file 
log_shit_found.write( '], \n'.join( str(dic_fa_shit_found).split('],') ) )

input ('\n >>> Good luck :)  \n')