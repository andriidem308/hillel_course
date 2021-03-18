def parse_cookie(query: str) -> dict:
    dct = {}
    if query:
        for o in query.split(';'):
            if '=' in o:
                o = o.split('=')
                dct[o[0]] = '='.join(o[1:])

    return dct


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

