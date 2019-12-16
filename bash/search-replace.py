import yaml
import os
import re
import sys

import logging
logging.basicConfig(filename='../app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)



# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def log(msg):
    print(msg)
    logging.info(msg)

def print_header():
    log('*****************************************************************')

def user_input(msg):
    return str(raw_input(msg))

def user_reponded_yes(user_resp):
    if(user_resp == "yes" or user_resp == "y"):
        return True
    else:
        return False

def find_word(directory, search):
    # search directory for files containing text
    grep_command = os.popen('grep -rwn '+directory+' -e "'+search+'"')
    grep_output = grep_command.read()
    grep_lines = str(grep_output).splitlines()

    # check if match found
    if len(str(grep_output)) == 0:
        log("match not found")

    files = []

    # loop through lines to update text with replacement
    for line in grep_lines:
        parts = str(line).split(":")
        filename = parts[0]
        line_no = int(parts[1])
        files.append({ "filename": filename, "line_no": line_no })
    
    return files

def find_and_replace(base_dir, find, replace):
    # search for word
    search_results = find_word(base_dir, find)
    total = len(search_results)
    log("found " + str(total) + " matches to replace with '"+replace+"'")
    # loop through results
    counter = 1
    for file in search_results:
        #log(file)
        filename = file['filename']
        line_no = file['line_no']
        line_index = line_no - 1

        # open file
        lines = open(filename).read().splitlines()

        # init user message
        msg = "("+str(counter)+" of "+str(total)+")["+filename + ":" + str(line_no) + ":" + lines[line_index]
        msg += "][ORIGINAL]"
        log(msg)
        # replace line
        lines[line_index] = lines[line_index].replace(find, replace, 1)
        newline = "("+str(counter)+" of "+str(total)+")["+filename + ":" + str(line_no) + ":" + lines[line_index]+"][NEW]"
        log(newline)
        # get user input

        replace_line_yes_no = user_input("REPLACE--> (y/no): ").lower()
        
        if(user_reponded_yes(replace_line_yes_no)):
            
            updated = "("+str(counter)+" of "+str(total)+")["+filename + ":" + str(line_no) + ":" + lines[line_index]+"][UPDATED]"
            # update line in file
            open(filename,'w').write('\n'.join(lines))
            log(updated)
            print_header()

        counter+=1


def get_user_input(default_var, default_prefix):
    base_dir = './'
    base_dir = user_input("directory (default='"+base_dir+"'): ") or base_dir
    log("dir="+base_dir)
    
    find = ansible_var_enclose(default_var)
    find = user_input("search for (default="+find+"): ") or find
    log("find="+find)
    
    replace = ansible_var_enclose(str(default_prefix + default_var).lower())
    replace = user_input("replace with (default=" + replace + "): ") or replace
    log("replace="+replace)

    return {
        "base_dir" : base_dir,
        "find": find,
        "replace": replace
    }


def ansible_var_enclose(var_name):
    return "{{ " + var_name + " }}"

def replace_project_vars(yaml_file, project_var_prefix):
    # Read YAML file
    with open(yaml_file, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    prefix = project_var_prefix
   
    log('loaded ' + str(len(data_loaded)) + " variables")
    for var in data_loaded:
        # skip vars starting with prefix
        if(str(var).startswith(prefix)):
            log("skipping " + var)
            continue
        
        newvar = str(prefix + var).lower()
        
        print_header()
        log("\nupdate '" + var + "' with '" + newvar + "'?\n")
        yes_no = user_input("SEARCH--> (y/no): ")

        if(user_reponded_yes(yes_no)):
            
            log("user responded 'yes'")
            
            search_info = get_user_input(var, prefix)
            
            base_dir = search_info['base_dir']
            find = search_info['find']
            replace = search_info['replace']

            print_header()
            log("searching for '"+find+"'...")
            find_and_replace(base_dir, find, replace)

def search_replace():
    prefix = user_input("project prefix: ") or "_"
    vars_file = "./vars/main.yml"
    vars_file = user_input("vars file (default='"+vars_file+"'): ") or vars_file

    log(str([prefix, vars_file]))
    replace_project_vars(vars_file, prefix)


search_replace()



