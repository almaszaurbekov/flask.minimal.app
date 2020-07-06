class Vacancy():
    def __init__(self, id, name, area, salary, address, published_at, created_at, url, snippet):

        self.name, self.id = name, id
        self.published_at, self.created_at, self.url  = published_at, created_at, url
        self.area_name = self.__try_set_value___(area, 'name')
        self.area_url = self.__try_set_value___(area, 'url')
        self.salary_from = self.__try_set_value___(salary, 'from')
        self.salary_to = self.__try_set_value___(salary, 'to')
        self.salary_currency = self.__try_set_value___(salary, 'currency')
        self.address_city = self.__try_set_value___(address, 'city')
        self.address_street = self.__try_set_value___(address, 'street')
        self.address_lat = self.__try_set_value___(address, 'lat')
        self.address_lng = self.__try_set_value___(address, 'lng')
        self.snippet_requirement = self.__try_set_value___(snippet, 'requirement')
        self.snippet_responsibility = self.__try_set_value___(snippet, 'responsibility')

    def __try_set_value___(self, object, key):
        try:
            result = object[key]
            return result
        except:
            return None

    def serialize(self):
        return {
            "name" : self.name,
            "address" : self.address_city,
            "published_at" : self.published_at,
            "created_at" : self.created_at,
            "url" : self.url
        }