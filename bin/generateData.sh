#!/bin/bash

#This script will be used to generate the pseudorandom data

ARGPARSE_DESCRIPTION="This script is used to generate random stream of alphabets in a text file."     
source $(dirname $0)/argparse.bash || exit 1
argparse "$@" <<EOF || exit 1
parser.add_argument('filename',default=False, help='Specify the name of the data file')
parser.add_argument('filesize',default=False, help='Specify the size of the file in MB')
EOF

echo
echo Data Stream file "$FILENAME" of size "$FILESIZE"MB will be generated in the current directory.
echo
echo Starting generator script...
echo
python3 ../src/datagenerator/main.py "$FILENAME" "$FILESIZE"
echo
