import pandas as pd
from botcity.web import WebBot, By
from person import Person
import glob
import os

def check_download() -> bool:
    """
    Checks if the 'challenge.xlsx' file is in the current directory.
    
    Returns:
        bool: True if the file is found, False otherwise.
    """
    list_files = glob(os.getcwd()+"/*.xlsx")

    for file in list_files:
        if "challenge.xlsx" in file:
            return True
    
    return False

def collect_data(path) -> list:
    """
    Reads an Excel file from the specified path and collects person data into a list of Person objects.

    Args:
        path (str): The file path to the Excel file containing the person data.

    Returns:
        list: A list of Person objects, each created from a row in the Excel file.
    """

    list_persons = []

    data_frame = pd.read_excel(path)

    for i,row in data_frame.iterrows():
        new_person = Person(row['First Name'],
                            row['Last Name '],
                            row['Company Name'],
                            row['Address'],
                            row['Email'],
                            row['Role in Company'],                                               
                            row['Phone Number'])
        
        list_persons.append(new_person)

    return list_persons


def fill_label(label_name:str, person:Person):
    """
    Retrieves the appropriate attribute from a Person object based on the given label name.

    Args:
        label_name (str): The name of the label indicating which attribute to retrieve.
        person (Person): The Person object from which to retrieve the attribute.

    Returns:
        str: The value of the specified attribute from the Person object.
    """

    match label_name:
        case 'labelFirstName':
            return person.get_first_name()
        
        case 'labelLastName':
            return person.get_last_name()
        
        case 'labelCompanyName':
            return person.get_company_name()
        
        case 'labelAddress':
            return person.get_address()
        
        case 'labelEmail':
            return person.get_email()
        
        case 'labelRole':
            return person.get_role()
        
        case 'labelPhone':
            return person.get_phone()


def fill_out_form(bot:WebBot, list_persons:list[Person]):
    """
    Fills out and submits a web form for each Person in the provided list.

    Args:
        bot (WebBot): The WebBot instance used to interact with the web page.
        list_persons (list[Person]): A list of Person objects whose data will be filled into the form.

    Returns:
        None
    """
    submit = bot.find_element("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input", By.XPATH)

    for person in list_persons:
        for i in range(1,8):
            label = bot.find_element(f'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/div/div[{i}]/rpa1-field/div/input', By.XPATH)
            data = fill_label(label.get_attribute("ng-reflect-name"),person)
            label.send_keys(data)

        submit.click()
        bot.wait(2000)
            
    