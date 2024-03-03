import unittest
from unittest.mock import patch
import broadcast_service


class TestBroadcastService(unittest.TestCase):

    @patch('broadcast_service.sio')
    def test_send_message(self, mock_sio):
        message = {"message": "Hello world"}
        broadcast_service.send_message(message)
        mock_sio.emit.assert_called_once_with('broadcast_message', message)

    def test_generate_message(self):
        expected_message = {"message": "Hello world"}
        self.assertEqual(broadcast_service.generate_message(),
                         expected_message)

    @patch('broadcast_service.random.randint')
    def test_get_interval(self, mock_randint):
        mock_randint.return_value = 5
        self.assertEqual(broadcast_service.get_interval(), 5)


if __name__ == '__main__':
    unittest.main()
