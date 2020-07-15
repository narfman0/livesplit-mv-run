import xml.etree.ElementTree as etree

from xml_dataclasses import load, dump

from livesplit_mv_run.models import Run


def parse(path):
    parser = etree.XMLParser()
    root = etree.parse(path, parser).getroot()
    container = load(Run, root, "Run")
    breakpoint()
    print(container.size)


def find_latest_run_number(root):
    """ Scan all attempts in run to find lowest id """
    initial_run = None
    for item in root.findall("AttemptHistory/Attempt"):
        current_run = int(item.attrib["id"])
        if initial_run == None or current_run > initial_run:
            initial_run = current_run
    return initial_run
