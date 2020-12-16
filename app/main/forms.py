from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

 title = StringField('Pitch title',validators=[Required()])
 content = TextAreaField('Pitch', validators=[Required()])
 category = SelectField('Category', choices=[('Advertisements','Advertisements'),('Products','Products'),('Projects','Projects'),('Business Ideas','Business Ideas'),('Jokes','Jokes'),('Unpopular Opinions','Unpopular Opinions')], validators=[Required()])
 submit = SubmitField('Submit')
 

class CommentForm(FlaskForm):

 comment = TextAreaField('Comment', validators=[Required()])

 submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Describe yourself.',validators = [Required()])
    submit = SubmitField('Submit')