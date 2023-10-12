from pathlib import Path
import pypandoc
import docx2txt
import os


def remove_link(rst_file):
    with open(rst_file, 'r+') as file:
        content = file.read()
        content = content.replace('<\l>', '')
        file.seek(0)
        file.write(content)
        file.truncate()


def convert_docx_to_rst(docx_file: str, rst_file: str) -> None:
    """
    Convert a DOCX file to RST format.

    :param docx_file: The path of the input DOCX file.
    :param rst_file: The path of the output RST file.
    :return: None
    """
    path = f"{str(abc)}/docs/media"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        pypandoc.convert_file(docx_file, "rst", outputfile=rst_file)
        _ = docx2txt.process(docx_file, path)
    except Exception as err:
        print("Error during conversion:")
        raise err


if __name__ == "__main__":
    abc = Path(os.path.abspath(__file__)).parent.parent
    docx_folder = f"{str(abc)}/doc_files"
    rst_folder = f"{str(abc)}/docs"
    for file in os.listdir(docx_folder):
        if file.endswith('.docx'):
            docx_file = os.path.join(docx_folder, file)
            rst_file = os.path.join(rst_folder, os.path.splitext(file)[0] + ".rst")
            convert_docx_to_rst(docx_file, rst_file)
            remove_link(rst_file)
