# coding: utf-8


def make_album(name, album_name, miusc_num=''):
    person = {'name': name, 'album': album_name}

    if miusc_num:
        person['num'] = miusc_num

    return person

while True:
    print("\nAny where enter 'q', exit it!")

    like_name = raw_input("\nTell me you like who:")
    if like_name == 'q':
        break

    a_name = raw_input("\nTell me album_name:")
    if a_name == 'q':
        break

    m_num = raw_input("\nTell me miusc_num:")
    if m_num == 'q':
        break

    full_album_name = make_album(like_name, a_name, m_num)
    print(full_album_name)
