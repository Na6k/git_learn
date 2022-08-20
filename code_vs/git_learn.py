'''
this function branch from developer
'''
class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + ' ' + self.last_name
        self.inicial = self.first_name[:1] + '.' + self.last_name[:1] + '.'
              
