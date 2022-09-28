import os

def get_fileList(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            # newDir = dir + '/' + s
            get_fileList(newDir, Filelist)

    return Filelist

def write():
    with open('may_jsons.txt', 'w') as f:
        file_list = get_fileList(r'./', [])
        # print('BAKA')
        json_list = filter(lambda x: x.endswith('.json'), file_list)
        for i in json_list:
            print(i)
            f.write(i + '\n')

def read():
    with open('json_files.txt', 'r') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    
    # write()
    read()
        