class SymLangInterpreter:
  def __init__(self):
      self.variables = {}

  def execute(self, code):
      lines = code.split('\n')
      for line in lines:
          if line.startswith('Declare'):
              parts = line.split(' as ')
              var_name = parts[0].split(' ')[1]
              value = int(parts[1].strip(';'))
              self.variables[var_name] = value
          elif line.startswith('Show'):
              value = line.split(' ')[1].strip(';')
              if value.startswith('"') and value.endswith('"'):
                  print(value[1:-1])
              else:
                  print(self.variables.get(value, "Variable not found"))

code = '''
Declare x as 5;
Declare y as 10;
Show x;
Show "Hello, World!";
'''

interpreter = SymLangInterpreter()
interpreter.execute(code)
