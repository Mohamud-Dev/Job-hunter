
class Hiring:
    '''
    Article class to define Movie Objects
    '''

    def __init__(self,id,location,language):
        self.id = id
        self.location=location
        self.language = language

class Jobs:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,title,company,type,url,location,description,time):
        self.id = id
        self.title = title
        self.company = company
        self.url = url
        self.location = location
        self.description = description
        self.time = time
   

       
        