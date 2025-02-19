@echo off
setlocal

:: entorno virtual ya existe ?
if exist venv (
    echo Activando entorno virtual...
) else (
    echo Creando entorno virtual...
    python -m venv venv
)

:: Activar el entorno virtual
call venv\Scripts\activate.bat

:: Instalar dependenciaxs
echo Instalando dependencias...
pip install -r requirements.txt

echo Instalación completada.
pause
