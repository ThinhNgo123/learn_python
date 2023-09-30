# import uncompyle6

# file_origin = "sprite.cpython-38.pyc"
# file_new = "surface.py"
# with open(file_new, "w") as f:
#     uncompyle6.decompile_file(file_origin, f)

import py_compile
print(__file__)
#d:/Data/Project_company/learn_python/decompyle_python/decom_python1.py
py_compile.compile("d:/Data/Project_company/learn_python/decompyle_python/test_pyc.py")

import marshal

s = open('d:/Data/Project_company/learn_python/decompyle_python/__pycache__/test_pyc.cpython-38.pyc', 'rb')
s.seek(8)  # go past first eight bytes
code_obj = marshal.load(s)
print(code_obj)