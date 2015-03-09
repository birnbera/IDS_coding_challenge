# IDS_coding_challenge

The code for word count and median count are written in Python 2.7.3 using only libraries included in the standard distribution. These are dependencies that should typically be available with any Python distribution.

Both my word count and streaming median count functions are called on the input text within the same python script. They output to wc_result.txt and med_result.txt, respectively.

The modules used are string, which is a library for manipulating ascii strings, and fileinput, which is reads file arguments from the command line and concatenates them into a single, line-buffered file-like object. I only use these libraries for convenience. For example, string.punctuation is a string of all the printable punctuation characters, which is useful with str.translate(), in order to remove punction in the the word count function. The fileinput module is easier than iterating over a list of sys.argv entries and includes performance enhancements that come from line-buffering.
