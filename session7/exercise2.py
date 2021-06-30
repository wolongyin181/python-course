with open ('pikachu.txt','w') as file_handler:
    file_handler.write("Pikachu")
with open ('pikachu.txt','a') as file_handler:
    file_handler.write("\nChrizard")
with open ('pikachu.txt','a') as file_handler:
    file_handler.writelines(["\nEevee", "\nSquirtle"])
