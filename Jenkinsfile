pipeline {
    agent any
    
    parameters {
        string(name: 'BUILD_VERSION', defaultValue: '', description: 'Build version to deploy (e.g., 1.0.0)', trim: true)
        choice(name: 'ENVIRONMENT', choices: ['dev', 'prod'], description: 'Select the environment to deploy to')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Should we run tests?')
    }

    environment {
        // Make sure the build version is set
        BUILD_VERSION = "${params.BUILD_VERSION}"
    }

    stages {
        stage('Validation') {
            steps {
                script {
                    if (params.BUILD_VERSION == null || params.BUILD_VERSION.trim() == "") {
                        error('Build Version is required. Please provide a valid Build Version.')
                    }
                }
            }
        }

        stage('Preparation') {
            steps {
                echo "Preparing for deployment to ${params.ENVIRONMENT} with Build Version: ${params.BUILD_VERSION}"
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (params.ENVIRONMENT == 'prod') {
                        echo 'Deploying to production environment...'
                    } else if (params.ENVIRONMENT == 'dev') {
                        echo 'Deploying to development environment...'
                    }
                    echo "Deploying Build Version: ${params.BUILD_VERSION}"
                }
            }
        }

        stage('Run Tests') {
            when {
                expression { return params.RUN_TESTS }
            }
            steps {
                echo 'Running tests...'
            }
        }
    }

    post {
        always {
            echo 'Post Actions'
        }
    }
}
