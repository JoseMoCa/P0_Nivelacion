from models.user_model import UsuarioCrear

def test_usuario_crear_modelo():
    usuario_datos = {
        "nombre_usuario": "usuario@example.com",
        "contrasena": "contrasena123",
        "imagen_perfil": "http://example.com/imagen.jpg"
    }
    usuario = UsuarioCrear(**usuario_datos)

    assert usuario.nombre_usuario == usuario_datos["nombre_usuario"]
    assert usuario.contrasena == usuario_datos["contrasena"]
    assert usuario.imagen_perfil == usuario_datos["imagen_perfil"]

# print(usuario.nombre_usuario)
