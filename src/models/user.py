
class User:

  def __init__(self, i, n, l, u, p, a, ph, d, r) -> None:
    self.id = i
    self.name = n
    self.lastName = l
    self.username = u
    self.password = p
    self.age = a
    self.photo = ph
    self.deleted = d
    self.rol = r

  def toJson(self):

    return {
      "id":self.id,
      "name": self.name,
      "lastName": self.lastName,
      "username": self.username,
      "password": self.password,
      "age": self.age,
      "photo": self.photo,
      "deleted": self.deleted,
      "rol": self.rol
    }