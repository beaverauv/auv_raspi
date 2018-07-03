import Adafruit_PCA9685
import time, curses

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

running = True
fwdmax = 600
stop = 400
revmax = 200
go = 400
inc = 5
spinup = 1

def bootup():
    boot = 200
    while boot < fwdmax:
        boot += inc
        pwm.set_pwm(0,0,boot)
        time.sleep(0.1)
        if boot > fwdmax:
            while boot > revmax:
                 boot -= inc
                 pwm.set_pwm(0,0,boot)
                 time.sleep(0.1)
                 if boot < revmax:
                     boot = 400
                     pwm.set_pwm(0,0,boot)
                     spinup = 0
                     break

while running:
        char = screen.getch()
        if char == ord('q'):
                running=False
        else:
                if char == ('b') and spinup == 1:
                    bootup()
                if char == curses.KEY_UP:
                        if go < fwdmax:
                                go += inc
                elif char == curses.KEY_DOWN:
                        if go > revmax:
                                go -= inc

                elif char == ord(' '):
                        go = stop
        pwm.set_pwm(0, 0, go)
	print go
# shut down cleanly
curses.nocbreak(); screen.keypad(0); curses.echo()
curses.endwin()
