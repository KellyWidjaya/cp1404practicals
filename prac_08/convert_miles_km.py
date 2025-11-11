"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Kelly Widjaya, IT@JCU
Started 10/11/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKm(App):
    """ ConvertMilesKm is a Kivy App to convert miles to kilometres """
    output_label = StringProperty('54.717')

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Handle calculation, output result to label widget """
        value = float(self.root.ids.input_miles.text)
        result = value * MILES_TO_KM
        self.output_label = str(result)

    def handle_increment(self, change):
        """
        Handle up/down button, update the text input with new value, call calculation function
        """
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

ConvertMilesKm().run()