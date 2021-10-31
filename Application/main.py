if __name__ == '__main__':
    ports = {'1': '9870',
             '2': '8080',
             '3': "8888",
             '4': '9000'}

    s = 'Welcome to Big Data Processing Application\n' + \
        'Please type the number that corresponds to which application you woule like to run:\n' + \
        '1. Apache Hadoop\n' \
        '2. Apache Spark\n' \
        '3. Jupyter Notebook\n' \
        '4. SonarQube and SonarScanner\n' + \
        'Type the number here >\n' + \
        'Note: Type other key to quit the program'

    while True:
        option = input(s)
        if option == '1':
            print("visit Apache Hadoop: http://34.134.156.140:9870\n")
        elif option == '2':
            print("visit Apache Spark: http://34.132.63.235:8888\n")
        elif option == '3':
            print("visit Jupyter Notebook: http://34.68.3.207:9000\n")
        elif option == '4':
            print("visit SonarQube and SonarScanner: http://34.136.31.24:8080\n")
        else:
            break