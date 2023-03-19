class EmployeeModel:
    
    def select_all(self) -> dict:
        """Connects to datastore to select all employees

        Returns:
            List of dictionary objects: key, value pair of column header and value
            Example: [{ "gender": female, "id": 5 }] or None if the table has no rows
        """
        pass