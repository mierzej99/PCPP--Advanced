import xml


class TemperatureConverter:
    def convert_celcius_to_fahrenheit(self, celcius):
        return 9/5 * celcius + 32

class ForecastXmlParser:

    def parse(self):
        tree = xml.etree.ElementTree.parse('forecast.xml')
        ET = tree.getroot()
