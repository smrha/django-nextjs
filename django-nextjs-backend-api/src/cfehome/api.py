from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticates: bool

@api.get("/hello")
def hello(request):
    print(request)
    return "Hello World"

@api.get("/me", response=UserSchema)
def me(request):
    return request.user