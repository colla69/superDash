from json import dump,load


def json_save(data, fname):
    with open(fname, 'w') as fp:
        dump(data, fp)


def json_load(fname):
    with open(fname, 'r') as fp:
        return load(fp)
