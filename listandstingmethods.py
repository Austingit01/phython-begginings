#string methods
challenge = "thirtydaysofpython"
print(challenge.capitalize())
print(challenge.count("y"))
print(challenge.endswith("on"))
print(challenge.endswith("ing"))
print(challenge.find("thon"))
print(challenge.isalnum())
print(challenge.isalpha())
print(challenge.split())
print(challenge.startswith("t"))
#list
Firstnames = ["kenenna", "precious", "nedu","chisom","123","50","80"]
print(Firstnames)
print(len(Firstnames))
Fruits = ["mango", "orange", "pawpaw", "apple"]
print(Fruits)
print(Firstnames[0])
print(Firstnames)
print(Fruits[0])
print(Firstnames[0:5])
Firstnames[0] = "chibike"
print(Firstnames)
does_exict = "kenenna" in Firstnames
print(does_exict)
Firstnames.append("ngozi")
print(Firstnames)
Firstnames.insert(1,"chima")
print(Firstnames)
Firstnames.remove("nedu")
print(Firstnames)
Firstnames.pop()
Firstnames.pop(5)
print(Firstnames)