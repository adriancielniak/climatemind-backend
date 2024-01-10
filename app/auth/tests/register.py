import unittest
import requests
###########################################################################################
######           Remember to input data into payload          #############################
###########################################################################################


class TestUserRegistration(unittest.TestCase):
    BASE_URL = "http://localhost:5000/register"
    HEADERS = {'Accept': 'application/json', 'Authorization': 'Bearer 123', 'Content-Type': 'application/json'}

    def test_successful_registration(self):
        payload = {
            "firstName": "Name",
            "lastName": Surname",
            "email": "NameSurname@example.com",
            "password": "PassWord7!",
            "quizId": "96f180d7-1355-4839-a09e-ec0b34f42387"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Successfully created user")

    def test_registration_with_missing_fields(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "testds1c1@example.com"
            # Missing password and quizId
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_with_existing_email(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "testds1c1@example.com",
            "password": "PassWord7!",
            "quizId": "96f180d7-1355-4839-a09e-ec0b34f42387"
        }
        # Assuming this email already exists in the system
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

def test_registration_with_invalid_email(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "invalidemail",
            "password": "PassWord7!",
            "quizId": "uniquequizid"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_with_weak_password(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "testemail@example.com",
            "password": "weak",
            "quizId": "uniquequizid"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_with_duplicate_quizId(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "newemail@example.com",
            "password": "PassWord7!",
            "quizId": "96f180d7-1355-4839-a09e-ec0b34f42387"  # Assuming this quizId is already used
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_with_special_characters_in_names(self):
        payload = {
            "firstName": "test@123",
            "lastName": "bunny!#",
            "email": "emailwithspecialchar@example.com",
            "password": "PassWord7!",
            "quizId": "uniquequizid"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_with_long_input_values(self):
        payload = {
            "firstName": "test" * 100,
            "lastName": "bunny" * 100,
            "email": "verylongemail@example.com",
            "password": "PassWord7!",
            "quizId": "uniquequizid"
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_registration_without_authorization_header(self):
        payload = {
            "firstName": "test",
            "lastName": "bunny",
            "email": "email@example.com",
            "password": "PassWord7!",
            "quizId": "uniquequizid"
        }
        response = requests.post(self.BASE_URL, json=payload)  # No headers included
        self.assertNotEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
