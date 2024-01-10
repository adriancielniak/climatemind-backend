import unittest
import requests

class TestLogout(unittest.TestCase):
    BASE_URL = "http://localhost:5000/logout"
    HEADERS = {'Accept': 'application/json', 'Authorization': 'Bearer 123', 'Content-Type': 'application/json'}

    def test_successful_logout(self):
        # Assuming 'Bearer 123' is a valid token
        response = requests.post(self.BASE_URL, headers=self.HEADERS)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "User logged out")

    def test_logout_with_invalid_token(self):
        # Simulating a logout request with an invalid token
        invalid_headers = {'Accept': 'application/json', 'Authorization': 'Bearer InvalidToken', 'Content-Type': 'application/json'}
        response = requests.post(self.BASE_URL, headers=invalid_headers)
        # The expected response might differ based on how your backend handles invalid tokens during logout
        self.assertNotEqual(response.status_code, 200)

    # Additional tests can be added for other scenarios, like already logged out users, etc.

if __name__ == '__main__':
    unittest.main()
