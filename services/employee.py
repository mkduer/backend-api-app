from datastore import get_model

class EmployeeService():

    @staticmethod
    def get() -> dict:
        employee = get_model()
        return employee.select_all()
        