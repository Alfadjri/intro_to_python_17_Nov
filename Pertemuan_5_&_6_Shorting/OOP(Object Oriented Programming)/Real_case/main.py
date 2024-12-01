from employee import Employee
from manager import Manger

def main():
    employee = Employee("Tika" , 20, "Software Developer",5000000)
    print(employee.get_detail())
    print(employee.work())
    manger = Manger("Bob",40,"Project Manager",7000000,10)
    print(manger.get_detail())
    print(manger.manage())

    print(f"Original Age of {employee._name} : {employee.getUmur()}")
    employee.set_umur(24)
    print(f"Original Age of {employee._name} : {employee.getUmur()}")

if __name__ == "__main__":
    main()

