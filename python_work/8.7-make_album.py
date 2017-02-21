# coding: utf-8


def make_album(name, album_name, miusc_num=''):
    person = {'name': name, 'album': album_name}

    if miusc_num:
        person['num'] = miusc_num

    return person

misucian1 = make_album('xd', 'wxyh', 5)
misucian2 = make_album('xd', 'aaaa', 59)
misucian3 = make_album('xd', 'cccc')

print misucian1
print misucian2
print misucian3
