def colorchangment(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="bleu":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color=="purple":
    return ("\033[35m")
  elif color=="green":
    return ("\033[32m")

title= f" {colorchangment('red')}={colorchangment('white')}={colorchangment('bleu')}= {colorchangment('yellow')} MUSIC APP {colorchangment('bleu')}={colorchangment('white')}={colorchangment('red')}="
#center the title
print(f" {title:^35}")
print(f"🔥 \t {colorchangment('bleu')} RADIO GAGA")
print(f"\t {colorchangment('bleu')} QUEEN")
prev="prev"
next="next"
pause="pause"
print(f"{prev:<35} ")
print(f"{colorchangment('purple')}{next:^35}")
print(f"{colorchangment('green')}{next:>35}")

#second interfase
print()
print()
welcome="WELCOME TO"
print(f"{welcome:^35}")
text0="-- ARMBOOK --"
print(f"{colorchangment('bleu')}{text0:^35}")
text1="Definitely not a rip off"
print(f"{colorchangment('purple')}{text1:>35}")
text2="a certain other social"
print(f"{colorchangment('purple')}{text2:>35}")
text3="networking site"
print(f"{colorchangment('purple')}{text3:>35}")
honest="HONEST"
print(f"{colorchangment('red')}{honest:^35}")
username="USERNAME"
password="PASSWORD"
print(f"{colorchangment('bleu')}{username:^35}")
print(f"{colorchangment('bleu')}{password:^35}")
