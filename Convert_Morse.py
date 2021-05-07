# this code will convert numbers and Capital letters into morse code:
def convert_morse (code):

     code = code.replace('1',  '.----')#will replace number 1 with the morse code
     code = code.replace('2',  '..---')
     code = code.replace('3',  '...--')
     code = code.replace('4',  '....-')
     code = code.replace('5',  '.....')
     code = code.replace('6',  '-....')
     code = code.replace('7',  '--...')
     code = code.replace('8',  '---..')
     code = code.replace('9',  '----.')
     code = code.replace('0',  '-----')
     code = code.replace('?',  '..--..')

     code = code.replace('A', '.-')
     code = code.replace('B', '-...')
     code = code.replace('C', '-.-.')
     code = code.replace('D', '-..')
     code = code.replace('E', '.')
     code = code.replace('F', '..-.')
     code = code.replace('G', '--.')
     code = code.replace('H', '....')
     code = code.replace('I', '..')
     code = code.replace('J', '.---')
     code = code.replace('K', '-.-')
     code = code.replace('L', '.-..')
     code = code.replace('M', '--')
     code = code.replace('N', '-.')
     code = code.replace('O', '---')
     code = code.replace('P', '.--.')
     code = code.replace('Q', '--.-')
     code = code.replace('R', '.-.')
     code = code.replace('S', '...')
     code = code.replace('T', '-')
     code = code.replace('U', '..-')
     code = code.replace('V', '...-')
     code = code.replace('W', '.--')
     code = code.replace('X', '-..-')
     code = code.replace('Y', '-.--')
     code = code.replace('Z', '--..')

     return code
print("Number and/or Caps (ABC)")
new_code= input("Enter your code:  ") #takes input from a user
#NOTE: the input must be number and/or Capital letter(ABC)

morse = convert_morse(new_code)
print(f"Morse Code: {morse} ") #will print code converted to morse


#This NOT part of the code
Output:
  
Initial code: H E L L O  W O R L D 
Morse Code: .... . .-.. .-.. ---  .-- --- .-. .-.. -.. 
  
Output : 
  
Enter your code:  2332 BAKER STREET
Morse Code: ..---...--...--..--- -....--.-..-. ...-.-...- 
     
Output :

Enter your code:  2 3 5 A B
Morse Code: ..--- ...-- ..... .- -... 
