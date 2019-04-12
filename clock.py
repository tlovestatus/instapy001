from apscheduler.schedulers.blocking import BlockingScheduler
""" Quickstart script for InstaPy usage """

# imports
import os
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random
from instapy import get_workspace

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=os.environ['hour'],minute=os.environ['minute'])
def scheduled_job():
    follow_likers_of_users = ['ramoswasoffside', 'passporttoearth', 'fav_skies', 'super_photosunsets', 'njsunrise_sunset', 'adventures_shutter', 'myskynow', 'newjerseyisbeautiful', 'igersmood', 'amazingly_sunsets', 'hey_ihadtosnapthat', 'passion_4_living_photos', 'goventureorange', 'onlythebestcapture', 'goandcapturethelight', 'bestpicturesgallery', 'rthouse']
    random.shuffle(follow_likers_of_users)
    # set workspace folder at desired location (default is at your home folder)
    set_workspace(path="./")
    workspace_in_use = get_workspace()
    print(workspace_in_use["path"])

    # get an InstaPy session!
    session = InstaPy(username=os.environ['username'],
                      password=os.environ['password'],
                      headless_browser=True)

    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_dont_include(["friend1", "friend2", "friend3"])
        #session.follow_likers(follow_likers_of_users, photos_grab_amount=int(os.environ['photos_grab_amount']), follow_likers_per_photo=int(os.environ['follow_likers_per_photo']), randomize=False, sleep_delay=int(os.environ['follow_sleep_delay']), interact=False)
        session.unfollow_users(amount=int(os.environ['unfollow_amount']), allFollowing=True, style="LIFO", unfollow_after=48 * 60 * 60, sleep_delay=int(os.environ['unfollow_sleep_delay']))
        # activity
        #session.like_by_tags(["natgeo"], amount=10)

sched.start()
