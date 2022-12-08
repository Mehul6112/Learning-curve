import os
l = True
while l == True: 
  f_name = open("one_piece.txt", "r")
  n_lines = 0
  n_words = 0
  n_chars = 0
  freq = {}
  for line in f_name:
    line = line.strip(os.linesep)
    words = line.split()
    if n_lines %2 == 0:
      file1 = open("file1.txt", "w")
      file1.write(line)
    else:
      file2 = open("file2.txt", "w")
      file2.write(line)
    n_lines += 1
    n_words += len(words)
    n_chars += sum(1 for c in line if c not in (os.linesep, ' '))
    
    for i in line:
      if i in freq:
        freq[i] += 1
      else:
        freq[i] = 1

  print("Total no. of lines is", n_lines)
  print("Total no. of words is", n_words)
  print("Total no. of characters is", n_chars)
  print("Frequency of every character in the file is: ","\n" + str(freq))

  f_name.close()
  
  l = input("Do you want to run the program again? (y/n): ")
  if l == "y":
      l = bool(1)
  else:
      l = bool(0)