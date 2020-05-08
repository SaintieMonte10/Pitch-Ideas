from app.models import User,Pitch
from app import db
import unittest

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'clares', password = 'access', email = 'claremonte53@gmail.com')
        self.new_pitch = Pitch(id = 123, pitch_content = 'Pitch content',pitch_category = 'pickup',user=self.new_user)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_content,"Pitch content")
        self.assertEquals(self.new_pitch.pitch_category,'pickup')
        self.assertEquals(self.new_pitch.user,self.new_user)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    