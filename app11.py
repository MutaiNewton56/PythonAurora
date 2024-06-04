import os

import platform

def print_system_info():
    cpu_count=os.cpu_count()
    os_type=platform.system()

    print(f"Numbner of cpu cores: {cpu_count}")
    print(f"OS: {os_type}")

print_system_info()