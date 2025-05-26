# config.py
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER= DESKTOP-EVNCRN1;"  # Cambia si usas otro nombre de instancia
    "DATABASE=SoporteTecnico;"
    "Trusted_Connection=yes;"
)

CONNECTION_STRING = f"mssql+pyodbc:///?odbc_connect={params}"