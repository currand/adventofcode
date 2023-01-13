def get_input(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        return [line.strip() for line in lines]