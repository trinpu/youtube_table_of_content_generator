from sys import argv
from generator import create_table_from_file

script_name, marker_file_name = argv
create_table_from_file(marker_file_name)