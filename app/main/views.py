from . import main
from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User, Comment, Pitch, Like, Dislike
from .forms import CommentForm, PitchForm, UpdateProfile
from .. import db, photos

@main.route('/')
def index():
    title="Perfect Pitch"
    return render_template('index.html', title = title)
@main.route("/pitch/ads")
def pitch_advert():
    Advertisements = Pitch.query.filter_by(category="Advertisements").order_by(Pitch.posted.desc()).all()
    pitches = Pitch.query.all()

    return render_template('ads.html', pitches=pitches,Advertisements = Advertisements)

@main.route("/pitch/Product")
def pitch_products():
    pitches = Pitch.query.all()
    Products = Pitch.query.filter_by(category="Products").order_by(Pitch.posted.desc()).all()
    return render_template('Product.html', pitches=pitches,Products = Products)

@main.route("/pitch/Projects")
def pitch_projects():
    pitches = Pitch.query.all()
    Projects = Pitch.query.filter_by(category="Projects").order_by(Pitch.posted.desc()).all()
    return render_template('Projects.html', pitches=pitches,Projects = Projects)

@main.route("/pitch/Idea")
def pitch_ideas():
    pitches = Pitch.query.all()
     Ideas = Pitch.query.filter_by(category="Business Ideas").order_by(Pitch.posted.desc()).all()
    return render_template('Idea.html', pitches=pitches, Ideas = Ideas)

@main.route("/pitch/jokes")
def pitch_jokes():
    pitches = Pitch.query.all()
    Jokes = Pitch.query.filter_by(category="Jokes").order_by(Pitch.posted.desc()).all()
    return render_template('jokes.html',pitches=pitches, Jokes = Jokes)

@main.route("/pitch/unpopular ")
def pitch_unpopular():
    pitches = Pitch.query.all()
    Unpopular = Pitch.query.filter_by(category="Unpopular Opinions").order_by(Pitch.posted.desc()).all()
    return render_template('unpopular.html',pitches=pitches, Unpopular  = Unpopular )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = f"{uname.capitalize()}"

    if user is None:
        abort (404) 

    return render_template("profile/profile.html", user = user, title=title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    A function that saves the  added pitches
    '''
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        body = pitch_form.content.data
        category = pitch_form.category.data
        title = pitch_form.title.data

        new_pitch = Pitch(title=title, content=body, category = category, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))


    title = 'New Pitch'
    return render_template('new.html', title = title, pitchform = pitch_form)


@main.route('/pitch/<int:pitch_id>/comment',methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    '''
    View comments page function that returns the comment page and its data
    '''

    comment_form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    if pitch is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data

        new_comment = Comment(comment=comment, pitch_id = pitch_id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('.comment', pitch_id=pitch_id))

    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    title = 'Comments'

    return render_template('comment.html', title = title, pitch=pitch ,comment_form = comment_form, comments = comments )





@main.route('/pitch/<int:pitch_id>/like',methods = ['GET','POST'])
def like(pitch_id):
    '''
    View like function that returns likes
    '''
    pitch = Pitch.query.get(pitch_id)

    likes = Like.query.filter_by(pitch_id=pitch_id)


    if Like.query.filter(Like.pitch_id==pitch_id).first():
        return  redirect(url_for('.index'))

    new_like = Like(pitch_id=pitch_id)
    new_like.save_likes()
    return redirect(url_for('main.index'))



@main.route('/pitch/<int:pitch_id>/dislike',methods = ['GET','POST'])
def dislike(pitch_id):
    '''
    View dislike function that returns dislikes
    '''
    pitch = Pitch.query.get(pitch_id)

    pitch_dislikes = Dislike.query.filter_by(pitch_id=pitch_id)

    if Dislike.query.filter(Dislike.pitch_id==pitch_id).first():
        return redirect(url_for('main.index'))

    new_dislike = Dislike(pitch_id=pitch_id)
    new_dislike.save_dislikes()
    return redirect(url_for('main.index')) 
