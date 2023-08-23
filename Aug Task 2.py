import re

class EmailValidator:
    def __init__(self, filename="email_list.txt"):
        self.pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.filename = filename

    def is_valid_email(self, email):
        return re.match(self.pattern, email)

    def display_stored_emails(self):
        with open(self.filename, "r+") as rd:
            stored_emails = [i.strip() for i in rd.readlines()]
            print(f"Stored Emails: {stored_emails}" if stored_emails else "There are no emails in the list.")

    def ask_and_store_emails(self):
        with open(self.filename, "w+") as wt:
            while True:
                user_des = input("Say 'yes' or 'no' : ")
                if user_des == "yes":
                    email = input("Enter an email (type 'exit' to quit): ")
                    if self.is_valid_email(email):
                        wt.writelines([email + '\n'])
                        print("Email added to the file")
                    else:
                        print("Invalid email format. Please try again.")
                        continue
                elif user_des == "no":
                    wt.close()
                    self.display_stored_emails()
                    break

email_validator = EmailValidator()
email_validator.ask_and_store_emails()
