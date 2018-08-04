import csv
from os.path import expanduser

__all__ = ["filepath","CSVWriter"]


filepath=expanduser('~')+'/weather.csv'

class CSVWriter(object):

    def __init__(self):
        self.fieldnames=[]

    def write_data(self,**kwargs):
        for key in kwargs.keys():
            self.fieldnames.append(key)

        with open(filepath,'w') as csv_file:
            writer=csv.DictWriter(csv_file,fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow(kwargs)
