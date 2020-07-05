import os

# """
# Recursively searches 'directory' for .txt files
# """
# that contain string s.
def searchDir(directory, s):
    filelist = []
    files = os.listdir(directory)
    for file in files:
        fullname = directory + '/' + file
    # try:
        if os.path.isdir(fullname):
            searchDir(fullname)
        else:
            if fullname[-4:] == '.txt':
                f = open(fullname, 'r')
                for lines in f:
                    if s in lines:
                        filelist.append(fullname)
                        break
searchDir('/home/l0wk3yofficial/Documents/self-made-projects/python/isoMountLinux', 'test.txt')
    # except:
    #     print('Not Found')                        

# def searchDir(directory, s):
#     filelist = []
#     files = os.listdir(directory)
#     for file in files:
#         fullname = directory + '/' + file
#     try:
#         if os.path.isdir(fullname):
#             searchDir(fullname)
#     except:
#         pass
#     else:
#         if fullname[-4:] == '.txt':
#             f = open(fullname, 'r')
#             for lines in f:
#                 if s in lines:
#                     filelist.append(fullname)
#                     break