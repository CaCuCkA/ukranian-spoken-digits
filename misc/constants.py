import os

class CONST:
    """
    Configuration constants for the Ukranian Audio Digits Recognition.
    """
    __slots__=()
    CSV_PATH =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "labels.csv")
    DATASET_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dataset") 
    DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recordings")
