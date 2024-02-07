

from company import Company
from dev import Dev
from freebie import Freebie


__all__ = [ 'Company', 'Dev', 'Freebie' ]

ibm = Company("IBM", 1980)
facebook = Company("Facebook", 1950)

rooj = Dev("Rooj")
isaiah = Dev("Isaiah")

freebie1 = Freebie(rooj, ibm, "Hat", 5)
freebie2 = Freebie(rooj, facebook, "Mug", 3)
freebie2 = Freebie(isaiah, ibm, "Pin", 3)

# print(freebie1.print_details())

facebook.give_freebie(rooj, "Shirt", 10)
# print(rooj.freebies())
# print(isaiah.freebies())
print(Company.oldest_company())
# rooj.give_away(isaiah, freebie1)

# print(isaiah.freebies())

