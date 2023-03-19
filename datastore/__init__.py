"""
Allow for abstraction of datastore
  - EmployeeModel works as a contract/interface that all datastores will implement
  - Ease of using a new datastore or deprecating an old datastore if needed
"""

datastore = 'sqlite'

if datastore == 'sqlite':
    from datastore.sqlite_datastore import SqliteDatastore as EmployeeModel
elif datastore == 'cloudstore':
    # option to import a different datastore -- perhaps Cloud Storage if relevant
    # not implemented and only provided as an example path
    pass
else:
    raise ValueError("Datastore is not configured")

model = EmployeeModel()

def get_model() -> EmployeeModel:
    return model