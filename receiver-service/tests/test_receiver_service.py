import unittest
from unittest.mock import patch
from receiver_service import app
import json

class TestReceiverService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_receive_valid_message(self):
        valid_message = {"message": "Hello world"}
        response = self.app.post('/receive', data=json.dumps(valid_message), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')
        self.assertEqual(response.json['message'], 'Message received')
        self.assertEqual(response.json['received_message'], valid_message['message'])

    def test_receive_invalid_message(self):
        invalid_message = {"text": "Hello world"}
        response = self.app.post('/receive', data=json.dumps(invalid_message), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['status'], 'error')
        self.assertEqual(response.json['message'], 'Invalid message format')

    def test_receive_multiple_messages(self):
        messages = [{"message": "Hello world 1"}, {"message": "Hello world 2"}, {"message": "Hello world 3"}]
        for message in messages:
            response = self.app.post('/receive', data=json.dumps(message), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['status'], 'success')
            self.assertEqual(response.json['message'], 'Message received')
            self.assertEqual(response.json['received_message'], message['message'])

    @patch('receiver_service.logging.info')
    def test_logging_on_success(self, mock_log):
        valid_message = {"message": "Hello world"}
        self.app.post('/receive', data=json.dumps(valid_message), content_type='application/json')
        mock_log.assert_called()

    @patch('receiver_service.logging.error')
    def test_logging_on_failure(self, mock_log):
        invalid_message = {"text": "Hello world"}
        self.app.post('/receive', data=json.dumps(invalid_message), content_type='application/json')
        mock_log.assert_called()

if __name__ == '__main__':
    unittest.main()
