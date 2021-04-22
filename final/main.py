shift = 3

def magic(method, text):
  processed_text = ""
  for c in text:
    if c.isupper():
      # find the position in 0-25
      c_index = ord(c) - ord("A")
       # perform the shift
      if method == "Verschlusseln":
        new_index = (c_index + shift) % 26
      if method == "Entschlüsseln":
        new_index = (c_index - shift) % 26
      # convert to new character
      new_unicode = new_index + ord("A")
      new_character = chr(new_unicode)
      # append to encrypted string
      processed_text += new_character
    else:
      # since character is not uppercase, leave it as it is
      processed_text += c    
  return processed_text

def work():
  # This is a dictionary representing options
  options = {
    1: 'Verschlusseln',
    2: 'Entschlüsseln'
  }

  question = "Was würdest du gern tun?\n\
    1) Verschlusseln\n\
    2) Entschlüsseln\n> "

  operation = ''
  while operation not in {1, 2}:
    operation = int(input(question))
  text = input("Was ist der Text? > ")
  result = magic(options[operation], text.upper())
  print("Ergebnis der {} ist: {}".format(options[operation], result))

def main():
  work()
  while input("Noch einmal? > ").lower() == "ja":
    work()
  
if __name__ == '__main__':
  main()