import re
def arithmetic_arranger(problems,display=False):
  line1 = ''
  temp_line1 = ''
  line2 = ''
  temp_line2 = ''
  line3 = ''
  line4 = ''
  temp_line4 = ''
  # Check if there are too many problems
  if len(problems) > 5:
    return "Error: Too many problems."
  # verify problems are valid  
  for problem in problems:
    filtered_problem = re.findall("\S+",problem)
    if re.search("\D",filtered_problem[0]) is not None or re.search("\D",filtered_problem[2]) is not None:
      return "Error: Numbers must only contain digits."
    elif re.search("^\+$|^\-$",filtered_problem[1]) is None:
      return "Error: Operator must be '+' or '-'."
    elif len(filtered_problem[0]) > 4 or len(filtered_problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
      if re.search("\+",filtered_problem[1]):
        solution = str(int(filtered_problem[0]) + int(filtered_problem[2]))
      else:
          solution = str(int(filtered_problem[0]) - int(filtered_problem[2]))
      length = len(max(filtered_problem,key=len)) + 2
      # create arranged_problems strings
      for i in range(length):
        if len(filtered_problem[0]) - 1 >= i:
          temp_line1 += filtered_problem[0][i]
        else:
          temp_line1 = ' ' + temp_line1
        if len(filtered_problem[2]) - 1 >= i:
          temp_line2 += filtered_problem[2][i]
        else:
          temp_line2 = ' ' + temp_line2
        line3 += '-'
        if len(solution) - 1 >= i:
          temp_line4 += solution[i]
        else:
          temp_line4 = ' ' + temp_line4
      line1 += temp_line1 + "    "
      temp_line2 = filtered_problem[1][0] + temp_line2[1:]
      line2 += temp_line2 + "    "
      line3 += "    "
      line4 += temp_line4 + "    "
      temp_line1 = ''
      temp_line2 = ''
      temp_line4 = ''
  # slice trailing spaces
  line1 = line1[0:len(line1)-4]
  line2 = line2[0:len(line2)-4]
  line3 = line3[0:len(line3)-4]
  line4 = line4[0:len(line4)-4]
  if display:
      arranged_problems = f'{line1}\n{line2}\n{line3}\n{line4}'
  else:
      arranged_problems = f'{line1}\n{line2}\n{line3}'
  return arranged_problems