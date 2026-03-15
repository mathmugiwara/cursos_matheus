from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from functools import wraps
from io import StringIO
import threading
import json
import sys
import os
from sqlalchemy import text, inspect as sa_inspect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'matheusDevPlatforma2024!@#SecureR4nd0m')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///plataforma.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar esta página.'

# ─────────────────────────── MODELS ───────────────────────────

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='student')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active_user = db.Column(db.Boolean, default=True)
    modules = db.relationship('UserModule', backref='user', lazy=True, cascade='all, delete-orphan')
    progress = db.relationship('LessonProgress', backref='user', lazy=True, cascade='all, delete-orphan')
    submissions = db.relationship('ExerciseSubmission', backref='user', lazy=True, cascade='all, delete-orphan')

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    short_name = db.Column(db.String(80))
    description = db.Column(db.Text)
    price = db.Column(db.Float, default=0.0)
    duration = db.Column(db.String(100))
    level = db.Column(db.String(50))
    color = db.Column(db.String(20), default='purple')
    icon = db.Column(db.String(10), default='🐍')
    is_active = db.Column(db.Boolean, default=True)
    lessons = db.relationship('Lesson', backref='module', lazy=True, order_by='Lesson.order')
    users = db.relationship('UserModule', backref='module', lazy=True)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200))
    content = db.Column(db.Text)
    week_number = db.Column(db.Integer, default=1)
    order = db.Column(db.Integer, default=1)
    duration_minutes = db.Column(db.Integer, default=60)
    exercises = db.relationship('Exercise', backref='lesson', lazy=True, order_by='Exercise.order')
    progress_records = db.relationship('LessonProgress', backref='lesson', lazy=True)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    starter_code = db.Column(db.Text, default='')
    expected_output = db.Column(db.Text)
    hint = db.Column(db.Text)
    points = db.Column(db.Integer, default=10)
    order = db.Column(db.Integer, default=1)
    submissions = db.relationship('ExerciseSubmission', backref='exercise', lazy=True)

class UserModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid_amount = db.Column(db.Float, default=0.0)

class LessonProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('user_id', 'lesson_id'),)

class ExerciseSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    code = db.Column(db.Text)
    passed = db.Column(db.Boolean, default=False)
    output = db.Column(db.Text)
    error = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    attempts = db.Column(db.Integer, default=1)

class CallAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class CallSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=True)
    week_number = db.Column(db.Integer, nullable=True)
    scheduled_date = db.Column(db.Date, nullable=False)
    scheduled_time = db.Column(db.String(5), nullable=False)
    status = db.Column(db.String(20), default='pending')
    discord_username = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_rel = db.relationship('User', backref='calls')
    module_rel = db.relationship('Module', backref='call_schedules')

class ProjectSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False)
    scheduled_time = db.Column(db.String(5), nullable=False)
    project_title = db.Column(db.String(200), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_rel = db.relationship('User', backref='project_sessions')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ─────────────────────────── SECURITY: Login Rate Limiting ───────────────────────────

_login_attempts = {}

def _check_rate_limit(ip):
    now = datetime.utcnow()
    if ip in _login_attempts:
        attempts, first_attempt = _login_attempts[ip]
        if (now - first_attempt).total_seconds() > 300:
            _login_attempts[ip] = (1, now)
            return True
        if attempts >= 10:
            return False
        _login_attempts[ip] = (attempts + 1, first_attempt)
    else:
        _login_attempts[ip] = (1, now)
    return True

def _sanitize_input(text, max_length=500):
    if not text:
        return text
    return text.strip()[:max_length]

# ─────────────────────────── CODE EXECUTOR ───────────────────────────

def execute_code(code, timeout=5):
    FORBIDDEN = ['import os', 'import sys', 'import subprocess', '__import__',
                 'eval(', 'exec(', 'open(', 'compile(', 'globals(', 'locals(',
                 'getattr(', 'setattr(', 'delattr(', '__class__', '__subclasses__',
                 'breakpoint(', 'input(']
    for fb in FORBIDDEN:
        if fb in code:
            return {'output': '', 'error': f'Operação não permitida: {fb}', 'success': False}

    if len(code) > 5000:
        return {'output': '', 'error': 'Código muito longo (máx 5000 caracteres)', 'success': False}

    result = {'output': '', 'error': None, 'success': False}

    def target():
        buf = StringIO()
        old_out = sys.stdout
        sys.stdout = buf
        safe = {
            '__builtins__': {
                'print': print, 'len': len, 'range': range,
                'int': int, 'float': float, 'str': str, 'bool': bool,
                'list': list, 'dict': dict, 'tuple': tuple, 'set': set,
                'type': type, 'isinstance': isinstance,
                'enumerate': enumerate, 'zip': zip,
                'map': map, 'filter': filter, 'sorted': sorted,
                'sum': sum, 'max': max, 'min': min, 'abs': abs,
                'round': round, 'True': True, 'False': False, 'None': None,
                'Exception': Exception, 'ValueError': ValueError,
                'TypeError': TypeError, 'ZeroDivisionError': ZeroDivisionError,
                'KeyError': KeyError, 'IndexError': IndexError,
            }
        }
        try:
            exec(code, safe)
            result['output'] = buf.getvalue()
            result['success'] = True
        except Exception as e:
            result['output'] = buf.getvalue()
            result['error'] = str(e)
            result['success'] = False
        finally:
            sys.stdout = old_out

    t = threading.Thread(target=target)
    t.daemon = True
    t.start()
    t.join(timeout)
    if t.is_alive():
        result['error'] = 'Tempo limite excedido! Verifique se há loops infinitos.'
    return result

# ─────────────────────────── AUTH ROUTES ───────────────────────────

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard') if current_user.role == 'admin' else url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        ip = request.remote_addr
        if not _check_rate_limit(ip):
            flash('Muitas tentativas de login. Aguarde 5 minutos.', 'error')
            return render_template('login.html')
        username = _sanitize_input(request.form.get('username', ''), 80)
        password = request.form.get('password', '')
        if not username or not password:
            flash('Preencha todos os campos.', 'error')
            return render_template('login.html')
        user = User.query.filter_by(username=username).first()
        if user and user.is_active_user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            return redirect(url_for('admin_dashboard') if user.role == 'admin' else url_for('dashboard'))
        flash('Usuário ou senha incorretos.', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ─────────────────────────── STUDENT ROUTES ───────────────────────────

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    user_modules = UserModule.query.filter_by(user_id=current_user.id).all()
    modules_data = []
    for um in user_modules:
        mod = um.module
        total = len(mod.lessons)
        lesson_ids = [l.id for l in mod.lessons]
        completed = LessonProgress.query.filter_by(user_id=current_user.id)\
            .filter(LessonProgress.lesson_id.in_(lesson_ids)).count() if lesson_ids else 0
        progress = int(completed / total * 100) if total > 0 else 0
        modules_data.append({'module': mod, 'progress': progress, 'completed': completed, 'total': total})
    return render_template('student/dashboard.html', modules_data=modules_data)

@app.route('/module/<int:module_id>')
@login_required
def module_view(module_id):
    if current_user.role != 'admin':
        um = UserModule.query.filter_by(user_id=current_user.id, module_id=module_id).first()
        if not um:
            flash('Você não tem acesso a este módulo.', 'error')
            return redirect(url_for('dashboard'))
    mod = Module.query.get_or_404(module_id)
    completed_ids = {lp.lesson_id for lp in LessonProgress.query.filter_by(user_id=current_user.id).all()}
    lessons_data = []
    for i, lesson in enumerate(mod.lessons):
        unlocked = i == 0 or mod.lessons[i - 1].id in completed_ids
        lessons_data.append({
            'lesson': lesson,
            'completed': lesson.id in completed_ids,
            'unlocked': unlocked,
            'ex_count': len(lesson.exercises)
        })
    return render_template('student/module.html', mod=mod, lessons_data=lessons_data)

@app.route('/lesson/<int:lesson_id>')
@login_required
def lesson_view(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    mod = lesson.module
    if current_user.role != 'admin':
        um = UserModule.query.filter_by(user_id=current_user.id, module_id=mod.id).first()
        if not um:
            flash('Sem acesso a este módulo.', 'error')
            return redirect(url_for('dashboard'))

        completed_ids = {lp.lesson_id for lp in LessonProgress.query.filter_by(user_id=current_user.id).all()}
        all_lessons = mod.lessons
        idx = next((i for i, l in enumerate(all_lessons) if l.id == lesson_id), 0)
        unlocked = idx == 0 or all_lessons[idx - 1].id in completed_ids
        if not unlocked:
            flash('Complete a aula anterior para desbloquear esta.', 'error')
            return redirect(url_for('module_view', module_id=mod.id))

    is_completed = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first() is not None
    ex_passed = {
        ex.id: ExerciseSubmission.query.filter_by(user_id=current_user.id, exercise_id=ex.id, passed=True).first() is not None
        for ex in lesson.exercises
    }
    ex_last_code = {}
    for ex in lesson.exercises:
        sub = ExerciseSubmission.query.filter_by(user_id=current_user.id, exercise_id=ex.id)\
            .order_by(ExerciseSubmission.submitted_at.desc()).first()
        ex_last_code[ex.id] = sub.code if sub else ex.starter_code

    all_lessons = mod.lessons
    idx = next((i for i, l in enumerate(all_lessons) if l.id == lesson_id), 0)
    completed_ids_nav = {lp.lesson_id for lp in LessonProgress.query.filter_by(user_id=current_user.id).all()}
    prev_lesson = all_lessons[idx - 1] if idx > 0 else None
    raw_next = all_lessons[idx + 1] if idx < len(all_lessons) - 1 else None
    next_lesson = raw_next if raw_next and (idx == 0 or lesson_id in completed_ids_nav or current_user.role == 'admin') else None
    all_done = all(ex_passed.values()) if lesson.exercises else True

    return render_template('student/lesson.html',
        lesson=lesson, mod=mod, is_completed=is_completed,
        ex_passed=ex_passed, ex_last_code=ex_last_code,
        all_done=all_done, prev_lesson=prev_lesson, next_lesson=next_lesson)

@app.route('/lesson/<int:lesson_id>/exercises')
@login_required
def lesson_exercises(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    mod = lesson.module
    if current_user.role != 'admin':
        um = UserModule.query.filter_by(user_id=current_user.id, module_id=mod.id).first()
        if not um:
            flash('Sem acesso a este módulo.', 'error')
            return redirect(url_for('dashboard'))
        completed_ids = {lp.lesson_id for lp in LessonProgress.query.filter_by(user_id=current_user.id).all()}
        all_lessons = mod.lessons
        idx = next((i for i, l in enumerate(all_lessons) if l.id == lesson_id), 0)
        unlocked = idx == 0 or all_lessons[idx - 1].id in completed_ids
        if not unlocked:
            flash('Complete a aula anterior para desbloquear esta.', 'error')
            return redirect(url_for('module_view', module_id=mod.id))
    if not lesson.exercises:
        flash('Esta aula não possui exercícios.', 'warning')
        return redirect(url_for('lesson_view', lesson_id=lesson_id))
    is_completed = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first() is not None
    ex_passed = {
        ex.id: ExerciseSubmission.query.filter_by(user_id=current_user.id, exercise_id=ex.id, passed=True).first() is not None
        for ex in lesson.exercises
    }
    ex_last_code = {}
    for ex in lesson.exercises:
        sub = ExerciseSubmission.query.filter_by(user_id=current_user.id, exercise_id=ex.id)\
            .order_by(ExerciseSubmission.submitted_at.desc()).first()
        ex_last_code[ex.id] = sub.code if sub else ''
    all_done = all(ex_passed.values()) if lesson.exercises else True
    return render_template('student/exercises.html',
        lesson=lesson, mod=mod, is_completed=is_completed,
        ex_passed=ex_passed, ex_last_code=ex_last_code, all_done=all_done)

@app.route('/complete-lesson/<int:lesson_id>', methods=['POST'])
@login_required
def complete_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if current_user.role != 'admin':
        um = UserModule.query.filter_by(user_id=current_user.id, module_id=lesson.module_id).first()
        if not um:
            return jsonify({'success': False})
    existing = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson_id).first()
    if not existing:
        db.session.add(LessonProgress(user_id=current_user.id, lesson_id=lesson_id))
        db.session.commit()
    return jsonify({'success': True})

@app.route('/submit-exercise', methods=['POST'])
@login_required
def submit_exercise():
    data = request.get_json()
    exercise_id = data.get('exercise_id')
    code = data.get('code', '')
    exercise = Exercise.query.get_or_404(exercise_id)
    lesson = exercise.lesson
    if current_user.role != 'admin':
        um = UserModule.query.filter_by(user_id=current_user.id, module_id=lesson.module_id).first()
        if not um:
            return jsonify({'success': False, 'message': 'Sem acesso'})

    result = execute_code(code)
    passed = False
    if exercise.expected_output:
        passed = result['success'] and result['output'].strip() == exercise.expected_output.strip()
    else:
        passed = result['success'] and bool(result['output'].strip())

    existing = ExerciseSubmission.query.filter_by(user_id=current_user.id, exercise_id=exercise_id)\
        .order_by(ExerciseSubmission.submitted_at.desc()).first()
    if existing:
        existing.code = code
        existing.passed = passed
        existing.output = result['output']
        existing.error = result.get('error')
        existing.submitted_at = datetime.utcnow()
        existing.attempts += 1
    else:
        db.session.add(ExerciseSubmission(
            user_id=current_user.id, exercise_id=exercise_id,
            code=code, passed=passed, output=result['output'], error=result.get('error')
        ))
    db.session.commit()

    return jsonify({
        'success': result['success'],
        'passed': passed,
        'output': result['output'],
        'error': result.get('error'),
        'expected': exercise.expected_output
    })

@app.route('/profile')
@login_required
def profile():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    user_modules = UserModule.query.filter_by(user_id=current_user.id).all()
    total_lessons = total_completed = total_ex = total_passed = 0
    modules_summary = []
    for um in user_modules:
        mod = um.module
        t = len(mod.lessons)
        lesson_ids = [l.id for l in mod.lessons]
        c = LessonProgress.query.filter_by(user_id=current_user.id)\
            .filter(LessonProgress.lesson_id.in_(lesson_ids)).count() if lesson_ids else 0
        all_ex = [ex for l in mod.lessons for ex in l.exercises]
        ex_ids = [e.id for e in all_ex]
        passed = ExerciseSubmission.query.filter_by(user_id=current_user.id, passed=True)\
            .filter(ExerciseSubmission.exercise_id.in_(ex_ids)).count() if ex_ids else 0
        total_lessons += t; total_completed += c
        total_ex += len(all_ex); total_passed += passed
        modules_summary.append({'module': mod, 'completed': c, 'total': t,
                                 'progress': int(c/t*100) if t else 0,
                                 'ex_passed': passed, 'ex_total': len(all_ex)})
    recent = ExerciseSubmission.query.filter_by(user_id=current_user.id)\
        .order_by(ExerciseSubmission.submitted_at.desc()).limit(8).all()
    stats = {'modules': len(user_modules), 'completed_lessons': total_completed,
             'total_lessons': total_lessons, 'passed_ex': total_passed, 'total_ex': total_ex}
    return render_template('student/profile.html', stats=stats,
                           modules_summary=modules_summary, recent=recent)

# ─────────────────────────── MINHA CONTA ───────────────────────────

@app.route('/minha-conta', methods=['GET', 'POST'])
@login_required
def minha_conta():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'change_password':
            current_pw = request.form.get('current_password', '')
            new_pw = request.form.get('new_password', '')
            confirm_pw = request.form.get('confirm_password', '')
            if not current_pw or not new_pw or not confirm_pw:
                flash('Preencha todos os campos.', 'error')
            elif not check_password_hash(current_user.password_hash, current_pw):
                flash('Senha atual incorreta.', 'error')
            elif len(new_pw) < 6:
                flash('A nova senha deve ter pelo menos 6 caracteres.', 'error')
            elif new_pw != confirm_pw:
                flash('As senhas não coincidem.', 'error')
            else:
                current_user.password_hash = generate_password_hash(new_pw)
                db.session.commit()
                flash('Senha alterada com sucesso!', 'success')
        elif action == 'update_profile':
            new_email = request.form.get('email', '').strip()
            if new_email:
                existing = User.query.filter(User.email == new_email, User.id != current_user.id).first()
                if existing:
                    flash('Este e-mail já está em uso.', 'error')
                else:
                    current_user.email = new_email
                    db.session.commit()
                    flash('Perfil atualizado!', 'success')
            else:
                current_user.email = None
                db.session.commit()
                flash('Perfil atualizado!', 'success')
        return redirect(url_for('minha_conta'))

    # Stats
    user_modules = UserModule.query.filter_by(user_id=current_user.id).all()
    total_lessons = total_completed = 0
    for um in user_modules:
        mod = um.module
        t = len(mod.lessons)
        lesson_ids = [l.id for l in mod.lessons]
        c = LessonProgress.query.filter_by(user_id=current_user.id)\
            .filter(LessonProgress.lesson_id.in_(lesson_ids)).count() if lesson_ids else 0
        total_lessons += t
        total_completed += c
    calls_count = CallSchedule.query.filter_by(user_id=current_user.id).count()
    stats = {
        'modules': len(user_modules),
        'completed_lessons': total_completed,
        'total_lessons': total_lessons,
        'calls': calls_count,
    }
    return render_template('student/account.html', stats=stats)

# ─────────────────────────── ROADMAP ───────────────────────────

@app.route('/roadmap')
@login_required
def roadmap():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    user_module_ids = {um.module_id for um in UserModule.query.filter_by(user_id=current_user.id).all()}
    all_modules = Module.query.filter_by(is_active=True).order_by(Module.id).all()
    modules_info = []
    for mod in all_modules:
        owned = mod.id in user_module_ids
        total = len(mod.lessons)
        completed = 0
        if owned:
            lesson_ids = [l.id for l in mod.lessons]
            completed = LessonProgress.query.filter_by(user_id=current_user.id)\
                .filter(LessonProgress.lesson_id.in_(lesson_ids)).count() if lesson_ids else 0
        progress = int(completed / total * 100) if total > 0 else 0
        modules_info.append({
            'module': mod, 'owned': owned, 'progress': progress,
            'completed': completed, 'total': total
        })
    return render_template('student/roadmap.html', modules_info=modules_info)

# ─────────────────────────── CALL SCHEDULING ───────────────────────────

@app.route('/schedule-call')
@login_required
def schedule_call():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    my_calls = CallSchedule.query.filter_by(user_id=current_user.id)\
        .order_by(CallSchedule.scheduled_date.desc()).all()
    availability = CallAvailability.query.filter_by(is_active=True).all()
    avail_map = {}
    for a in availability:
        if a.day_of_week not in avail_map:
            avail_map[a.day_of_week] = []
        avail_map[a.day_of_week].append({'start': a.start_time, 'end': a.end_time})

    # Build call quota: 1 call per week per owned module
    user_modules = UserModule.query.filter_by(user_id=current_user.id).all()
    all_weeks = []
    for um in user_modules:
        mod = um.module
        weeks_q = db.session.query(Lesson.week_number, Lesson.title)\
            .filter_by(module_id=mod.id)\
            .order_by(Lesson.week_number, Lesson.order).all()
        seen = set()
        for wn, wt in weeks_q:
            if wn not in seen:
                seen.add(wn)
                all_weeks.append({
                    'module_id': mod.id,
                    'module_name': mod.short_name or mod.name,
                    'module_icon': mod.icon,
                    'week_number': wn,
                    'week_title': wt,
                })

    # Which (module_id, week_number) already have a non-cancelled call
    booked_weeks = set()
    for c in my_calls:
        if c.status in ['pending', 'confirmed', 'completed'] and c.module_id and c.week_number:
            booked_weeks.add((c.module_id, c.week_number))

    unbooked_weeks = [w for w in all_weeks
                      if (w['module_id'], w['week_number']) not in booked_weeks]
    total_calls = len(all_weeks)
    used_calls = len(booked_weeks)
    can_schedule = len(unbooked_weeks) > 0

    booked_slots = CallSchedule.query.filter(
        CallSchedule.status.in_(['pending', 'confirmed'])
    ).all()
    booked = [{'date': str(c.scheduled_date), 'time': c.scheduled_time} for c in booked_slots]

    booked_weeks_data = [w for w in all_weeks
                         if (w['module_id'], w['week_number']) in booked_weeks]

    return render_template('student/schedule.html',
        my_calls=my_calls, avail_map=json.dumps(avail_map),
        can_schedule=can_schedule,
        unbooked_weeks=json.dumps(unbooked_weeks),
        unbooked_weeks_raw=unbooked_weeks,
        booked_weeks_data=booked_weeks_data,
        total_calls=total_calls, used_calls=used_calls,
        booked_slots=json.dumps(booked))

@app.route('/book-call', methods=['POST'])
@login_required
def book_call():
    data = request.get_json()
    date_str = data.get('date')
    time_str = data.get('time')
    discord = _sanitize_input(data.get('discord', ''), 100)
    notes = _sanitize_input(data.get('notes', ''), 500)
    module_id = data.get('module_id')
    week_number = data.get('week_number')

    if not date_str or not time_str:
        return jsonify({'success': False, 'message': 'Data e horário obrigatórios.'})
    if not module_id or week_number is None:
        return jsonify({'success': False, 'message': 'Selecione o módulo e a semana da call.'})

    # Validate student owns this module
    owns = UserModule.query.filter_by(
        user_id=current_user.id, module_id=module_id
    ).first()
    if not owns:
        return jsonify({'success': False, 'message': 'Você não possui acesso a este módulo.'})

    # 1 call per (module, week) — check for existing non-cancelled call
    week_taken = CallSchedule.query.filter_by(
        user_id=current_user.id, module_id=module_id, week_number=week_number
    ).filter(CallSchedule.status.in_(['pending', 'confirmed', 'completed'])).first()
    if week_taken:
        return jsonify({'success': False, 'message': 'Esta semana já possui uma call agendada.'})

    try:
        sched_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'success': False, 'message': 'Data inválida.'})

    # Check slot not already taken by someone else
    slot_taken = CallSchedule.query.filter_by(
        scheduled_date=sched_date, scheduled_time=time_str
    ).filter(CallSchedule.status.in_(['pending', 'confirmed'])).first()
    if slot_taken:
        return jsonify({'success': False, 'message': 'Horário já reservado. Escolha outro.'})

    call = CallSchedule(
        user_id=current_user.id, scheduled_date=sched_date,
        scheduled_time=time_str, discord_username=discord, notes=notes,
        module_id=module_id, week_number=week_number
    )
    db.session.add(call)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Call agendada com sucesso!'})

@app.route('/admin/calls')
@admin_required
def admin_calls():
    calls = CallSchedule.query.order_by(CallSchedule.scheduled_date.desc()).all()
    availability = CallAvailability.query.order_by(CallAvailability.day_of_week).all()
    return render_template('admin/calls.html', calls=calls, availability=availability)

@app.route('/admin/update-call-status', methods=['POST'])
@admin_required
def admin_update_call_status():
    call_id = request.form.get('call_id', type=int)
    new_status = request.form.get('status')
    call = CallSchedule.query.get_or_404(call_id)
    call.status = new_status
    db.session.commit()
    flash(f'Status atualizado para {new_status}.', 'success')
    return redirect(url_for('admin_calls'))

@app.route('/admin/set-availability', methods=['POST'])
@admin_required
def admin_set_availability():
    if request.is_json:
        data = request.get_json()
        CallAvailability.query.delete()
        for slot in data.get('slots', []):
            db.session.add(CallAvailability(
                day_of_week=slot['day'], start_time=slot['start'],
                end_time=slot['end'], is_active=True
            ))
        db.session.commit()
        return jsonify({'success': True})
    else:
        CallAvailability.query.delete()
        for day in range(7):
            enabled = request.form.get(f'day_{day}_on')
            if enabled:
                start = request.form.get(f'day_{day}_start', '09:00')
                end = request.form.get(f'day_{day}_end', '18:00')
                if start and end:
                    db.session.add(CallAvailability(
                        day_of_week=day, start_time=start,
                        end_time=end, is_active=True
                    ))
        db.session.commit()
        flash('Disponibilidade atualizada com sucesso!', 'success')
        return redirect(url_for('admin_calls'))

# ─────────────────────────── PROJETO PRÁTICO ───────────────────────────

@app.route('/projeto-pratico')
@login_required
def projeto_pratico():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    existing = ProjectSession.query.filter_by(user_id=current_user.id).first()
    availability = CallAvailability.query.filter_by(is_active=True).all()
    avail_map = {}
    for a in availability:
        if a.day_of_week not in avail_map:
            avail_map[a.day_of_week] = []
        avail_map[a.day_of_week].append({'start': a.start_time, 'end': a.end_time})
    booked_slots = ProjectSession.query.filter(
        ProjectSession.status.in_(['pending', 'confirmed'])
    ).all()
    booked = [{'date': str(s.scheduled_date), 'time': s.scheduled_time} for s in booked_slots]
    return render_template('student/projeto_pratico.html',
        existing=existing, avail_map=json.dumps(avail_map),
        booked_slots=json.dumps(booked))

@app.route('/book-projeto', methods=['POST'])
@login_required
def book_projeto():
    data = request.get_json()
    date_str = data.get('date')
    time_str = data.get('time')
    title = _sanitize_input(data.get('title', ''), 200)
    description = _sanitize_input(data.get('description', ''), 2000)
    if not date_str or not time_str or not title or not description:
        return jsonify({'success': False, 'message': 'Todos os campos são obrigatórios.'})
    try:
        sched_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'success': False, 'message': 'Data inválida.'})
    existing_slot = ProjectSession.query.filter_by(
        scheduled_date=sched_date, scheduled_time=time_str
    ).filter(ProjectSession.status.in_(['pending', 'confirmed'])).first()
    if existing_slot and existing_slot.user_id != current_user.id:
        return jsonify({'success': False, 'message': 'Este horário já está reservado.'})
    session_obj = ProjectSession.query.filter_by(user_id=current_user.id).first()
    if session_obj:
        session_obj.scheduled_date = sched_date
        session_obj.scheduled_time = time_str
        session_obj.project_title = title
        session_obj.project_description = description
        session_obj.status = 'pending'
    else:
        session_obj = ProjectSession(
            user_id=current_user.id, scheduled_date=sched_date,
            scheduled_time=time_str, project_title=title,
            project_description=description
        )
        db.session.add(session_obj)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Sessão de projeto agendada com sucesso!'})

