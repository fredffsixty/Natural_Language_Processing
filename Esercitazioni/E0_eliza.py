#!/usr/bin/env python

import regex as rg

def main():
    
    print("Ciao, sono Eliza, la tua trapista personale!\nParlami dei tuoi problemi\n>>> ",end='')
    
    while True:
        user = input()
        r1 = rg.search(".*([Ss]ono|[Mm]i sento) (molto|tanto|così|) (triste|depress[ao]|stanc[ao]|).*",user)
        r2 = rg.search('.*[Ii]o (sono|mi sento) (molto|tanto|così|) (triste|depress[ao]|stanc[ao]|).*',user)
        
        if(r1):
            print(f"Mi dispiace che tu sia {r1.group(3)}\n>>> ",end='')
        elif(r2):
            print(f"Perché pensi di essere {r1.group(3)}?\n>>> ",end='')
        elif(rg.match('.*tutt[ie].*',user)):
            print("In che modo?\n>>> ",end='')
        elif(rg.match('.*sempre.*',user)):
            print("Mi puoi fare un esempio specifico?\n>>> ",end='')
        else:
            print("Dimmi di più ...\n>>> ",end='')


if __name__ == "__main__":
    main()