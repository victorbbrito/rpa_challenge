class Person:
    """
    A class to represent a person.

    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        company_name (str): The name of the company where the person works.
        address (str): The address of the person.
        email (str): The email address of the person.
        role (str): The role or job title of the person within the company.
        phone (str): The phone number of the person.
    """
    def __init__(self, first_name:str, last_name:str, company_name:str, address:str, email:str, role:str, phone:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.email = email
        self.role = role
        self.phone = phone
    
    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_company_name(self) -> str:
        return self.company_name
    
    def get_address(self) -> str:
        return self.address
    
    def get_email(self) -> str:
        return self.email
    
    def get_role(self) -> str:
        return self.role

    def get_phone(self) -> str:
        return self.phone
    

