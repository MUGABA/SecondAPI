import uuid

class User:

	def __init__(self,user_id, firstname, lastname,othername,email,phone_number,
					username, registered,is_admin):


		self.user_id = user_id
		self.firstname = firstname
		self.lastname = lastname
		self.othername = othername
		self.email = email
		self.phone_number = phone_number
		self.username =  username
		self.registered = registered
		self.is_admin = is_admin


class Incident:

	def __init__(self,incident_type, incident_id,created_by, created_on, 
					status, location, images, videos, comment):


		self.incident_type = incident_type
		self.incident_id = incident_id
		self.created_by = created_by
		self.created_on = created_on
		self.status = status
		self.location = location
		self.images = images
		self.videos = videos
		self.comment = comment