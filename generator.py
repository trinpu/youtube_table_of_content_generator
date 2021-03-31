import csv
import codecs

def open_csv(file_path:str):
    """Opens up csv file and returns a list"""
    file_contents = csv.reader(codecs.open(file_path, mode='r', encoding="utf-16"))
    file_lines = list(file_contents)
    content_list = [line[0].split("\t") for line in file_lines]
    content_list = [line[:6] for line in content_list]       
    return content_list

def extract_details(content_list:list):
    """ Returns a list of details for table of contents"""
    table_of_contents_list = [[line[2], line[0]] for line in content_list[1:]]
    return table_of_contents_list

def format_time(unformatted_list:list):
    """ Returns a list with correct format for time"""

    # -- Alternative solution
    # formatted_list = []
    # for line in unformatted_list:
    #     time_stamp_length = len(line[0])
    #     time_stamp = line[0][:time_stamp_length - 3]
    #     section_name = line[1]
    #     formatted_list.append([time_stamp, section_name])

    formatted_list = []
    delimiter = ":"
    for line in unformatted_list:
        time_stamp_elements = line[0].split(delimiter)
        time_stamp = delimiter.join(time_stamp_elements[:3])
        section_name = line[1]
        formatted_list.append([time_stamp, section_name])

    return formatted_list

def create_table_of_contents(formatted_list:list):
    """ Generate table of contents forom list and returns new file contents """

    with open("table_of_contents.txt", mode="w") as table_of_contents:
        table_of_contents.write("TABLE OF CONTENTS\n")
        table_of_contents.write("\n")
        for line in formatted_list:
            line_contents = " ".join(line)
            table_of_contents.write(line_contents + "\n")

    with open("table_of_contents.txt", mode="rt") as table_of_contents:
        file_contents = table_of_contents.read()

    return file_contents

def create_table_from_file(file_name:str):
    content_list = open_csv(file_name)
    table_of_contents_list = extract_details(content_list)
    table_of_contents_formatted = format_time(table_of_contents_list)
    file_contents = create_table_of_contents(table_of_contents_formatted)
    return file_contents

