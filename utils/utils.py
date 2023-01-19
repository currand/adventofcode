def get_input(filename, no_strip=False):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        if no_strip:
            return [line for line in lines]
        else:
            return [line.strip() for line in lines]