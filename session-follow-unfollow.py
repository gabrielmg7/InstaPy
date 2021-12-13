# imports
from instapy import InstaPy
from instapy import smart_run
import random

# credenciais de login
insta_username = 'mrktnglider'
insta_password = ''

# obtenha uma sessão InstaPy!
# set headless_browser = True para executar o InstaPy em segundo plano
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """Fluxo de atividades"""
    # Configurações Gerais
    session.set_quota_supervisor(enabled=True, sleep_after=["comments_h", "unfollows_h","server_calls_h"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_daily=300, 
                                 peak_likes_hourly=None, 
                                 peak_follows_daily=200,
                                 peak_follows_hourly=None,
                                 peak_unfollows_daily=200,
                                 peak_unfollows_hourly=160,
                                 peak_comments_daily=None,
                                 peak_comments_hourly=30,
                                 peak_server_calls_daily=500,
                                 peak_server_calls_hourly=None)
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"]) 
    session.set_dont_like(["pizza", "#store"])

    # activities
    
    
    custom_list = [""]
    session.unfollow_users(amount=84, custom_list_enabled=True, custom_list=custom_list, custom_list_param="all", style="RANDOM", 	unfollow_after=55*60*60, sleep_delay=600)
    

    session.follow_user_followers(['camila.cruz.01'], amount=60,
                                  randomize=False, interact=False)
   
    session.unfollow_users(amount=random.randint(80, 120),
                            unfollow_after=3*60*60,  nonFollowers=False,  sleep_delay=601)             
    
    """ Segunda etapa de seguir...
    """

    session.follow_user_followers(['alneidesguedes'], amount=30,
                                  randomize=False, interact=False)

    """ Segunda etapa da ação Deixar de seguir - Deixar de seguir usuários não seguidores ...
    """

    session.unfollow_users(amount=random.randint(30, 60),
                            unfollow_after=3*60*60,  nonFollowers=False,  sleep_delay=601)

