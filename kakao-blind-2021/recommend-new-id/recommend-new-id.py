def solution(new_id):
    allow_char = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '-_.'

    # 1
    new_id = new_id.lower()

    # 2
    new_id = list(
        filter(
            lambda x: x in list(allow_char),
            list(new_id)
        )
    )

    # 3
    tmp = ''
    for index, char in enumerate(new_id):
        if tmp != char:
            tmp = char
        elif char == '.':
            new_id[index] = ''
    new_id = list(filter(lambda x: x != '', new_id))

    # 4
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5
    if len(new_id) < 1:
        new_id = ['a']

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    while len(new_id) < 3:
        new_id.append(new_id[-1])

    return ''.join(new_id)
