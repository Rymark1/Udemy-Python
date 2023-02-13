import os
import fnmatch


def list_songs(root, ext=""):
    for path, dir, files in os.walk(root):
        # if ext != "" and files.lower().endswith(ext):
        for f in files:
            if ext != "":
                if f.lower().endswith(ext.lower()):
                    yield path + "\\" + f
                else:
                    pass
            else:
                yield path + "\\" + f


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f'*{extension}'):
            yield os.path.join(path, file)


file_list = list_songs("music", "mp3")
for f in file_list:
    print(f)

for f in find_music("music", "emp3"):
    print(f)

