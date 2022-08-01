from decouple import config
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
import psycopg

from model.location_model import Location

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
                cur.execute("select * from public.locations where users_username=%s", (username,))
                locations_info = cur.fetchall()
                return {"locations": locations_info}

    @staticmethod
    def add_location(location_obj):
        name_added = location_obj.username
        location_added = location_obj.location

        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO public.locations (users_username, location) VALUES (%s,%s) RETURNING *", (name_added, location_added))

                locations_info = cur.fetchall()
                if locations_info is None:
                    return None
                else:
                    conn.commit()
                    return Location(locations_info[0][0], locations_info[0][1], locations_info[0][2])

    @staticmethod
    def delete_location_by_id(username, location):
        print(location)
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM public.locations WHERE users_username=%s AND location=%s",
                            (username, location))

                row_deleted = cur.rowcount
                if row_deleted !=1:
                    return False
                else:
                    conn.commit()
                    return True