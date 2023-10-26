import os
import shutil

folders_to_ignore = ['_images', '_sources', '_static']
static_source_folder = '/Users/amq/Documents/innophase_doc/docs/_static'


def copy_static_files(root_folder):
    for root, folder, _ in os.walk(root_folder):
        for folder_to_ignore in folders_to_ignore:
            if folder_to_ignore in folder:
                folder.remove(folder_to_ignore)
        static_folder = os.path.join(root, "_static")
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
        for item in os.listdir(static_source_folder):
            item_path = os.path.join(static_source_folder, item)
            if os.path.isfile(item_path):
                shutil.copy(item_path, os.path.join(static_folder, item))


copy_static_files("/Users/amq/Documents/innophase_doc/docs/_build/html")
