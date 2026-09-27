from logging.config import fileConfig
import os, sys
from alembic import context

# allow imports from project root
sys.path.append(os.getcwd())

# import your DB objects
import database

config = context.config
fileConfig(config.config_file_name)

target_metadata = database.Base.metadata

def run_migrations_offline():
    url = str(database.url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = database.engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()