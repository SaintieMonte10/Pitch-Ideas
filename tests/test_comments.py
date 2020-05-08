import unittest
from app.models import Pitch, User, Comment
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_anto = User(username='clares',password='password',email='anto@mail.com')
        self.new_pitch = Pitch(pitch_content = "Pitch Test", pitch_category='Technology',user=self.user_anto)
        self.new_comment = Comment(comment_content = "Test Comment", pitch=self.new_pitch, user=self.user_anto)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"Test Comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        self.assertEquals(self.new_comment.user,self.user_anto)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)