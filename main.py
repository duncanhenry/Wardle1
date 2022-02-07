
import random
from termcolor import colored
import os
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
text = colored('Hello, World!', 'red')
info = "good luck"
def skip(x):
  for y in range(0, x):
    print("         ")
li = ["d", "f"]
li[0] = li[0].capitalize()

letters1 = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
c = "!"
k = "?"
w = "/"

def scan(u):
  word_file = open('dict.txt')
  if u in word_file.read().split():
    return True
  else: 
    return False
  word_file.close()
def rword(leng):
    word_file = open('dict.txt').read()
    x = True
    while x == True:
      secret_word = random.choice(word_file.split())
      if len(str(secret_word)) == leng:
        return secret_word
def board():
  cls()
  print("         "," | ".join(g1))
  print("         "," | ".join(g2))
  print("         "," | ".join(g3))
  print("         "," | ".join(g4))
  print("         "," | ".join(g5))
  print("         "," | ".join(g6))
  skip(1)
  print(" ".join(letters))
  skip(1)
  print(info)
pla = True
while pla == True:
  g1 = []
  g2 = []
  g3 = []
  g4 = []
  g5 = []
  g6 = []
  j = True
  while j == True:
    print("Welcome to wardle a knock off of wordle, but you can play indefinately and you can choose the length of the word. Press enter to coninue: ")
    if input() == "":
      j = False
      cls()
    else:
      cls()
      print("Not an option")
  f = True
  while f == True:
   leng = int(input("Number of letters? (4 - 17) 5 recommended: "))
   if leng >= 4:
     f = False
   else:
      cls()
      print("Not an option ")
  letters = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
  for i in range(leng):
    g1.append("_")
    g2.append("_")
    g3.append("_")
    g4.append("_")
    g5.append("_")
    g6.append("_")
  nums = 0
  win = False
  word = str(rword(leng))
  lets = list(word)

  gam = True
  while gam == True:
    info = ""
    board()
    nums += 1
    gusn = True
    while gusn == True:
      guess = input("what word would you like to guess? ").lower()
      if len(guess) == leng and scan(guess) == True:
        gusn = False
      elif len(guess) > leng:
        info = "too long"
        board()
      elif len(guess) < leng:
        info = "too short!"
        board()
      elif scan(guess) == False:
        info  = "Not a word!"
        board()
      if guess == word:
        win = True
    if nums == 1:
      g1 = list(guess)
    if nums == 2:
      g2 = list(guess)
    if nums == 3:
      g3 = list(guess)
    if nums == 4:
      g4 = list(guess)
    if nums == 5:
      g5 = list(guess)
    if nums == 6:
      g6 = list(guess)
    glets = list(guess)
    print(glets)
    x = 0
    for i in range(len(glets)): 
      if glets[x] in lets:
        #for glets[x] in lets:
        pos = lets.index(glets[x])
        if pos == glets.index(glets[x]):
            lets[x] = lets[x].capitalize
            glets[x] = colored(glets[x], 'green')
        else:
            glets[x] = colored(glets[x], 'yellow')
      else:
        lr = letters1.index(glets[x])
        letters[lr] = colored(letters[lr], 'grey')    
      
      x += 1
    print("".join(glets))
    lets = list(word)
    if nums == 1:
      g1 = glets
    if nums == 2:
      g2 = glets
    if nums == 3:
      g3 = glets
    if nums == 4:
      g4 = glets
    if nums == 5:
      g5 = glets
    if nums == 6:
      g6 = glets
    
    

  
    
    
    if win == True:
      gam = False
      info = ("You win!")
      board()
    
    elif nums == 6:
      info = ("You  lose! the word was")

      board()
      print(word)
      gam = False
  h = True
  while h == True:
    cont = input("Play again? (yes) or (no): ")
    if cont == "yes":
      h = False
      cls()
    if cont == "no":
      h = False
      pla = False
    else:
      print("Not an option")