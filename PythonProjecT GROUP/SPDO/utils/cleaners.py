def remove_duplicates(data):
    seen = set()
    new_data = []
    for d in data:
        if d['email'] not in seen:
            seen.add(d['email'])
            new_data.append(d)
    return new_data

def remove_empty(data):
    return [d for d in data if d['name'] != ""]