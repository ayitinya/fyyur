import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = f"postgresql://postgres:postgres@172.25.218.225:5432/{self.database_name}"
        setup_db(self.app, database_path=f"postgresql://postgres:postgres@172.25.218.225:5432/{self.database_name}")

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # test get all questions
    def test_get_all_questions(self):
        res = self.client().get('/questions')
        # data = json.loads(res.data)

        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['success'], True)
        # self.assertTrue(data['total_questions'])
        # self.assertTrue(len(data['questions']))
        # self.assertTrue(data['categories'])
        # self.assertTrue(data['current_category'])

"""
    # # test get all questions with a search term
    # def test_get_all_questions_search(self):
    #     res = self.client().get('/questions?search=search')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])
    
    # # test get all questions with a search term that doesn't exist
    # def test_get_all_questions_search_not_found(self):
    #     res = self.client().get('/questions?search=notfound')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a category
    # def test_get_all_questions_category(self):
    #     res = self.client().get('/questions?category=1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a category that doesn't exist
    # def test_get_all_questions_category_not_found(self):
    #     res = self.client().get('/questions?category=100')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a page
    # def test_get_all_questions_page(self):
    #     res = self.client().get('/questions?page=2')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a page that doesn't exist
    # def test_get_all_questions_page_not_found(self):
    #     res = self.client().get('/questions?page=100')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a page and category
    # def test_get_all_questions_page_category(self):
    #     res = self.client().get('/questions?page=2&category=1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])
    
    # # test get all questions with a page and category that doesn't exist
    # def test_get_all_questions_page_category_not_found(self):
    #     res = self.client().get('/questions?page=100&category=100')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a page and search term
    # def test_get_all_questions_page_search(self):
    #     res = self.client().get('/questions?page=2&search=search')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])
    
    # # test get all questions with a page and search term that doesn't exist
    # def test_get_all_questions_page_search_not_found(self):
    #     res = self.client().get('/questions?page=100&search=notfound')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])
    
    # # test get all questions with a page and category and search term
    # def test_get_all_questions_page_category_search(self):
    #     res = self.client().get('/questions?page=2&category=1&search=search')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])
    
    # # test get all questions with a page and category and search term that doesn't exist
    # def test_get_all_questions_page_category_search_not_found(self):
    #     res = self.client().get('/questions?page=100&category=100&search=notfound')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # # test get all questions with a page and search term and category
    # def test_get_all_questions_page_search_category(self):
    #     res = self.client().get('/questions?page=2&search=search&category=1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['current_category'])

    # #test categories
    # def test_get_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['total_categories'])

    # # test get questions by category
    # def test_get_questions_by_category(self):
    #     res = self.client().get('/categories/1/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(data['current_category'])

    # # test get questions by category that doesn't exist
    # def test_get_questions_by_category_not_found(self):
    #     res = self.client().get('/categories/100/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 0)
    #     self.assertEqual(len(data['questions']), 0)
    #     self.assertTrue(data['current_category'])

    # # test quizzes
    # def test_get_quizzes(self):
    #     res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'type': 'Science', 'id': '1'}})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['question'])

    # # test quizzes with a category that doesn't exist
    # def test_get_quizzes_category_not_found(self):
    #     res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'type': 'Science', 'id': '100'}})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['question'], None)
"""

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()