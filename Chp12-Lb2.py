#Jackie_Merritt-Chp12-L2_7/13/2025
import os
import sys

def main():
    print('Unique Word Counter\n')
    file_name = input('Enter the name of the file you wish to process: ')
    verified_file = check(file_name)
    with open(verified_file) as file:
        contents = file.read()
    split_contents = contents.split()
    content_set = set(split_contents)
    print(f'There are {len(content_set)} unique words in {verified_file}.')



def check(file_name):
    valid = False
    while valid == False:
        file = os.path.isfile(file_name)
        if file == True:
            valid = True
        else:
            print(f'The file {file_name} could not be found')
            file_name = input('Enter the name of the file you wish to process or type exit to quit: ')
            if file_name.lower() == 'exit':
                sys.exit()
    return file_name
    
if __name__ == '__main__':
    main()
