# import os
# import json
# import time
 
# def create_new_command_log():
#     """Crea un nuevo archivo de registro de comandos en la carpeta historico."""
#     timestamp = int(time.time())
#     directory = './logs/comandos/'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     filename = f"command_log_{timestamp}.json"
#     filepath = os.path.join(directory, filename)
#     with open(filepath, "w") as file:
#         json.dump([], file, indent=4)
#     return filename

import os
import time
import json
 
def create_new_command_log():
    """Crea un nuevo archivo de registro de comandos en la carpeta ./logs/comandos/."""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    directory = './logs/comandos/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = f"command_log_{timestamp}.json"
    filepath = os.path.join(directory, filename)
    # filepath = os.path.join(filename)
    with open(filepath, "w") as file:
        json.dump([], file, indent=4)
    return filename
 
def list_recent_command_logs(n=5):
    directory = "./logs/comandos"
    if not os.path.exists(directory):
        return []
 
    files = [f for f in os.listdir(directory) if f.startswith("command_log_") and f.endswith(".json")]
    files.sort(reverse=True)
    return files[:n]
 
def select_existing_command_log():
    recent_logs = list_recent_command_logs()
    if not recent_logs:
        print("There are no registries saved. Create a new one")
        return create_new_command_log()
    
    print("Choose an existing registry file, or create a new one:")
    for idx, log in enumerate(recent_logs):
        print(f"{idx + 1}. {log}")
    print("0. Create new")
 
    while True:
        choice = input("Choose between (0-5): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return create_new_command_log()
            elif 1 <= choice <= len(recent_logs):
                return os.path.join("", recent_logs[choice - 1])
        print("Invalid option. Please, choose a number between 0 and 5.")