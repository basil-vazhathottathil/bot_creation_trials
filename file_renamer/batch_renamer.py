import os

search_string= 'document' #the value to be checked if present in the  file name
replace_string= 'file' #the new name that will replace the old name
type_extension= '.py' #used to check the extension type of the file whose name is going to be replaced 

directory_content=os.listdir('.')  #retrieves a list of all the content in the directory ,all files and directories and then store them in directory_content
docs=[doc for doc in directory_content if os.path.isfile(doc)] #list comprehension?? idk .this is used to get just the files from directory_content into docs
renamed_counter=0

print(f'{len(docs)} of {len(directory_content)} elements are files')

#the main mojo --> renaming 
for doc in docs:
    doc_name , file_type =os.path.splitext(doc) #splits the file name into the 2 lists
    
    if file_type==type_extension:
        if search_string in doc_name:
            new_name= doc_name.replace(search_string,replace_string) + file_type       #uk what it does
            os.rename(doc,new_name)
            renamed_counter+=1

            print(f'renamed {doc} to {new_name}')


print(f'{renamed_counter} of {len(docs)} has been renamed')
