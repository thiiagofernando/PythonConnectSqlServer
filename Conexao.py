import pyodbc

#String de Conexao com o Banco

server = 'localhost\SQLEXPRESS'
database = 'Agenda'
username = 'sa'
password  ='12345678'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# variareis para o insert
nome = "Thiago"
email = "Thiago.Fernando@msn.com"
#realiza um insert na tabela Pessoas
cursor.execute("insert into [dbo].[Pessoas](Nome,Email) values('"+nome+"','"+email+"')")
cnxn.commit()


# realiza um select na tabela Pessoas
cursor.execute("Select Nome,Email from [dbo].[Pessoas]")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()