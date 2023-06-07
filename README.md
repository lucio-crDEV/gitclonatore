# GitClonatore

GitClonatore es una herramienta de línea de comandos que te permite clonar repositorios de GitHub de un usuario específico.

## Requisitos

- Python 3.6 o superior
- Pip (administrador de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga el archivo `script.py`.
2. Abre una terminal en el directorio donde se encuentra el archivo `script.py`.

## Uso

```
python script.py -u [nombre_usuario] -n [cantidad_repositorios]
```

[nombre_usuario] es el nombre de usuario de GitHub del cual deseas clonar los repositorios.
[cantidad_repositorios] es opcional y representa el número de repositorios que deseas clonar. Si no se especifica, se clonarán todos los repositorios del usuario.

Ejemplos:

### Clonar todos los repositorios de un usuario:

```
python script.py -u username
```

### Clonar solo 3 repositorios de un usuario:

```
python script.py -u username -n 3
```


## Clonar solo 3 repositorios de un usuario:

Los repositorios se clonarán en la carpeta [descargas] dentro del directorio actual.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.