import glob

#prints content of directory
def dir_info(glob_path,print_out=False,recursive_bool = False):
    if print_out:        
        for file in glob.glob(glob_path,recursive=recursive_bool):
            print(file)
    else:
        array= []
        for file in glob.glob(glob_path, recursive=recursive_bool):
            array.append(file)
        return array

if __name__ == "__main__":
    

    dir_info("code/**",True)