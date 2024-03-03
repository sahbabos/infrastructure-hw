import unittest
from unittest.mock import patch, MagicMock
import sys
import time
import threading
import requests
sys.path.append('../')
import broadcast_service

class TestBroadcastService(unittest.TestCase):
    
    def setUp(self):
        broadcast_service.running = True

    def tearDown(self):
        broadcast_service.running = False

    @patch('broadcast_service.requests.post')
    @patch('broadcast_service.time.sleep', side_effect=InterruptedError)
    def test_broadcast_message(self, mock_sleep, mock_post):
        with self.assertRaises(InterruptedError):
            broadcast_service.broadcast_message()
        mock_post.assert_called_with('http://localhost:5000/receive', json={'message': 'Hello world'})

    @patch('broadcast_service.requests.post')
    def test_multiple_broadcasts(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.side_effect = [mock_response] * 10 + [InterruptedError]
        with self.assertRaises(InterruptedError):
            broadcast_service.broadcast_message()
        self.assertGreaterEqual(mock_post.call_count, 2)

    @patch('broadcast_service.requests.post')
    def test_logging_on_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        with patch('broadcast_service.logging.info') as mock_log:
            broadcast_service.running = True
            # Run the broadcast_message function in a separate thread to avoid blocking
            thread = threading.Thread(target=broadcast_service.broadcast_message)
            thread.start()
            time.sleep(1)
            broadcast_service.running = False
            thread.join()

            mock_log.assert_called()

    @patch('broadcast_service.requests.post', side_effect=requests.exceptions.RequestException('Error'))
    def test_logging_on_failure(self, mock_post):
        with patch('broadcast_service.logging.error') as mock_log:
            broadcast_service.running = True
            thread = threading.Thread(target=broadcast_service.broadcast_message)
            thread.start()
            time.sleep(1)
            broadcast_service.running = False
            thread.join()

            mock_log.assert_called()

    def test_graceful_shutdown(self):
        def set_running_false():
            time.sleep(1)
            broadcast_service.running = False

        threading.Thread(target=set_running_false).start()
        with patch('broadcast_service.requests.post') as mock_post:
            broadcast_service.broadcast_message()
            mock_post.assert_called()

if __name__ == '__main__':
    unittest.main()
