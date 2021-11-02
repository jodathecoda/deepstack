import os
import sys
import re

#start = "CARDS"
start = "Hand"
flop =  "FLOP"
turn =  "TURN"
river = "RIVER"
end =   "SUMMARY"
dealt = "Dealt"
collected = "collected"
seat = "Seat"

checks = "checks"
posts =  "posts"
calls =  "calls"
bets =   "bets"
raises = "raises"
folds =  "folds"

actions = []
actions.append(start)
actions.append(flop)
actions.append(turn)
actions.append(river)
actions.append(posts)
actions.append(calls)
actions.append(bets)
actions.append(raises)
actions.append(folds)
actions.append(checks)
actions.append(dealt)
actions.append(collected)


global cwd
cwd = os.getcwd()

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

if os.name == 'posix':
    pass

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

pl = 0
history = []
index = 0

incognito = 0
if len(sys.argv) > 1:
    if sys.argv[1] == 'i':
        #incognito mode
        incognito = 1

incognito = 1

if incognito:
    print("1-33")
else:
    print("1 bachmann.juergen")
    print("2 bos.alexander")
    print("3 dmit.pol")
    print("4 eshkar.eyal")
    print("5 freire.gaia")
    print("6 gavin.fintan")
    print("7 indenok.sergey")
    print("8 islam.jefri")
    print("9 laak.phil")
    print("10 lesnoy.dmitry")
    print("11 moschitta.luca")
    print("12 naumenko.igor")
    print("13 okearney.dara")
    print("14 parlavecchio.antonio")
    print("15 pastor.juan_manuel")
    print("16 phan.mike")
    print("17 pizzarello.silvio")
    print("18 qin.youwei")
    print("19 santos.victor")
    print("20 schaumann.lucas")
    print("21 schwab.sebastian")
    print("22 sethi.muskan")
    print("23 shabalin.ivan")
    print("24 shaposhnikov.roman")
    print("25 shrimankar.prakshat")
    print("26 sturc.martin")
    print("27 sun.fan")
    print("28 sun.kaishi")
    print("29 takeda.tsuneaki")
    print("30 talacka.giedrius")
    print("31 tishekvich.stas")
    print("32 voloshin.stanislav")
    print("33 zurr.shai")
try:
    pl = int(input("choose number: "))
except:
    print("enter number 1-33")

if pl > 0 and pl < 34:
    pass
else:
    print("error file number")
    sys.exit()
hero = ""
villain = "DeepStack"
villain_nickname = "deep.stack"
if pl == 1:
    hero = "bachmann.juergen"
    f = open(cwd + '\\full_info\\all_hands.bachmann.juergen.log',"r")
elif pl == 2:
    hero = "bos.alexander"
    f = open(cwd + '\\full_info\\all_hands.bos.alexander.log',"r")
elif pl == 3:
    hero = "dmit.pol" 
    f = open(cwd + '\\full_info\\all_hands.dmit.pol.log',"r")
elif pl == 4:
    hero = "eshkar.eyal"
    f = open(cwd + '\\full_info\\all_hands.eshkar.eyal.log',"r")
elif pl == 5:
    hero = "freire.gaia" 
    f = open(cwd + '\\full_info\\all_hands.freire.gaia.log',"r")
elif pl == 6:
    hero = "gavin.fintan" 
    f = open(cwd + '\\full_info\\all_hands.gavin.fintan.log',"r")
elif pl == 7:
    hero = "indenok.sergey"
    f = open(cwd + '\\full_info\\all_hands.indenok.sergey.log',"r")
elif pl == 8:
    hero = "islam.jefri"
    f = open(cwd + '\\full_info\\all_hands.islam.jefri.log',"r")
elif pl == 9:
    hero = "laak.phil"
    f = open(cwd + '\\full_info\\all_hands.laak.phil.log',"r")
elif pl == 10:
    hero = "lesnoy.dmitry"
    f = open(cwd + '\\full_info\\all_hands.lesnoy.dmitry.log',"r")
elif pl == 11:
    hero = "moschitta.luca"
    f = open(cwd + '\\full_info\\all_hands.moschitta.luca.log',"r")
elif pl == 12:
    hero = "naumenko.igor"
    f = open(cwd + '\\full_info\\all_hands.naumenko.igor.log',"r")
elif pl == 13:
    hero = "okearney.dara"
    f = open(cwd + '\\full_info\\all_hands.okearney.dara.log',"r")
elif pl == 14:
    hero = "parlavecchio.antonio"
    f = open(cwd + '\\full_info\\all_hands.parlavecchio.antonio.log',"r")
