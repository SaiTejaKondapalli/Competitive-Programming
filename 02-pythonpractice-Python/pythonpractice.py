"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
    def addItem(self, item):
        self.items.append(item)
    def classiness(self):
        c = 0
        for each in self.items:
            if each == "tophat":
                c += 2
            if each == "bowtie":
                c += 4
            if each == "monocle":
                c += 5
        return c


