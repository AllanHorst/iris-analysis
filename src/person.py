class Person:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName

  def toJSON(self):
    return {
      "firstName": self.firstName,
      "lastName": self.lastName
    }