#!/bin/bash

#This is what will be used to run the final script.


ARGPARSE_DESCRIPTION="This script is used to spawn 10 processes that will search the specified data file for the string \"FiCo\"."     
source $(dirname $0)/argparse.bash || exit 1
argparse "$@" <<EOF || exit 1
parser.add_argument('filename',default=False, help='Specify the name of the data file')
parser.add_argument('-t','--timeout',default=60, type=int, help='Specifies how long each process should run in seconds. If no argument is specified, it defaults to 60 seconds.')
EOF

echo
echo 10 processes will be spawned to search "$FILENAME" for the string \"FiCo\".
echo 
echo Each process will run for "$TIMEOUT" seconds.
echo Starting processor script...
echo
python3 ../processor/main.py "$FILENAME"  -t "$TIMEOUT"
echo
