# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key        = os.environ.get("consumer_key")
consumer_secret     = os.environ.get("consumer_secret")
access_token        = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
slack_url           = os.environ.get("slack_url")
line_notify_token   = os.environ.get("line_notify_token")