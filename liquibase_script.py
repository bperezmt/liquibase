import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

def run_liquibase(command_parts):
    liquibase_path = os.getenv('LIQUIBASE_PATH')
    changelog_file = os.getenv('CHANGELOG_FILE')
    db_url = os.getenv('DB_URL')
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    mysql_connector_path = os.getenv('MYSQL_CONNECTOR_PATH')

    cmd = [
        liquibase_path,
        f"--changeLogFile={changelog_file}",
        f"--url={db_url}",
        f"--username={db_username}",
        f"--password={db_password}",
        f"--classpath={mysql_connector_path}",
    ] + command_parts

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando Liquibase: {e.stderr.decode()}")

def show_menu():
    print("\nMenu de Opciones:")
    print("1. Snapshot")
    print("2. Rollback")
    print("3. Validate")
    print("4. Update")
    print("5. Salir")

def main():
    while True:
        show_menu()
        choice = input("Selecciona una opción (1-5): ")

        if choice == '1':
            output_file = input("Ingresa el nombre del archivo de salida (ej. snapshot.xml): ")
            run_liquibase(["snapshot", f"--output-file={output_file}"])
        elif choice == '2':
            version = input("Ingresa el tag o número de cambios a revertir: ")
            run_liquibase(["rollback", version])
        elif choice == '3':
            run_liquibase(["validate"])
        elif choice == '4':
            run_liquibase(["update"])
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == '__main__':
    main()