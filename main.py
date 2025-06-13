import os 

def encoder(): #ffmpeg command execution 
    file_local=input("Enter the file location: ")
    save_local=input("Were to Save the file: ")
    new_name=input("Enter a new name: ")
    if file_local and new_name and save_local != ' ':
        if save_local.endswith('/') == False:
            save_local+='/' # adds '/' if not found 
            os.system(f'ffmpeg -i "{file_local}" -vcodec copy -acodec pcm_s16le "{save_local}{new_name}"')
        else:
            os.system(f'ffmpeg -i "{file_local}" -vcodec copy -acodec pcm_s16le "{save_local}{new_name}"')
    else:
        print("Error (Fields are not filled)")


def main(): # menu  
    print('Welcome To Fix my file format app')
    startapp=input("Do you want to start this procces? (Y/n): ").strip() #strip to remove whitespace in input 
    if startapp =='y' or startapp == 'Y' or startapp == '': 
        encoder()
    
    elif startapp=='n' or startapp =='N':
        print("Exiting the app.")

main() 