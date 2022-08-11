import logging


def test_count_for_countries(connection):
    # Test count of records in table 'countries'
    query = 'Select count(*) from hr.countries'
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchone()
    assert (result[0]) == 25


def test_pattern_for_country_id(connection):
    # Test pattern of country_id in table 'countries'
    # Country_id should contain only capital latin letters and have length of 2 symbols
    query = 'SELECT country_id FROM TRN.hr.countries where country_id not like \'[A-Z][A-Z]\''
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchall()
    assert result == []


def test_job_id_exists_in_table_jobs(connection):
    # Test that all employees have correct job_id
    # Job_id should exist in table 'jobs'
    query = 'SELECT employee_id FROM hr.employees where job_id not in (SELECT job_id from hr.jobs)'
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchall()
    assert result == []


def test_average_salary(connection):
    # Test that average salary is in particular range
    # Average salary should be between 8000 and 9000
    query = 'SELECT avg(salary) FROM TRN.hr.employees'
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchone()
    assert 8000 <= result[0] <= 9000


def test_min_salary(connection):
    # Test that min salary is not lower than particular value
    # Min salary should not be lower than 2000
    query = 'SELECT min(min_salary) FROM hr.jobs'
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchone()
    assert result[0] >= 2000


def test_max_salary(connection):
    # Test that max salary is not greater than particular value
    # Max salary should not be greater than 50000
    query = 'SELECT max(max_salary) FROM hr.jobs'
    logging.info(f'Executing test: {query}')
    connection.execute(query)
    result = connection.fetchone()
    assert result[0] <= 50000

