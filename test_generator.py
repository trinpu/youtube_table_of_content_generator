# -*- coding: utf8 -*-

import pytest
import generator

def test_open_csv():
    output = [
        ['Marker Name', 'Description', 'In', 'Out', 'Duration', 'Marker Type'],
        ['Section 1', 'Section 1 Description', '00:00:00:00', '00:00:00:00', '00:00:00:00', 'Chapter'],
        ['Section 2', 'Section 2 Description', '00:00:18:26', '00:00:18:26', '00:00:00:00', 'Chapter'],
        ['Section 3', 'Section 3 Description', '00:00:40:29', '00:00:40:29', '00:00:00:00', 'Chapter']
    ]

    assert generator.open_csv("test_data/exports/markers.csv") == output

def test_extract_details():

    input_list = [
        ['Marker Name', 'Description', 'In', 'Out', 'Duration', 'Marker Type'],
        ['Section 1', 'Section 1 Description', '00:00:00:00', '00:00:00:00', '00:00:00:00', 'Chapter'],
        ['Section 2', 'Section 2 Description', '00:00:18:26', '00:00:18:26', '00:00:00:00', 'Chapter']
    ]

    output_list = [
        ['00:00:00:00', 'Section 1'],
        ['00:00:18:26', 'Section 2']
    ]

    assert generator.extract_details(input_list) == output_list

def test_format_time():
    input_list = [
        ['00:00:00:00', 'Section 1'],
        ['00:00:18:26', 'Section 2']
    ]

    output_list = [
        ['00:00:00', 'Section 1'],
        ['00:00:18', 'Section 2']
    ]

    assert generator.format_time(input_list) == output_list