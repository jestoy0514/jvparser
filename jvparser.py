#!/usr/bin/env python3
#
# jvparser.py - a simple module for calculating mathematical expression.
#
# Copyright (c) 2015 - Jesus Vedasto Olazo - jessie@jvaolazo.net76.net
#

__version__ = '1.0'


class JVParser:

    def __init__(self, num_str):
        self.num_str = num_str

    def makelist(self):
        if self.num_str[0] == '-':
            self.num_str = self.num_str[1:]
            temp_chars = "-"
        else:
            temp_chars = ''
        gen_list = []
        for char in self.num_str:
            if char in '0123456789.':
                temp_chars = temp_chars + char
            elif char in '*/-+':
                if temp_chars != '':
                    gen_list.append(temp_chars)
                    gen_list.append(char)
                    temp_chars = ''
                elif temp_chars == '':
                    if char == '-':
                        if gen_list[-1] == '+':
                            del gen_list[-1:]
                            gen_list.append(char)
                        elif gen_list[-1] == '*' or gen_list[-1] == '/':
                            temp_chars = '-'
                        else:
                            return None
        gen_list.append(temp_chars)
        return gen_list

    def showresult(self):
        #  Convert the string to list for further breakdown.
        mylist = self.makelist()

        if len(mylist) == 1:
            result = float(mylist[0])
            if int(result) != 0:
                if result/int(result) > 1:
                    return result
                elif result/int(result) == 1:
                    return int(result)
            else:
                return result

        #  The oper variable will be used to determine which operator to use in the created sub equation.
        oper = ""
        #  Loop to the mylist to be able to breakdown it into smaller pieces.
        while True:
            counter = 0
            #  Test if the below given operators is available in the sub equation.
            #  If available it will generate the position of the operator and which operator will be using.
            if "*" in mylist and "/" in mylist:
                pos_mul = mylist.index("*")
                pos_div = mylist.index("/")
                if pos_mul < pos_div:
                    pos = pos_mul
                    oper = "mul"
                else:
                    pos = pos_div
                    oper = "div"
            elif "*" in mylist:
                pos = mylist.index("*")
                oper = "mul"
            elif "/" in mylist:
                pos = mylist.index("/")
                oper = "div"
            elif "+" in mylist and "-" in mylist:
                pos_add = mylist.index("+")
                pos_sub = mylist.index("-")
                if pos_add < pos_sub:
                    pos = pos_add
                    oper = "add"
                else:
                    pos = pos_sub
                    oper = "sub"
            elif "+" in mylist:
                pos = mylist.index("+")
                oper = "add"
            elif "-" in mylist:
                pos = mylist.index("-")
                oper = "sub"

            #  Variable for remebering the possiton where the new value will be inserted inside mylist list.
            rem_pos = pos - 1

            #  Operations which will be used in respect to variable oper.
            ans = 0
            if oper == "mul":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 * num2)
            elif oper == "div":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 / num2)
            elif oper == "add":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 + num2)
            elif oper == "sub":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 - num2)

            #  Delete the elements inside mylist to make way
            #  to the newly created result.
            del mylist[pos]
            del mylist[pos]
            del mylist[pos-1]

            #  Insert the result of the operation in mylist.
            mylist.insert(rem_pos, ans)

            #  Loop through the mylist to record the number of operator inside.
            for ind in range(len(mylist)):
                if mylist[ind] in "*/+-":
                    counter += 1

            #  Test whether counter is equal to zero, if yes exit from the loop.
            if counter == 0:
                break

        result = float(mylist[0])

        if int(result) != 0:
            if result/int(result) > 1:
                return result
            elif result/int(result) == 1:
                return int(result)
        else:
            return result


def main():
    given_string = "-6+89*7-65-3*55-6+33/4"
    mparser = JVParser(given_string)
    print('Mathematical Expression: ', given_string)
    print()
    print('JVParser Result: ', mparser.showresult())
    print('Eval Result: ', eval(given_string))

if __name__ == '__main__':
    main()
