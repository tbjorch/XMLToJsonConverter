import xml.etree.ElementTree as et
import json


class XMLToJSONConverter:
    """
    Helper class enablind conversion of xml files to json files.
    """

    def convert_xml_to_json(self, xml_file, output_filename=None):
        """
        Takes xml file as input, converts it to json, and creates a
        json file with the same data in json format
        """
        xml = et.parse(xml_file)
        json_array = [self.__get_tag_data(child) for child in xml.getroot()]
        if output_filename is None:
            output_filename = xml_file.split(".")[0]+".json"
        with open(output_filename, "wt") as f:
            f.write(json.dumps(json_array, indent=2, ensure_ascii=False))

    def __get_tag_data(self, xml_element):
        """
        recursive method iterating through xml elements and returning
        data. XML element attributes are extracted as well.
        """
        temp_dict = xml_element.attrib
        if self.__element_has_children(xml_element):
            temp_dict.update({child.tag: self.__get_tag_data(child)
                              for child in xml_element})
            return {xml_element.tag: temp_dict}
        return xml_element.text

    def __element_has_children(self, xml_element):
        return len(list(xml_element)) > 0
