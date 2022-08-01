from decouple import config
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
import psycopg

API_HOST = config('host')
API_PORT = config('port')
API_DBNAME = config('dbname')
API_USER = config('user')
API_PASSWORD = config('password')


class UsersDao:
    @staticmethod
    def get_users():
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from public.users")
                user_info = cur.fetchall()
                return {"users": user_info}

    @staticmethod
    def create_user(data):
        try:
            username = data["username"]
            name = data["name"]
            email = data["email"]
            password = data["password"]
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "insert into public.users(username, name, email,  password) values(%s, %s, %s, %s) RETURNING *",
                        (username, name, email, password))
                    user_just_created = cur.fetchone()
                    print(user_just_created)
                    return "New user successfully created"
        except (psycopg.errors.ForeignKeyViolation, psycopg.errors.UniqueViolation):
            return None

    @staticmethod
    def login(username, password):
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from public.users where username = %s and password = %s", (username, password))
                user_info = cur.fetchone()
                if not user_info:
                    return None
                
                return {"users": user_info}

