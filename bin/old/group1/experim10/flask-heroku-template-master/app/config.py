database = {
    'user': 'admin', 
    'password': 'P@SSW0RD',
    'port': '3306',
    'host': 'localhost',
    'database': 'project2',
    'dialect': 'mysql',
    'driver': None
}
# Supported dialects https://docs.sqlalchemy.org/en/13/dialects/index.html

db_prefix = database['dialect']
if database['driver'] is not None:
    db_prefix += database['driver']

# Logic for building database connection URLS
DATABASE_URL = f"{db_prefix}://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}"

# Docs on building database connection URLS
# https://docs.sqlalchemy.org/en/13/core/engines.html


