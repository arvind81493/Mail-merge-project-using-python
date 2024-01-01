#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



placeholder="[name]"
with open("./Input/Names/invited_names.txt") as names:
    names_list=names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letter=letters.read()
    for name in names_list:
        striped_name=name.strip()
        new_letter=letter.replace(placeholder,striped_name)
        with open(f"./Output/ReadyToSend/send_to_{striped_name}.txt",mode='w') as completed_letter:
            completed_letter.write(new_letter)