@app.route('/admin/projetos')
@admin_required
def admin_projetos():
    sessions = ProjectSession.query.order_by(ProjectSession.scheduled_date.desc()).all()
    return render_template('admin/projetos.html', sessions=sessions)

@app.route('/admin/update-projeto-status', methods=['POST'])
@admin_required
def admin_update_projeto_status():
    proj_id = request.form.get('proj_id', type=int)
    new_status = request.form.get('status')
    proj = ProjectSession.query.get_or_404(proj_id)
    proj.status = new_status
    db.session.commit()
    flash(f'Status atualizado para {new_status}.', 'success')
    return redirect(url_for('admin_projetos'))

# ─────────────────────────── ADMIN ROUTES ───────────────────────────

@app.route('/admin')
@admin_required
def admin_dashboard():
    total_students = User.query.filter_by(role='student').count()
    total_revenue = db.session.query(db.func.sum(UserModule.paid_amount)).scalar() or 0
    total_sales = UserModule.query.count()
    modules = Module.query.all()
    module_stats = []
    for mod in modules:
        ums = UserModule.query.filter_by(module_id=mod.id).all()
        rev = sum(u.paid_amount for u in ums)
        module_stats.append({'module': mod, 'revenue': rev, 'count': len(ums)})
    recent_students = User.query.filter_by(role='student').order_by(User.created_at.desc()).limit(6).all()

    from sqlalchemy import extract
    import calendar
    monthly = []
    now = datetime.utcnow()
    for i in range(5, -1, -1):
        month_offset = (now.month - 1 - i) % 12 + 1
        year_offset = now.year + ((now.month - 1 - i) // 12)
        rev = db.session.query(db.func.sum(UserModule.paid_amount)).filter(
            extract('month', UserModule.assigned_at) == month_offset,
            extract('year', UserModule.assigned_at) == year_offset
        ).scalar() or 0
        monthly.append({'month': calendar.month_abbr[month_offset], 'revenue': float(rev)})

    return render_template('admin/dashboard.html',
        total_students=total_students, total_revenue=total_revenue,
        total_sales=total_sales, module_stats=module_stats,
        recent_students=recent_students, monthly_data=json.dumps(monthly))

@app.route('/admin/students')
@admin_required
def admin_students():
    students = User.query.filter_by(role='student').order_by(User.created_at.desc()).all()
    students_data = []
    for s in students:
        ums = UserModule.query.filter_by(user_id=s.id).all()
        total_p = total_t = 0
        for um in ums:
            t = len(um.module.lessons)
            ids = [l.id for l in um.module.lessons]
            c = LessonProgress.query.filter_by(user_id=s.id)\
                .filter(LessonProgress.lesson_id.in_(ids)).count() if ids else 0
            total_t += t; total_p += c
        avg = int(total_p / total_t * 100) if total_t > 0 else 0
        students_data.append({'student': s, 'modules': ums, 'avg_progress': avg})
    all_modules = Module.query.filter_by(is_active=True).all()
    return render_template('admin/students.html', students_data=students_data, all_modules=all_modules)

@app.route('/admin/student/<int:student_id>')
@admin_required
def admin_student_detail(student_id):
    student = User.query.get_or_404(student_id)
    user_modules = UserModule.query.filter_by(user_id=student_id).all()
    all_modules = Module.query.filter_by(is_active=True).all()
    assigned_ids = [um.module_id for um in user_modules]
    modules_data = []
    for um in user_modules:
        mod = um.module
        t = len(mod.lessons)
        ids = [l.id for l in mod.lessons]
        c = LessonProgress.query.filter_by(user_id=student_id)\
            .filter(LessonProgress.lesson_id.in_(ids)).count() if ids else 0
        lesson_details = []
        for lesson in mod.lessons:
            lp = LessonProgress.query.filter_by(user_id=student_id, lesson_id=lesson.id).first()
            ex_ids = [e.id for e in lesson.exercises]
            ep = ExerciseSubmission.query.filter_by(user_id=student_id, passed=True)\
                .filter(ExerciseSubmission.exercise_id.in_(ex_ids)).count() if ex_ids else 0
            lesson_details.append({'lesson': lesson, 'completed': lp is not None,
                                   'ex_passed': ep, 'ex_total': len(lesson.exercises)})
        modules_data.append({'um': um, 'module': mod, 'completed': c, 'total': t,
                             'progress': int(c/t*100) if t else 0, 'details': lesson_details})
    return render_template('admin/student_detail.html',
        student=student, modules_data=modules_data,
        all_modules=all_modules, assigned_ids=assigned_ids)

@app.route('/admin/assign-module', methods=['POST'])
@admin_required
def admin_assign_module():
    student_id = request.form.get('student_id', type=int)
    module_id = request.form.get('module_id', type=int)
    paid = request.form.get('paid_amount', type=float, default=0.0)
    if UserModule.query.filter_by(user_id=student_id, module_id=module_id).first():
        flash('Aluno já tem acesso a este módulo.', 'warning')
    else:
        db.session.add(UserModule(user_id=student_id, module_id=module_id, paid_amount=paid))
        db.session.commit()
        flash('Módulo atribuído com sucesso!', 'success')
    return redirect(url_for('admin_student_detail', student_id=student_id))

@app.route('/admin/remove-module', methods=['POST'])
@admin_required
def admin_remove_module():
    student_id = request.form.get('student_id', type=int)
    module_id = request.form.get('module_id', type=int)
    um = UserModule.query.filter_by(user_id=student_id, module_id=module_id).first()
    if um:
        db.session.delete(um)
        db.session.commit()
        flash('Acesso removido com sucesso.', 'success')
    return redirect(url_for('admin_student_detail', student_id=student_id))

@app.route('/admin/create-student', methods=['POST'])
@admin_required
def admin_create_student():
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip() or None
    password = request.form.get('password', '').strip()
    if not username or not password:
        flash('Username e senha são obrigatórios.', 'error')
        return redirect(url_for('admin_students'))
    if User.query.filter_by(username=username).first():
        flash('Este username já existe.', 'error')
        return redirect(url_for('admin_students'))
    user = User(username=username, email=email,
                password_hash=generate_password_hash(password), role='student')
    db.session.add(user)
    db.session.flush()

    module_ids = request.form.getlist('module_ids', type=int)
    paid_amount = request.form.get('paid_amount', type=float, default=0.0) or 0.0
    paid_per_module = paid_amount / len(module_ids) if module_ids else 0.0
    for mid in module_ids:
        db.session.add(UserModule(user_id=user.id, module_id=mid, paid_amount=paid_per_module))

    db.session.commit()
    msg = f'Aluno {username} criado'
    if module_ids:
        msg += f' com {len(module_ids)} módulo(s) atribuído(s)'
    flash(msg + '!', 'success')
    return redirect(url_for('admin_student_detail', student_id=user.id))

@app.route('/admin/toggle-student/<int:student_id>', methods=['POST'])
@admin_required
def admin_toggle_student(student_id):
    student = User.query.get_or_404(student_id)
    student.is_active_user = not student.is_active_user
    db.session.commit()
    return redirect(url_for('admin_student_detail', student_id=student_id))

@app.route('/admin/revenue')
@admin_required
def admin_revenue():
    total_revenue = db.session.query(db.func.sum(UserModule.paid_amount)).scalar() or 0
    total_sales = UserModule.query.count()
    modules = Module.query.all()
    module_stats = []
    for mod in modules:
        ums = UserModule.query.filter_by(module_id=mod.id).all()
        rev = sum(u.paid_amount for u in ums)
        module_stats.append({'module': mod, 'revenue': rev, 'sales': len(ums),
                             'avg': rev / len(ums) if ums else 0})
    all_sales = db.session.query(UserModule, User, Module)\
        .join(User, UserModule.user_id == User.id)\
        .join(Module, UserModule.module_id == Module.id)\
        .order_by(UserModule.assigned_at.desc()).all()
    return render_template('admin/revenue.html',
        total_revenue=total_revenue, total_sales=total_sales,
        module_stats=module_stats, all_sales=all_sales)

# ─────────────────────────── SEED DATA ───────────────────────────

from seed_data import ALL_MODULES, CONTENT_FUNCTIONS

# NOTE: Old content functions below are deprecated. All content now lives in seed_data.py.

def _old_get_lesson1_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Python é a linguagem de programação mais popular do mundo para automação e dados. Nesta semana você vai do zero ao seu primeiro script funcional.</p>
  </div>

  <h2>🐍 Por que Python?</h2>
  <p>Python domina automação e dados por razões simples:</p>
  <ul>
    <li><strong>Legível como inglês</strong> — você consegue ler o código e entender o que ele faz</li>
    <li><strong>Enorme ecossistema</strong> — bibliotecas para tudo: automação, dados, IA, web</li>
    <li><strong>Alta demanda</strong> — linguagem mais pedida em vagas de automação e dados no Brasil</li>
  </ul>

  <h2>📦 Variáveis e Tipos de Dados</h2>
  <p>Variáveis são "caixinhas" que guardam informações. Em Python você não precisa declarar o tipo — ele descobre sozinho:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code># Os 4 tipos básicos
nome = "Ana"          # str — texto (use aspas)
idade = 28            # int — número inteiro
salario = 4500.50     # float — número decimal
ativo = True          # bool — verdadeiro ou falso

# Verifique o tipo com type()
print(type(nome))     # &lt;class 'str'&gt;
print(type(idade))    # &lt;class 'int'&gt;

# f-strings: o jeito moderno de montar textos
print(f"Olá, {nome}! Você tem {idade} anos.")
# Saída: Olá, Ana! Você tem 28 anos.</code></pre>
  </div>

  <h2>🔢 Operadores</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code># Aritméticos
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333... (sempre float)
print(10 // 3)  # 3 (divisão inteira, sem resto)
print(10 % 3)   # 1 (resto da divisão — muito útil!)
print(2 ** 3)   # 8 (potência: 2³)

# Comparação — retornam True ou False
print(5 > 3)    # True
print(5 == 5)   # True (== compara, = atribui)
print(5 != 3)   # True

# Lógicos
print(True and False)  # False
print(True or False)   # True
print(not True)        # False</code></pre>
  </div>

  <h2>🔀 Condicionais: if, elif, else</h2>
  <p>Condicionais permitem que seu código tome decisões:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>nota = 7.5

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Saída: Aprovado

# Dica: indentação (os espaços) é obrigatória em Python!
# Use 4 espaços ou Tab — seja consistente.</code></pre>
  </div>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div>
      <strong>Dica prática:</strong> No VS Code, instale a extensão <code>Python</code> da Microsoft. Ela adiciona autocomplete, destaque de erros e permite rodar o código com um clique.
    </div>
  </div>

  <h2>🎯 Exemplo Completo</h2>
  <div class="code-block">
    <div class="code-header">Calculadora de Salário</div>
    <pre><code>salario_bruto = 5000.0
dependentes = 2
desconto_inss = salario_bruto * 0.11
desconto_ir = 150.0 if dependentes >= 2 else 300.0

salario_liquido = salario_bruto - desconto_inss - desconto_ir

print(f"Salário Bruto:  R$ {salario_bruto:.2f}")
print(f"INSS:           R$ {desconto_inss:.2f}")
print(f"IR:             R$ {desconto_ir:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")</code></pre>
  </div>
</section>
"""

def get_lesson2_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Estruturas de dados são onde a programação fica poderosa. Aprenda a trabalhar com coleções de dados e a criar funções reutilizáveis.</p>
  </div>

  <h2>📋 Listas</h2>
  <p>Listas são coleções ordenadas e mutáveis — você pode mudar o conteúdo depois de criar:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>frutas = ["maçã", "banana", "laranja", "uva"]

# Acesso por índice (começa no 0)
print(frutas[0])   # maçã
print(frutas[-1])  # uva (último elemento)
print(frutas[1:3]) # ['banana', 'laranja'] (slicing)

# Métodos essenciais
frutas.append("manga")     # adiciona no final
frutas.remove("banana")    # remove por valor
frutas.sort()              # ordena in-place
print(len(frutas))         # quantidade de itens

# Iterando
for fruta in frutas:
    print(f"- {fruta}")</code></pre>
  </div>

  <h2>📚 Dicionários</h2>
  <p>Dicionários guardam pares chave-valor — como uma tabela Excel com nome e conteúdo:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>funcionario = {
    "nome": "Carlos",
    "cargo": "Analista",
    "salario": 6500.0,
    "ativo": True
}

# Acessando valores
print(funcionario["nome"])           # Carlos
print(funcionario.get("setor", "N/A"))  # N/A (sem erro se não existe)

# Modificando e adicionando
funcionario["salario"] = 7000.0
funcionario["setor"] = "TI"

# Iterando
for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")</code></pre>
  </div>

  <h2>🔄 Loops: for e while</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code># for — quando você sabe quantas vezes vai repetir
for i in range(5):      # 0, 1, 2, 3, 4
    print(f"Item {i}")

# Enumerate: pega índice e valor juntos
nomes = ["Ana", "Bob", "Carla"]
for i, nome in enumerate(nomes):
    print(f"{i+1}. {nome}")

# while — repete enquanto condição for True
contador = 0
while contador < 3:
    print(f"Rodada {contador}")
    contador += 1

# break e continue
for n in range(10):
    if n == 3: continue   # pula o 3
    if n == 7: break      # para no 7
    print(n)</code></pre>
  </div>

  <h2>⚙️ Funções</h2>
  <p>Funções são blocos de código reutilizáveis. Defina uma vez, use quantas vezes quiser:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>def calcular_bonus(salario, percentual=10):
    # Calcula bonus com percentual padrao de 10%
    bonus = salario * (percentual / 100)
    return bonus

# Chamadas
print(calcular_bonus(5000))        # 500.0
print(calcular_bonus(5000, 15))    # 750.0

# Função com múltiplos retornos
def analisa_lista(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, media = analisa_lista([4, 7, 2, 9, 1])
print(f"Min: {minimo}, Max: {maximo}, Média: {media}")</code></pre>
  </div>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div>
      <strong>Como ler a documentação:</strong> Use <code>help(funcao)</code> no Python ou pesquise <code>python docs [nome_da_função]</code>. O site oficial <strong>docs.python.org</strong> tem tudo em detalhe.
    </div>
  </div>
</section>
"""

def get_lesson3_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Automação com Python (RPA — Robotic Process Automation) é uma das habilidades mais valorizadas no mercado. Aprenda a fazer o computador trabalhar por você.</p>
  </div>

  <h2>🤖 O que é Automação de Processos?</h2>
  <p>RPA é a tecnologia que permite que softwares imitem ações humanas em computadores — clicar, digitar, navegar em sistemas, copiar dados. Com Python, você cria esses robôs.</p>

  <div class="highlight-grid">
    <div class="highlight-card">
      <span>⏰</span>
      <strong>Antes:</strong> 30 min por dia copiando dados manualmente
    </div>
    <div class="highlight-card">
      <span>⚡</span>
      <strong>Depois:</strong> Script roda em 2 min automaticamente toda manhã
    </div>
  </div>

  <h2>🖱️ PyAutoGUI — Controlando Mouse e Teclado</h2>
  <div class="code-block">
    <div class="code-header">Python — pip install pyautogui</div>
    <pre><code>import pyautogui
import time

# Movendo o mouse
pyautogui.moveTo(500, 300, duration=0.5)  # move suavemente
pyautogui.click()                          # clica onde está

# Clique em posição específica
pyautogui.click(x=150, y=400)

# Digitando texto
pyautogui.typewrite("relatório mensal", interval=0.05)
pyautogui.press('enter')

# Atalhos de teclado
pyautogui.hotkey('ctrl', 'a')  # selecionar tudo
pyautogui.hotkey('ctrl', 'c')  # copiar

# Screenshot para saber onde clicar
# pyautogui.screenshot('tela.png')

# SEMPRE adicione time.sleep() entre ações!
time.sleep(1)  # aguarda 1 segundo</code></pre>
  </div>

  <h2>🪟 pywin32 — Controlando Janelas</h2>
  <div class="code-block">
    <div class="code-header">Python — pip install pywin32</div>
    <pre><code>import win32gui
import win32con
import subprocess

# Abrir um programa
subprocess.Popen(r"C:\Windows\System32\notepad.exe")

import time
time.sleep(1)

# Encontrar a janela pelo título
hwnd = win32gui.FindWindow(None, "Sem título - Bloco de Notas")

if hwnd:
    # Trazer para frente
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    print("Janela encontrada e maximizada!")
else:
    print("Janela não encontrada")</code></pre>
  </div>

  <h2>🛡️ Tratamento de Erros com try/except</h2>
  <p>Em automações, erros são inevitáveis. Use try/except para criar scripts robustos que não quebram na primeira falha:</p>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>import logging

# Configure o log para salvar erros em arquivo
logging.basicConfig(
    filename='automacao.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clicar_botao(x, y, nome="botão"):
    try:
        import pyautogui
        pyautogui.click(x, y)
        logging.info(f"Clique em {nome} bem-sucedido")
        return True
    except Exception as e:
        logging.error(f"Falha ao clicar em {nome}: {e}")
        return False

def abrir_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return None
    except PermissionError:
        print("Sem permissão para ler o arquivo")
        return None</code></pre>
  </div>

  <h2>💾 Salvando Resultados</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>import csv
from datetime import datetime

dados = [
    {"nome": "Produto A", "valor": 150.0, "qtd": 10},
    {"nome": "Produto B", "valor": 89.90, "qtd": 25},
]

# Salvando em CSV
data_hoje = datetime.now().strftime("%Y-%m-%d")
nome_arquivo = f"relatorio_{data_hoje}.csv"

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "valor", "qtd"])
    writer.writeheader()
    writer.writerows(dados)

print(f"Relatório salvo em: {nome_arquivo}")</code></pre>
  </div>

  <div class="tip-box">
    <span class="tip-icon">⚠️</span>
    <div>
      <strong>Dica de segurança:</strong> Sempre teste sua automação em um ambiente seguro antes. Use <code>pyautogui.FAILSAFE = True</code> — mova o mouse para o canto superior esquerdo para interromper o script de emergência.
    </div>
  </div>
</section>
"""

def get_lesson4_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Pandas é a biblioteca mais poderosa do Python para análise de dados. Pense nela como um Excel turbinado que você controla com código.</p>
  </div>

  <h2>🐼 O que é Pandas?</h2>
  <p>Pandas trabalha com duas estruturas principais:</p>
  <div class="highlight-grid">
    <div class="highlight-card">
      <span>📊</span>
      <strong>DataFrame</strong>: Tabela completa (linhas + colunas) — como uma planilha Excel
    </div>
    <div class="highlight-card">
      <span>📈</span>
      <strong>Series</strong>: Uma coluna ou linha isolada — como uma lista com índice
    </div>
  </div>

  <h2>📂 Lendo Arquivos</h2>
  <div class="code-block">
    <div class="code-header">Python — pip install pandas openpyxl</div>
    <pre><code>import pandas as pd

# Lendo diferentes formatos
df_csv = pd.read_csv("vendas.csv", sep=";", encoding="utf-8")
df_excel = pd.read_excel("relatorio.xlsx", sheet_name="Jan")

# Primeiras linhas e informações gerais
print(df_csv.head())        # primeiras 5 linhas
print(df_csv.info())        # tipos de dados e nulos
print(df_csv.describe())    # estatísticas básicas
print(df_csv.shape)         # (linhas, colunas)</code></pre>
  </div>

  <h2>🔍 Filtrando e Transformando</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>import pandas as pd

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    "produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "valor": [2500, 90, 150, 1200],
    "categoria": ["Tech", "Periférico", "Periférico", "Tech"]
})

# Filtrando linhas
caros = df[df["valor"] > 200]
tech = df[df["categoria"] == "Tech"]

# Criando novas colunas
df["valor_com_taxa"] = df["valor"] * 1.1  # +10%
df["descricao"] = df["produto"] + " - " + df["categoria"]

# Agrupando (GROUP BY do Excel)
por_categoria = df.groupby("categoria")["valor"].sum()
print(por_categoria)</code></pre>
  </div>

  <h2>🧹 Limpeza de Dados</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code># Tratando valores nulos
df["valor"].fillna(0, inplace=True)         # substitui NaN por 0
df.dropna(subset=["produto"], inplace=True)  # remove linhas sem produto

# Removendo duplicatas
df.drop_duplicates(subset=["produto"], inplace=True)

# Convertendo tipos
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")</code></pre>
  </div>

  <h2>💾 Exportando Resultados</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>from datetime import datetime

data = datetime.now().strftime("%Y-%m-%d")

# Salvar como Excel
df.to_excel(f"relatorio_{data}.xlsx", index=False, sheet_name="Dados")

# Salvar como CSV
df.to_csv(f"relatorio_{data}.csv", index=False, sep=";", encoding="utf-8")</code></pre>
  </div>

  <h2>⏰ Agendando a Execução</h2>
  <p>O Agendador de Tarefas do Windows permite rodar seu script automaticamente todo dia:</p>
  <div class="code-block">
    <div class="code-header">Agendador de Tarefas — Passos</div>
    <pre><code>1. Pesquise "Agendador de Tarefas" no Windows
2. "Criar Tarefa Básica..."
3. Dê um nome: "Relatório Diário"
4. Frequência: Diariamente — Horário: 08:00
5. Ação: "Iniciar um programa"
6. Programa: C:\Python312\python.exe
7. Argumentos: C:\Scripts\meu_relatorio.py
8. Iniciar em: C:\Scripts\

# No seu script, adicione log de execução:
import logging
from datetime import datetime

logging.basicConfig(filename='log.txt', level=logging.INFO)
logging.info(f"Script executado em {datetime.now()}")</code></pre>
  </div>
</section>
"""

def get_ia_lesson1_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>IA não é mágica — é uma ferramenta. Quem aprende a usá-la bem tem uma vantagem enorme. Nesta aula você vai entender como funcionam os LLMs e como extrair o máximo deles.</p>
  </div>

  <h2>🧠 O que são LLMs?</h2>
  <p>LLMs (Large Language Models) são modelos de linguagem treinados em bilhões de textos. Eles aprendem padrões estatísticos da linguagem humana.</p>

  <div class="highlight-grid">
    <div class="highlight-card">
      <span>🤖</span>
      <strong>ChatGPT (OpenAI)</strong>: Melhor para tarefas gerais, código, criatividade. GPT-4o é excelente.
    </div>
    <div class="highlight-card">
      <span>⚡</span>
      <strong>Claude (Anthropic)</strong>: Melhor para textos longos, análise de documentos, raciocínio.
    </div>
    <div class="highlight-card">
      <span>🔍</span>
      <strong>Gemini (Google)</strong>: Integrado ao Google Workspace, bom com multimodal.
    </div>
  </div>

  <h2>✍️ Prompt Engineering — A Arte de Pedir</h2>
  <p>Um bom prompt tem 4 elementos:</p>
  <div class="code-block">
    <div class="code-header">Estrutura de Prompt Profissional</div>
    <pre><code># ❌ Prompt ruim:
"Escreva um e-mail"

# ✅ Prompt com as 4 partes:

[CONTEXTO]
Você é um atendente de customer success de uma empresa de SaaS B2B.

[TAREFA]
Responda o e-mail abaixo de um cliente insatisfeito com o tempo de resposta
do suporte. O e-mail do cliente é: "Abri um ticket há 3 dias e ninguém me
respondeu. Isso é inaceitável."

[FORMATO]
Resposta em tom profissional mas empático, máximo 4 parágrafos:
1. Reconhecimento do problema
2. Pedido de desculpas genuíno
3. Solução imediata proposta
4. Compromisso de melhoria

[RESTRIÇÕES]
- Não prometa prazos específicos
- Não culpe outros setores
- Não use termos técnicos</code></pre>
  </div>

  <h2>🧩 Técnicas Avançadas</h2>
  <div class="code-block">
    <div class="code-header">Chain of Thought — Raciocínio Passo a Passo</div>
    <pre><code># Peça ao modelo para pensar antes de responder:
"Pense passo a passo antes de responder.
Qual é a melhor estratégia para reduzir o churn de clientes
em uma plataforma de cursos online?"

# O modelo vai raciocinar antes de concluir, produzindo
# respostas mais precisas e fundamentadas.</code></pre>
  </div>

  <div class="code-block">
    <div class="code-header">Few-Shot — Dar Exemplos</div>
    <pre><code># Mostre exemplos do formato que você quer:
"Classifique o sentimento dos comentários.

Exemplos:
'Adorei o produto!' → Positivo
'Péssima qualidade' → Negativo
'É razoável, serve' → Neutro

Agora classifique:
'Entrega rápida, produto ok, mas embalagem ruim'"</code></pre>
  </div>

  <h2>🖥️ Cursor e GitHub Copilot</h2>
  <div class="code-block">
    <div class="code-header">Dicas de uso no dia a dia</div>
    <pre><code># Cursor (editor com IA integrada):
# - Ctrl+K: editar código com IA
# - Ctrl+L: chat com contexto do arquivo
# - Tab: aceitar sugestão

# GitHub Copilot (extensão VS Code):
# - Escreva um comentário descrevendo o que quer
# - Pressione Tab para aceitar a sugestão

# Exemplo — escreva o comentário e deixe a IA completar:
# Função que lê um Excel, filtra linhas onde valor > 1000
# e salva o resultado em um novo arquivo
def filtrar_valores_altos(arquivo_entrada, arquivo_saida):
    # ← IA vai completar aqui</code></pre>
  </div>

  <div class="tip-box">
    <span class="tip-icon">⚠️</span>
    <div>
      <strong>Quando NÃO confiar na IA:</strong> dados precisos (números, datas), eventos recentes após o cutoff, cálculos matemáticos complexos, decisões legais ou médicas. Sempre verifique informações críticas.
    </div>
  </div>
</section>
"""

def get_ia_lesson2_content():
    return """
<section class="lesson-section">
  <div class="lesson-intro-box">
    <p>Nesta aula você vai além do ChatGPT e aprende a consumir APIs de IA diretamente no seu código Python — abrindo possibilidades ilimitadas de automação inteligente.</p>
  </div>

  <h2>🔌 Como funcionam as APIs de IA?</h2>
  <p>Você envia uma requisição HTTP com seu prompt e recebe a resposta do modelo. É exatamente como o ChatGPT funciona por dentro.</p>

  <div class="code-block">
    <div class="code-header">Python — pip install anthropic openai</div>
    <pre><code>import anthropic

# Inicializa o cliente com sua chave de API
client = anthropic.Anthropic(api_key="sua-chave-aqui")

# Primeira requisição
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explique o que é pandas em 3 linhas."}
    ]
)

