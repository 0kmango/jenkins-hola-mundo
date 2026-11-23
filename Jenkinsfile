// Jenkinsfile - Pipeline del ejercicio «Hola mundo» (OCY1102)
//
// No necesita plugins adicionales: solo el plugin *Pipeline*, que viene en la
// instalación estándar de Jenkins, y Python 3.11+ disponible en el agente.
//
// Cada etapa falla de verdad si algo se rompe (antes el pipeline solo
// imprimía un texto con `echo`, así que nunca podía fallar).
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Clonar código') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno (Linux/macOS)') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && python -m pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements-dev.txt'
                sh '. .venv/bin/activate && python --version'
            }
        }

        stage('Ejecutar programa') {
            steps {
                sh '. .venv/bin/activate && python hola.py'
            }
        }

        stage('Pruebas automatizadas') {
            steps {
                sh 'mkdir -p resultados'
                sh '. .venv/bin/activate && pytest -q --junitxml=resultados/pruebas.xml'
            }
        }
    }

    post {
        always {
            // El reporte XML queda guardado como artefacto del build.
            archiveArtifacts artifacts: 'resultados/**', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline OK: el programa se ejecuto y las pruebas pasaron.'
        }
        failure {
            echo 'Pipeline FALLO: revisa la etapa en rojo y los artefactos del build.'
        }
    }
}
