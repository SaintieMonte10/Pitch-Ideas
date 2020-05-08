from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch = TextAreaField('Write Your Pitch',validators=[Required()])
    pitch_category = SelectField('Pitch Category',choices=[('Technology-Pitch','Technology Pitch'),('Business-Pitch','Business Pitch'),('Interview-Pitch','Interview Pitch'),('Pickup-Line','Pickup-Line Pitch'),('Promotion-Pitch','Promotion Pitch')],validators=[Required()])
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment about the above Pitch', validators=[Required()])
    submit = SubmitField('Submit Comment')