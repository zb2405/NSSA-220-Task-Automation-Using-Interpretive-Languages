#!/usr/bin/python
filename_1 = input('filename for md5sum original: ')
filename_2 = input('filename for md5sum modified: ')
file_executable = []
file_md5sum_1 = []
file_md5sum_2 = []
with open(filename_1, 'r') as f:
    for line in f:
        if '[' in line:
            continue
        string = line.strip().split()
        file_executable.append(string[0])
        file_md5sum_1.append(string[1])
# print(len(file_executable))
# print(len(file_md5sum_1))

with open(filename_2, 'r') as f:
    for line in f:
        if '[' in line:
            continue
        file_md5sum_2.append(line.strip().split()[1])

for ind in range(len(file_md5sum_2)):
	if file_md5sum_1[ind] != file_md5sum_2[ind]:
		print(file_executable[ind]+": MD5 original = " + file_md5sum_1[ind] +" , MD5 new = " + file_md5sum_2[ind]+ "\n")

# print(len(file_md5sum_2))