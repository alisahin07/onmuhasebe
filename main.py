import pywhatkit

import metin
import time_find

phone_numbers=['+9050658576','+353831437861']

for tel in phone_numbers:

    pywhatkit.sendwhatmsg(tel,
                           metin.gonder()[0],
                          time_find.zaman()[0], time_find.zaman()[1]+1 )