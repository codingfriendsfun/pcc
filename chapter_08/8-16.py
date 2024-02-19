# 8-16. Imports
# originally 8-9. Messages

#I know I'm supposed to have imports at the top, but I'm doing this
# compressed into one file so I'm putting the list at the top

messages_list = [
    "On my way!",
    "Running a bit late.",
    "Do you believe in love after love?"
]

import messages # 1
from messages import show_messages # 2
from messages import show_messages as sh_mess # 3
import messages as m # 4

messages.show_messages(messages_list) 
show_messages(messages_list) 
sh_mess(messages_list) 
m.show_messages(messages_list) 

from messages import * # had to put this down here because it overwrites # 2
show_messages(messages_list)
