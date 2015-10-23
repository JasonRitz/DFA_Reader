# Open file and read in DFA
f = open('DFA.txt', 'r')
dfa_info_line = f.readline()
dfa_info_line = dfa_info_line.split(';')
delta_line = f.readline()
delta_line = delta_line.split(',')
description_line = f.readline()
f.close()


number_of_states = int(dfa_info_line[0])
sigma = dfa_info_line[1].split(',')  
accepting_states = dfa_info_line[2] 


x = 0
size = len(delta_line) - 1
delta = [[9,9] for i in range(number_of_states)]
delta_line.reverse()

# Load the 2D array with the delta function. if sigma = (a, b,...z) convert to
# int (1, 2,...,n)
if 'a' in sigma:
    while x < size:
        index_row = int(delta_line.pop())
        convert_char = delta_line.pop()
        index_column = ord(convert_char) - 97
        delta[index_row][index_column] = int(delta_line.pop())
        x+=3

# Else just load the 2D array with the delta function  
else:
    while x < size:
        index_row = int(delta_line.pop())
        index_column = int(delta_line.pop())
        delta[index_row][index_column] = int(delta_line.pop())
        x+=3

# Print DFA description and get string from user input 
current_position = 0
input_string = ""
exit_test = 0
print description_line, '\n'

while (input_string != 'x!'):
    print '\ntest a string from the alphabet ', sigma, '\n'
    input_string = raw_input('Input a string or "!" to number_of_statesuit: ')

    if (input_string == '!'):
        break
    for i in range(0, len(input_string)):
        if (input_string[i] not in sigma):
            exit_test = 1

    if (exit_test == 1):
        print '\nInput is not in the alphabet \n'
        break
    original_input_string = input_string

# if sigma is (a,b,...,z) convert input_string to (0,1,...,n)
    if 'a' in input_string or 'b' in input_string:
        holder = []
        for i in range(len(input_string)):
            holder.append(ord(input_string[i]) - 97)
        input_string = holder



# Run through the DFA machine 
    for i in range(0, len(input_string)):
        current_position = delta[current_position][int(input_string[i])]


# Print Result
    if (str(current_position) in accepting_states):
        print '\nThe string ', original_input_string, ' is in the language\n\n\n'

    else:
        print '\nThe string ', original_input_string, ' is not in the language\n\n\n'

print "\nGood Bye!\n"









