import readline
HELP_MESSAGE = "Type \\h to open the help message, \\p to edit the previous line (write mode only), and \\s to save and close the file."
EDIT_MESSAGE = "Type \\e to edit the current line or anything else to continue."
class FileIterator:
    """
    An iterator that yields every time a line is written to the file.
    """
    def __init__(self, file_obj):
        self.file_obj = file_obj
        self.line_count = 1
        print(HELP_MESSAGE)

    def __iter__(self):
        while True:
            status = "line {0}:".format(self.line_count)
            next_line = input(status)
            if next_line == "\\h":
                print(HELP_MESSAGE)
                continue
            elif next_line == "\\p":
                self.file_obj.seek(previous_line_location, 0)
                self.line_count -= 1
                continue
            elif next_line == "\\s":
                raise StopIteration
            previous_line_location = self.file_obj.tell()
            self.file_obj.write(next_line + "\n")
            yield
            self.line_count += 1

class FileReviewer:
    """
    An iterator for going through the existing file.
    See if you can implement the feature of adding new lines,
    not just modifying the existing lines!
    """
    def __init__(self, file_obj):
        self.file_obj = file_obj
        print(EDIT_MESSAGE)

    def __iter__(self):
        new_file = ""
        for line in self.file_obj.readlines():
            print(line)
            command = input("?")
            if command == "\\e":
                new_line = input("Edited line:")
                new_file = new_file + new_line + "\n"
                yield
                continue
            else:
                new_file = new_file + line
                yield
                continue
        with open(self.file_obj.name, "w") as f:
            f.write(new_file)
        raise StopIteration

