properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("Checkout"){
        git "https://github.com/MorLiberty/WoG"
    }
    stage("Build"){
        sh label: '', script: 'dos2unix docker-run.sh'
        sh label: '', script: 'sh docker-run.sh'
    }
    stage("Test"){
        try {
            sh label: '', script: 'python Tests/e2e.py'
            currentBuild.result = 'SUCCESS'
        } catch(Exception ValueError) {
            currentBuild.result = 'FAILURE'
            sh "exit 1"
        }
    }
    stage("Finalize"){
        sh label: '', script: 'sudo docker stop wog_mainscore_1'
        sh label: '', script: 'sudo docker login --username mor12324 --password ml14678678'
        sh label: '', script: 'sudo docker push mor12324/scoreapp'
        sh label: '', script: 'sudo docker logout'
    }
}