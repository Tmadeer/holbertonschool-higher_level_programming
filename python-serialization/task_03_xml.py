#!/usr/bin/env python3
"""Module for serializing and deserializing a dictionary with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to filename."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Read an XML file and return the deserialized dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
