import os
import re
import sys

def user_input(msg):
    return str(raw_input(msg))

# get program args
directory = sys.argv[1]
find = sys.argv[2]
find_excape = re.escape(find)
replace = sys.argv[3]
replace_escape = re.escape(replace)

# search directory for files containing text
grep_command = os.popen('grep -rwn '+directory+' -e "'+find+'"')
grep_output = grep_command.read()
grep_lines = str(grep_output).splitlines()

# check if match found
if len(str(grep_output)) == 0:
    print("match not found")
    sys.exit()

print ""
print(grep_output)

files = []

print("found " + str(len(grep_lines)) + " matches")

# loop through lines to update text with replacement
for line in grep_lines:
    parts = str(line).split(":")
    filename = parts[0]
    line_no = int(parts[1])-1
    lines = open(filename).read().splitlines()

    msg = "["+filename + ":" + str(line_no) + ":" + lines[line_no]
    msg += "] replace? (yes/no): "

    replace_line_yes_no = user_input(msg).lower()

    if(replace_line_yes_no == "yes" or replace_line_yes_no == "y"):
        lines[line_no] = lines[line_no].replace(find, replace)
        newline = "["+filename + ":" + str(line_no) + ":" + lines[line_no]+"][UPDATED]"
        open(filename,'w').write('\n'.join(lines))
        print(newline)  

    if (filename in str(files)) == False:
        files.append(filename)



