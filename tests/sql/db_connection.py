import pymysql

db_params = {
    'host': 'localhost',
    'user': 'root',
    'password': 'college',
    'db': 'employees'
}

query_all_departments = 'select * from departments'
query_all_employees = 'select first_name, last_name, gender from employees'

with pymysql.connect(**db_params) as conn:
    cursor = conn.cursor()

    cursor.execute(query_all_departments)
    assert cursor.rowcount == 9, "departments rowcount is not 9"
    actual_result = cursor.fetchmany(size=2)
    print(actual_result)
    expected_result = (('d009', 'Customer Service'), ('d005', 'Development'))
    assert actual_result == expected_result