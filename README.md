# white_dtc_translator
a program that translate new DTC files based on a several data sets programmed for TNM car's ECU programmer device.


## Summary
There was a problem that for every car which was going to add into in TNM programmer and diagnosis device, there was hundreds of files of dtc comments used for car diagnosis process. These files are some code like P0012 (based on global portocol for ecu dtc's) or a english comment but the diag device has to show comments in persian. On the other hand we had lots of file from cars which had already translated one by one by company engineer and added to device based on the portocol. 
Therefore we had this idea to use a python program to do this process faster and more percise.
This program takes a folder which contains old english dataset and a folder of persian files which you want to translate based on them. 
Then as results it creats four folders named **White_translated** and **White_NOTfound** and **White_NOTtranslated** and **White_ensemble** which contain several files:
* White_translated: files that found the exact code in the main dataset 
* White_NOTfound: files with codes that are not in dataset 
* White_NOTtranslated: files with codes that had been found in dataset but the they contain english contex wich is not useful.
* White_ensemble: the same as white_translated but it ensemble those files data


## Technology Stack
> List of front-end and back-end technologies and libraries used in the project:
* python 3

## Browser/Software Support
* There would be several version for 32bit and 64bit system

## Project Resources
> List of the names and roles of the different people that have been involved with the project (past and present):
* Sajjad Rezvani Khaledi (programmer)
* Mehdi Ezzarvar (Project Manager)


## Table Of Contents
* HINT: 
  * Put **dtc_fa_dataset** and **dtc_en** folders next to this program .exe file
  * **White_translated** and **White_NOTfound** and **White_NOTtranslated** and **White_ensemble** folders will be given as result 

* warn = 'Warning: if you have these folders next to program the result files will be overwrited in these folders!

