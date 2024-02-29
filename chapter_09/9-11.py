# 9-11. Imported Admin

from Users import *

myAdmin = Admin("Ruthe", "Ginsburg", privileges=["Notorious", "Can write laws", 
                                        "Takes no shit"])

myAdmin.privileges.show_priveleges()