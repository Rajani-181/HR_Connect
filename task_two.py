from datetime import datetime


from utils.csv_operation import HandleCSV


def hire_date_emp():
    emp_hire_date = {}
    for employee in HandleCSV.read_csv_line_by_line():
        if int(employee["DEPARTMENT_ID"]) in range(30, 111) and int(
                employee["SALARY"]) > 4200:
            hire_date = employee.get("HIRE_DATE")
            #print(hire_date)
            f_name = employee.get("FIRST_NAME")
            l_name = employee.get("LAST_NAME")
            name = f"{f_name} {l_name}"
            date_formate = "%d-%b-%y"
            date_ = datetime.strptime(hire_date, date_formate)
            #print(date_)
            # converting date to string
            date_ = str(date_)
            # "2002-06-07 00:00:00 removing suffix 00:00:00"
            date_ = date_.removesuffix("00:00:00")
            # checking suffix removed or not
            #print(date_)
            # adding to hire date and names to empty dictionary
            emp_hire_date.setdefault(date_, [name])
    return emp_hire_date


hire_dict = hire_date_emp()
print(hire_dict)