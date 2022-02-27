


def format_name(f_name, l_name):
  """"This function formats f_name and l_name as titles"""
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"


print(format_name("First name", "Second name"))