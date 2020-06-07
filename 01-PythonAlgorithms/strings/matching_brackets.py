"""
Write a function to detect if a string is valid or not

"abc_123{}"
"{abc_123}"
"abc_{1}23"
"abc_123{()}()"
"abc_123{()}[()]&"

invalid 
"}abc_123{"
"abc_123{"
"ab{[}]"
Raise exception which has the position at which the error occured. 

"""


class RaiseException(Exception):
  pass



def validate(text):
    """
    >>> validate('abc_123')
    True
    >>> validate('-=*')
    False
    """
    valid_brackets = {
      '{': '}',
      '(': ')',
      '[': ']',
      '<': '>'
    }
    stack = []
    for index, each_char in enumerate(text):
      flag = True
      if each_char.isalnum() or each_char in '_&':
        continue
      if each_char in valid_brackets.keys():
        stack.append((index,each_char))
        continue
      
      if stack and each_char in valid_brackets.values():
          temp_char = stack.pop()
          if not (each_char == valid_brackets.get(temp_char[1])):
            flag = False
          continue
      else:
         flag = False
      
      if not flag:
        raise RaiseException('Error at postition {} of input "{}"'.format(index, text))

    if stack:
      raise RaiseException('Error at postition {} of input "{}"'.format(stack[-1][0], text))
    return True


assert True == validate('{')
assert True == validate('abc_123{}&')
assert False == validate('{abc_123}')
assert True == validate('[ab(c_1)23]()[({})]')
assert False == validate('{{abc_123}')
assert False == validate('{abc_123}[(])')
assert True == validate('a{bc_123}4')
assert False == validate('a{bc_123}4-')
print(validate('{'))
