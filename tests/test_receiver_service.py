import unittest
from unittest.mock import patch
import sys
sys.path.append('../receiver-service')

import receiver_service

class TestBroadcastService(unittest.TestCase):

    @patch('broadcast_service.requests.post')
    def test_broadcast_message(self, mock_post):
        broadcast_service.broadcast_message()
        mock_post.assert_called_once()
        self.assertTrue(mock_post.call_args.kwargs['json'], {'message': 'Hello world'})

if __name__ == '__main__':
    unittest.main()
