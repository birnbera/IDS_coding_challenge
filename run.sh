#!/usr/bin/env bash

# modify programs for execution
chmod a+x src/IDS_word_count.py

# pass text files from input folder as arguments to python script
ls wc_input/*.txt | xargs python ./src/IDS_word_count.py