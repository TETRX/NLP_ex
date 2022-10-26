import os

def load_bill(path):
    with open(path, "r") as bill_file:
        return bill_file.read()

def load_all_bills(corpus_directory = 'corpus'):
    bills = {}
    for filename in os.listdir(corpus_directory):
        path = os.path.join(corpus_directory, filename)
        # checking if it is a file
        if os.path.isfile(path):
            bills[filename]=load_bill(path)
    return bills