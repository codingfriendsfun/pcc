# 9-12. Multiple Modules

from Admin import *

myAdmin = Admin("Ruthe", "Ginsburg", privileges=["Notorious", "Can write laws", 
                                        "Takes no shit"])

myAdmin.privileges.show_priveleges()