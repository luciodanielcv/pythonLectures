

my_string = "This is a string with no style"
#print(my_string)

my_string = my_string.title()
#print(my_string.title())

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  #print(f"{formated_f_name} {formated_l_name}")
  return f"{formated_f_name} {formated_l_name}"




formated_name = format_name("First name", "Last name")

print(formated_name)
