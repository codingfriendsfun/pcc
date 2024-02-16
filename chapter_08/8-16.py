import book_functions
book_functions.favorite_book("the poppy war")

from book_functions import favorite_book
favorite_book("city of brass")

from book_functions import favorite_book as fb
fb("way of kings")

import book_functions as bf
bf.favorite_book("fourth wing")

from book_functions import *
favorite_book("arrows of the queen")