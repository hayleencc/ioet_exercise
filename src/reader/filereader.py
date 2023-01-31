class fileReader:

    def readFile(path):
        lines = []
        with open(path) as file:
            for line in file:
                lines.append(line.rstrip())

        return lines