print(message.content[0].text)</code></pre>
  </div>

  <h2>⚙️ Parâmetros Importantes</h2>
  <div class="code-block">
    <div class="code-header">Python</div>
    <pre><code>message = client.messages.create(
    model="claude-3-5-sonnet-20241022",  # qual modelo usar
    max_tokens=2048,      # máximo de tokens na resposta
    temperature=0.7,      # 0=determinístico, 1=criativo
    system="Você é um analista de dados sênior. Responda de forma técnica e concisa.",
    messages=[
        {"role": "user", "content": "Qual a diferença entre merge e join no pandas?"}
    ]
)

# Tokens = pedaços de palavras. Aprox. 1 token = 0.75 palavras
# 1M tokens Claude Haiku ≈ R$ 0.25 (muito barato!)</code></pre>
  </div>

  <h2>🤖 Assistente que Analisa seus Dados</h2>
  <div class="code-block">
    <div class="code-header">Python — Bot Analista de Excel</div>
    <pre><code>import pandas as pd
import anthropic

def analisar_dados(arquivo_excel, pergunta):
    # Carrega os dados
    df = pd.read_excel(arquivo_excel)

    # Converte para texto resumido
    resumo = (
        f"Dados do arquivo {arquivo_excel}:\n"
        f"- Colunas: {list(df.columns)}\n"
        f"- Linhas: {len(df)}\n"
        f"- Amostra:\n{df.head(5).to_string()}\n"
        f"- Estatisticas:\n{df.describe().to_string()}"
    )

    client = anthropic.Anthropic(api_key="sua-chave")
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="Você é um analista de dados. Responda perguntas sobre os dados fornecidos.",
        messages=[
            {"role": "user", "content": f"Dados:\n{resumo}\n\nPergunta: {pergunta}"}
        ]
    )
    return response.content[0].text

