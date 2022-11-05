import colorama  
from colorama import Fore 
class Database: 
    def clas1(): 
        name= input('enter your name : ')
        print(f'hi {name}  let us start the test : ')
        num = 0 
        a= 2 +  2 
        print('Ans.  the folowing question : ')
        print( 'Q1 : 2+ 2  == ')
        b= int(input('enter the result : '))
        if b== 4 : 
            num+=1 
            print(Fore.CYAN, 'right answewr ' )


        else : 
            print( Fore.RED,  'wrong ans....  right asnwer is 4 ')
            num-=1 
        ab = 3 * 2 
        print( ' Q2 . 3 x 2 ? ')
        ba=  int(input('enter the ans.....'))
        if ba == 6 : 
            num+= 1 
            print(Fore.CYAN, 'right answewr ' )
        else: 
            print(Fore.RED, 'wrong ans  , right ans is 6  ')
            num-=  1 
            
        c =   67 
        print( ' Q3 . enter the pronounciation  of 67  ')
        bc=  str(input('enter the ans.....'))
        if bc == 'sixty-seven ' or  bc== 'Sixty-Seven ' or bc == 'Sixty-seven'  : 
            num+= 1 
            print(Fore.CYAN, 'right answewr ' )
        else: 
            print(Fore.RED, 'wrong ans  , right ans is Sixty- Seven   ')
            num-=  1 
        cb =  10 / 2  
        print( ' Q4 . 10 / 2  ? ')
        bv=  int(input('enter the ans.....'))
        if bv == 5 : 
            num+= 1 
            print(Fore.CYAN, 'right answewr ' )
        else: 
            print(Fore.RED, 'wrong ans  , right ans is 5  ')
            num-=  1 
        bx = 101 + 202  
        print( ' Q5 .  if u have  101 choklects and your frined has  202 chocklets , than how much have you two of them : ? ')
        xb=  int(input('enter the ans.....'))
        if xb == 303 : 
            num+= 1 
            print(Fore.CYAN, 'right answewr ' )
        else: 
            print(Fore.RED, 'wrong ans  , right ans is 6  ')
            num-=  1 
        print(' your total number : ' , num )
        if num== 5 : 
            print(Fore.BLUE, 'Excellent : ')
        elif num == 4 : 
            print(Fore.GREEN, 'good ')
        elif num == 3 : 
            print(Fore.LIGHTBLACK_EX , 'normal ')
        else:
            print(Fore.RED ,'such a bad result ') 
               
                
            



        
        

        