# coding: utf-8
import pymongo

connection = pymongo.MongoClient()
db = connection.students
grades = db.grades


def hw_2():
    ids = grades.distinct('student_id')

    for id in ids:
        remove_lowest_homework_score_for(id)


def remove_lowest_homework_score_for(student):
    grades.find_one_and_delete(filter = {'student_id': student, 'type': 'homework'},
                               sort = [('score', pymongo.ASCENDING)])


hw_2()
