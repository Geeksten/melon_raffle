class Customer(object):
    """A customer at Ubermelon."""

    # using init we can set instance attributes at class creation time

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode
