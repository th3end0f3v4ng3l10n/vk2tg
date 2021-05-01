#!/bin/bash
echo "---CREATING DIRS FOR WORK...---"
mkdir audio packs
echo "---INSTALL REQUIREMENTS...---"
pip3 install -r requirements.txt
echo "---CHMOD +X MAIN.PY...---"
chmod +x main.py
echo "Completed"