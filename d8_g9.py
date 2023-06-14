from os import system
import time
system('cls')

# Clase Usuario
# atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
# métodos: login(), registrar()

class Usuario:
    contador_id = 0
    
    def __init__(self, nombre, apellido, teléfono, username, email,
                 contraseña, fecha_registro, avatar=None, estado=None, online=None):
        Usuario.contador_id += 1 
        self.id = Usuario.contador_id
        self.nombre = nombre
        self.apellido = apellido
        self.teléfono = teléfono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
    
    def registrar(self):
        system('cls')
        print('Registrarse')
        print('----------------------------------------')
        self.nombre = input('Nombre: ')
        self.apellido = input('Apellido: ')
        self.email = input('Correo electrónico: ')
        self.telefono = input('Teléfono: ')
        self.username = input('Usuario: ')
        self.contraseña = input('Contraseña: ')
        self.fecha_registro = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.avatar = input('Avatar: ')
        self.estado = input('Estado: ')
        system('cls')
        print('')
        print('Usuario registrado con éxito!')
        time.sleep(4)

    def login(self):
        system('cls')
        print('Inicio de Sesión')
        print('------------------------------------------')
        username = input('Usuario: ')
        contraseña = input('Contraseña: ')
    
        if contraseña == self.contraseña and username == self.username:
            print('Inicio de sesión exitoso')
            self.online = True
            time.sleep(4)
        else:
            print('')
            print('El nombre de usuario o la contraseña son incorrectos')
            print('Intente nuevamente')
            time.sleep(4)
            self.login()

lista_usuarios = []

usuario_nuevo = Usuario("nombre", "apellido", "telefono", "username", "correo",
                        "contraseña", "fecha", "avatar", "estado", False)

lista_usuarios.append(usuario_nuevo)

usuario_nuevo.nombre()








#Clase Publico(Usuario)
# atributo: es_publico
# métodos: registrar(), comentar()



#clase Colaborador(Usuario)
#atributos: es_colaborador
#métodos: registrar(), comentar(), publicar()



#clase Articulo
#id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado



#clase Comentario
#id, id_articulo, id_usuario, contenido, fecha_hora, estado



#Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y
#logueado, código que permita comentar al Publico y además publicar al Colaborador.'''




#INTEGRANTES:
#AQUINO ALAN MAURICIO SEBASTIAN