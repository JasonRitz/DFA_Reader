# DFA_Reader
A Program that will confirm if a string is in the language of a specified DFA. The DFA is inputed from a file called DFA.txt and the string to test is input by the user at run time.  




Requires a DFA.txt file to read in that is the DFA. the DFA.txt file here is the test file. To create your own, the format is:

number of states ; comma sep language (a,b,c) ; accepting state(s)
on state, input, goto state, on state, input, goto state....ect
 Description: D = {Q, sigma, delta, q0, F} L(D) = {w|w}
 
 
 
 
 
 
here is an example of the DFA.txt file to input the DFA: 
 
2;a,b;1
0,a,1,0,b,0,1,a,0,1,b,1
D = {2, [0,1], delta, q0, 1}  L(D) = {w|w contains an 0dd number of a's}
