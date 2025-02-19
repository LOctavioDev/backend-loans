# Proyecto de Backend con Python

## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Instalación

### Clonar el repositorio

```sh
git clone https://github.com/LOctavioDev/test-api-fastapi.git
```

### Entrar en la carpeta del proyecto

```sh
cd test-api-fastapi
```

### Ejecutar el script de instalación

```sh
./install.bat
```

Este script:
- Creará un entorno virtual (`venv`).
- Activará el entorno virtual.
- Instalará las dependencias necesarias.

## Ejecución del Servidor

Para ejecutar el servidor con Uvicorn, usa el siguiente comando:

```sh
uvicorn main:app --reload
```

Esto iniciará el servidor en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) con recarga automática de cambios en el código.

## Endpoints Disponibles

Puedes ver la documentación automática de la API en los siguientes enlaces cuando el servidor esté corriendo:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [Redoc UI](http://127.0.0.1:8000/redoc)

## Notas Adicionales

- Si `install.bat` no se ejecuta correctamente, asegúrate de tener Python agregado a la variable de entorno `PATH`.
- Si tienes problemas con permisos, ejecuta `install.bat` como administrador.
