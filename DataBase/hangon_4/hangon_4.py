import time
import mysql.connector  # or psycopg2 for PostgreSQL

# ------------------------------------------------------------
# DB CONNECTION (adjust credentials as needed)
# ------------------------------------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="charles@12345678",
    database="college_db"
)
cursor = conn.cursor()


# ------------------------------------------------------------
# STEP 56: SIMULATE THE N+1 PROBLEM
# ------------------------------------------------------------

def n_plus_one_version():
    query_count = 0
    start = time.time()

    # Query 1: fetch ALL enrollments
    cursor.execute("SELECT enrollment_id, student_id, course_id FROM enrollments")
    enrollments = cursor.fetchall()
    query_count += 1   # this is the "1" in N+1

    results = []
    for enrollment_id, student_id, course_id in enrollments:
        # Query 2, 3, 4 ... N: one SEPARATE query PER ROW
        cursor.execute(
            "SELECT first_name, last_name FROM students WHERE student_id = %s",
            (student_id,)
        )
        student = cursor.fetchone()
        query_count += 1   # this happens once per enrollment — the "N" in N+1

        results.append((enrollment_id, student[0], student[1], course_id))

    elapsed = time.time() - start
    print(f"[N+1 VERSION] Queries executed: {query_count}")
    print(f"[N+1 VERSION] Time taken: {elapsed:.4f} seconds")
    return results, query_count, elapsed


def join_version():
    query_count = 0
    start = time.time()

    cursor.execute("""
        SELECT e.enrollment_id, s.first_name, s.last_name, e.course_id
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
    """)
    results = cursor.fetchall()
    query_count += 1   # only ONE query total, no matter how many rows

    elapsed = time.time() - start
    print(f"[JOIN VERSION] Queries executed: {query_count}")
    print(f"[JOIN VERSION] Time taken: {elapsed:.4f} seconds")
    return results, query_count, elapsed

if __name__ == "__main__":
    n_plus_one_version()
    join_version()
    print("=" * 50)
    n1_results, n1_count, n1_time = n_plus_one_version()

    print("=" * 50)
    join_results, join_count, join_time = join_version()

    print("=" * 50)
    print(f"N+1 version:  {n1_count} queries, {n1_time:.4f}s")
    print(f"JOIN version: {join_count} query,  {join_time:.4f}s")
    print(f"Extra queries avoided: {n1_count - join_count}")

    # Sanity check — both should return the same number of rows
    assert len(n1_results) == len(join_results), "Row counts don't match!"
    print("Data consistency check passed — both return identical row counts.")

    cursor.close()
    conn.close()