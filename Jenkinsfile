// This defines a Jenkins continuous integration job pipeline which sets up this project's Poetry environment inside a
// python docker container (set agent/docker/image below to your project's python version), runs unit tests using pytest,
// and reports success/failure back to bitbucket and via email to the last committer.
// All projects with a Jenkinsfile in their root in https://bitbucket.csiro.au/projects/ENERGY should get CI builds running automatically any time a change is pushed to any branch.
pipeline {
    // Defines the Docker image inside of which to run the job.
    agent {
        docker {
            image 'python:3.9.4' // Need to manually match python version to poetry version here to use the correct docker base image
            args  '--net="host"' // net=host allows docker to access the host machine's network, (eg for accessing file shares etc)
        }
    }

    stages{
        stage('install poetry') {
          steps {
            sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -"
          }
        }

        stage('build env') {
          steps {
            // Need to provide git creds here to allow poetry to install packages from bitbucket urls
            withCredentials([gitUsernamePassword(credentialsId: 'your-username')]) {
                sh "$HOME/.poetry/bin/poetry install"
            }
          }
        }

        stage('test') {
            steps {
                 // Credentials are pre-defined inside Jenkins, just specify the 'credentialsId' here to use them. See https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/injecting-secrets
                withCredentials([usernamePassword(credentialsId: 'your-username', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh("pwd")
                    sh("ls -l")
                    sh('$HOME/.poetry/bin/poetry run scripts/test.sh') // single quotes are more secure - http://www.jenkins.io/doc/book/pipeline/jenkinsfile/#string-interpolation
                    archiveArtifacts artifacts: 'htmlcov/*', fingerprint: true
                    sh('$HOME/.poetry/bin/poetry build')
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }

        stage('doc') {
            steps {
                sh('$HOME/.poetry/bin/poetry run ./scripts/gen-doc.sh')
                archiveArtifacts artifacts: 'docs/build/', fingerprint: true
            }
        }
    }

    post {
        always {
            script {
                echo 'Notifying Bitbucket of build status'
                currentBuild.result = currentBuild.result ?: 'SUCCESS'
                notifyBitbucket() // see https://github.com/jenkinsci/stashnotifier-plugin/blob/release/1.x/readme.md
            }
        }
        success {
            echo 'Build successful'
        }
        failure {
            script{
                echo 'Build failed'
            }
        }
        changed {
            script {
                if (currentBuild.currentResult == 'FAILURE') { // Other values: SUCCESS, UNSTABLE
                    // Send an email only if the build status has changed from green/unstable to red
                    emailext subject: '$DEFAULT_SUBJECT',
                        body: '$DEFAULT_CONTENT',
                        recipientProviders: [
                            [$class: 'CulpritsRecipientProvider'],
                            [$class: 'DevelopersRecipientProvider'],
                            [$class: 'RequesterRecipientProvider']
                        ],
                        replyTo: '$DEFAULT_REPLYTO',
                        to: '$DEFAULT_RECIPIENTS'
                }
            }
        }
    }
}
