Proyecto 2: Cocina para Mancos

Integrantes:

Diego Luis Bazán Lostaunau
Giuseppe Antonio Del Negro Yabar

Descripción del proyecto: El proyecto consiste en crear un blog de cocina en donde el usuario puede interactuar con otros personas con el fin de aprender sobre nuevas maneras de cocinar que sean de su agrado. El usuario es completamente libre de compartir sus experiencias y habilidades con los demás, ya sea publicando recetas como experiencias en la cocina.

Objetivos principales: El trabajo tiene como objetivo crear una comunidad de personas, con experiencia tanto profesional como novatos con disposición a aprender y compartir su conocimiento acerca de la gastronomía y su hermoso mundo.

Crear una comunidad saludable donde todos puedan expresar su gusto, dedicacion, pasion o entre otros por la cocina

Misión: Nuestra misión es poder hacer que la persona que entre pueda mejorar su conocimiento y también que pueda ayuda compartiendo sus ideas. Que en esta red el usuario que entre tanto sea un profesional o un novato pueda crecer como cocinero y llegar a una autorrealización.

Visión: Nuestra visión es empezar como un blog chico pero luego poder ampliarnos y tener miles de usuarios que comenten al dia y que logren mejorar su rendimiento con diferentes consejos. Gracias a esto tendremos una plataforma con millones de variantes de recetas lo que nos dara la capacidad de poder decidir y convinar hasta llegar al sabor perfecto de cada una.

Información acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos:

Flask para poder crear la aplicación web, de aquí importamos lo siguiente: render template: nos sirve para para renderizar la plantilla html en Python, request: lo usamos para extraer la información de los formularios html

Sqlalchemy: para manipular la base de datos y usamos la funcion func para poder sacar la hora en la que se registran

postgresql : para crear la base de datos y tener donde almacenar los datos

Migrate: para migraciones de bases de datos cuando usamas SQLAlchemy

Flask-login: para que las personas puedan registrarse, para administrar las sesiones del usuario tras la autenticación. lo que importamos fue:

login_User: esto le permite iniciar sesión a la persona

logout_User: para que pueda salir de su sesion

Login_required: para que el usuario tenga que registrar para poder seguir en nuestra pagina

Current_User: Un proxy para el usuario.

Usermixin: nos ayuda para el login porque nos da metodos de autenticación, para hallar el id y entre otros.

Login manager contiene el código que permite que su aplicación y Flask-Login funcionen juntos

werkzeug.security: para proteger la contraseña, importamos generate_password_hash para hacer un hash a la contraseña y check_password_hash que sirve para chequear la contraseña del usuario.

Nuestra base de datos fue creada con postgresql.

Script a ejecutar para iniciar la base de datos con datos: El script a ejecutar para iniciar la base de datos es app.py.

Endpoints utilizados en el sistema: Nuestra app cuenta con 10 endpoints. Estos son:

@app.route("/create-post"): sirve para crear los post del servidor. se pide que el texto no este vacio y luego se crea esto guardando el id del usuario y luego redireccionando al inicio

@app.route("/delete-post): esto sirve para poder eliminar el post que se halla publicado. Esto primero verifica que exista y luego si el usuario es el creador de este. cuando confirma esto luego borra el post

@app.route("/posts/"): Esto sirve para ver todo los post de algún usuario, sino existe te manda un error y te redirige al inicio.

@app.route("/create-comment/<post_id>"): este sirve para comentar los post de las personas donde revisa que haya texto y que exista.

@app.route("/delete-comment/<comment_id>"): Esto sirve para eliminar algún comentario que hayas escrito, primero revisa que exista y luego que sea tuyo. si esto pasa entonces se elimina tu comentario.

@app.route("/like-post/<post_id>" Esto esta para poder agregar y quitar likes, primero revisa que el comentario exista y luego comprobando si le has dado like antes, si es asi ahora le quitas pero si no le habías dado ahora le aumentas.

@app.route("/login"): Este sirve para poder iniciar tu sesión. primero recibe la información del form y luego de esto compara el email para ver si existe, sino existe te manda un flash y si está en nuestra base de datos pasa a comparar la contraseña del usuario, si esto es igual te deja entrar,

@app.route("/sign-up"): Esto sirve para que nuestros usuarios puedan registrarse, primero se pide que llenen sus datos y luego de esto nuestra base de datos busca si existe ese usuario o contraseña, que las 2 contraseñas coincidan, que tengan un cierto lagro el usuario y entre otras. finalmente se registra el usuario y se hace un hash a la contraseña

@app.route("/logout"): sirve para que nuestro usuario cierre su sesión y se vaya de la página.

@app.route("/users", methods=["GET"])

Hosts: El API se encuentra en el localhost de la computadora en el puerto predeterminado de postgres 5432 y en el puerto 5000.

Vue.js: Se encuentra en el puerto 8081

Forma de autenticación:

– Manejo de errores HTTP:

(500) : Errores en el Servidor. Esto lo manejamos con un if y else, lo que ocurre que si falla algo marca un error y se redirecciona a otra página donde le llega un mensaje del fallo con un flash.

(400) : Errores en el Cliente: esto lo mantenemos con login_required para que no entre a paginas que no puede

(300) : Redirección, usamos redirect (200)Exitoso y (100)Informacional. si todo funciona se manda un mensaje flash que dice que tuvo exito.

La información se guarda en el localstorage después de registrarte como usuario o hacer el login.

– Cómo ejecutar el API:

Crear un virtual environment (env).
Instalar los elementos requeridos que se encuentran en “requirements.txt”
Ejecutar FLASK RUN.

- Cómo ejecutar Vue.js:

Entrar a la carpeta de frontend 
Descargar node modules con el comando "npm install"
Ejecutar el comando yarn serve 
