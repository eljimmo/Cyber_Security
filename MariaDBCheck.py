import mysql.connector



# common security misconfigurations to check for in MariaDB are:
# Root Login Without a Password: It's a bad practice to leave the root account without a password.
# User Accounts With Empty Passwords: Any user account without a password is a potential security risk.
# Remote Root Login: Root login from any host other than localhost can be dangerous.
# Outdated MariaDB Version: Older versions might have known vulnerabilities.
# Use of Deprecated or Unsafe Functions: For example, usage of old passwords.



def check_mariadb_config(host, user, password):
    try:
        # Connect to the MariaDB instance
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Check for root login without a password
        cursor.execute("SELECT host, user, password FROM mysql.user WHERE user='root'")
        for (host, user, password) in cursor:
            if not password:
                print(f"[!] Root login without password from {host}.")

        # Check for accounts with empty passwords
        cursor.execute("SELECT host, user FROM mysql.user WHERE password=''")
        for (host, user) in cursor:
            print(f"[!] User '{user}' from host '{host}' has an empty password.")
        
        # Check for remote root logins
        cursor.execute("SELECT host FROM mysql.user WHERE user='root' AND host <> 'localhost' AND host <> '127.0.0.1'")
        for (host,) in cursor:
            print(f"[!] Root login allowed from remote host: {host}")

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"[!] Error: {err}")
        return

def main():
    host = input("Enter the MariaDB host: ")
    user = input("Enter the user (preferably with high privileges for thorough checks): ")
    password = input("Enter the password: ")

    check_mariadb_config(host, user, password)

if __name__ == "__main__":
    main()
