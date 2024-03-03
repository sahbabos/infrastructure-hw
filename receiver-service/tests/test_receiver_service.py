import unittest
from unittest.mock import patch
from receiver_service import app, log_message, emit_message


class ReceiverServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Received Messages', response.data)

    @patch('receiver_service.print')
    def test_log_message(self, mock_print):
        data = {'message': 'Hello, world!'}
        log_message(data)
        mock_print.assert_called_once_with(
            "Received broadcast message: Hello, world!")

    @patch('receiver_service.socketio')
    def test_emit_message(self, mock_socketio):
        data = {'message': 'Hello, world!'}
        emit_message(data)
        mock_socketio.emit.assert_called_once_with(
            'new_message', {'message': 'Hello, world!'})


if __name__ == '__main__':
    unittest.main()
