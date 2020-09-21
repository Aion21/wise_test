class Customer:
    def __init__(self, data_list):
        self.customer_ID = data_list[0]
        self.customer_name = data_list[1]
        self.contact_name = data_list[2]
        self.address = data_list[3]
        self.city = data_list[4]
        self.postal_code = data_list[5]
        self.country = data_list[6]

    def __str__(self) -> str:
        return f'|customer_ID:{self.customer_ID} ' \
               f'|customer_name:{self.customer_name} ' \
               f'|contact_name:{self.contact_name} ' \
               f'|address:{self.address} ' \
               f'|city:{self.city} ' \
               f'|postal_code:{self.postal_code} ' \
               f'|country:{self.country} '

    def __eq__(self, other):
        if isinstance(other, Customer):
            return (self.customer_ID == other.customer_ID and
                    self.customer_name == other.customer_name and
                    self.contact_name == other.contact_name and
                    self.address == other.address and
                    self.city == other.city and
                    self.postal_code == other.postal_code and
                    self.country == other.country)

        return NotImplemented
