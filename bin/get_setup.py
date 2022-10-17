import logging
import os
from glob import glob
from pathlib import Path
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from shutil import copy2 as copy, rmtree

from distutils.dir_util import copy_tree

log = logging.getLogger(__name__)

#change this to get setup docs
log.info(f"Getting setup info")
os.system(f"git submodule add --force -b main https://github.com/Southampton-RSG-Training/setup-documents.git submodules/setup-documents")
os.system("git submodule update --remote --merge")


# get list of setup.md chunks from _config.yml and apply order to them
# Open the website config, which contains a list of the lessons we want in the
# workshop, then create the directory "submodules" which will contain the files
# for each lesson
with open('_config.yml') as config:
    website_config = load(config, Loader=Loader)
    #select element of the dictionary called setup_docs
    set_up_docs = website_config['setup_docs']
    site_kind = website_config['kind']
    site_type = website_config['type']

# Get the images for the setup documents
copy_tree(f"submodules/setup-documents/fig", "fig/")

#for each element in the list
#paste into a string 'submodules/setup-documents/markdown'+setup docs element
with open("setup.md", "w") as file_out:
    file_out.write('# Setup for Lesson')
    for i in range(len(set_up_docs)):
        doc = 'submodules/setup-documents/markdown/'+ set_up_docs[i]
        with open(doc, "r") as file_in:
            file_out.write("\n")
            file_out.write(file_in.read())


if site_kind == 'lesson':
    dest = f"_includes/"
    Path(dest).mkdir(parents=True, exist_ok=True)
    for file in ["blurb.html"]:
        try:
            copy(f"{file}", f"{dest}/{file.split('/')[-1]}")
            log.info(f"Copied {file} to {dest}")
        except:
            log.error(f"Cannot find or move submodules/{lesson_name}/{file}, but carrying on anyway")

    if site_type == 'episode_r':
        try:
            for file in glob("_episodes_rmd/fig/*"):
                copy(f"{file}", f"fig/")
        except:
            log.error("Unable to move figures")

