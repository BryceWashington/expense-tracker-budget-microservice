from app.db.database import get_db
import pymysql.cursors

def get_budgets(user_id: int, limit: int, offset: int):
    connection = get_db(db_name="budget_service")
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    if user_id:
        query = """
        SELECT * FROM budgets
        WHERE user_id = %s
        LIMIT %s OFFSET %s
        """
        cursor.execute(query, (user_id, limit, offset))
    else:
        query = """
        SELECT * FROM budgets
        LIMIT %s OFFSET %s
        """
        cursor.execute(query, (limit, offset))

    result = cursor.fetchall()

    cursor.close()
    connection.close()
    # print(result[0])
    # print(result)
    return result

def get_budget_by_id(budget_id: int):
    connection = get_db(db_name="budget_service")
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT * FROM budgets WHERE id = %s
    """

    cursor.execute(query, (budget_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    # print(result)
    return result

def create_budget(budget):
    connection = get_db(db_name="budget_service")
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    query = """
    INSERT INTO budgets (amount, start_date, end_date, user_id, budget_type_id)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (budget.amount, budget.start_date, budget.end_date, budget.user_id, budget.budget_type_id))
    new_budget_id = cursor.lastrowid


    connection.commit()

    cursor.close()
    connection.close()

    return get_budget_by_id(new_budget_id)

def delete_budget(budget_id: int):
    connection = get_db(db_name="budget_service")
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    query = """
    DELETE FROM budgets WHERE id = %s
    """

    cursor.execute(query, int(budget_id))
    connection.commit()

    # print(cursor.rowcount) # number of rows deleted.

    cursor.close()
    connection.close()

    return cursor.rowcount > 0

def update_budget(budget_id: int, current_budget, new_budget_data):
    connection = get_db(db_name="budget_service")
    cursor = connection.cursor(pymysql.cursors.DictCursor)


    new_budget_data = new_budget_data.dict()
    amount = new_budget_data["amount"] if new_budget_data["amount"] is not None else current_budget["amount"]
    start_date = new_budget_data["start_date"] if new_budget_data["start_date"] is not None else current_budget["start_date"]
    end_date = new_budget_data["end_date"] if new_budget_data["end_date"] is not None else current_budget["end_date"]
    budget_type_id = new_budget_data["budget_type_id"] if new_budget_data["budget_type_id"] is not None else current_budget["budget_type_id"]

    print(amount)
    print(start_date)
    print(end_date)
    print(budget_type_id)

    query = """
    UPDATE budgets
    SET amount = %s, start_date = %s, end_date = %s, budget_type_id = %s
    WHERE id = %s
    """

    cursor.execute(query, (amount, start_date, end_date, budget_type_id, budget_id))
    connection.commit()

    cursor.close()
    connection.close()

    if cursor.rowcount > 0:
        return get_budget_by_id(budget_id)
    return None