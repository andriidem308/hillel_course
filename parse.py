def parse(query: str) -> dict:
    dct = {}
    if '?' in query:
        query = query.split('?')[1]
        for o in query.split('&'):
            if '=' in o:
                o = o.split('=')
                dct[o[0]] = o[1]
    return dct


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

