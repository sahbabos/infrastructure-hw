import unittest
from flask_socketio import SocketIO
from frontend_service import app

class TestFrontendService(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.socketio = SocketIO(self.app)
        self.client = self.socketio.test_client(self.app, namespace='/')

    def test_index_route(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_receive_broadcast_message(self):
        test_message = {'message': 'Hello world'}
        self.client.emit('new_message', test_message)
        received = self.client.get_received()
        print(f"Received events: {received}")  # Debugging log
        self.assertTrue(any(event['name'] == 'new_message' for event in received))



if __name__ == '__main__':
    unittest.main()
