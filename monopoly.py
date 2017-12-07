from random import randint #plugin that makes dice work
from random import shuffle #plugin that makes cc and chance work
#fix any int() w/o try:------------------------------------------------------------------------
name = ['', '', '', '', '', '', '', '', '']
def pregame(): #number and name of players
  i = 0
  while i == 0:
    global num
    global numalive
    try:
      num = int(input())
      if num < 2 or num > 8:
        print('Please select a number between 2 and 8')
      else:
        numalive = num #set number of players still in the game for later
        i = 1
    except:
      print('Please select a number between 2 and 8')
  a = 1
  while a <= num:
    print('Name for player '+str(a)+'?')
    name[a] = input()
    a += 1

injail = [-1, False, False, False, False, False, False, False, False]
tile = [-1, 0, 0, 0, 0, 0, 0, 0, 0]
bal = [-1, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
p = 0
tilename = ['Go', 'Old Kent Road', 'Community Chest', 'Whitechapel Road', 'Income Tax', 'King\'s Cross Staton', 'The Angel Islington', 'Chance', 'Euston Road', 'Pentonville Road', 'Jail', 'Pall Mall', 'Electric Company', 'Whitehall', 'Northumrl\'d Avenue', 'Marylebone Station', 'Bow Street', 'Community Chest', 'Marlborough Street', 'Vine Street', 'Free Parking', 'Strand', 'Chance', 'Fleet Street', 'Trafalgar Square', 'Fenchurch Station', 'Leicester Square', 'Conventry Street', 'Water Works', 'Piccadilly', 'Go To Jail', 'Regent Street', 'Oxford Street', 'Community Chest', 'Bond Street', 'Liverpool St. Station', 'Chance', 'Park Lane', 'Super Tax', 'Mayfair']
pricebuy = [-1, 60, -1, 60, -1, 200, 100, -1, 100, 120, -1, 140, 150, 140, 160, 200, 180, -1, 180, 200, -1, 220, -1, 220, 240, 200, 260, 260, 150, 280, -1, 300, 300, -1, 320, 200, -1, 350, -1, 400]
ownedby = [-1, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0]
rentprice = [-1, -1, -1, -1, -1, -1, 2, 10, 30, 90, 160, 250, -1, -1, -1, -1, -1, -1, 4, 20, 60, 180, 360, 450, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 30, 90, 270, 400, 550, -1, -1, -1, -1, -1, -1, 6, 30, 90, 270, 400, 550, 8, 40, 100, 300, 450, 600, -1, -1, -1, -1, -1, -1, 10, 50, 150, 450, 625, 750, -1, -1, -1, -1, -1, -1, 10, 50, 150, 450, 625, 750, 12, 60, 180, 500, 700, 900, -1, -1, -1, -1, -1, -1, 14, 70, 200, 550, 750, 950, -1, -1, -1, -1, -1, -1, 14, 70, 200, 550, 750, 950, 16, 80, 220, 600, 800, 1000, -1, -1, -1, -1, -1, -1, 18, 90, 250, 700, 875, 1050, -1, -1, -1, -1, -1, -1, 10, 90, 250, 700, 875, 1050, 20, 100, 300, 750, 925, 1100, -1, -1, -1, -1, -1, -1, 22, 110, 330, 800, 975, 1150, 22, 110, 330, 800, 975, 1150, -1, -1, -1, -1, -1, -1, 22, 120, 360, 850, 1025, 1200, -1, -1, -1, -1, -1, -1, 26, 130, 390, 900, 1100, 1275, 26, 130, 390, 900, 1100, 1275, -1, -1, -1, -1, -1, -1, 28, 150, 450, 1000, 1200, 1400, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 35, 175, 500, 1100, 1300, 1500, -1, -1, -1, -1, -1, -1, 50, 200, 600, 1400, 1700, 2000]
numhouse = [-1, 0, -1, 0, -1, -1, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, -1, -1, 0, -1, 0]
rrprice = [0, 25, 50, 100, 200]
ccorder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
shuffle(ccorder)
ccn = 0
chanceorder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
shuffle(chanceorder)
chancen = 0
ccname = ['Advance to Go (Collect $200)', 'Bank error in your favor\nCollect $200', 'Doctor\'s fee\nPay $50', 'From sale of stock you get $50', 'Get Out of Jail Free', 'Go to Jail\nGo directly to jail\nDo not pass Go\nDo not collect $200', 'Grand Opera Night\nCollect $50 from every player for opening night seats', 'Holiday Fund matures\nReceive $100', 'Income tax refund\nCollect $20', 'It is your birthday\nCollect $10', 'Life insurance matures\nCollect $100', 'Pay hospital fees of $100', 'Pay school fees of $150', 'Receive $25 consultancy fee', 'You are assessed for street repairs\n$40 per house\n$115 per hotel', 'You have won second prize in a beauty contest\nCollect $10', 'You inherit $100']
chancename = ['Advance to Go (Collect $200)', 'Advance to Illinois Ave\nIf you pass Go, collect $200.', 'Advance to St. Charles Place\nIf you pass Go, collect $200', 'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.', 'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.', 'Bank pays you dividend of $50', 'Get Out of Jail Free', 'Go Back 3 Spaces', 'Go to Jail\nGo directly to Jail\nDo not pass Go\nDo not collect $200', 'Make general repairs on all your property\nFor each house pay $25\nFor each hotel $100', 'Pay poor tax of $15', 'Take a trip to Reading Railroad\nIf you pass Go, collect $200', 'Take a walk on the Boardwalk\nAdvance token to Boardwalk', 'You have been elected Chairman of the Board\nPay each player $50', 'Your building and loan matures\nCollect $150', 'You have won a crossword competition\nCollect $100']
ismortgaged = [-1, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0]
mortgageprice = [-1, 50, -1, 50, -1, 100, 50, -1, 50, 60, -1, 70, 75, 70, 80, 100, 90, -1, 90, 100, -1, 110, -1, 110, 120, 100, 140, 140, 75, 150, -1, 200, 200, -1, 200, 100, -1, 175, -1, 200]
tenmortgageprice = [-1, 55, -1, 55, -1, 110, 55, -1, 55, 66, -1, 77, 83, 77, 88, 110, 99, -1, 99, 110, -1, 121, -1, 121, 132, 110, 154, 154, 83, 165, -1, 220, 220, -1, 220, 110, -1, 188, -1, 220]
houseprice = [-1, 30, -1, 30, -1, -1, 50, -1, 50, 50, -1, 100, -1, 100, 100, -1, 100, -1, 100, 100, -1, 150, -1, 150, 150, -1, 150, 150, -1, 150, -1, 150, 150, -1, 150, -1, -1, 200, -1, 200]
goojf = [-1, 0, 0, 0, 0, 0, 0, 0, 0]
alive = [-1, True, True, True, True, True, True, True, True]
jailturn = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

def monopolytest(t,test):
  pga = [1, 6, 11, 16, 21, 26, 31, 37]
  pgb = [3, 8, 13, 18, 23, 27, 32, 39]
  pgc = [3, 9, 14, 19, 24, 29, 34, 39]
  if test == 'm':
    for i in range(7):
      if bool(bool(t == pga[i] or t == pgb[i] or t == pgc[i]) and bool(ownedby[pga[i]] == ownedby[pgb[i]] == ownedby[pgc[i]]) and bool(ownedby[pga[i]] != 0)):
        return True
    return False
  elif test == 'h':
    for i in range(7):
      if bool(bool(t == pga[i] or t == pgb[i] or t == pgc[i]) and bool(bool(numhouse[pga[i]] != 0) or bool(numhouse[pgb[i]] != 0) or bool(numhouse[pgc[i]]) != 0) and bool(ownedby[pga[i]] != 0)):
        return True
    return False
  return False

def clear(): #just prints lots of blank lines
  for x in range(40):
    print('')

def trade():
  clear()
  print('Select the player you want to trade with')
  a = 1
  monp = 0
  monn = 0
  jp = 0
  jn = 0
  tradeidp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  tradeidn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ptotrade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ntotrade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  while a < 9:
    if a <= num:
      if a == p or not alive[a]:
        a += 1
        continue
      else:
        print(str(a)+' '+name[a])
        a += 1
        continue
    else:
      a += 1
      continue
  i = 0
  while i != 1:
    try:
      tradep = int(input())
      if 1 <= tradep <= num and tradep != p and alive[tradep] == True:
        i = 1
      else:
        print('Select one of the options')
        continue
    except:
      print('Select one of the options')
  a = 0
  pti = 1
  while a < 40:
    if ownedby[a] == p and numhouse[a] == 0:
      tradeidp[pti] = a
      pti += 1
    a += 1
  while i == 1:
    clear()
    print('id sel name')
    a = 1
    while a < pti:
      if ptotrade[tradeidp[a]] == 1:
        print(str(a)+'  +   '+tilename[tradeidp[a]])
      else:
        print(str(a)+'      '+tilename[tradeidp[a]])
      a += 1
    print('$'+str(monp))
    if jp == 1:
      print(str(jp)+' get out of jail free card')
    else:
      print(str(jp)+' get out of jail free cards')
    print('')
    print('Type the number of the properties you want to give, "m" to give money, "j" to give get out of jail free cards, and "d" when you are done')
    t = input()
    try:
      if 0 < int(t) < pti and ptotrade[tradeidp[int(t)]] == 0:
        ptotrade[tradeidp[int(t)]] = 1
        continue
      elif 0 < int(t) < pti and ptotrade[tradeidp[int(t)]] == 1:
        ptotrade[tradeidp[int(t)]] = 0
        continue
      else:
        pass
    except ValueError:
      if t == 'm':
        print('How much money? You have $'+str(bal[p]))
        monp = int(input())
        if monp > bal[p]:
          monp = 0
        continue
      elif t == 'd':
        i = 2
        continue
      elif t == 'j':
        print('How many? You have '+str(goojf[p]))
        jp = int(input())
        if jp > goojf[p]:
          jp = 0
        continue
      else:
        continue
  a = 0
  nti = 1
  while a < 40:
    if ownedby[a] == tradep and numhouse[a] == 0:
      tradeidn[nti] = a
      nti += 1
    a += 1
  while i == 2:
    clear()
    print('id sel name')
    a = 1
    while a < nti:
      if ntotrade[tradeidn[a]] == 1:
        print(str(a)+'  +   '+tilename[tradeidn[a]])
      else:
        print(str(a)+'      '+tilename[tradeidn[a]])
      a += 1
    print('$'+str(monn))
    if jn == 1:
      print(str(jn)+' get out of jail free card')
    else:
      print(str(jn)+' get out of jail free cards')
    print('')
    print('Type the number of the properties you want to take, "m" to take money, "j" to take get out of jail free cards, and "d" when you are done')
    t = input()
    try:
      if 0 < int(t) < nti and ntotrade[tradeidn[int(t)]] == 0:
        ntotrade[tradeidn[int(t)]] = 1
        continue
      elif 0 < int(t) < nti and ntotrade[tradeidn[int(t)]] == 1:
        ntotrade[tradeidn[int(t)]] = 0
        continue
      else:
        pass
    except ValueError:
      if t == 'm':
        print('How much money? You have $'+str(bal[tradep]))
        monn = int(input())
        if monn > bal[tradep]:
          monn = 0
        continue
      elif t == 'd':
        i = 3
        continue
      elif t == 'm':
        print('How many? You have '+str(goojf[tradep]))
        jn = int(input())
        if jn > goojf[tradep]:
          jn = 0
        continue
      else:
        continue
  clear()
  print('Confirm with y or quit with n')
  print('')
  print('You will give:')
  a = 1
  while a < pti:
    if ptotrade[tradeidp[a]] == 1:
      print(tilename[tradeidp[a]])
    a += 1
  print('$'+str(monp))
  if jp == 1:
    print(str(jp)+' get out of jail free card')
  else:
    print(str(jp)+' get out of jail free cards')
  print('')
  print('You will get:')
  a = 1
  while a < nti:
    if ntotrade[tradeidn[a]] == 1:
      print(tilename[tradeidn[a]])
    a += 1
  print('$'+str(monn))
  if jn == 1:
    print(str(jn)+' get out of jail free card')
  else:
    print(str(jn)+' get out of jail free cards')
  print('')
  while i == 3:
    a = input()
    if str(a) == 'y':
      i = 4
    elif str(a) == 'n':
      i = 10
    else:
      print('Select y or n')
      continue
  if i == 4:
    clear()
    print(name[tradep]+'\'s turn!')
    print(name[p]+' would like to trade with you! Here is their offer')
    print('Accept with y or deny with n')
    print('')
    print('You will get:')
    a = 1
    while a < pti:
      if ptotrade[tradeidp[a]] == 1:
        print(tilename[tradeidp[a]])
      a += 1
    print('$'+str(monp))
    if jp == 1:
      print(str(jp)+' get out of jail free card')
    else:
      print(str(jp)+' get out of jail free cards')
    print('')
    print('You will give:')
    a = 1
    while a < nti:
      if ntotrade[tradeidn[a]] == 1:
        print(tilename[tradeidn[a]])
      a += 1
    print('$'+str(monn))
    if jn == 1:
      print(str(jn)+' get out of jail free card')
    else:
      print(str(jn)+' get out of jail free cards')
    print('')
    while i == 4:
      a = input()
      if str(a) == 'y':
        i = 5
        continue
      elif str(a) == 'n':
        i = 10
        continue
      else:
        print('Select y or n')
        continue
  if i == 5:
    bal[p] += monn
    bal[tradep] += monp
    bal[p] -= monp
    bal[tradep] -= monn
    goojf[p] += jn
    goojf[tradep] += jp
    goojf[p] -= jp
    goojf[tradep] -= jn
    a = 0
    while a < pti: 
      if ptotrade[tradeidp[a]] == 1:
        ownedby[tradeidp[a]] = tradep
      a += 1
    a = 0
    while a < nti:
      if ntotrade[tradeidn[a]] == 1:
        ownedby[tradeidn[a]] = p
      a += 1
  print('Back to '+name[p]+'\'s turn!')
  
def roll(): #dice roll code callable
  global d1
  global d2
  d1 = randint(1,6)
  d2 = randint(1,6)
  if d1 == d2:
    print(name[p]+' rolled a '+str(d1)+' and a '+str(d2)+', Doubles!')
  else:
    print(name[p]+' rolled a '+str(d1)+' and a '+str(d2))

def jail():
  print(name[p]+' is in jail!')
  if jailturn[p] == -1:
    jailturn[p] = 0
  jailturn[p] += 1
  if goojf[p] > 0:
    if jailturn[p] == 4:
      print('Your 3 turns in jail are up. Type "b" to post bail, or "g" to use your "Get Out of Jail Free" card.')
    else:
      print('Type "r" to roll, "b" to post bail, or "g" to use your "Get Out of Jail Free" card.')
  else:
    if jailturn[p] == 4:
      print('Your 3 turns in jail are up. You have to type "b" to post bail.')
    else:
      print('Type "r" to roll or "b" to post bail.')
  choice = input()
  jr = 0
  while jr == 0:
    if choice == 'r' and not jailturn[p] == 4:
      roll()
      if d1 == d2:
        print('You rolled out of jail.')
        jailturn[p] = -1
        injail[p] = False
        land()
        jr = 1
      else:
        print('Sorry, not doubles')
        jr = 1
    elif choice == 'r' and jailturn[p] == 4:
      print('Select one of the options.')
    elif choice == 'b' and bal[p] >= 50:
      bal[p] -= 50
      print('You posted bail. You now have $'+str(bal[p]))
      jailturn[p] = -1
      injail[p] = False
      roll()
      land()
      jr = 1
    elif choice == 'b' and bal[p] < 50:
      print('You cannot afford bail, you only have $'+str(bal[p]))
    elif choice == 'g' and goojf[p] > 0:
      goojf[p] -= 1
      print('You used your get out of jail free card.')
      jailturn[p] = -1
      injail[p] = False
      roll()
      land()
      jr = 1
    else:
      print('Select one of the options.')

def debt():
  while bal[p] < 0:
    print('You are in debt. You have $'+str(bal[p])+'.')
    print('Select an option to get out of debt:')
    print('t: Trade')
    print('m: Mortgage')
    print('h: Sell Houses')
    print('g: Give up')
    choice = input()
    if choice == 't':
      trade()
    elif choice == 'm':
      mortgage()
    elif choice == 'h':
      house()
    elif choice == 'g':
      a = 0
      while a == 0:
        print('Are you sure? (y/n)')
        choice = input()
        if choice == 'y':
          a = 1
          for i in range(40):
            if ownedby[i] == p:
              ownedby[i] = 0
              numhouse[i] = 0
              ismortgaged[i] = 0
          alive[p] = False
          print(name[p]+' is now out of the game.')
        elif choice == 'n':
          a = 1
        else:
          print('Select one of the options')
    else:
      print('Select one of the options')
  print('You are now out of debt. You now have $'+str(bal[p]))

def mortgage():
  clear()
  mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  mi = 1
  for a in range(40):
    if ownedby[a] == p and numhouse[a] <= 0:
      mid[mi] = a
      mi += 1
  i = 0
  clear()
  while i == 0:
    a = 1
    print('id isM price name')
    while a < mi:
      if monopolytest(a,'h') == False:
        if ismortgaged[mid[a]] == 1:
          print('{:2}   + {:5d} {}'.format(a,mortgageprice[mid[a]],tilename[mid[a]]))
        else:
          print('{:2}     {:5d} {}'.format(a,mortgageprice[mid[a]],tilename[mid[a]]))
      a += 1
    t = input()
    try:
      t = int(t)
      if 0 < t < mi:
        if ismortgaged[mid[t]] == 0:
          print('Mortgage '+tilename[mid[t]]+' for $'+str(mortgageprice[mid[t]])+'? (y/n) You have $'+str(bal[p]))
          a = 0
          while a == 0:
            responce = input()
            if responce == 'y':
              bal[p] += mortgageprice[mid[t]]
              ismortgaged[mid[t]] = 1
              clear()
              print('You now have $'+str(bal[p]))
              a = 1
            elif responce == 'n':
              clear()
              a = 1
            else:
              print('Select y or n')
        else:
          if bal[p] >= tenmortgageprice[mid[t]]:
            print('Unmortgage '+tilename[mid[t]]+' for $'+str(tenmortgageprice[mid[t]])+'? (y/n) You have $'+str(bal[p])+'. ($'+str(mortgageprice[mid[t]])+' + 10% interest)')
            a = 0
            while a == 0:
              responce = input()
              if responce == 'y':
                ismortgaged[mid[t]] = 0
                bal[p] -= tenmortgageprice[mid[t]]
                clear()
                print('You now have $'+str(bal[p]))
                a = 1
              elif responce == 'n':
                clear()
                a = 1
              else:
                print('Select y or n')
          else:
            clear()
            print('You cannot afford the $'+str(tenmortgageprice[mid[t]])+' it would take to unmortgage that. You only have $'+str(bal[p]))
      else:
        clear()
        print('Select one of the options')
    except ValueError:
      if t == 'd':
        clear()
        i = 1
      else:
        clear()
        print('Select one of the options')

def house():
  clear()
  hid = [0, 0, 0, 0, 0, 0, 0, 0]
  hs = [1, 6, 11, 16, 21, 26, 31, 37]
  for x in hs:
    if monopolytest(x, 'm'):
      pass

def cc():
  global ccn
  print('Your card reads:\n'+ccname[ccorder[ccn]])
  if ccorder[ccn] == 0:
    tile[p] = 0
    bal[p] += 200
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 1:
    bal[p] += 200
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 2:
    bal[p] -= 50
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 3:
    bal[p] += 50
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 4:
    goojf[p] += 1
    if goojf[p] == 1:
      print('You now have '+str(goojf[p])+' get out of jail free card.')
    else:
      print('You now have '+str(goojf[p])+' get out of jail free cards.')
  elif ccorder[ccn] == 5:
    tile[p] = 10
    injail[p] = True
  elif ccorder[ccn] == 6:
    bal[p] += 50*numalive
    for i in range(1,num+1):
      if alive[i]:
        bal[i] -= 50
        print(name[i]+' now has $'+str(bal[i]))
  elif ccorder[ccn] == 7 or ccorder[ccn] == 10 or ccorder[ccn] == 16:
    bal[p] += 100
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 8:
    bal[p] += 20
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 9 or ccorder[ccn] == 15:
    bal[p] += 10
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 11:
    bal[p] -= 100
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 12:
    bal[p] -= 150
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 13:
    bal[p] += 25
    print('You now have $'+str(bal[p]))
  elif ccorder[ccn] == 14:
    housepay(40, 115)
  ccn += 1
  if ccn > 16:
    shuffle(ccorder)
    ccn = 0

def chance(): 
  global chancen
  print('Your card reads:\n'+chancename[chanceorder[chancen]])
  if chanceorder[chancen] == 0:
    tile[p] = 0
    bal[p] += 200
    print('You now have $'+str(bal[p]))
  elif chanceorder[chancen] == 1:
    if tile[p] > 24:
      bal[p] += 200
      print('You passed go, you now have $'+str(bal[p]))
    tile[p] = 24 
    cchanceland()
  elif chanceorder[chancen] == 2:
    if tile[p] > 11:
      bal[p] += 200
      print('You passed go, you now have $'+str(bal[p]))
    tile[p] = 11
    cchanceland()
  elif chanceorder[chancen] == 3:
    if tile[p] <= 12:
      tile[p] = 12
    elif 12 < tile[p] <= 28:
      tile[p] = 28
    else:
      bal[p] += 200
      print('You passed go, you now have $'+str(bal[p]))
      tile[p] = 12 
    print('You are now at '+name[tile[p]])
    if ownedby[tile[p]] == 0 and bal[p] >= pricebuy[tile[p]]:
      print('Would you like to buy '+tilename[tile[p]]+' for $'+str(pricebuy[tile[p]])+'? (y/n) You have $'+str(bal[p])+'.')
      a = 0
      while a == 0:
        response = input()
        if response == 'y': #buy property
          bal[p] -= pricebuy[tile[p]]
          ownedby[tile[p]] = p
          print(name[p]+' now owns '+tilename[tile[p]]+' and has $'+str(bal[p]))
          a = 1
        elif response == 'n': #pass on property
          a = 1
        else:
          print('Please select y or n')
          continue
    elif ownedby[tile[p]] == 0 and bal[p] < pricebuy[tile[p]]:
      print('You cannot afford '+tilename[tile[p]]+', you only have $'+str(bal[p])+' of $'+str(pricebuy[tile[p]])+'.')
    elif ownedby[tile[p]] == p: #player is owner
      print('You own this property already.')
    elif ismortgaged[tile[p]] == 1:
      print('This property is mortgaged.')
    elif ownedby[tile[p]] > 0: #pay rent
      roll()
      bal[p] -= ((d1 + d2)*10)
      bal[ownedby[tile[p]]] += ((d1 + d2)*10)
      print('You paid $'+str((d1 + d2)*10)+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
  elif chanceorder[chancen] == 4:
    if tile[p] <= 5:
      tile[p] = 5
    elif tile[p] <= 15:
      tile[p] = 15
    elif tile[p] <= 25:
      tile[p] = 25
    elif tile[p] <= 35:
      tile[p] = 35
    else:
      bal[p] += 200
      print('You passed go, you now have $'+str(bal[p]))
      tile[p] = 5
    print('You are now at '+tilename[tile[p]])
    rr = 0
    if ownedby[tile[5]] == ownedby[tile[p]]:
      rr += 1
    if ownedby[tile[15]] == ownedby[tile[p]]:
      rr += 1
    if ownedby[tile[25]] == ownedby[tile[p]]:
      rr += 1
    if ownedby[tile[35]] == ownedby[tile[p]]:
      rr += 1
    bal[p] -= rrprice[rr]
    bal[ownedby[tile[p]]] += rrprice[rr]
    print('You paid $'+str(rrprice[rr])+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
  elif chanceorder[chancen] == 5:
    bal[p] += 50
    print('You now have $'+str(bal[p]))
  elif chanceorder[chancen] == 6:
    if goojf[p] == 1:
      print('You now have '+str(goojf[p])+' get out of jail free card.')
    else:
      print('You now have '+str(goojf[p])+' get out of jail free cards.')
  elif chanceorder[chancen] == 7:
    tile[p] -= 3
    landnd()
  elif chanceorder[chancen] == 8:
    tile[p] = 10
    injail[p] = True
  elif chanceorder[chancen] == 9:
    housepay(25, 100)
  elif chanceorder[chancen] == 10:
    bal[p] -= 15
    print('You now have $'+str(bal[p]))
  elif chanceorder[chancen] == 11:
    if tile[p] > 5:
      bal[p] += 200
      print('You passed go, you now have $'+str(bal[p]))
    tile[p] = 5
    rr = 0
    if ownedby[5] == ownedby[tile[p]]:
      rr += 1
    if ownedby[15] == ownedby[tile[p]]:
      rr += 1
    if ownedby[25] == ownedby[tile[p]]:
      rr += 1
    if ownedby[35] == ownedby[tile[p]]:
      rr += 1
    bal[p] -= rrprice[rr]
    bal[ownedby[tile[p]]] += rrprice[rr]
    print('You paid $'+str(rrprice[rr])+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
  elif chanceorder[chancen] == 12:
    tile[p] = 39
    cchanceland()
  elif chanceorder[chancen] == 13:
    bal[p] -= 50*numalive
    for i in range(1,num+1):
      if alive[i]:
        bal[i] += 50
        print(name[i]+' now has $'+str(bal[i]))
  elif chanceorder[chancen] == 14:
    bal[p] += 150
    print('You now have $'+str(bal[p]))
  elif chanceorder[chancen] == 15:
    bal[p] += 100
    print('You now have $'+str(bal[p]))
  chancen += 1
  if chancen > 16:
    shuffle(chanceorder)
    chancen = 0

def cchanceland():
  if ownedby[tile[p]] == 0 and bal[p] >= pricebuy[tile[p]]:
    print('Would you like to buy '+tilename[tile[p]]+' for $'+str(pricebuy[tile[p]])+'? (y/n) You have $'+str(bal[p])+'.')
    a = 0
    while a == 0:
      response = input()
      if response == 'y': #buy property
        bal[p] -= pricebuy[tile[p]]
        ownedby[tile[p]] = p
        print(name[p]+' now owns '+tilename[tile[p]]+' and has $'+str(bal[p]))
        a = 1
      elif response == 'n': #pass on property
        a = 1
      else:
        print('Please select y or n')
        continue
  elif ownedby[tile[p]] == 0 and bal[p] < pricebuy[tile[p]]:
    print('You cannot afford '+tilename[tile[p]]+', you only have $'+str(bal[p])+' of $'+str(pricebuy[tile[p]])+'.')
  elif ownedby[tile[p]] == p: #player is owner
    print('You own this property already.')
  elif ismortgaged[tile[p]] == 1:
    print('This property is mortgaged.')
  elif ownedby[tile[p]] > 0: #pay rent
    if monopolytest(tile[p], 'm'):
      bal[p] -= 2*(rentprice[tile[p]*6+numhouse[tile[p]]])
      bal[ownedby[tile[p]]] += 2*(rentprice[tile[p]*6+numhouse[tile[p]]])
      print('You paid $'+str(2*(rentprice[tile[p]*6+numhouse[tile[p]]]))+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
    else:
      bal[p] -= rentprice[tile[p]*6+numhouse[tile[p]]]
      bal[ownedby[tile[p]]] += rentprice[tile[p]*6+numhouse[tile[p]]]
      print('You paid $'+str(rentprice[tile[p]*6+numhouse[tile[p]]])+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')

def housepay(h1, h2):
  pay = 0
  for i in range(40):
    if ownedby[i] == p:
      if numhouse[i] == 0:
        pass
      elif numhouse[i] == 5:
        pay += h2
      else:
        pay += h1*numhouse[i]
  bal[p] -= pay
  print('You pay $'+str(pay)+' in repairs. You now have $'+str(bal[p]))

def land():
  tile[p] += d1 + d2
  if tile[p] >= 40: #going past go
    tile[p] -= 40
    bal[p] += 200
    print('You passed go! You now have $'+str(bal[p]))
  landnd()

def landnd():
  print(name[p]+' landed at '+tilename[tile[p]])
  if ownedby[tile[p]] == 0 and bal[p] >= pricebuy[tile[p]]: #unowned and can afford
    print('Would you like to buy '+tilename[tile[p]]+' for $'+str(pricebuy[tile[p]])+'? (y/n) You have $'+str(bal[p])+'.')
    a = 0
    while a == 0:
      response = input()
      if response == 'y': #buy property
        bal[p] -= pricebuy[tile[p]]
        ownedby[tile[p]] = p
        print(name[p]+' now owns '+tilename[tile[p]]+' and has $'+str(bal[p]))
        a = 1
      elif response == 'n': #pass on property
        a = 2
      else:
        print('Please select y or n')
        continue
  elif ownedby[tile[p]] == 0 and bal[p] < pricebuy[tile[p]]: #unowned can't afford
    print('You cannot afford '+tilename[tile[p]]+', you only have $'+str(bal[p])+' of $'+str(pricebuy[tile[p]])+'.')
  elif ownedby[tile[p]] == p: #player is owner
    print('You own this property already.')
  elif ismortgaged[tile[p]] == 1:
    print('This property is mortgaged.')
  elif ownedby[tile[p]] > 0 and rentprice[tile[p]] > -1: #pay rent
    if monopolytest(tile[p], 'm'):
      bal[p] -= 2*(rentprice[tile[p]*6+numhouse[tile[p]]])
      bal[ownedby[tile[p]]] += 2*(rentprice[tile[p]*6+numhouse[tile[p]]])
      print('You paid $'+str(2*(rentprice[tile[p]*6+numhouse[tile[p]]]))+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
    else:
      bal[p] -= rentprice[tile[p]*6+numhouse[tile[p]]]
      bal[ownedby[tile[p]]] += rentprice[tile[p]*6+numhouse[tile[p]]]
      print('You paid $'+str(rentprice[tile[p]*6+numhouse[tile[p]]])+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
  elif ownedby[tile[p]] > 0 and rentprice[tile[p]] == -1: #rr and utilities
    if tile[p] in (12, 28): #utility
      if ownedby[12] == ownedby[28]: #own both
        bal[p] -= ((d1 + d2)*10)
        bal[ownedby[tile[p]]] += ((d1 + d2)*10)
        print('You paid $'+str((d1 + d2)*10)+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
      else: #own only one
        bal[p] -= ((d1 + d2)*4)
        bal[ownedby[tile[p]]] += ((d1 + d2)*4)
        print('You paid $'+str((d1 + d2)*4)+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.') 
    elif tile[p] in (5, 15, 25, 35):
      rr = 0
      if ownedby[5] == ownedby[tile[p]]:
        rr += 1
      if ownedby[15] == ownedby[tile[p]]:
        rr += 1
      if ownedby[25] == ownedby[tile[p]]:
        rr += 1
      if ownedby[35] == ownedby[tile[p]]:
        rr += 1
      bal[p] -= rrprice[rr]
      bal[ownedby[tile[p]]] += rrprice[rr]
      print('You paid $'+str(rrprice[rr])+' of rent to '+name[ownedby[tile[p]]]+'. You now have $'+str(bal[p])+'. '+name[ownedby[tile[p]]]+' now has $'+str(bal[ownedby[tile[p]]])+'.')
  elif ownedby[tile[p]] == -1: #other spaces
    if tile[p] in (0, 20):
      pass
    elif tile[p] in (2, 17, 33): #cc
      cc()
    elif tile[p] in (7, 22, 36): #chance
      chance()
    elif tile[p] == 10:
      print('Just visiting!')
    elif tile[p] == 30:
      injail[p] = True
      tile[p] = 10
      print('You are now in jail!')
    elif tile[p] == 4:
      bal[p] -= 200
      print('You paid $200 of Income Tax. You now have $'+str(bal[p]))
    elif tile[p] == 38:
      bal[p] -= 100
      print('You paid $100 of Super Tax. You now have $'+str(bal[p]))
    else: #--------------------------------------------------------<error test code>-----------
      print('ownedby == -1 but still failed.\n',
        tile[p] in (0, 20),'\n',
        tile[p] in (2, 17, 33),'\n',
        tile[p] in (7, 22, 36),'\n',
        tile[p] == 10,'\n',
        tile[p] == 30,'\n',
        tile[p] == 4,'\n',
        tile[p] == 38)
  else:
    print('fail overall.\n',
    ownedby[tile[p]] == 0 and bal[p] >= pricebuy[tile[p]],'\n',
    ownedby[tile[p]] == 0 and bal[p] < pricebuy[tile[p]],'\n',
    ownedby[tile[p]] == p,'\n',
    ismortgaged[tile[p]] == 1,'\n',
    ownedby[tile[p]] > 0 and rentprice[tile[p]] > -1,'\n',
    ownedby[tile[p]] > 0 and rentprice[tile[p]] == -1,'\n',
    ownedby[tile[p]] == -1) #--------------------------------------</error test code>----------
  if bal[p] < 0:
    debt() 

def turn(): 
  global p
  global tile
  global bal
  nod = 0
  clear()
  print(name[p]+'\'s turn!')
  if injail[p]:
    jail()
  else:
    wd = 1
    r = 0
    while wd == 1:
      r = 0
      while r == 0:
        print('Type r to roll, t to trade, or m to mortgage.')
        choice = input()
        if choice == 'r': #normal turn 
          roll()
          if d1 == d2:
            nod += 1
          else:
            wd = 0
          if nod == 3:
            print('You rolled doubles 3 times in a row, you are now in jail!')
            tile[p] = 10
            injail[p] = True
            wd = 0
          else:
            land()
          if injail[p]:
            wd = 0 #stops you from rolling doubles before going into jail and getting out 
          r = 1
        elif choice == '?': #run debug code
          debug()
        elif choice == 't': #make a trade
          trade()
        elif choice == 'm': #mortgage
          mortgage()
  r = 1
  while r == 1 and alive[p] == 1:
    print('Type t to trade, m to mortgage, or d when done')
    choice = input()
    if choice == 't':
      trade()
    elif choice == 'd':
      r = 2
    elif choice == '?':
      debug()
    elif choice == 'm':
      mortgage()

def gameover(): #game over code after someone wins
  print('Game Over') #temp code----------------------------------------------------------------

def gamerun(): #code for changing player by turn
  global p
  p = 1
  while numalive >= 2:
    if p > num:
      p = 1
    if alive[p]:
      turn()
    p += 1
  return

def debug(): #print debug info
  db = 0 #manual switch
  print('id','price','owner','ism','mprice','numh','hprice','name') 
  a = 0
  while a < 40:
    print('{:2d} {:5d} {:5d} {:3d} {:6d} {:4d} {:6d} {}'.format(a,pricebuy[a],ownedby[a],ismortgaged[a],mortgageprice[a],numhouse[a],houseprice[a],tilename[a]))
    if db == 1:
      b = 0
      while b < 6:
        print('house',b,'=',rentprice[6*a+b])
        b += 1
    a += 1
  print(bal[1:])

#start of run code
print('Welcome to Monopoly. How many players?')
debug()
pregame()
gamerun()
gameover()
