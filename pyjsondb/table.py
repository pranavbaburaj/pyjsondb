from .db import *
import os
import json


class Table():
    def __init__(self, table_name):
        self.table_name = str(table_name).replace(" ", "_")
        self.create_new_table()
        self.dictionary = {}
        self.all_fields = ""
        self.id_ = 1

    def create_new_table(self):
        if isinstance(self.table_name, str):
            for index, files in enumerate(folder_name):
                if f"{self.table_name}.json" in os.listdir(files):
                    raise Exception(f"Database already exists")
                else:
                    self.file_ = os.path.join(files, f"{self.table_name}.json")
                    with open(self.file_, "w") as file_to_write:
                        file_to_write.write("")
                    databases.append(self.file_)
                    return True
        else:
            raise Exception(f"Table name should be a string")
    def set_fields(self, fields):
        assert isinstance(fields, list) == True

        self.all_fields = fields

    def commit(self):
        
        with open(self.file_, "w") as file__:
            json.dump(self.dictionary, file__, indent=6)
 
    def add(self, data):
        assert isinstance(data, list) == True
        new_dict = {}
        if self.all_fields:
            assert len(self.all_fields) <= len(data), f"Data Overflow [data more than the fields]"
            for element in range(len(self.all_fields)):
                new_dict[str(self.all_fields[element])] = data[element]
        else:
            raise Exception(f"Fields should be set before adding items (set_fields(field:list))")
        self.dictionary[str(self.id_)] = new_dict
        self.id_ += 1
        self.commit()

    def all(self):
        return self.dictionary

    def remove_by_id(self, filter_id):
        filter_id = str(filter_id)
        assert filter_id <= str(self.id_), f"Id {filter_id} does not exists"
        del self.dictionary[str(filter_id)]
        self.commit()

        return True

    def delete(self, data):
        assert isinstance(data, tuple) == True, "data should be a tuple after filter"
        self.remove_by_id(str(data[0]))

    def filter_by(self, match):
        data = []
        assert isinstance(match, dict) == True, f"Expected a dict"
        for index in self.dictionary:
            # print(self.dictionary[str(index)])
            for keys in self.dictionary[str(index)]:
                # data.append(self.dictionary[index])
                if keys in match:
                    if self.dictionary[str(index)][str(keys)] == match[str(keys)]:
                        data.append((index, self.dictionary[str(index)]))
        return data

    def __repr__(self):
        return str(self.table_name)
        