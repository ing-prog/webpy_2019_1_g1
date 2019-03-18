vacTitle = [] #"Python Developer"
vacIntro = []#"Django 2.1+, FLask, + PostGre + Sql + C++"
vacSalary = []#135000
vacCompany = [] #"MTS"

vacTitle.append("Python Developer")
vacIntro.append("Django 2.1+, FLask, + PostGre + Sql + C++")
vacSalary.append(135000)


class Vacancy:
    vacTitle = ""
    vacIntro = ""
    vacSalary = 0
    vacCompany = ""


vac1 = Vacancy()
vac1.vacTitle = "Python Developer"
vac1.vacSalary = 135000

vac2 = Vacancy()
vac2.vacTitle = "JS Developer"
vac2.vacSalary = 70000

print(vac1.vacSalary, vac1.vacTitle)
print(vac2.vacSalary, vac2.vacTitle)



