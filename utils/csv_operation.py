import csv


class HandleCSV:
    filename = "C:\\Users\\hi\\PycharmProjects\\Hr_connect\\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            csv_file = csv.DictReader(foo)
            # for j in csv_file:
            #     print(dict(j))
        return csv_file

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            for line in csv.DictReader(bar):
                yield line





s = HandleCSV()
s.read_entire_csv()
s.read_csv_line_by_line()