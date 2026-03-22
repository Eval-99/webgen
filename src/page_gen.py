import os

from extract_markdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        doc_markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_doc = (
        template.replace("{{ Title }}", extract_title(doc_markdown))
        .replace("{{ Content }}", markdown_to_html_node(doc_markdown).to_html())
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    with open(f"{dest_path}/{from_path.split('/')[-1].split('.')[0]}.html", "w") as f:
        f.write(html_doc)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(
                os.path.join(dir_path_content, item),
                template_path,
                dest_dir_path,
                basepath,
            )
            continue
        else:
            generate_pages_recursive(
                os.path.join(dir_path_content, item),
                template_path,
                os.path.join(dest_dir_path, item),
                basepath,
            )
