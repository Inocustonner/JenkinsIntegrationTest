pipeline {
    agent{
        label python
    }
    stages{
        stage("Test") {
            steps {
                git url: "https://github.com/Inocustonner/JenkinsIntegrationTest"
                sh "python test.py"
            }
        }   
    }
}