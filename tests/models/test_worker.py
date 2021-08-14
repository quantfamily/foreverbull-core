from foreverbull_core.models.worker import Database, Parameter, WorkerConfig


def test_database():
    database = Database(
        user="test_user",
        password="test_password",
        hostname="test_hostname",
        port=1337,
        db_name="test_name",
        dialect="ofc_postgres",
    )

    data = database.dump()
    loaded = Database.load(data)
    assert database == loaded


def test_parameter():
    parameter = Parameter(key="test_key", value=1, default=11)

    data = parameter.dump()
    loaded = Parameter.load(data)
    assert parameter == loaded


def test_worker_configuration():
    database = Database(
        user="test_user",
        password="test_password",
        hostname="test_hostname",
        port=1337,
        db_name="test_name",
        dialect="ofc_postgres",
    )
    parameter1 = Parameter(key="test_key", value=1, default=11)
    parameter2 = Parameter(key="test_key2", value=2, default=22)
    worker_config = WorkerConfig(session_id="test_id", database=database, parameters=[parameter1, parameter2])
    data = worker_config.dump()
    loaded = WorkerConfig.load(data)
    assert worker_config == loaded
