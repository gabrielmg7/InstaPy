
# IMPORTS

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace



# CREDENCIAIS

insta_username = "planetaverdestore"
insta_password = ""


# DIRETÓRIO WORKSPACE (none=default home)

set_workspace(path=None)


# INÍCIO DA SESSÃO
# set headless_browser = True para executar o InstaPy em segundo plano

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)





with smart_run(session):
    
    # CONFIGURAÇÕES GERAIS
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


    # INTERAÇÕES    

    session.like_by_tags(["natgeo"], amount=10)
