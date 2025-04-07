def rep_char(c,n):
    print(c * n)

def draw_line_string(msg1, msg2):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1}')
    print(f' {msg2}')
    rep_char('-', nstr + 2)

a = input('Input his/her name: ')
draw_line_string('Hello '+a+',','Welcome to Seoul.')
