#django-nextjs-backend-api\src\cfehome\api.py
import helpers
from ninja import NinjaAPI,Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController


#api=NinjaAPI() - changed to below, our new api
api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")
#waitlists is the name of the app moule, api in the name of api module under waitlists app

class UserSchema(Schema):#having Schema as an argument
    username: str
    is_authenticated:bool
    #if user is not request.user.is_authenticated = none, else display email
    email:str=None

@api.get("/hello")
def hello(request):
    print (request)
    return {"message":"Hello World"}

@api.get("/me", response=UserSchema, auth=helpers.api_auth_user_required)#add auth requirements for this user
#auth=JWTAuth() is similar to @login_required decorater
def me(request):
    #print (request)
    return request.user
