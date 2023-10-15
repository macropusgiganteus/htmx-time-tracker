import time
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize a counter variable
duration = 30
timer = duration

# Components
timer_component = lambda timer, trigger='' : f'''
<h2 class="card-title text-6xl" id="number" hx-get="/countdown" hx-trigger="{trigger}">
    {format_duration(timer)}
</h2 >
'''

# Helpers
def format_duration(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

# API
@app.route("/")
def index():
    return render_template("index.html", duration=format_duration(timer))

@app.route("/set", methods=["POST"])
def set_timer():
    global duration
    global timer
    
    duration = int(request.form['duration'])
    timer = duration
    return timer_component(timer)

@app.route('/countdown')
def countdown():
    global timer
    if timer <= 0:
        return timer_component(0), 286
    
    timer -= 1 
    return timer_component(timer)

@app.route('/start')
def start():
    global timer
    
    return timer_component(timer, 'every 1s')

@app.route('/pause')
def pause():
    global timer
    return timer_component(timer)

@app.route('/stop')
def stop():
    global timer
    return timer_component(timer)

@app.route('/reset')
def reset():
    global timer 
    timer = duration
    return timer_component(timer)

if __name__ == "__main__":
    app.run(debug=True)