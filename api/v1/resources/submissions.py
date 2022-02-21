import json
from flask import Blueprint, request, abort, current_app
from v1.database.models import Submission
from mongoengine import DoesNotExist
import random as rand
from datetime import datetime

submissions = Blueprint('submissions', __name__)

possible_problem = (1, 20)
possible_user = (1, 50)
possible_lang = (0, 3)
possible_status = (-2, 6)
possible_score = [0, 10, 15, 20, 25, 50, 60, 75, 80, 100]

@submissions.route('/')
def get_submission_list():
    limit = int(request.args.get('limit') or 10)
    offset = int(request.args.get('offset') or 0)
    sort = request.args.get('sort') or 'timestamp'
    direction = request.args.get('direction') or 'desc'

    submissions = Submission.objects.skip(offset).limit(limit).order_by(f"{'-' if direction == 'desc' else '+'}{sort}")
    count = Submission.objects.count()
    return {
        'count': count,
        'data': json.loads(submissions.to_json()),
    }, 200


@submissions.route('/<id>')
def get_single_submission(id):
    try:
        submission = Submission.objects.get(id=id)
        return json.loads(submission.to_json()), 200
    except(DoesNotExist):
        abort(404)
    except:
        abort(500)


@submissions.route('/recovery')
def recovery_database():
    Submission.drop_collection()
    for _ in range(100000):
        Submission(
            problem=rand.randint(*possible_problem),
            user='user' + str(rand.randint(*possible_user)),
            language=rand.randint(*possible_lang),
            timestamp=datetime(2022, 1, rand.randint(1, 31), rand.randint(0, 23), rand.randint(0, 59), rand.randint(0, 59)),
            status=rand.randint(*possible_status),
            score=rand.choice(possible_score),
            exec_time=rand.randint(0, 2048),
            memory_usage=rand.randint(0, 20480),
        ).save()
    return '', 200
