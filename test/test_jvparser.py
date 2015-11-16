
math_exp = '4+5*6'


def make_list(m_exp):
    # Create a variable for converting the math expression string
    # into a list.
    exp_list = []

    # This option will check whether the start of the expression
    # is negative/minus sign.
    if m_exp[0] == '-':
        tmp_str = '-'
        m_exp = m_exp[1:]
    else:
        tmp_str = ''

    # Loop through the math expression string and append the newly
    # created list above.
    for idx in range(len(m_exp)):
        if math_exp[idx] in '0123456789.':
            tmp_str += m_exp[idx]
        elif math_exp[idx] in '*/+-':
            if tmp_str == '':
                if exp_list[-1] == '*':
                    exp_list = exp_list[:-1]
                    exp_list.append('**')
                elif exp_list[-1] == '/':
                    exp_list = exp_list[:-1]
                    exp_list.append('//')
            else:
                exp_list.append(tmp_str)
                exp_list.append(math_exp[idx])
                tmp_str = ''
    exp_list.append(tmp_str)

    return exp_list


def test_make_list():
    assert make_list(math_exp) == ['4', '+', '5', '*', '6']
