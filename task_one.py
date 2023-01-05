from utils.csv_operation import HandleCSV


def do_task_one():
    salary_9000 = {}
    print("Employees details having salary > 9000")
    for employee in HandleCSV.read_csv_line_by_line():
        # print(employee["SALARY"])
        if int(employee["SALARY"]) > 9000:
            name = employee.get("FIRST_NAME") + " " + employee.get("LAST_NAME")
            email = employee.get("EMAIL")
            phone = employee.get("PHONE_NUMBER")
            #print(phone.replace(".",""))
            phone = phone.replace(".","")
            #print(phone)
            salary_9000.update({"name": name})
            salary_9000.update({"email": email})
            salary_9000.update({"phone number":phone})
            # print(f{"NAME":employee.get("FIRST_NAME"),"LNAME":employee.get("LAST_NAME"),"EMAIL":employee.get("EMAIL"),"PHONE_NO":employee.get("PHONE_NUMBER")})
            print(salary_9000)

do_task_one()
