############################################################
##################### kata_5 ###############################
############################################################

""" 
Complete the function/method so that it takes a PascalCase pascalcase and returns the pascalcase in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a pascalcase.
Examples

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
"""
# # recordar ñ
# import string

# def to_underscore(pascalcase: any) -> str:
#     upper_case = string.ascii_uppercase
#     if isinstance(pascalcase, int):
#         return str(pascalcase)

#     elif isinstance(pascalcase, str):
#         first_letter=[pascalcase[0].lower()]

#         for I in pascalcase[1:]:
#             if I in upper_case:
#                 first_letter.append('_')
#                 first_letter.append(I.lower())

#             else:
#                 first_letter.append(I)
#     return "".join(first_letter)
# print(to_underscore("MoviesAndData"))

############################################################
##################### BEST_KATA ############################
############################################################

# import re

# def to_underscore(string):
#     return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()   