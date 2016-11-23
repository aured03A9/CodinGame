# Number of elements which make up the association table.
n = int(input())

# Number Q of file names to be analyzed.
q = int(input())

# Mapping MIME type to a file extension, ext: file extension, mt: MIME type.
mmime = {ext.lower(): mt for ext, mt in [input().split() for i in range(n)]}

for i in range(q):
    # One file name per line.
    fname = input().rsplit('.', 1)
    fext = fname[-1].lower()

    # For each of the Q filenames, display on a line the corresponding MIME
    # type. If there is no corresponding type, then display UNKNOWN.
    print(mmime[fext] if len(fname) > 1 and mmime.get(fext) else 'UNKNOWN')
