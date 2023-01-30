# Run this in the Slides directory to rebuild for local use
# TODO: Update the Workshop repo to handle this. 
# Will involve installing Pandoc into the vagrant box.

pandoc -t revealjs -s -o index.html index.md -V theme=black --slide-level=3