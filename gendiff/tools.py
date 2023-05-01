import os


def normalize_file_name(arg): 
    return arg.replace('/', os.sep).replace('\\', os.sep)