from sense_hat import SenseHat
import datetime
import random
import time

# select headphone jack audio output
# amixer cset numid=3 1
# amixer cset numid=1 -- 400

import pygame
sense = SenseHat()
sense.clear()

days_of_christmas = ["It's Christmas Day!","It's Boxing day","It's the 3rd day of Christmas","It's the 4th day of Christmas","It's the 5th day of Christmas","It's the 6th day of Christmas",
"It's New Years Eve","It's New Years Day","It's the 9th day of Christmas","It's the 10th day of Christmas","It's the 11th day of Christmas","It's the 12th day of Christmas"]

def play_random_track():
    # pick a track
    trackID = random.randint(1,44)
    pygame.mixer.init()
    pygame.mixer.music.load("../xmas_music/tune%d.mp3"%trackID)
    pygame.mixer.music.play()
    print 'Playing tune %d' % trackID


def sleep_till_next_hour():
    start_time = datetime.datetime.now()
    trunc_start = start_time.replace(minute=0, second=0, microsecond=0)
    hour_start = trunc_start + datetime.timedelta(hours=1)
    # sleep until beginning of next hour
    sleep_time = hour_start - start_time
    print "We need to sleep for %d seconds" % sleep_time.seconds
    time.sleep(sleep_time.seconds)

def do_we_play_music_now():
    # get current time
    now = datetime.datetime.now()
    if now.hour > 8 and now.hour < 20:
        return True
    else:
        return False

def time_til_xmas():
    now = datetime.datetime.now()
    xmas = datetime.datetime(now.year, 12, 25)
    delta = xmas - now
    return delta


def get_message():
    delta = time_til_xmas()
    hours = delta.seconds / 60 / 60
    minutes = (delta.seconds - hours * 60 * 60) / 60
    if delta.days > 1:
        return "It's %d days until Christmas" % delta.days
    if delta.days == 1:
        return "It's 1 day and %d hours until Christmas" % hours
    if delta.days == 0 and hours > 0:
        return "It's %d hours %d minutes until Christmas" % (hours, minutes)
    if delta.days < 0 and delta.days > -12:
        index = (delta.days * -1) - 1
        return days_of_christmas[index]
    return "Christmas is over, pack up the house till December!"

def open_the_presents():
    for x in range(10):
        pygame.mixer.init()
        pygame.mixer.music.load("../xmas_music/open_presents.wav")
        pygame.mixer.music.play()
        print 'Playing open presents message'
        time.sleep(10)

while True:
    now = datetime.datetime.now()
    if now.month == 12 and now.day == 26 and now.hour == 14:
        open_the_presents()
    else:
        # how many days till xmas?
        if do_we_play_music_now():
            play_random_track()

        for x in range(10):
            message = get_message()
            sense.show_message(message,
                               text_colour=[255, 255, 255],
                               back_colour=[255, 0, 0])
        time.sleep(20)

    sense.clear()
    sleep_till_next_hour()