import tweepy
import pandas as pd

CK = 'xxxxxxxxxxxxx'
CS = 'xxxxxxxxxxxxx'
AT = 'xxxxxxxxxxxxx'
AS = 'xxxxxxxxxxxxx'

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
for page in range(1,5):
	results = api.user_timeline(
		screen_name="hirosetakao",
		count=200,
		page=page)

	# 配列を初期化する
	datelist=[]
	textlist=[]

	# データを配列に格納する
	for i in range(200):
		datelist.append(results[i].created_at)
		textlist.append(results[i].text)

	# 配列をデータフレーム化する
	df_date=pd.DataFrame(datelist,columns=['date'])
	df_text=pd.DataFrame(textlist,columns=['text'])

	# データフレームを横連結する
	df_temp=pd.concat([df_date, df_text], axis=1)

	# データフレームを縦連結する
	df_sum=pd.concat([df_sum, df_temp])

# 表示する
# print(df_sum)

# 索引を振り直す
df=df_sum.reset_index(drop=True)

# データクレンジング - URLを消す
df['text']=df['text'].str.replace("https?://[a-zA-Z0-9;/?:@&=\+$,\-_\.!~*`\(\)%#]+","")

# データクレンジング - メンションを消す
df['text']=df['text'].str.replace("@[a-zA-Z0-9]+","")

# csv出力する
df.to_csv("./tweet.csv", sep=',')

exit()
