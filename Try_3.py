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
    assert len(s)==3, '��������� ������� �����������'
    assert s[2].isdigit(), '��������� ������� �� �������� ������'
    assert s[0].isdigit(), '������ ������� �� �������� ������'
    assert s[1] in d, '������ �������� �� ��������������'
    try:
        return print(d[s[1]](int(s[0]), int (s[2])))
    except ZeroDivisionError:
        print ('������� �� ����')

x=input()
calc(x)
        