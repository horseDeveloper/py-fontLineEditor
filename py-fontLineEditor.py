# Copyright
    # Line finder and editor for big .ttx files.
    # Copyright (C) 2025 Nicolò Arrigo

# # FILE INFO # 
# ## Script summary:
    # 1) This script can search for 'namerecord nameID' and/or 'target index'. 
    # 2) After the first match, line by line, you can (keep/delete/edit) the line.
    # Why edit here? Fonts can be very big and Notepad does not handle scrolling/editing very well.
    # Why edit `namerecord`? So that your custom font has the appropriate `Copyright/Author/...`
    # Why remove lines after a certain `index`? So you can freeze just the alternative features (glyphs) you want and remove the other substitutions of the (lookup index) set.
# ## WorkFlows using this code
    # WF01: .ttf => .ttx ;; py-fontLineEditor ;; .ttx ⇒ .ttf ;; (pyftfeatfreeze)
# ## Status check
    # ✅ Script working on Python 3.11.2 as of 2025-02-05. 
    # 🛑EDIT_HERE🛑 occurrences: 0

import os

# tt-my-string
txt = "╙─── (N) Save & Upload a new file, (E) Save & Exit script: "
texx = "(E) Exit now: "
tex8 = "(8) Search for 'namerecord nameID', (9) Search for 'target index'"
byebye = ""

# Define function: get the source_file_path from user
def fff_upload_file():
    while True:
        source_file_path = input("╙─── Enter the path to the source file: ")
        if os.path.isfile(source_file_path):
            return source_file_path
        else:
            print("♠ The file does not exist. Be sure to enter a valid file path.")

# Define function: save changes to file
def fff_save_changes(source_file_path, source_file_lines):
    with open(source_file_path, 'w') as f:
        f.writelines(source_file_lines)
        print("♥ Changes saved to file!")

# Define function: get the search query from the user
def fff_get_search_query():
    while True:
        try:
            search_option = input(f"╟─── {tex8} \n╙─── (B) Go back and choose another file, {texx}")
            search_option = search_option.upper()  # Convert input to uppercase
            if search_option in ['8', '9']:
                return search_option
            elif search_option == 'B':
                print("♥ Going back...")
                source_file_path = fff_upload_file()
                return fff_get_search_query()
            elif search_option == 'E':
                print("♥ Exiting script...")
                exit()
            else:
                print("♠ Invalid option. Please choose one of the available choices.")
        except ValueError:
            print("♠ Invalid value entered. Please choose one of the available choices.")

def fff_search_file(source_file_path, search_option):
    if search_option == '8':
        var_search = "<namerecord nameID=\""        # We cannot escape characters inside `f` so I do it here by defining a variable
    elif search_option == '9':
        var_search = "<Lookup index=\""             # We cannot escape characters inside `f` so I do it here by defining a variable
    else:
        return
    target_prompt = f"╙─── Enter the target: {var_search}"

    next_action = ''        # Initialize next_action variable
    target_line = None      # Set target_line to None
    while True:
        with open(source_file_path, 'r') as f:      # Read the source file into a list
            source_file_lines = f.readlines()

        search_match = False
        target_line = None  # Reset target_line to None
        target_query = input(target_prompt) #enter the target {}
        print(f'♥ Trying to search for: {var_search}{target_query}" ................................................................')
        for index, line in enumerate(source_file_lines):
            if f'{var_search}{target_query}"' in line:
                search_match = True
                target_line = index
                break

        if not search_match:
            print("♠ Sorry, the search query was not found in the file. Please enter another query.")
            continue

        # Ask the user if each line should be kept, deleted, or replaced
        while target_line is not None and target_line < len(source_file_lines):
            line = source_file_lines[target_line]
            option = input("♥ Line " + str(target_line + 1) + ": " + line.strip() + f"\n╟─── (Press any key) Keep, (2) Delete, (3) Replace, \n╟─── {tex8} \n{txt}")            # Line strip removes whitespace in the beginning of the line
            option = option.upper()     # Convert input to uppercase
            if option == '2':
                del source_file_lines[target_line]
            elif option == '3':     # Replace while preserving any leading spaces in the original line
                replacement_text = input("╙─── Enter the replacement text: ")
                source_file_lines[target_line] = f"{line[:line.index(line.lstrip())]}{replacement_text}\n"
                target_line += 1
            elif option in ['8', '9', 'N', 'E']:
                next_action = search_option = option    # 'N'&'E' may end up being assigned to 'option', but it doesn't matter. What matters is DRY CODE
                break

            # This elif is at the end so that my (S/N/E) is not ignored if entered on a line that has the search query closing tag. Also so that If I press (1/2) after this prompt, nothing happens.
            elif '</Lookup>' in line:
                next_action = (input(f"███████████████████████████████████████████████████████████████████████████████████\n♥ Oops, sorry! You have reached the closing tag. What would you like to do?\n╙─── (C) Continue with the next line  \n╙─── {tex8} \n{txt}"))
                next_action = next_action.upper() # Convert input to uppercase
                while True:
                    if next_action == 'C': 
                        target_line += 1
                        break
                    elif next_action in ['N', 'E', '8', '9']:
                        search_option = option = next_action
                        print("♣ End tag break")
                        break
                    else: 
                        next_action = input(":(")
                if next_action == 'C':
                    continue
                else: break                            
            else:
                target_line += 1


        fff_save_changes(source_file_path, source_file_lines)

        if option == '8' or option == '9' or next_action == '8' or next_action == '9':
            fff_search_file(source_file_path, search_option)
        elif next_action == 'N':
            source_file_path = fff_upload_file()    # Assign the returned source file path
            target_query = fff_get_search_query()   # Assign the returned target index
        elif next_action == 'E':
            print("♥ Exiting () now.")
            exit()
        
        else:   # Maybe not needed
            print("♣ Final `else` of the function.")
            break
    

source_file_path = fff_upload_file()
search_option = fff_get_search_query()
fff_search_file(source_file_path, search_option)
