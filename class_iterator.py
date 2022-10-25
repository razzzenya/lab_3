import csv
import datetime
import os


class DateIterator:

    def __init__(self, path):

        self.counter = 0
        self.file_name = path

    def __next__(self) -> tuple:

        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))

                if self.counter == len(reader_object):
                    raise StopIteration

                elif self.counter < len(reader_object):
                    self.counter += 1
                    output = (reader_object[self.counter - 1][0], reader_object[self.counter - 1][1], reader_object[self.counter - 1][2],
                                reader_object[self.counter - 1][3], reader_object[self.counter - 1][4], reader_object[self.counter - 1][5], reader_object[self.counter - 1][6])
                    return output
        else:
            raise FileNotFoundError


class DateIteratorFromXY:

    def __init__(self, path_to_x: str , path_to_y: str):

        self.counter = 0
        self.X = path_to_x
        self.Y = path_to_y

    def __next__(self) -> tuple:

        if os.path.exists(self.X) and os.path.exists(self.Y):

            with open(self.X, 'r', encoding='utf-8') as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))

            if self.counter == len(reader_object):
                raise StopIteration

            elif self.counter < len(reader_object):
                self.counter += 1
                with open(self.X, 'r', encoding='utf-8') as csvfilex:

                    reader_object_X = list(
                        csv.reader(csvfilex, delimiter=","))
                    date = reader_object_X[self.counter][0]

                with open(self.Y, 'r', encoding='utf-8') as csvfiley:

                    reader_object_Y = list(
                        csv.reader(csvfiley, delimiter=","))
                    output = (date, reader_object_Y[self.counter - 1][0], reader_object_Y[self.counter - 1][1], reader_object_Y[self.counter - 1]
                                [2], reader_object_Y[self.counter - 1][3], reader_object_Y[self.counter - 1][4], reader_object_Y[self.counter - 1][5])
                    return output
            else:
                raise FileNotFoundError


class DateIteratorFromWeeks:
    def __init__(self, path: str):

        self.file_name = path
        self.counter = 0
        self.data = []

        if os.path.exists(self.file_name):

            for root, dirs, files in os.walk(self.file_name):
                for file in files:

                    with open(os.path.join(self.file_name, file), 'r', encoding='utf-8') as csvfile:
                        dates = list(csv.reader(csvfile, delimiter=","))

                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:

        if self.counter == len(self.data):
            raise StopIteration

        elif self.counter < len(self.data):
            self.counter += 1
            output = (self.data[self.counter - 1][0], self.data[self.counter - 1][1], self.data[self.counter - 1][2],
                        self.data[self.counter - 1][3], self.data[self.counter - 1][4], self.data[self.counter - 1][5], self.data[self.counter - 1][6])
            return output


class DateIteratorFromYears:
    def __init__(self, path: str):

        self.file_name = path
        self.counter = 0
        self.data = []

        if os.path.exists(self.file_name):

            for root, dirs, files in os.walk(self.file_name):
                for file in files:

                    with open(os.path.join(self.file_name, file), 'r', encoding='utf-8') as csvfile:
                        dates = list(csv.reader(csvfile, delimiter=","))

                        for i in range(len(dates)):
                            self.data.append(dates[i])
        else:
            raise FileNotFoundError

    def __next__(self) -> tuple:

        if self.counter == len(self.data):
            raise StopIteration

        elif self.counter < len(self.data):
            self.counter += 1
            output = (self.data[self.counter - 1][0], self.data[self.counter - 1][1], self.data[self.counter - 1][2],
                        self.data[self.counter - 1][3], self.data[self.counter - 1][4], self.data[self.counter - 1][5], self.data[self.counter - 1][6])
            return output


# obj = DateIterator()
# while True:
#     print(next(obj))

# obj = DateIteratorFromWeeks()
# while True:
#     print(next(obj))

# obj = DateIteratorFromYears()
# while True:
#     print(next(obj))

# obj = DateIteratorFromXY()
# while True:
#     print(next(obj))
