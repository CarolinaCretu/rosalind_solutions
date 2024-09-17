def readFileSimple(file_path):
    """
    Read a simple txt file
    """
    with open(file_path, "r") as f:
        return f.readline().rstrip("\n")
