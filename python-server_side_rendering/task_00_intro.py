#!/usr/bin/python3
""" Creating a templating program for invitations"""
# import os
import logging
import sys

# path = '/home/Holberton/holbertonschool-higher_level_programming/
# python-server_side_rendering/template.txt'
# isExist = os.path.exists(path)


def generate_invitations(template, attendees):
    """ Templating function """
    # Check input types for template & attendees
    if not isinstance(str, template) or not isinstance(dict, attendees):
        sys.exit('neither template nor attendees are the expected data types')

    # remove whitespaces in template.txt
    template_words = template.strip()

    # Check whether template or attendee lists are empty
    if len(template_words) == 0:
        sys.exit('Template is empty, no output files generated.')
    if len(attendees) == 0:
        sys.exit('No data provided, no output files generated.')

    count = 1
    for row in attendees:
        template_copy = template_words

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = ""
            to_replace = "{" + key + "}"

            if key not in row:
                value = "N/A"
            else:
                value = row[key]

            if value == "" or value is None:
                value = "N/A"

            template_copy = template_copy.replace(to_replace, value)

        # write in file
        f = open("output_" + str(count) + ".txt", "a")
        f.write(template_copy)
        f.close()

        count = count + 1
