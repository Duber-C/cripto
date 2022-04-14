import getpass
import json
import base64
import os
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def leerArchivo(file_dir):
    s = ''
    try:
        with open(file_dir) as f:
            s = f.read()
        f.close()
        
    except:
        print('nombre de archivo o ruta incorrecta..')

    return(s)   

def escribirArchivo(file_dir, text):
    try:
        with open(file_dir, 'w') as f:
            f.write(text)
        f.close()
        print('se escribio correctamente..')
    except:
        print('nombre de archivo o ruta incorrecta..')
    
def codificar(text, key):
    c = Fernet(key)
    return c.encrypt(text)

def decodificar(text, key):
    d = Fernet(key)

    try:
        return d.decrypt(text)
    except:
        print('archivo o contrasenia incorrecta..')
        return ''

def crearLlave(password, salt):
    SALT = str.encode(leerArchivo(salt))
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=SALT, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(str.encode(password)))
    
    return key

def imprimir(text):
    text = text.replace(',' , '\n')
    text = text.replace(';', '\t')
    print(text)


if __name__ == "__main__":

    # variables globales 
    JFILE = json.loads(leerArchivo('variables.json'))
    PASSWORD = ''
    FILE_DIR = JFILE['file_dir']
    SALT_DIR = JFILE['salt']
    TEXT = ''
    OPTIONS = {'d': 'desencriptar: muestra la informacion desencriptada del archivo seleccionado', 
                'n': 'nuevo: nueva entrada en un archivo encriptado',
                'e': 'encriptar: encripta el archivo seleccionado',
                's': 'crearsal: crea la "sal" necesaria para la encriptacion de archivos',
                'fd': 'fdesencriptar: desencripta un archivo',
                'sa': 'sarchivo: guarda la ubicacion de un archivo encriptado',
                'ss': 'ssal: guarda la ubicacion de sal',
                'h': 'help: muestra todos los comandos disponibles',
                'g': 'generar: genera una contraseña'}

    if FILE_DIR == '':
        print('no se ha seleccionado ningun archivo')
    if SALT_DIR == '':
        print('no se ha seleccionado ninguna sal')

    
    print(JFILE)

    args = ''
    while args != 'salir':
        args = input(': ')
        log = '-> '
              
        if args in ['desencriptar', 'd']: 
            if FILE_DIR == '':
                text = leerArchivo(input('ruta o nombre del archivo: '))
            else:
                text = leerArchivo(FILE_DIR)

            if text == '':
                break

            password = getpass.getpass('contraseña: ')
            key = crearLlave(password, SALT_DIR)

            
            try:
                imprimir(decodificar(text.encode(), key).decode())
            except:
                pass

        elif args in ['nuevo', 'n']:
            if FILE_DIR == '':
                file_dir = input('ruta o nombre del archivo: ')
                text = leerArchivo(file_dir)
            else:
                text = leerArchivo(FILE_DIR)
                file_dir = FILE_DIR

            if text == '':
                pass

            password = getpass.getpass('contraseña: ')
            key = crearLlave(password, SALT_DIR)
            
            try:
                texto_nuevo = input('tabs(;) nueva linea (,) --> ')
                texto_nuevo = decodificar(text.encode(), key).decode() + texto_nuevo
                escribirArchivo(file_dir, codificar(texto_nuevo.encode(), key).decode())
                log += 'se ha agregado correctamente..'
            except:
                pass
            
        elif args in ['fdesencriptar', 'fd']:
            if FILE_DIR == '':
                file_dir = input('ruta o nombre del archivo: ')
                text = leerArchivo(file_dir)
            else:
                text = leerArchivo(FILE_DIR)
                file_dir = FILE_DIR

            if text == '':
                break
            
            password = getpass.getpass('contraseña: ')
            key = crearLlave(password, SALT_DIR)
            
            try:
                escribirArchivo(file_dir, decodificar(text.encode(), key).decode())
                log += 'se ha desencriptado correctamente..'
            except:
                break

        elif args in ['crearsal', 's']:
            escribirArchivo(input('nombre del archivo: ') + '.txt', str(os.urandom(256)))
            log += 'se ha creado la sal..'

        elif args in ['encriptar', 'e']:
                archivo = input('ruta o nombre del archivo: ')
                password = getpass.getpass('contraseña: ')
                key = crearLlave(password, SALT_DIR)
                text = leerArchivo(archivo)

                if text != '':
                    if input('esta seguro de encriptar este archivo(y): ') == 'y':
                        escribirArchivo(archivo, codificar(text.encode(), key).decode())
                        log += 'se encripto correctamente..'

        elif args in ['sarchivo', 'sa']:
            FILE_DIR = input('ruta o nombre del archivo: ')
            JFILE['file_dir'] = FILE_DIR
            escribirArchivo('variables.json', json.dumps(JFILE))
    

        elif args in ['ssal', 'ss']:
            SALT_DIR = input('ruta o nombre de la sal: ')
            JFILE['salt'] = SALT_DIR
            escribirArchivo('variables.json', json.dumps(JFILE))

        elif args in ['help', 'h']:
            for i in OPTIONS.keys():
                print('-> {}: \n    {}'.format(i, OPTIONS[i]))
        
        elif args in ['g', 'generar']:
            letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]=+-_?~"
            password = ''
            for i in range(24):
                password += random.choice(letras)
            print(password)
        

        print(log)

