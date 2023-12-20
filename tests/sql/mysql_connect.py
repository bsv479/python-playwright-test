from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqldb://root:college@localhost/employees")

query_all_departments = 'select * from departments'
query_all_employees = 'select first_name, last_name, gender from employees'

with engine.connect() as conn:
    result = conn.execute(text('select * from departments'))
    print(result.all())