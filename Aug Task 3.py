import re
import subprocess

class IPValidator:
    def __init__(self, output_file="ip_list.txt"):
        self.pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        self.output_file = output_file

    def is_valid_ip(self, ip):
        return re.match(self.pattern, ip) is not None

    def is_pingable(self, ip):
        try:
            subprocess.check_call(["ping", "-n", "1", ip])
            return True
        except subprocess.CalledProcessError:
            return False

    def validate_and_log(self):
        with open(self.output_file, "w") as file:
            while True:
                ip = input("Provide IP address ('exit' to quit): ")

                if ip == "exit":
                    break

                if self.is_valid_ip(ip):
                    print(f"{ip} is valid")
                    if self.is_pingable(ip):
                        print(f"{ip} is pingable")
                        file.writelines(f"{ip} Valid and Pingable\n")
                    else:
                        print(f"{ip} is valid but not pingable")
                        file.writelines(f"{ip} Valid but Not Pingable\n")
                else:
                    print(f"{ip} is not valid. Skipping...")

ip_validator = IPValidator()
ip_validator.validate_and_log()
