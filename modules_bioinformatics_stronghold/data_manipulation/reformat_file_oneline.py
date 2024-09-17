def readFileReformat(file_path):
    """
    Reads the file and returns a list of lines
    """
    with open(file_path, "r") as f:
        return [i.strip() for i in f.readlines()]
