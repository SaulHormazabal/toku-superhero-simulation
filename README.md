# Toku Superhero Simulation

## Instalación

```sh
pip install git+ssh://git@github.com/Toku-SuperHero/toku-superhero-simulation.git
```

⚠️ Este proyecto se encuentra privado, por lo que es necesario que se otorgue
acceso antes de su instalación.

Crea el archivo de variables de entorno con nombre `.env` y las siguiente variables.

```text
DATABASE_NAME=superheroes
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5433

SECRET_KEY=soy-una-super-secret-key

CELERY_BROKER_REDIS_URL=redis://localhost:6379/0

SUPERHERO_API_URL=https://superheroapi.com/api/{token}

ALLOWED_HOSTS=simulation.localhost
```

Instalación de dependencias:

```sh
poetry install
```

Configura el host para este servicio agregando al archivo `/etc/hosts` lo siguiente:

```text
127.0.0.1 simulation.localhost
```

Para facilitar el desarrollo puedes usar postgres y redis con el docker-compose
disponible en el proyecto:

```sh
docker-compose pull
docker-compose up -d
```

## Desarrollo

### Tecnologías utilizadas

- **Poetry**: gestor de dependencias para Python
- **Django**: framework para la creación aplicaciones web
- **Django Rest Framework**: librería para crear APIs Rest
- **Celery**: ejecucción de tareas en segundo plano
- **Prospector**: suite para análisis estático de código Python
- **markdownlint-cli2**: librería para análisis estático de archivos markdown

### Diseño

Se desarrolló una api rest utilizando Django debido a la robustes en la
construcción de APIs y las librerías disponibles facilitando el uso de la
base de datos, organización e integración con Celery.

![image](https://github.com/Toku-SuperHero/toku-superhero-simulation/assets/1095706/05e466be-0415-4c62-8417-057dd927117f)

### Modelo de datos

Para facilitar el cálculo de estadística se relegó la tarea a la base de datos
utilizando vistas, favoreciendo la integridad de los datos y un mayor rendimiento.

![image](https://github.com/Toku-SuperHero/toku-superhero-simulation/assets/1095706/37153ba3-61ce-44db-ab27-26c84174d771)

### Componentes

El proyecto se organizó en 3 apps.

![image](https://github.com/Toku-SuperHero/toku-superhero-simulation/assets/1095706/f1b49c37-5d75-44e2-9be6-7d0d21128cd4)

### Integración continua

El proyecto tiene configurado un proceso de integración continua usando GitHub
Actions donde se evalúa lo siguiente:

- Tests: pruebas para asegurar el correcto funcionamiento ante modificaciones
en el código fuente
- Análisis estático de markdown: permite mantener un formato consistente
favoreciendo un estilo de escritura fácil de leer sin un visualizador
- Análisis estático de código Python: se utiliza prospecto para agrupar
y facilitar el uso de las siguientes herramientas
  - Dodgy: detecta problemas de seguridad
  - McCabe: complejidad ciclomática
  - PyCodeStyle: detecta incumplimientos a la convención de docstring PEP 257
  - PyFlakes: análisis del estilo de código
  - PyLint: análisis del estilo de código
