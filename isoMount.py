#!/usr/bin/ python

import subprocess
import keyboard
from tkinter import *  
from tkinter import filedialog
from tkinter.ttk import *

window = Tk()



def windowProperties():
    window.resizable(width=False, height=False)
windowProperties()

def upload():
    filename = filedialog.askopenfilename(initialdir = "/", title='Select Image')
    with open("uploadPath.txt", "w") as text_file:        
        text_file.write(str('%s' % filename.replace(" ", "\ ").replace("'", "\ '"))) #Get help with this replacing "'" with "\'"
        text_file.close()
    print('Selected Image: ', filename)

inputButton = Button(window, text='Image File', command=upload, )

def output():
    outputDirectory = textBox.get("1.0",END)
    
    with open("outputPath.txt", "w") as text_file:        
        text_file.write(str('%s' % outputDirectory.replace(" ", "\ ").replace("'", "\ ")))
        text_file.close()
    if outputDirectory == u'\n':
        subprocess.call(["clear"])
        print("No output directory selected.\n\n")
        subprocess.call('df -h', shell=True)
    else:
        print('Destination: ', outputDirectory)
    



outputButton = Button(window, text='Set Output Location', command=lambda: output())
textBoxLabel = Label(window, text='Output Destination: ')


#This is a button for output
# def output():
#     outputDirectory = filedialog.askdirectory(initialdir = "/media", title='Select Image Output Directory')
#     with open("outputPath.txt", "w") as text_file:        
#         text_file.write(str('%s' % outputDirectory))
#         text_file.close()
#     if outputDirectory == '':
#         print("No output directory selected.")
#     print('Destination: ', outputDirectory)
# outputButton = Button(window, text='Output Location', command=output)


def action():
    uploadList = []
    outputList = []

    with open("outputPath.txt", "r") as f:
        lines = f.readlines()

        # Loop through all lines, ignoring header.
        # Add last element to list (i.e. the process name)
        for l in lines:
            outputList.append(l)
            outputString = ''.join(outputList)

    with open("uploadPath.txt", "r") as f:
        lines = f.readlines()

        # Loop through all lines, ignoring header.
        # Add last element to list (i.e. the process name)
        for l in lines:
            uploadList.append(l)
            uploadString = ''.join(uploadList)
    
    print uploadString +' '+ outputString

    formatAsk = input('[+]Would you like to format your file system?\n1. Yes\n2. No\nYour choice: ')
    if formatAsk == 1:
        print('[+]Unmounting file system\n')
        subprocess.call('sudo umount ' + outputString, shell=TRUE)

        mkfs = input('[+]Which format would you like?\n1. FAT\n2. vFAT\n3. NTFS\n4. EXT4\nYour choice: ')
        if mkfs == 1:
            print('[+]FAT format selected.')
            subprocess.call('sudo mkfs.fat ' + outputString, shell=TRUE)
        if mkfs == 2:
            print('[+]vFAT format selected.')
            subprocess.call('sudo mkfs.vfat ' + outputString, shell=TRUE)
        if mkfs == 3:
            print('[+]NTFS format selected.')
            subprocess.call('sudo mkfs.ntfs ' + outputString, shell=TRUE)
        if mkfs == 4:
            print('[+]EXT format selected.')
            subprocess.call('sudo mkfs.ext4 ' + outputString, shell=TRUE)
        if mkfs == 5:
            print('[+]Beginning ISO mounting process...')
            subprocess.call('sudo dd status=progress if=' + uploadString + ' ' + 'of=' + outputString, shell=True)
            
            print('[+]Mounting file system\n')
            # subprocess.call('sudo mkdir /media/usb/', shell=TRUE)
            subprocess.call('sudo mount ' + outputString + ' ' + '/media/usb/', shell=True )
            # subprocess.call('sudo rm -rf /media/usb/', shell=TRUE)
            subprocess.call('xdg-open ' + outputString, shell=True)
            text1 = Label(window, text='[+]Operation Complete')
            text1.grid()

    if formatAsk == 2: 
        print('[+]Beginning ISO mounting process...\n')
        subprocess.call('sudo dd status=progress if=' + uploadString + ' ' + 'of=' + outputString, shell=True)
        # subprocess.call('xdg-open ' + outputString, shell=True)
        text1 = Label(window, text='[+]Operation Complete')
        text1.grid()

actionButton = Button(window, text='Start', command=action)



# Progress bar widget 
progress = Progressbar(window, orient = HORIZONTAL, 
            length = 100, mode = 'indeterminate') 
  
# Function responsible for the updation 
# of the progress bar value 
def progBar(): 
    import time 
    progress['value'] = 0
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 20
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 100
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 20
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 0
    window.update_idletasks() 
    time.sleep(0.5) 
    progress['value'] = 0


# infinite loop 

textBoxLabel.grid(row=1, column=0)
textBox=Text(window, height=1, width=10)
textBox.grid(row=1, column=1)
inputButton.grid(row=0, column=1)
outputButton.grid(row=1, column=2)
actionButton.grid(row=2, column=1)
# progress.grid()


# text2.grid(column=0, row=1)

window.title('ISO Mount')

window.mainloop()


#Create text area for verbose option

#Create loading bar