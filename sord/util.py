from collections import defaultdict


def group_items(items, identifiers):
    hashes = defaultdict(list)
    for item, id_ in zip(items, identifiers, strict=True):
        hash_ = hash(item)
        hashes[hash_].append(id_)
    return hashes


def file_contents(paths):
    for p in paths:
        with open(p, 'rb') as f:
            yield f.read()
