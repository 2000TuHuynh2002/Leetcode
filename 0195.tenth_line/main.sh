# Read from the file file.txt and output the tenth line to stdout.
NUM=10
sed "${NUM}q;d" file.txt
