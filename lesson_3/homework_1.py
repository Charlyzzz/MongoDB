# coding: utf-8
from pymongo import MongoClient

client = MongoClient()
db = client.school
students = db.students


def lowest_score_for(student_id):
    pipeline = [{'$unwind': '$scores'}, {"$match": {"scores.type": "homework", '_id': student_id}},
                {'$group': {'_id': '$_id', 'score': {'$min': '$scores.score'}}}]

    for y in students.aggregate(pipeline):
        return y['score']


def update_students_scores(student_id, lowest_homework_score):
    query = {'_id': student_id}
    action = {'$pull': {'scores': {'score': lowest_homework_score}}}

    students.update(query, action)

    for x in students.find(query):
        print x


for x in range(0, students.count()):
    update_students_scores(x, lowest_score_for(x))