elif pl == 15:
    hero = "pastor.juan_manuel"
    f = open(cwd + '\\full_info\\all_hands.pastor.juan_manuel.log',"r")
elif pl == 16:
    hero = "phan.mike"
    f = open(cwd + '\\full_info\\all_hands.phan.mike.log',"r")
elif pl == 17:
    hero = "pizzarello.silvio"
    f = open(cwd + '\\full_info\\all_hands.pizzarello.silvio.log',"r")
elif pl == 18:
    hero = "qin.youwei"
    f = open(cwd + '\\full_info\\all_hands.qin.youwei.log',"r")
elif pl == 19:
    hero = "santos.victor"
    f = open(cwd + '\\full_info\\all_hands.santos.victor.log',"r")
elif pl == 20:
    hero = "schaumann.lucas"
    f = open(cwd + '\\full_info\\all_hands.schaumann.lucas.log',"r")
elif pl == 21:
    hero = "schwab.sebastian"
    f = open(cwd + '\\full_info\\all_hands.schwab.sebastian.log',"r")
elif pl == 22:
    hero = "sethi.muskan"
    f = open(cwd + '\\full_info\\all_hands.sethi.muskan.log',"r")
elif pl == 23:
    hero = "shabalin.ivan"
    f = open(cwd + '\\full_info\\all_hands.shabalin.ivan.log',"r")
elif pl == 24:
    hero = "shaposhnikov.roman"
    f = open(cwd + '\\full_info\\all_hands.shaposhnikov.roman.log',"r")
elif pl == 25:
    hero = "shrimankar.prakshat"
    f = open(cwd + '\\full_info\\all_hands.shrimankar.prakshat.log',"r")
elif pl == 26:
    hero = "sturc.martin"
    f = open(cwd + '\\full_info\\all_hands.sturc.martin.log',"r")
elif pl == 27:
    hero = "sun.fan"
    f = open(cwd + '\\full_info\\all_hands.sun.fan.log',"r")
elif pl == 28:
    hero = "sun.kaishi"
    f = open(cwd + '\\full_info\\all_hands.sun.kaishi.log',"r")
elif pl == 29:
    hero = "takeda.tsuneaki"
    f = open(cwd + '\\full_info\\all_hands.takeda.tsuneaki.log',"r")
elif pl == 30:
    hero = "talacka.giedrius"
    f = open(cwd + '\\full_info\\all_hands.talacka.giedrius.log',"r")
elif pl == 31:
    hero = "tishekvich.stas"
    f = open(cwd + '\\full_info\\all_hands.tishekvich.stas.log',"r")
elif pl == 32:
    hero = "voloshin.stanislav"
    f = open(cwd + '\\full_info\\all_hands.voloshin.stanislav.log',"r")
elif pl == 33:
    hero = "voloshin.stanislav"
    f = open(cwd + '\\full_info\\all_hands.zurr.shai.log',"r")
else:
    pass
   
hand_lines = []
counter_lines = 0   
for line in f:
    history.append(line)
f.close()

line_counter = 0
counter_hands = 0
action_points = []
for current_line in history:
    if start in current_line:
        counter_hands += 1
    tokens = current_line.split()
    for act in actions:
        if act in tokens and seat not in tokens:
            #print(current_line)
            action_points.append(current_line)
    line_counter += 1
            
print("number of hands: " + str(counter_hands))
marker = 0
current = action_points[marker]
clear_it = 0
pot = 0
back = 0
while(True):
    but_press = input("]")
    if clear_it:
        clearscreen()
        clear_it = 0
        pot = 0
    else:
        pass
    if but_press == "b" and marker > 0:
        marker -= 1
        back = 1
        current = action_points[marker]
    elif marker <= len(action_points):
        marker += 1
        back = 0
        current = action_points[marker]
    else:
        pass
    print("pot: " + str(pot))
    print(current)
    if posts in current or raises in current or bets in current or calls in current:
        tokens = current.split()
        potential_bet = 0
        found_bet = 0
        #for t in tokens[::-1]:     REVERSE ORDER
        #for t in tokens:
        for t in tokens[::-1]:
            if found_bet:
                break
            print(re.findall('\d+', t))
            isthis_bet = re.findall('\d+', t)
            for potential_bet in isthis_bet:
                if potential_bet.isdigit():
                    if back:
                        pot -= int(potential_bet)
                    else:
                        pot += int(potential_bet)
                    found_bet = 1
    if start in current:
        clear_it = 1


