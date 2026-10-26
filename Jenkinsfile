pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Compilando el codigo fuente...'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicacion en el entorno de prueba...'
            }
        }
    }
}
