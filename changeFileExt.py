import os

folder_path = #FILLE HERE

ext_type = #FILL HERE (EX: .jpg, .png)

os.chdir(folder_path)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    new_name = '{} {}'.format(f_name, ext_type)
    os.rename(f, new_name)