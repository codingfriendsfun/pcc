from admin import Admin, Privileges

admin_0 = Admin('mace', 'windu')

admin_0.privileges = Privileges([
    'can grant rank of master',
    'can grant seat on council',
    'can declare sith lord'
    ])

admin_0.privileges.show_privileges()