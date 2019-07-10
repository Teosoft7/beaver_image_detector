import xml.etree.ElementTree as et
import glob
import os
from os import listdir
import shutil
from sklearn.model_selection import train_test_split


def make_species_xml_list(species, data_dir):
    """Takes in string of species name.
    Makes list of xml files with specific species."""
    species_list = []
    path = data_dir + 'annots'
    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()
        if root.find("./object/name") == None:
            continue
        if root.find("./object/name").text == species:
            species_list.append(xml_file)
    return species_list


def make_annot_list(data_dir):
    """Takes in data directory. Makes list of
    xml files."""
    annot_list = []
    path = data_dir + 'annots'
    for xml_file in glob.glob(path + '/*.xml'):
        annot_list.append(xml_file)
    return annot_list    
        
def copy_annot_and_img_to_folder(xml_list, data_dir, new_dir):
    """Takes in list of xml filepaths, data directory path,
    and new directory path path. New folder is
    named as string of xml_list. Assumes images are same name
    as xml file."""
    for xml_file in xml_list:
        shutil.copy(xml_file, new_dir)
        img_file = data_dir + 'images/' + xml_file[74:-4] + ".jpg"
        shutil.copy(img_file, new_dir)

        
def train_test_split_data(xml_list, data_dir, test_size, random_state):
    """Takes in list of xml files, data directory path, test size,
    and random_state. Populates train and test folder with images
    and xml files."""
    train, test = train_test_split(xml_list, test_size=test_size, random_state=random_state)
    new_dir = data_dir + 'train/'
    copy_annot_and_img_to_folder(train, data_dir, new_dir)
    new_dir = data_dir + 'test/'
    copy_annot_and_img_to_folder(test, data_dir, new_dir)     
    