# Uso:
resposta = analisar_dados("vendas.xlsx", "Qual produto teve maior crescimento?")
print(resposta)</code></pre>
  </div>

  <h2>💰 Controlando Custos</h2>
  <div class="code-block">
    <div class="code-header">Python — Estimativa de Custo</div>
    <pre><code"># Preços aproximados (por 1M tokens, Mar/2025):
# claude-3-5-haiku:    input R$0.50  | output R$1.25  (mais barato)
# claude-3-5-sonnet:   input R$15.00 | output R$75.00 (melhor custo-benefício)
# gpt-4o-mini:         input R$0.75  | output R$3.00

def estima_custo(texto, modelo="sonnet"):
    tokens_aprox = len(texto.split()) * 1.3  # estimativa
    if modelo == "haiku":
        custo = (tokens_aprox / 1_000_000) * 0.50
    else:
        custo = (tokens_aprox / 1_000_000) * 15.0
    return f"~{tokens_aprox:.0f} tokens = R$ {custo:.4f}"

print(estima_custo("Texto de 100 palavras aqui " * 100))</code></pre>
  </div>

  <div class="tip-box">
    <span class="tip-icon">💡</span>
    <div>
      <strong>Onde pegar as chaves:</strong> OpenAI → <code>platform.openai.com</code> | Anthropic → <code>console.anthropic.com</code>. Nunca coloque sua chave direto no código — use variáveis de ambiente ou um arquivo <code>.env</code>.
    </div>
  </div>
