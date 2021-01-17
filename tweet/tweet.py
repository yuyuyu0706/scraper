import tweepy
import pandas as pd

CK = 'xxxxxx'
CS = 'xxxxxx'
AT = 'xxxxxx'
AS = 'xxxxxx'

# OAuth認証
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

'''
#ツイート取得
data = []

# API Call
for page in range(1,5):
    results = api.user_timeline(screen_name="hirosetakao",
				count=200,
				page=page)
    for r in results:
        #r.textで、投稿の本文のみ取得する
        data.append(r.text)

 line = ''.join(data)
 with open("text.txt", 'wt') as f:
    f.write(line)
'''

# データフレームの初期化
df_sum=pd.DataFrame(index=[], columns=['date','text'])

# Tweet を取得する
for page in range(3):
	results = api.user_timeline(
		screen_name="hirosetakao",
		count=200,
		page=page)

	# 配列を初期化する
	datelist=[]
	textlist=[]

	# 配列をデータフレーム化する
	for i in range(200):
		textlist.append(results[i].text)
		datelist.append(results[i].created_at)

	# 配列をデータフレーム化する
	df_text=pd.DataFrame(textlist,columns=['text'])
	df_date=pd.DataFrame(datelist,columns=['date'])

	# データフレームを横連結する
	df_temp=pd.concat([df_date, df_text], axis=1)
	df_sum=pd.concat([df_sum, df_temp])

# 表示する
# print(df_sum)

# 索引を振り直す
df=df_sum.reset_index(drop=True)

# csv出力する
df.to_csv("./tweet.csv", sep=',')

exit()
