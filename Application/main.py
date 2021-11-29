import socket

if __name__ == '__main__':

    s = """\
HTTP/1.1 200 OK

Welcome to Big Data Processing Application
Please type the number that corresponds to which application you woule like to run:
1. Apache Hadoop
2. Apache Spark
3. Jupyter Notebook
4. SonarQube and SonarScanner

visit Apache Hadoop: http://34.134.156.140:9870
visit Jupyter Notebook: http://34.132.63.235:8888
visit SonarQube and SonarScanner: http://34.68.3.207:9000
visit Apache Spark: http://34.136.31.24:8080
"""

    # 'HTTP/1.1 200 OK\n' + \
    # 'Welcome to Big Data Processing Application\n' + \
    # 'Please type the number that corresponds to which application you woule like to run:\n' + \
    # '1. Apache Hadoop\n' + \
    # '2. Apache Spark\n' + \
    # '3. Jupyter Notebook\n' + \
    # '4. SonarQube and SonarScanner\n\n' + \
    # 'visit Apache Hadoop: http://34.134.156.140:9870\n' + \
    # 'visit Apache Spark: http://34.132.63.235:8888\n' + \
    # 'visit Jupyter Notebook: http://34.68.3.207:9000\n' + \
    # 'visit SonarQube and SonarScanner: http://34.136.31.24:8080\n'

    HOST, PORT = '', 1234
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print(request.decode("utf-8"))
        client_connection.sendall(s.encode("utf-8"))
        client_connection.close()