"""
Generate the code reference pages and navigation.
"""

from pathlib import Path
import os
import mkdocs_gen_files
import sys

nav = mkdocs_gen_files.Nav()

root_code_dir = None
if (Path(__file__).parent.parent / "apps" / "annotator").exists():
    root_code_dir = (Path(__file__).parent.parent / "apps").resolve()
elif (Path(__file__).parent.parent.parent / "annotator").exists():
    root_code_dir = (Path(__file__).parent.parent).resolve()

if root_code_dir is None:
    raise FileNotFoundError("Could not find the root code directory")

sys.path.insert(0, str(root_code_dir.parent))

all_paths = []
for path in sorted(Path(root_code_dir).rglob("*.py")):
    if not "__" in path.__str__() and not "/_" in path.__str__():
        all_paths.append(path)


for path in all_paths:
    module_path = path.relative_to(root_code_dir).with_suffix("")
    doc_path = path.relative_to(root_code_dir).with_suffix(".md")
    full_doc_path = Path("codebase", doc_path)

    parts = tuple(module_path.parts)

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        module_name = parts[-1].replace('_', ' ').title()
        fd.write(f"# {module_name}\n\n------\n\n::: {root_code_dir}.{ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)


with mkdocs_gen_files.open("codebase/CODE_INDEX.md", "w") as nav_file:  #
    if os.path.exists(root_code_dir):
        nav_file.writelines(nav.build_literate_nav())  #
    else:
        nav_file.writelines(["Do not edit: here will be documentation generated by mkdocstrings"])