
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.

class IdValidatorTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('validate')

    def test_validate_with_valid_data(self):
        response = self.client.post(self.url,{
            'id': "25601011234567"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),3)
        self.assertEqual(response.status_code,200)

        self.assertEqual(response_data.get("gender"),"Female")
        self.assertEqual(response_data.get("governorate"),"Daqahliya")
        self.assertEqual(response_data.get("birth_date"),"1956-01-01")

    def test_validate_with_invalid_century(self):
        response = self.client.post(self.url,{
            'id': "95601011234567"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"id should start with 2 or 3")

    def test_validate_with_invalid_length(self):
        response = self.client.post(self.url,{
            'id': "2560101"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"id length should be 14 numbers")

    def test_validate_with_chars_id(self):
        response = self.client.post(self.url,{
            'id': "256010112hello"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"id should contain numbers only")
    
    def test_validate_with_invalid_white_space(self):
        response = self.client.post(self.url,{
            'id': "256010112345 7"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"id shouldn't contain spaces")

    def test_validate_with_invalid_month(self):
        response = self.client.post(self.url,{
            'id': "25618011234547"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"Month should be between 1 and 12")

    def test_validate_with_invalid_governorate(self):
        response = self.client.post(self.url,{
            'id': "25601017834567"
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"Wrong Governorate")

    def test_validate_with_invalid_birth_date_in_future(self):
        response = self.client.post(self.url,{
            'id': "35601011234567"
        })
        response_data = response.json()

        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"Birth date shouldn't be in the future")

    def test_validate_with_invalid_params(self):
        response = self.client.post(self.url,{
        })
        response_data = response.json()
        self.assertEqual(len(response_data),1)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data.get("error"),"id can't be blank")