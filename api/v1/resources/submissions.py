import json
from flask import Blueprint, abort
from v1.database.models import Submission
from mongoengine import DoesNotExist

submissions = Blueprint('submissions', __name__)

@submissions.route('/')
def get_submission_list():
    return json.dumps([
        {
            'id': submission.id,
            'problem': submission.problem,
            'user': submission.user,
            'language': submission.language,
            'status': submission.status,
            'score': submission.score,
            'exec_time': submission.exec_time,
            'memory_usage': submission.memory_usage,
            'code': submission.code,
        }
        for submission in Submission.objects()
    ]), 200


@submissions.route('/<id>')
@submissions.response(404, 'Submission not found')
@submissions.param('id', 'The submission id')
def get_single_submission(id):
    try:
        submission = Submission.objects.get(id=id)
        return json.dumps({
            'id': submission.id,
            'problem': submission.problem,
            'user': submission.user,
            'language': submission.language,
            'status': submission.status,
            'score': submission.score,
            'exec_time': submission.exec_time,
            'memory_usage': submission.memory_usage,
            'code': submission.code,
        }), 200
    except(DoesNotExist):
        abort(404)
    except:
        abort(500)
