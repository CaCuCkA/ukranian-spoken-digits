import os
import csv
import shutil
import typing

from misc.constants import CONST


class Initializer:
    def __init__(self, data_path: str) -> None:
        self.__data_path = data_path
    
    
    def initialize_project(self) -> None:
        self.__create_label_table()
        self.__create_dataset_folder()
        self.__extract_recordings()

    
    def __create_label_table(self) -> None:
        """
        Creates a CSV file from two lists: file_paths and labels.
        """
        file_names, labels = self.__collect_file_names_and_labels()
        assert len(file_names) == len(labels), "file_paths and labels lists must have the same length"

        with open(CONST.CSV_PATH, mode='w+', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['file_path', 'label']) 

            for file_name, label in zip(file_names, labels):
                writer.writerow([file_name, label])

    
    def __collect_file_names_and_labels(self) ->typing.Tuple[typing.List[str], typing.List[str]]:
        """
        Collects and returns a list of full paths and labels to files in the given directory and its subdirectories.

        :return: A lists of full paths and labels to each file found.
        """
        file_names = []
        labels = [] 
        for _, _, files in os.walk(self.__data_path):
            for file in files:
                base_name, _ = os.path.splitext(file)
                full_path = os.path.join(CONST.DATASET_PATH, file)
                file_names.append(full_path)
                labels.append(base_name[-1])
        return file_names, labels
    

    def __create_dataset_folder(self) -> None:
        os.mkdir(CONST.DATASET_PATH)


    def __extract_recordings(self) -> None:
        """
        Copies all files from the source directory to the DATASET_PATH, maintaining the directory structure.
        """
        for root, _, files in os.walk(self.__data_path):
            for file in files:
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(CONST.DATASET_PATH, file)
                shutil.copy2(source_file_path, target_file_path)
        