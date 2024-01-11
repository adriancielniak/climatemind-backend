import unittest
import requests

class TestCreateConversationInvite(unittest.TestCase):
    BASE_URL = "http://localhost:5000/create-conversation-invite"
    AUTH_HEADER = {'Authorization': 'Bearer 123', 'Content-Type': 'application/json'}

    def test_create_conversation_invite_success(self):
        """ Test creating conversation invite with valid data """
        payload = {"invitedUserName": "Jim Bob"}
        response = requests.post(self.BASE_URL, headers=self.AUTH_HEADER, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("invitedUserName", response.json())
        self.assertEqual(response.json()["invitedUserName"], "Jim Bob")

    def test_create_conversation_invite_no_auth_header(self):
        """ Test creating conversation invite without authorization header """
        payload = {"invitedUserName": "Jim Bob"}
        response = requests.post(self.BASE_URL, json=payload)
        self.assertNotEqual(response.status_code, 200)

    def test_create_conversation_invite_invalid_user_name(self):
        """ Test creating conversation invite with invalid user name """
        payload = {"invitedUserName": ""}
        response = requests.post(self.BASE_URL, headers=self.AUTH_HEADER, json=payload)
        self.assertNotEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
