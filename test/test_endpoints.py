import unittest

from api import app

from api.views import incident


class TestApi(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()

		self.test_incident = {"comment" : "This is my comment", \
			"created_by" : 4, "created_on" : "07/02/2019 24:05", \
			"images" : "hey.png", "incident_id" : 1, "incident_type" : "redflag", \
			"location" : "Kampala", "Status" : "drafted", "videos" : "why.mp4"
			}
		self.test_incident2 = {"comment": "This is the patched comment", \
			"created_by": "3", "created_on" : "08/02/2019 36:05", \
			"images": "helo.png", "incident_id": 2, "incident_type": "redflag", \
			"location": "Jinja", "Status": "made", "videos": "helo.mp4"
		}

		self.test_users = {"user_id": 1, "firstname": "Mugaba", "lastname": "Rashid", \
			"othername": "Muhamad", "email": "mgb@gmail.com", "phone_number": "077565", \
			"username": "MUGABAM", "registered": "07/02/2019 47:05", "is_admin": False
		}


	def tearDown(self):
		incident.incident_list, incident.user_list = [],[]

	def test_welcome_message(self):
		response = self.client.get('v1/api/')
		self.assertEqual(response.status_code, 200)
		self.assertIn('Welcome to ireporter', str(response.data))

	def test_empty_incidents_list(self):
		response = self.client.get('v1/api/red-flags')
		self.assertEqual(response.status_code, 200)

	def test_empty_user_list(self):
		response = self.client.get('v1/api/users')
		self.assertEqual(response.status_code, 200)

	def test_register_user(self):
		self.assertEqual(len(incident.fetch_all_users()), 0)
		response = self.client.post('v1/api/users', json = self.test_users)
		self.assertEqual(response.status_code, 201)
		self.assertEqual(len(incident.fetch_all_users()), 1)

	def test_report_incident(self):
		self.assertEqual(len(incident.fetch_all_incidence()), 0)
		response = self.client.post('v1/api/incidents', json =self.test_incident)
		self.assertEqual(response.status_code, 201)
		self.assertEqual(len(incident.fetch_all_incidence()), 1)


if __name__ == '__main__':
	unittest.main()