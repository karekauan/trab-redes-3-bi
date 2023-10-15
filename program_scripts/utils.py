import psycopg2

#STYLES#

title_style = "<h1 style='text-align: center; color: grey;'>Trabalho de Redes</h1>"

declaration_style = "<h1 style='text-align: center; color: black;'>Declaração</h1>"



#DATA#

course_options = [
    'Licenciatura em Química', 'TADS'
]

def declaration(name, year, course):
    f"<span style='font-size:20px'>Eu <b>{name}</b>, aluno do <b>{year}</b> ano do curso de <b>{course}</b>, aceito ser cadastrado no banco de dados deste trabalho.</span>"

#BD#

conn = psycopg2.connect(
        host="database",
        port="5432",
        database="school",
        user="postgres",
        password="postgres"
    )


#FUNCTIONS#

def save_student(name, course, year):

    cursor = conn.cursor()

    insert_query = "INSERT INTO students (name, course, year) VALUES (%s, %s, %s)"
    values = (name, course, year)
    cursor.execute(insert_query, values)

    conn.commit()
    cursor.close()
    conn.close()