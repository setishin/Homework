def calc (s):
    d={
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x//y,
        '%': lambda x,y: x%y,
        '^': lambda x,y: x**y,
    }
    s=s.split()
    assert len(s)==3, 'Выражение введено некорректно'
    assert s[2].isdigit(), 'Последняя позиция не является числом'
    assert s[0].isdigit(), 'Первая позиция не является числом'
    assert s[1] in d, 'Данная операция не поддерживается'
    try:
        return print(d[s[1]](int(s[0]), int (s[2])))
    except ZeroDivisionError:
        print ('Деление на ноль')

x=input()
calc(x)
        