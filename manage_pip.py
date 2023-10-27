import sys
import subprocess

def find_package_match(package: str, packages_version: list) -> list:
    return [match for match in packages_version if (package + "==") in match]

def substring_in_file(substring):
    with open("requirements.txt", 'r') as file:
        lines = file.read()
        if substring in lines:
            return True
        else:
            return False

def write_to_file(substrings):
    with open("requirements.txt", 'a') as file:
        for i in substrings:
            if substring_in_file(i) == False:
                file.write('\n' + i)

def remove_from_file(substrings):
    with open("requirements.txt", 'r') as file:
        lines = file.readlines()

    for i in substrings:
        # delete matching content
        with open("requirements.txt", 'w') as file:
            for line in lines:
                if line.find((i + '==')) != -1:
                    pass
                else:
                    file.write(line)

def run_pip(package):
    subprocess.check_call([sys.executable, '-m', 'pip', package_command[0], package])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('\n')[0] for r in reqs.split()]

    packages = find_package_match(package, installed_packages)
    write_to_file(packages)
    if package_command[0] == 'uninstall':
        remove_from_file(package)

if len(sys.argv) > 2:
    package_command = sys.argv[1:2]
    package_list = sys.argv[2:]
    if package_command[0] == 'install' or package_command[0] == 'uninstall':
        # implement pip as a subprocess:
        for package in package_list:
            run_pip(package)

    else:
        print("install or uninstall command is missing")
else:
    print("Error in command")