</section>
"""

def init_db():
    db.create_all()

    try:
        inspector = sa_inspect(db.engine)
        existing_cols = [c['name'] for c in inspector.get_columns('call_schedule')]
        with db.engine.connect() as conn:
            if 'module_id' not in existing_cols:
                conn.execute(text('ALTER TABLE call_schedule ADD COLUMN module_id INTEGER'))
                conn.commit()
            if 'week_number' not in existing_cols:
                conn.execute(text('ALTER TABLE call_schedule ADD COLUMN week_number INTEGER'))
                conn.commit()
    except Exception:
        pass

    if not User.query.filter_by(username='mathmugiwara').first():
        old_admin = User.query.filter_by(role='admin').first()
        if old_admin:
            old_admin.username = 'mathmugiwara'
            old_admin.email = 'admin@matheusdev.com'
            old_admin.password_hash = generate_password_hash('Mugiwara1!')
        else:
            db.session.add(User(
                username='mathmugiwara', email='admin@matheusdev.com',
                password_hash=generate_password_hash('Mugiwara1!'),
                role='admin'
            ))

    if Module.query.count() == 0:
        for mod_data in ALL_MODULES:
            mod = Module(
                name=mod_data['name'],
                short_name=mod_data['short_name'],
                description=mod_data['description'],
                price=mod_data['price'],
                duration=mod_data['duration'],
                level=mod_data['level'],
                color=mod_data['color'],
                icon=mod_data['icon']
            )
            db.session.add(mod)
            db.session.flush()

            for lesson_data in mod_data['lessons']:
                content = ''
                cf = lesson_data.get('content_func')
                if cf and cf in CONTENT_FUNCTIONS:
                    content = CONTENT_FUNCTIONS[cf]()
                lesson = Lesson(
                    module_id=mod.id,
                    title=lesson_data['title'],
                    subtitle=lesson_data['subtitle'],
                    content=content,
                    week_number=lesson_data['week'],
                    order=lesson_data['order'],
                    duration_minutes=lesson_data['duration']
                )
                db.session.add(lesson)
                db.session.flush()
                for i, (et, ed, es, eo, eh, ep) in enumerate(lesson_data.get('exercises', [])):
                    db.session.add(Exercise(
                        lesson_id=lesson.id, title=et, description=ed,
                        starter_code=es, expected_output=eo, hint=eh, points=ep, order=i+1
                    ))

    if CallAvailability.query.count() == 0:
        defaults = [
            (1, '19:00', '21:00'),
            (3, '19:00', '21:00'),
            (5, '14:00', '18:00'),
            (6, '10:00', '16:00'),
        ]
        for day, start, end in defaults:
            db.session.add(CallAvailability(day_of_week=day, start_time=start, end_time=end))

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
