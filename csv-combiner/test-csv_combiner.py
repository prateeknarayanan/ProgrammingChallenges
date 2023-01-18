#Libraries used
import unittest
import sys
from csv_combiner import CSV_Combiner
from io import StringIO

#Test class
class TestCombineMethods(unittest.TestCase):
    #Variables used for unit testing
    csv = "./csv_combiner.py"
    accessories = "./fixtures/accessories.csv"
    clothing = "./fixtures/clothing.csv"
    household_cleaners = "./fixtures/household_cleaners.csv"
    fake = "./fixtures/fake.csv"
    empty = "./fixtures/empty.csv"
    combiner = CSV_Combiner()

    #Set up in order to get output
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    #Test with no path
    def test_no_paths(self):
        argv = [self.csv]
        self.combiner.combine_files(argv)
        self.assertIn("Error: No file-path input", self.output.getvalue())

    #Test with a non-existent path
    def test_non_existent(self):
        argv = [self.csv, self.fake]
        self.combiner.combine_files(argv)
        self.assertIn("Error: file path does not exist", self.output.getvalue())

    #Test with one file path
    def test_one_file(self):
        argv = [self.csv, self.accessories]
        self.combiner.combine_files(argv)
        self.assertIn("accessories.csv", self.output.getvalue())

    #Test with multiple file paths
    def test_multiple_files(self):
        argv = [self.csv, self.accessories, self.clothing]
        self.combiner.combine_files(argv)
        self.assertIn("clothing.csv", self.output.getvalue())

    #Test with a path leading to an empty file
    def test_empty_file(self):
        argv = [self.csv, self.empty]
        self.combiner.combine_files(argv)
        self.assertIn("This file is empty", self.output.getvalue())

    
        

    

