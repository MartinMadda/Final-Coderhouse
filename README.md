# Proyecto final de Coderhouse (Python-Django)

# Alumnos: Romero Johan, Bubich Agustina y Maddalena Martín.

## Instalaciones desde VSCode

- Instalar Python

```bash
$ pip install python
```
- Instalar Django
```bash
$ pip install django
```
- Instalar Crispy-forms
```bash
$ pip install django_crispy-forms
```
- Instalar Pilow
```bash
$ pip install pillow 
```
- Instalar ckeditor
```bash
$ pip install django-ckeditor
```

## Verificar que este todo correctamente instalado

- Python en el bash
```bash
$ python --version
Python 3.10.7
```
- Django en el shell
```ps
>>> import django
>>> django.VERSION
(4, 1, 2, 'final', 0)
>>>
```

### Lo primero que debemos hacer es crear nuestro repositorio en github  https://github.com/MartinMadda/Final-Coderhouse.git.

### Luego en VScode vamos a crear una nueva carpeta y vamos a abrir la terminal para clonar nuestro repositorio y asi poder trabajar en él de la siguiente manera:

```ps
git clone https://github.com/MartinMadda/Final-Coderhouse.git .
```
```ps
"Es muy importante el espacio y el .(punto) ya que asi nuestro repositorio no creara otras carpetas dentro de la nuestra."
```

```
El administrador debe autenticarse y es el unico autorizado de subir posteos, modificar los datos del negocio, las tarifas y la galeria.
Cualquier usuario que ingrese a la pagina puede hacer una reserva, la cual por detras sera un mail al administrador que evaluara el pedido y respondera al mail cargado por el cliente con los pasos a seguir.