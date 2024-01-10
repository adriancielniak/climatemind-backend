import unittest
import requests
###########################################################################################
######           Remember to input data below          ####################################
###########################################################################################

correctemail = #input
correctpassword = #input

class TestLogin(unittest.TestCase):
    BASE_URL = "http://localhost:5000/login"
    HEADERS = {'Accept': 'application/json', 'Authorization': 'Bearer 123', 'Content-Type': 'application/json'}

    def test_successful_login(self):
        payload = {
            "email": correctemail,
            "password": correctpassword
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    def test_incorrect_credentials(self):
        payload = {
            "email": "wrong@example.com",
            "password": "wrongPassword"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 200)


    def test_missing_credentials1(self):
        payload = {
            "email": correctemail
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 200)

    def test_missing_credentials2(self):
        payload = {
            "password": correctpassword
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
