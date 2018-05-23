# template for "Stopwatch: The Game"
import simplegui
# define global variables
time=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(num):
        a=int(num/60)
        b=num%60
        if(len(str(b))==1):
            c=str(a)+":0"+str(b)
        else:
            c=str(a)+":"+str(b)

        return c


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()
def stop_timer():
    timer.stop()
def reset_timer():
    global time
    time=0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time=time+1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),[50,50],40,"Yellow")

# create frame
frame=simplegui.create_frame("Timer",300,100)
frame.add_button("Start",start_timer,100)
frame.add_button("Stop",stop_timer,100)
frame.add_button("Reset",reset_timer,100)
timer=simplegui.create_timer(1000,tick)
frame.set_draw_handler(draw)
# register event handlers


# start frame
frame.start()
