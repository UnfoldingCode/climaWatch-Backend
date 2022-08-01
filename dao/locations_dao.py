from decouple import config
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
import psycopg

API_HOST = config('host')
API_PORT = config('port')
API_DBNAME = config('dbname')
API_USER = config('user')
API_PASSWORD = config('password')


class LocationDao:
    @staticmethod
    def get_location(username):
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from climawatch.locations where users_username=%s", (username,))
                locations_info = cur.fetchall()
                return {"locations": locations_info}

    @staticmethod
    def add_location(location, username):
        try:

            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "insert into climawatch.locations(location, users_username) values(%s, %s) RETURNING *",
                        (location, username))
                    user_just_created = cur.fetchone()
                    print(user_just_created)
                    return f"New location {location } successfully added to your favorite list"
        except psycopg.errors.UniqueViolation as e:
            return None

    @staticmethod
    def delete_location(location, username):
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "Delete from climawatch.locations where location=%s and users_username=%s RETURNING *",
                    (location, username))
                location_just_deleted = cur.rowcount
                if not location_just_deleted:
                    return None
                return True
