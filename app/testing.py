import unittest
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app
from models import setup_db
import json

#unittesting
class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "yape3"
        self.database_path = "postgresql+psycopg2://{}@{}/{}".format('postgres:2000', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

    def test_get_users_success(self):
        res = self.client.get('/users', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_users'], 0)
        self.assertEqual(data['users'], [])
    
    def test_get_users_failure(self):
        res = self.client.get('/users', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_get_Post_success(self):
        res = self.client.get('/Post')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_users'], 0)
        self.assertEqual(data['users'], [])
    
    def test_get_Post_failure(self):
        res = self.client.get('/Post')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')
    
    def test_api_login_success(self):
        res = self.client.post('/login', json={'username': 'test', 'password': 'test'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['access_token'])

    def test_api_login_failure(self):
        res = self.client.post('/login', json={'username': 'test', 'password': 'wrong'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Wrong credentials')
    
    def test_api_signup_success(self):
        res = self.client.post('/signup', json={'username': 'test', 'email': ''})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['access_token'])
    
    def test_api_signup_failure(self):
        res = self.client.post('/signup', json={'username': 'test', 'email': ''})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_logout_success(self):
        res = self.client.post('/logout', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Successfully logged out')
    
    def test_api_logout_failure(self):
        res = self.client.post('/logout', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized')
    
    def test_api_create_post_success(self):
        res = self.client.post('/posts', json={'title': 'test', 'content': 'test'}, headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['post'])
    
    def test_api_create_post_failure(self):
        res = self.client.post('/posts', json={'title': 'test', 'content': 'test'}, headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_delete_post_success(self):
        res = self.client.delete('/posts/1', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Successfully deleted post')
    
    def test_api_delete_post_failure(self):
        res = self.client.delete('/posts/1', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_get_posts_success(self):
        res = self.client.get('/posts', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['posts'])
    
    def test_api_get_posts_failure(self):
        res = self.client.get('/posts', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_create_comment_success(self):
        res = self.client.post('/comments', json={'content': 'test'}, headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['comment'])
    
    def test_api_create_comment_failure(self):
        res = self.client.post('/comments', json={'content': 'test'}, headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_delete_comment_success(self):
        res = self.client.delete('/comments/1', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Successfully deleted comment')

    def test_api_delete_comment_failure(self):
        res = self.client.delete('/comments/1', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_api_like_post_success(self):
        res = self.client.post('/posts/1/like', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Successfully liked post')
    
    def test_api_like_post_failure(self):
        res = self.client.post('/posts/1/like', headers={'Authorization': 'Bearer ' + self.get_auth_token()})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
