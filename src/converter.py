import os
import pypandoc
import docx2txt
from pathlib import Path
from shutil import copyfile


def remove_link(rst_file):
    with open(rst_file, 'r+') as file:
        content = file.read()
        content = content.replace('<\l>', '')
        file.seek(0)
        file.write(content)
        file.truncate()


def convert_docx_to_rst(docx_file: str, rst_file: str) -> None:
    try:
        pypandoc.convert_file(docx_file, "rst", outputfile=rst_file)
        images_folder = os.path.join(os.path.dirname(rst_file), "media")
        os.makedirs(images_folder, exist_ok=True)
        _ = docx2txt.process(docx_file, images_folder)
    except Exception as err:
        print(f"Error during conversion of {docx_file}: {err}")
        raise err


if __name__ == "__main__":
    abc = Path(__file__).parent.parent
    docx_folder = abc / "doc_files"
    rst_folder = abc / "docs"

    for root, dirs, files in os.walk(docx_folder):
        rel_path = Path(root).relative_to(docx_folder)
        new_folder = rst_folder / rel_path
        new_folder.mkdir(parents=True, exist_ok=True)

        for file in files:
            if file.endswith('.docx'):
                docx_file = os.path.join(root, file)
                rst_file = new_folder / (os.path.splitext(file)[0] + ".rst")
                convert_docx_to_rst(docx_file, rst_file)

                media_folder = new_folder / "media"  # Set media folder path
                if os.path.exists(media_folder):
                    for media_file in os.listdir(media_folder):
                        src_media_file = os.path.join(media_folder, media_file)
                        dst_media_folder = os.path.join(new_folder, "media")
                        os.makedirs(dst_media_folder, exist_ok=True)
                        dst_media_file = os.path.join(dst_media_folder, media_file)
                        if src_media_file != dst_media_file:  # Check if source and destination are different
                            copyfile(src_media_file, dst_media_file)
                            remove_link(rst_file)
