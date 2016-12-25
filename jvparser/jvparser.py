#!/usr/bin/env python3
#
# jvparser.py - a simple module for calculating mathematical expression.
#
# Copyright (c) 2015 - Jesus Vedasto Olazo - jessie@jvaolazo.net76.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
A simple mathematical expression parser and return a float or integer
type result.

Ex:

>>> from jvparser.jvparser import solveIt
>>>
>>> math_expression = "45+34-3/5*103"
>>>
>>> solveIt(math_exression)

"""

__version__ = '1.4'
__author__ = 'Jesus Vedasto Olazo'
__email__ = 'jessie@jestoy.frihost.net'


def createList(math_exp):
    # Create a variable for converting the math expression string
    # into a list.
    exp_list = []

    # This option will check whether the start of the expression
    # is negative/minus sign.
    if math_exp[0] == '-':
        tmp_str = '-'
        math_exp = math_exp[1:]
    else:
        tmp_str = ''

    # Loop through the math expression string and append the newly
    # created list above.
    for idx in range(len(math_exp)):
        if math_exp[idx] in '0123456789.':
            tmp_str += math_exp[idx]
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


def showResult(exp_list):
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


def processPar(m_exp):
    m_exp = m_exp[1:-1]
    new_list = createList(m_exp)
    result = showResult(new_list)

    return result


def countPar(m_exp):
    count_open = 0
    for idx in range(len(m_exp)):
        if m_exp[idx] == '(':
            count_open += 1
    return count_open


def breakdownPar(m_exp):
    count_open = countPar(m_exp)
    tmp_m_exp = m_exp
    result = 0
    pos_open = 0
    idx = 0
    if count_open > 1:
        while True:
            if countPar(tmp_m_exp) == 1:
                break
            if tmp_m_exp[idx] == '(':
                pos_open = idx
                idx += 1
            elif tmp_m_exp[idx] == ')':
                pos_close = idx
                idx = 0
                tmp_exp = tmp_m_exp[pos_open:pos_close+1]
                if countPar(tmp_exp) > 1:
                    tmp_str = breakdownPar(tmp_exp)
                    tmp_m_exp = tmp_m_exp.replace(tmp_exp, tmp_str, 1)
                elif countPar(tmp_exp) == 1:
                    tmp_str = processPar(tmp_exp)
                    tmp_m_exp = tmp_m_exp.replace(tmp_exp, str(tmp_str), 1)
            else:
                idx += 1
        result = tmp_m_exp
    elif count_open == 1:
        result = m_exp

    return result


def solveIt(str_exp):
    """

    :param str_exp: string

    This is an eval like function that have the capabilities to
    compute small mathematical expressions in a form of a string.
    This was created for the purpose of creating simple calculators.
    The mathematical expression pass through a loop to generate a list
    for further breakdown and calculations until it reach only one
    element in the list and return as a result in either of integer
    type or float type.

    """
    result = 0
    # Check if the beginning of the expression is an open parenthesis.
    if str_exp[0] == '(':
        # Check if the opening parenthesis has been closed at the end
        # of the expression. If yes to if statement.
        if str_exp[-1] == ')':
            result = breakdownPar(str_exp)
            result = processPar(result)
        # Do the elif statement if not.
        elif str_exp[-1] != ')':
            str_exp = '(' + str_exp + ')'
            result = breakdownPar(str_exp)
            result = processPar(result)
    # If the beginning of the expression is not open parenthesis.
    elif str_exp[0] != '(':
        # Check if any parenthesis is available somewhere in the expression.
        if '(' in str_exp:
            str_exp = '(' + str_exp + ')'
            result = breakdownPar(str_exp)
            result = processPar(result)
        # Else will execute if and only if there is no parenthesis available.
        else:
            new_list = createList(str_exp)
            result = showResult(new_list)

    return result


def main():
    #print(__doc__)
    math_expression = "45+34-3/3*103"
    print(math_expression)
    result = solveIt(math_expression)
    print(result)
    print(eval(math_expression))

# Standard Boilerplate Template.
if __name__ == '__main__':
    main()
