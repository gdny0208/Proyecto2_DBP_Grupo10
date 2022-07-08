from crypt import methods
from flask import Flask, jsonify, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

from models import setup_db, setup_db, User, Post, Comment, Like

login_manager = LoginManager()

def create_app(test_config=None):
    app=Flask(__name__)
    setup_db(app)
    CORS(app, origins=['http://localhost:8081', 'http://localhost:5000'])

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS, POST, PATCH, DELETE")
        return response
    
    @app.route('/', methods=['GET'])
    def api_home():
        try:
            return {
                "success": True,
                "message": "Bienvenido"
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }, 500

    @app.route("/users", methods=["GET"])
    def get_users():
        users = User.query.order_by("id").all()

        if len(users) == 0:
            return {
                "message": "No se encontaron usuarios"
            }, 404
        
        return {
            "success": True,
            "users": [user.format() for user in users],
            "total_users": len(users)
        }, 200

    @app.route("/Post", methods=["GET"])
    def get_Post():
        users = Post.query.order_by("id").all()

        if len(users) == 0:
            return {
                "message": "No se encontaron usuarios"
            }, 404
        
        return { 
            "success": True,
            "users": 
            [user.format() for user in users],
        }, 200

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/login', methods=['POST'])
    def api_login():
        if request.method == 'POST':
            username = request.json.get("username")
            password = request.json.get("password")

            user = User.query.filter_by(username=username).first()

            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return {
                        "success": True,
                        "message": "Usuario autenticado correctamente",
                        "id": current_user.id,
                        "usuario": current_user.username,
                        "email": current_user.email
                    }
                else:
                    return {
                        "success": False,
                        "message": "Contraseña incorrecta"
                    }, 404
            else:
                return {
                    "success": False,
                    "message": "Usuario no encontrado"
                }, 404


    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return jsonify({
            'success': True,
            'message': 'Logout successful'
        })

    @app.route('/signup', methods=['GET', 'POST'])
    def api_signup():
        if request.method == 'POST':
            email = request.json.get("email")
            username = request.json.get("username")
            password1 = request.json.get("password1")
            password2 = request.json.get("password2")

            email_exists = User.query.filter_by(email=email).first()
            username_exists = User.query.filter_by(username=username).first()

            if email_exists:
                return jsonify({
                    'success': False,
                    'message': 'Email already exists'
                }),400
            if username_exists:
                return jsonify({
                    'success': False,
                    'message': 'Username already exists'
                }),400
            if password1 != password2:
                return jsonify({
                    'success': False,
                    'message': 'Passwords do not match'
                })
            if len(username)<3:
                return jsonify({
                    'success': False,
                    'message': 'Username must be at least 3 characters'
                }),400
            if len(password1)<6:
                return jsonify({
                    'success': False,
                    'message': 'Password must be at least 6 characters'
                }),400
            if len(email)<4:
                return jsonify({
                    'success': False,
                    'message': 'Email is invalid'
                })
            else:
                user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
                user.insert()
                return jsonify({
                    'success': True,
                    'user': user.format(),
                    'message': 'Signup successful'
                }),200

    @app.route("/create_post", methods=['POST'])
    def api_create_post():
        if request.method == 'POST':
            text = request.json.get("text")
            id1 = request.json.get("id1")
            v = int(id1)
            if not text or id1 ==" " or None:
                return jsonify({
                    'success': False,
                    'message': 'No text provided'
                })
            else:
                post = Post(text=text, author=id1)
                post.insert()
                return jsonify({
                    'success': True,
                    'message': 'Post created',
                    'hola': v
                    
                })
    
    @app.route("/delete", methods=['POST'])
    def api_delete_post():
        if request.method == 'POST':
            id1 = request.json.get("id")
            id3 = int(id1)
            id2 = request.json.get("id2")
            id4 = int(id2)
            post = Post.query.filter_by(id=id3).first()

            if not post:
                return jsonify({
                    'success': False,
                    'message': 'Post not found'
                })
            elif id4 != post.author:
                return jsonify({
                    'success': False,
                    'message': 'You do not have permission to delete this post'
                })
            else:
                post.delete()
                return jsonify({
                    'success': True,
                    'message': 'Post deleted'
                })

    @app.route("/create-comment/<post_id>", methods=['POST'])
    @login_required
    def api_create_comment(post_id):
        text = request.json.get("text")

        if not text:
            return jsonify({
                'success': False,
                'message': 'No text provided. Comment cannot be empty.'
            })
        else:
            post=Post.query.filter_by(id=post_id).first()
            if post:
                comment = Comment(text=text, author=current_user.id, post_id=post_id)
                comment.insert()
                return jsonify({
                    'success': True,
                    'message': 'Comment created'
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Post does not exist'
                })
    
    
    return app