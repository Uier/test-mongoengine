from mongoengine import Document, DateTimeField, IntField, StringField
from datetime import datetime


class Submission(Document):
    meta = {
        'indexes': [(
            'problem',
            'timestamp',
            'user',
            'language',
            'status',
            'score',
        )]
    }
    problem = IntField(required=True)
    user = StringField(required=True)
    language = IntField(
        required=True,
        min_value=0,
        max_value=3,
        db_field='languageType',
    )
    timestamp = DateTimeField(default=datetime.now)
    status = IntField(default=-2)
    score = IntField(default=-1)
    exec_time = IntField(default=-1, db_field='runTime')
    memory_usage = IntField(default=-1, db_field='memoryUsage')
    code = StringField(required=True)

