# def valid_length(user):
#     valid=False
#     if 3 <= len(user) <= 16:
#         valid=True
#     return valid
#
#
# def valid_containment(user):
#     valid=False
#     if user.isdigit() or user.isalpha() or "_" in user or "-":
#         valid=True
#     return valid
#
#
# def redundant_filter(user):
#     forbidden_symbols=["!", "@", "?", ".", ",","'",'"']
#     valid=True
#     for symbol in forbidden_symbols:
#         if symbol in user:
#             valid=False
#             return valid
#     return valid
#
#
# valid_names=[]
# usernames=input().split(", ")
# for name in usernames:
#     if valid_length(name) and valid_containment(name)and redundant_filter(name) :
#         valid_names.append(name)
# print("\n".join(valid_names))

