from app.models import User

def test_new_user():
  newUser = User(
      username = 'john.doe',
      email = 'john.doe@example.com',
      password = 'ThisisaBadPassword'
      )
  assert newUser.username == 'john.doe'
  assert newUser.email == 'john.doe@example.com'
  assert newUser.password != 'ThisisaBadPassword'