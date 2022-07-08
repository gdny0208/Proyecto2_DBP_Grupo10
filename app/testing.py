import unittest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from app import create_app
from models import setup_db
import json

#unittesting
class Test_User(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "yape3"
        self.database_path = "postgresql+psycopg2://{}@{}/{}".format('postgres:2000', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

    def test_get_users_success(self):
        res = self.client.get('/users')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_Post_success(self):
        res = self.client.get('/Post')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_api_login_success(self):
        res = self.client.post('/login', json={'username': 'gfgfggfhgf', 'password': '12345678'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_api_login_failure(self):
        res = self.client.post('/login', json={'username': 'user', 'password': 'wrong'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    

    # cambiar el email y username
    def test_api_signup_success(self):
        res = self.client.post('/signup', json={'email': 'testfgfdfhgd', 'username': 'dfghddfgcvcjdfhlñññ','password1': '12345678', 'password2': '12345678'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_api_signup_failure(self):
        res = self.client.post('/signup', json={'email': 'test', 'username': 'hola@gmail.com','password1': 'test1', 'password2': 'test123'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    
    
    def test_api_create_post_success(self):
        res = self.client.post('/create_post', json={'text': 'test', 'id1': '16'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_api_create_post_failure(self):
        res = self.client.post('/create_post', json={'text': '', 'id1': '16'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'No text provided')
    
    
    def test_api_delet_posts_False(self):
        res = self.client.post('/postuser', json={'id1': '16', 'id2':'30'})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    
    def test_api_get_posts_failure(self):
        res = self.client.post('/postuser', json={'username1': 1000})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
    
    