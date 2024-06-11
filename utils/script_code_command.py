import subprocess
import re
import json
import os
import time

# Función para ejecutar un comando del sistema y devolver su salida.
def execute_command(command):
    """Ejecuta un comando del sistema y devuelve su salida."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return None, str(e)

# Función para extraer comandos encerrados en <code>...</code> del texto proporcionado.
def extract_commands(text):
    """Extrae comandos encerrados en <code>...</code> del texto proporcionado."""
    commands = re.findall(r'<code>([\s\S]*?)<\/code>', text)  
    return [command.strip().replace('\n', ' ') for command in commands]

def extract_terminal(text):
    """Extrae comandos encerrados en <code>...</code> del texto proporcionado."""
    commands = re.findall(r'<term>([\s\S]*?)<\/term>', text)  
    return [command.strip().replace('\n', ' ') for command in commands]

# # Función para guardar los resultados en un archivo de texto.
def save_results_to_file(command, results, filename):
    """Guarda los resultados en un archivo de texto."""
    # Asegúrate de que el directorio existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(results)


# Función para guardar los resultados en un archivo JSON.
def save_results_to_json(command, result, filename):
    """Guarda los resultados en un archivo JSON."""
    command_id = str(int(time.time()))
    command_entry = {
        "comando_id": command_id,
        "comando": command,
        "resultado": result
    }

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(command_entry)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def analyze_text(texto, json_unico):
    # Simulación de la variable que contiene la respuesta de GPT
    respuestagpt = texto
    """
    Este es un ejemplo de respuesta de GPT que contiene múltiples comandos para ejecutar.
    Primero, muestra el contenido del directorio actual:
    <code>ls -l</code>
    Luego, muestra la dirección IP:
    <code>ifconfig</code>
    """

    # Extraer y ejecutar comandos
    commands = extract_commands(respuestagpt)
    comandos_terminal = extract_terminal(respuestagpt)
    
    results = ""
    for commando_t in comandos_terminal:
        stdout, stderr = execute_command(commando_t)
        print("")
        print(" - - - - - - - - ")
        if stdout:
            print(f"Command result: '{commando_t}':\n{stdout}")
            results += f"Command result: '{commando_t}':\n{stdout}\n"
        if stderr:
            print(f"Error while executing the command: '{commando_t}':\n{stderr}")
            results += f"Error while executing the command: '{commando_t}':\n{stderr}\n"
        # Guardar el último comando en un archivo de texto
        # save_last_command_to_file(command, results, "./logs/comandos/result.txt")
        save_results_to_file(commando_t, results, "./logs/comandos/result.txt")
        
        # Guardar los resuldtados en un archivo JSON
        # save_results_to_json(command, results, "./logs/comandos/command_log.json")
        save_results_to_json(commando_t, results, f"./logs/comandos/{json_unico}")

    
    
    results = ""
    for command in commands:
        print("")
        execute = input(f"¿Would you like to execute the command: '{command}'? (y/N): ")
        # if execute.lower() == 'y' or execute == "":
        if execute.lower() == 'y':
            stdout, stderr = execute_command(command)
            print("")
            print(" - - - - - - - - ")
            if stdout:
                print(f"Command result: '{command}':\n{stdout}")
                results += f"Command result: '{command}':\n{stdout}\n"
            if stderr:
                print(f"Error while executing the command: '{command}':\n{stderr}")
                results += f"Error while executing the command: '{command}':\n{stderr}\n"
            # Guardar el último comando en un archivo de texto
            # save_last_command_to_file(command, results, "./logs/comandos/result.txt")
            save_results_to_file(command, results, "./logs/comandos/result.txt")
            
            # Guardar los resuldtados en un archivo JSON
            # save_results_to_json(command, results, "./logs/comandos/command_log.json")
            save_results_to_json(command, results, f"./logs/comandos/{json_unico}")

if __name__ == "__main__":
    analyze_text()