class FileReader:

    def read_file(path):
        lines = []
        with open(path) as file:
            for line in file:
                lines.append(line.rstrip())

        return lines