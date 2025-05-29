---


# Blog Flask - Un Simple Blog Construido con Flask y MongoDB

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-4.x%2B-4EA94B?style=for-the-badge&logo=mongodb)
![Gunicorn](https://img.shields.io/badge/Gunicorn-22.x-lightgrey?style=for-the-badge&logo=gunicorn)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render)

Un proyecto de blog sencillo que demuestra el uso de Flask como framework web junto con MongoDB como base de datos NoSQL para almacenar las entradas del blog. La aplicación permite a los usuarios crear y visualizar entradas.

## ✨ Características

* **Creación de Entradas:** Publica nuevas entradas de blog con título, contenido y fecha.
* **Visualización de Entradas:** Muestra todas las entradas existentes en la página principal.
* **Persistencia de Datos:** Almacena todas las entradas en una base de datos MongoDB.
* **Variables de Entorno:** Gestión segura de la cadena de conexión a la base de datos usando `python-dotenv`.
* **Listo para Producción:** Configurado para ser desplegado con Gunicorn.

## 🚀 Tecnologías Utilizadas

* **Python 3.11+**: Lenguaje de programación.
* **Flask**: Microframework web para Python.
* **PyMongo**: Driver oficial de MongoDB para Python.
* **python-dotenv**: Para cargar variables de entorno desde un archivo `.env`.
* **Gunicorn**: Servidor WSGI para producción.
* **MongoDB Atlas (o local)**: Base de datos NoSQL.
* **Render**: Plataforma de despliegue en la nube.

## ⚙️ Configuración del Entorno Local

Sigue estos pasos para levantar el proyecto en tu máquina local:

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/Diony-dev/blog_flask.git](https://github.com/Diony-dev/blog_flask.git)
cd blog_flask
```

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica trabajar con entornos virtuales para gestionar las dependencias del proyecto.

**En Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**En macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

Una vez activado el entorno virtual, instala todas las librerías necesarias:

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Crea un archivo llamado `.env` en la raíz de tu proyecto (al mismo nivel que `app.py` y `requirements.txt`).

```dotenv
# .env
MONGODB_URI="tu_cadena_de_conexion_a_mongodb"
# Ejemplo: MONGODB_URI="mongodb+srv://usuario:contraseña@cluster.xyz.mongodb.net/mi_blog?retryWrites=true&w=majority"
```
**Importante:** Reemplaza `"tu_cadena_de_conexion_a_mongodb"` con la URL de conexión a tu base de datos MongoDB (por ejemplo, de MongoDB Atlas o una instancia local). **Nunca subas tu archivo `.env` a control de versiones (Git).**

### 5. Ejecutar la Aplicación Localmente

Con todas las dependencias instaladas y las variables de entorno configuradas, puedes iniciar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000` (o el puerto que configure Flask).

## ☁️ Despliegue en Render

Este proyecto está diseñado para ser desplegado en plataformas como Render.

### Comando de Inicio

En la configuración de tu servicio en Render (en la sección "Start Command" o "Run Command"), utiliza el siguiente comando:

```bash
/usr/local/bin/python -m gunicorn app:app
```

### Variables de Entorno en Render

Asegúrate de configurar la variable de entorno `MONGODB_URI` en la interfaz de Render para tu servicio, con la cadena de conexión a tu base de datos MongoDB.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias, mejoras o encuentras algún error, no dudes en:

1.  Hacer un "fork" del repositorio.
2.  Crear una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3.  Realizar tus cambios.
4.  Hacer "commit" de tus cambios (`git commit -m 'feat: añade nueva característica'`).
5.  Enviar tus cambios (`git push origin feature/nueva-caracteristica`).
6.  Abrir un "Pull Request".

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
```
