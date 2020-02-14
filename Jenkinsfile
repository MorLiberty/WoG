properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("checkout"){
        git "https://github.com/MorLiberty/WoG"
    }
    stage("Build"){
        sh label: '', script: 'dos2unix run-docker.sh'
        sh label: '', script: 'sh run-docker.sh'
    }
    stage("Test"){
        sh label: '', script: 'python Test/e2e.py'
    }
    stage("Finalize"){
        sh label: '', script: 'docker stop docker_mainscore_1'
        sh label: '', script: 'docker login --username mor12324 --password ml14678678'
        sh label: '', script: 'docker push mor12324/scoreapp'
        sh label: '', script: 'docker logout'
    }	
}