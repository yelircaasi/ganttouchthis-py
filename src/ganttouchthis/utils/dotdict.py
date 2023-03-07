# class dotdict(dict):
#     """dot.notation access to dictionary attributes"""

#     __getattr__ = dict.get
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__


# def as_dotdict(nested_dict: dict) -> dotdict:
#     nested_dict = dotdict(nested_dict)
#     for key, value in nested_dict.items():
#         if isinstance(value, dict):
#             nested_dict[key] = as_dotdict(value)
#     return nested_dict
