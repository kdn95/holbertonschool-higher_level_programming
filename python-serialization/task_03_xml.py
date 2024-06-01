#!/usr/bin/python3
"""
Serialization and deserialization
using XML to JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML file"""
    root = ET.Element("data")

    for k, v in dictionary.items():
        child = ET.Element(k)
        child.text = str(v)
        root.append(child)

    tree = ET.ElementTree(root)

    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize from XML to Python dict"""
    tree = ET.parse(filename)
    root = tree.getroot()

    the_dict = {}

    for child in root:
        the_dict[child.tag] = child.text

    return the_dict
