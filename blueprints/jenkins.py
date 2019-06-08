
import flask
import jenkins

connection = jenkins.Jenkins('http://localhost:8081', 'lcsavb', 'rraptnor')

blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods=[ 'GET' ])
def get_jenkins():
    
    print(dir(connection))
    context = {
        'page': 'jenkins',
        'route': {
            'is_public': False
        },
        'jobs': [ connection.get_job_info(j['name'])
            for j in connection.get_jobs()
        ]
    }

    return flask.render_template('jenkins.html', context=context)


@blueprint.route('/jenkins/update/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_update(jobname):
    
    context = {
        'page': 'jenkins-update',
        'route': {
            'is_public': False
        },
    }

    return flask.render_template('jenkins_update.html', context=context)

@blueprint.route('/jenkins', methods=[ 'POST' ])
def post_jenkins_update():
    pass