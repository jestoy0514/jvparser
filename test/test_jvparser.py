
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
        if m_exp[idx] in '0123456789.':
            tmp_str += m_exp[idx]
        elif m_exp[idx] in '*/+-':
            if tmp_str == '':
                if exp_list[-1] == '*':
                    exp_list = exp_list[:-1]
                    exp_list.append('**')
                elif exp_list[-1] == '/':
                    exp_list = exp_list[:-1]
                    exp_list.append('//')
            else:
                exp_list.append(tmp_str)
                exp_list.append(m_exp[idx])
                tmp_str = ''
    exp_list.append(tmp_str)

    return exp_list


def showresult(exp_list):
    # Declare the variable result to 0
    result = 0
    # This variable is for temporary storage of values from the
    # calculations.
    tmp_result = ''
    # This is the list of operators the condition has to meet to
    # be able to know whether the loop has to continue or not.
    list_of_operators = ('**', '*', '/', '+', '-', '//')
    while True:
        # Declare a counter variable to count the operators avail.
        # in the list.
        counter = 0
        for elem in exp_list:
            if elem in list_of_operators:
                counter += 1

        # If the varible counter value is equal to zero, it convert
        # the string result to float and check whether the result is
        # a whole number or a decimal and return the result accordingly.
        if counter == 0:
            result = float(exp_list[0])
            if result != 0:
                if (result / int(result)) == 0:
                    result = int(result)
            elif result == 0:
                result = int(result)
            break
        # Else if the counter is greater than zero. Perform the check
        # for operators available and get the index of the elements
        # and operators and perform the calculation and add it into
        # the variable tmp_result.
        if '**' in exp_list:
            pos = exp_list.index('**')
            tmp_result = str(float(exp_list[pos-1])**float(exp_list[pos+1]))
        elif '//' in exp_list:
            pos = exp_list.index('//')
            tmp_result = str(float(exp_list[pos-1])//float(exp_list[pos+1]))
        elif ('*' in exp_list) and ('/' in exp_list):
            pos_mul = exp_list.index('*')
            pos_div = exp_list.index('/')
            if pos_mul < pos_div:
                pos = pos_mul
                tmp_result = str(float(exp_list[pos-1])*float(exp_list[pos+1]))
            else:
                pos = pos_div
                tmp_result = str(float(exp_list[pos-1])/float(exp_list[pos+1]))
        elif '*' in exp_list:
            pos = exp_list.index('*')
            tmp_result = str(float(exp_list[pos-1])*float(exp_list[pos+1]))
        elif '/' in exp_list:
            pos = exp_list.index('/')
            tmp_result = str(float(exp_list[pos-1])/float(exp_list[pos+1]))
        elif ('+' in exp_list) and ('-' in exp_list):
            pos_add = exp_list.index('+')
            pos_sub = exp_list.index('-')
            if pos_add < pos_sub:
                pos = pos_add
                tmp_result = str(float(exp_list[pos-1])+float(exp_list[pos+1]))
            else:
                pos = pos_sub
                tmp_result = str(float(exp_list[pos-1])-float(exp_list[pos+1]))
        elif '+' in exp_list:
            pos = exp_list.index('+')
            tmp_result = str(float(exp_list[pos-1])+float(exp_list[pos+1]))
        elif '-' in exp_list:
            pos = exp_list.index('-')
            tmp_result = str(float(exp_list[pos-1])-float(exp_list[pos+1]))

        # Once the index and tmp_result is known, we have to delete the
        # old entries and replace it with the new tmp_result base on the
        # given index and set the tmp_result to empty string to use again
        # in the calculation.
        del exp_list[pos-1:pos+2]
        exp_list.insert(pos-1, tmp_result)
        tmp_result = ''

    return result


def process_par(m_exp):
    m_exp = m_exp[1:-1]
    new_list = make_list(m_exp)
    result = showresult(new_list)

    return result


def count_par(m_exp):
    count_open = 0
    for idx in range(len(m_exp)):
        if m_exp[idx] == '(':
            count_open += 1
    return count_open


def breakdown_par(m_exp):
    count_open = count_par(m_exp)
    tmp_m_exp = m_exp
    result = 0
    pos_open = 0
    idx = 0
    if count_open > 1:
        while True:
            if count_par(tmp_m_exp) == 1:
                break
            if tmp_m_exp[idx] == '(':
                pos_open = idx
                idx += 1
            elif tmp_m_exp[idx] == ')':
                pos_close = idx
                idx = 0
                tmp_exp = tmp_m_exp[pos_open:pos_close+1]
                if count_par(tmp_exp) > 1:
                    tmp_str = breakdown_par(tmp_exp)
                    tmp_m_exp = tmp_m_exp.replace(tmp_exp, tmp_str, 1)
                elif count_par(tmp_exp) == 1:
                    tmp_str = process_par(tmp_exp)
                    tmp_m_exp = tmp_m_exp.replace(tmp_exp, str(tmp_str), 1)
            else:
                idx += 1
        result = tmp_m_exp
    elif count_open == 1:
        result = m_exp

    return result


def jvparser(str_exp):
    new_list = make_list(str_exp)
    result = showresult(new_list)
    return result


def test_make_list():
    assert make_list(math_exp) == ['4', '+', '5', '*', '6']


def test_showresult():
    assert showresult(['4', '+', '5', '*', '6']) == 34


def test_jvparser():
    assert jvparser(math_exp) == 34


def test_process_par():
    assert process_par("(4+5*3)") == 19


def test_count_par():
    assert count_par('(4+(3*4))') == 2


def test_breakdown_par():
    assert breakdown_par('(4+(3*4))') == '(4+12.0)'

