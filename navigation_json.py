"""The program that works with user's inputs like a navigation in file(JSON)."""
import json


def main():
    """
    The main function that executes all another functions.
    """
    print("Hi, there!\nNow, you are in the program-navigator.")
    print("If you want to stop the execution of the program please write: exit.")
    data = reading_the_file()
    work_with_data(data)
    return ""


def reading_the_file(path="info.json"):
    """
    The function that reads the JSON file and returns the content of it.
    >>> type(reading_the_file())
    <class 'dict'>
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def work_with_data(info):
    """
    One of the main function that checks data and it's data.
    According to the type of info, makes needed job. Moreover, the function
    launches the function for the input.
    >>> work_with_data("I LOVE PYTHON!")
    I LOVE PYTHON!
    """
    try:
        if type(info) == dict:
            print("It is dictionary object.\n\
You can choose one of the following items that you need:")
            for each in info.keys():
                print(" -->", each)
            return work_with_data(info[str(user_input())])
        if type(info) == list:
            lengh_list = len(info)
            print("it is iterative object. Write down the num from 0 to", lengh_list - 1)
            return work_with_data(info[int(user_input())])
        if type(info) == int or type(info) == str:
            print(info)
            return
        if type(info) == bool:
            print(info)
            return
    except (ValueError, TypeError, KeyError, IndexError):
        print("Please pay attention. Write down again correctly.")
        return work_with_data(info)


def user_input():
    """
    The function that takes the information from user input and returns it.
    If the user's input is 'exit' the program will stop the program.
    """
    user_data = input(" >>> ")
    if user_data == "":
        print("Please pay attention. Write down again correctly.")
        return user_input()
    if user_data == "exit":
        exit()
    else:
        return user_data


if __name__ == "__main__":
    main()
