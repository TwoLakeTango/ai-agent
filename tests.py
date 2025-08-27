"""test cases for functions.get_file_info

from functions.get_files_info import get_files_info

print("Result for current directory:")
print(get_files_info("calculator", "."))

print("Result for current directory:")
print(get_files_info("calculator", "pkg"))

print("Result for current directory:")
print(get_files_info("calculator", "/bin"))

print("Result for current directory:")
print(get_files_info("calculator", "../"))"""

"""test cases for functions.get_file_content

from functions.get_file_content import get_file_content
print(get_file_content("calculator", "lorem.txt"))

from functions.get_file_content import get_file_content
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
"""

"""test cases for functions.write_file"""
from functions.write_file import write_file

print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))