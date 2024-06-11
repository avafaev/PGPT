import os

def read_command_log(file_path='./logs/comandos/result.txt'):
    """Lee el contenido del archivo result.txt y devuelve el texto."""
    try:
        with open(file_path, 'r') as file:
            respuesta = file.read()
            return respuesta
    except FileNotFoundError:
        return "El archivo result.txt no se encontró."

if __name__ == "__main__":
    read_command_log()