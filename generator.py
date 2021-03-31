import csv
import codecs

def open_csv(file_path:str):
    """Opens up csv file and returns a list"""
    file_contents = csv.reader(codecs.open(file_path, mode='rU', encoding="utf-16"))
    file_lines = list(file_contents)
    content_list = [line[0].split("\t") for line in file_lines]
    content_list = [line[:6] for line in content_list]       
    return content_list

if __name__ == '__main__':
    contents = open_csv("test_data/exports/markers.csv")

