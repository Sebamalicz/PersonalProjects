from os import walk 

def import_folder(path):
    surface_list = []

    for folder_name, sub_folder, img_files in walk(path):
        print(folder)

    return surface_list