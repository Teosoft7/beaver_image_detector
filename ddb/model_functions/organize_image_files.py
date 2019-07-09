import os
import glob
from os import listdir
import shutil
from random import sample
from sklearn.model_selection import train_test_split

def copy_file_to_directory(file_dir, file, new_dir):
    """Takes in file directory path, file name, and new
    directory to copy file to. Makes copy of file in new
    directory."""
    filepath = os.path.join(file_dir, file)
    shutil.copy(filepath, new_dir)
    

def make_data_subset(img_dir, subset_size, subset_dir,
                     annot_dir):
    """Takes in paths for xml annotation directory, jpg image
    directory, and subset size. Populates subset directory
    with random subset."""
    images = listdir(img_dir)
    img_subset = sample(images, subset_size)
    for img in img_subset:
        copy_file_to_directory(img_dir, img, subset_dir)
    annot_subset = [x[:-4] + '.xml' for x in img_subset]
    for annot in annot_subset:
        copy_file_to_directory(annot_dir, annot, subset_dir)

        
def copy_image_and_annot_files_to_dir(file_dir, file, new_dir):
    """Take file name, file directory, and new directory. Make
    image and xml annotation files from file name. Populate
    new directory with image and xml annotation files."""
    img_file = file + ".jpg"
    annot_file = file + ".xml"
    copy_file_to_directory(file_dir, img_file, new_dir)
    copy_file_to_directory(file_dir, annot_file, new_dir)
    
        

def train_test_split_files(data_dir, train_dir, test_dir,
                          test_size):
    """Takes in directory of xml annotation and image 
    files, and the size of the train set. Populates train
    and test directories with random split."""
    file_roots = [f[:-4] for f in listdir(data_dir) if f.endswith(".jpg")]
    train, test = train_test_split(file_roots, test_size=0.2)
    for file in train:
        copy_image_and_annot_files_to_dir(data_dir, file, train_dir)
    for file in test:
        copy_image_and_annot_files_to_dir(data_dir, file, test_dir)
        
        
    