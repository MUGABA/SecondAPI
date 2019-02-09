from api.models.models import Incident

class Validator:


    def input_fields(self, incident_type, location, status, images, videos, comment): 

        if self.normal_string(incident_type) and self.pure_text(status) and\
        self.pure_text(comment) and self.normal_string(location) and\
        self.normal_string(images) and self.normal_string(videos):
            return [incident_type, location, status, images, videos, comment]
        return


    def pure_text(self, text):

        if self.normal_string(text):
            if text.strip().isalpha() == True:
                return text 

    
    def normal_string(self, text):

        if isinstance(text, str):

            new_text = str(text).strip()
            if not new_text:
                return
            return new_text
        
        else:
            return 

    
    def incident_id(self, number):
        """tthfjbaifghafvajfvvaja """

        if isinstance(number, int):
            if number > 0:
                return number
            else:
                return 
        else:
            return