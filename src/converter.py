import os
import pypandoc
import docx2txt
from pathlib import Path


def remove_link(rst_file):
    with open(rst_file, 'r+') as file:
        content = file.read()
        content = content.replace('<\l>', '')
        file.seek(0)
        file.write(content)
        file.truncate()


def convert_docx_to_rst(docx_file: str, rst_file: str) -> None:
    images_path = f"{os.path.dirname(rst_file)}/media"
    try:
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        pypandoc.convert_file(docx_file, "rst", outputfile=rst_file)
        _ = docx2txt.process(docx_file, images_path)
    except Exception as err:
        print("Error during conversion:")
        raise err


def create_folder_mapping(root_folder, recursive=True):
    folder_mapping = {}

    for dirpath, dirnames, filenames in os.walk(root_folder):

        relative_path = os.path.relpath(dirpath, root_folder)
        if relative_path == ".":
            relative_path = ""

        docx_files = [filename for filename in filenames if filename.endswith(".docx")]
        if docx_files:
            parent_folder_name = os.path.basename(relative_path)
            if parent_folder_name not in folder_mapping:
                folder_mapping[parent_folder_name] = []

            folder_mapping[parent_folder_name].extend([os.path.join(dirpath, filename) for filename in docx_files])

        if recursive:
            for subdir in dirnames:
                subdir_path = os.path.join(dirpath, subdir)
                create_folder_mapping(subdir_path, recursive)

    return folder_mapping


def find_file_recursive(folder_path, target_extension='.docx'):
    folder_tree = {}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            result = find_file_recursive(item_path, target_extension)
            if result:
                print(result)
                return result
        else:
            if os.path.isfile(item_path) and item_path.endswith(target_extension):
                folder_tree["folder_path"] = item_path
                return folder_tree


def folders_name(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        break
    return subfolders


def create_development_environments_rst(rst_file_path, folder_name, rst_mapping):
    with open('index.rst', 'a') as index_writer:
        index_writer.write("\n\n")
        index_writer.write(f"{folder_name}\n")
        index_writer.write("========================\n\n")
        index_writer.write(".. toctree::\n")
        index_writer.write("   :maxdepth: 2\n")
        index_writer.write("   :hidden:\n")
        index_writer.write(f"   :caption: {folder_name}\n\n")
        for filenames in rst_mapping[folder_name]:
            rel_path = os.path.relpath(filenames, rst_folder)
            index_writer.write(f"   {rel_path}\n")


if __name__ == "__main__":
    abc = Path(os.path.abspath(__file__)).parent.parent
    docx_folder = f"{str(abc)}/doc_files"
    rst_folder = f"{str(abc)}/docs"
    folder_to_convert_list = folders_name(docx_folder)

    for folder_to_convert in folder_to_convert_list:
        rst_mapping = {}
        folder_name = os.path.join(docx_folder, folder_to_convert)
        folder_maps = create_folder_mapping(folder_name)
        rst_mapping[folder_to_convert] = []
        for folders, files in folder_maps.items():
            folder_path = os.path.join(rst_folder, folder_to_convert, folders)
            os.makedirs(folder_path, exist_ok=True)
            for file in files:
                file_name = os.path.basename(file)
                path = os.path.splitext(file_name)[0] + '.rst'
                rst_file_path = os.path.join(folder_path, path)
                convert_docx_to_rst(file, rst_file_path)
