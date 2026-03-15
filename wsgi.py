import sys
import os

# ============================================================
# WSGI para PythonAnywhere
# Substitua SEU_USUARIO pelo seu username do PythonAnywhere
# Exemplo: path = '/home/matheusdev/plataforma_de_cursos'
# ============================================================
path = os.environ.get('APP_PATH', '/home/SEU_USUARIO/plataforma_de_cursos')
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from app import app as application

if __name__ == '__main__':
    application.run()
