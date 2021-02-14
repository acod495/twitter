import tweepy
import slackweb
import time, schedule
import key

slack_url=key.slack_url
slack = slackweb.Slack(url=slack_url)


#Twitter API
#各キーを取得
consumer_key        = key.consumer_key
consumer_secret     = key.consumer_secret
access_token        = key.access_token
access_token_secret = key.access_token_secret

def authTwitter():
    #認証情報を設定 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #APIインスタンスの作成
    api = tweepy.API(auth)
    return(api)

def printTweetBySearch(s):
    api = authTwitter() # 認証

    tweets = tweepy.Cursor(api.search, q =s,\
                            include_entities = True, \
                            tweet_mode = 'extended', \
                            result_type = 'recent', \
                            lang = 'ja').items(10)
    N_of_tweet = 0
    for tweet in tweets:
        N_of_tweet += 1
        #if tweet.favorite_count + tweet.retweet_count >= 100:
        print('＝＝＝＝＝＝＝＝＝＝')
        print('user_name : ',tweet.user.name)
        print('user_id : ',tweet.user.screen_name)
        print('date : ', tweet.created_at)
        print(tweet.full_text)
        print('favo : ', tweet.favorite_count)
        print('retw : ', tweet.retweet_count)

        attachments = []
        attachment = {"title": "Searched for '%s'." %(s),
                      "pretext": "Tweet notification #%d" %(N_of_tweet),
                      "text": "＝＝＝＝＝＝＝＝＝＝＝＝ \n" \
                              "user_name : %s \n" \
                              "user_id : %s \n" \
                              "date : %s \n" \
                              "%s" \
                              %(tweet.user.name, tweet.user.screen_name, tweet.created_at, tweet.full_text),
                      "mrkdwn_in": ["text", "pretext"]}
        attachments.append(attachment)
        slack.notify(attachments=attachments)
    slack.notify(text="%s tweets have been posted!" %(N_of_tweet))
    print("%s tweets have been posted!" %(N_of_tweet))

def main():
    printTweetBySearch('#あてなよる from:NHK_PR exclude:retweets')  

if __name__ == "__main__":
    main()
