#Libraries used
import pandas as pd
import os
import sys

#Object oriented in order to unit test
class CSV_Combiner:
    #Function to test if given file path is valid
    @staticmethod
    def validate_paths(argv):
        #Checks for input
        if len(argv) <= 1:
            print("Error: No file-path input")
            return False
        filepaths = argv[1:]
        for filepath in filepaths:
            #Checks if file path exists
            if not os.path.exists(filepath):
                print("Error: file path does not exist: " + filepath)
                return False
            #Checks if the file is empty
            if os.stat(filepath).st_size == 0:
                print("This file is empty " + filepath)
                return False
        return True

    #Function to read from different CSV files and write to output CSV file
    def combine_files(self, argv):
        #Variables for how many rows to read at once and storing input
        chunksize = 10 ** 6
        chunks = []
        #Calls helper function to see if file path is valid
        if self.validate_paths(argv):
            filepaths = argv[1:]
            for filepath in filepaths:
                for chunk in pd.read_csv(filepath, chunksize=chunksize):
                    filename = os.path.basename(filepath)
                    chunk['filename'] = filename
                    chunks.append(chunk)
            #Print the column name only once
            header = True
            for chunk in chunks:
                print(chunk.to_csv(index=False, header=header, line_terminator='\n', chunksize=chunksize))
                header = False
        else:
            return
            
#Calls the function to read CSV files and write to output
def main():
    combiner = CSV_Combiner()
    combiner.combine_files(sys.argv)

if __name__ == '__main__':
    main()
    
