"""
Pretend this is a database migration tool like yoyo or something.
"""
from time import sleep
from etl_src.services.postgres import post_gres

sleep(10)
def run_migration():
    migrations = open("/app/migrations/migrations.sql", "r").read()

    with post_gres() as cursor:
        cursor.execute(migrations)

run_migration()
print("Migrations completed")