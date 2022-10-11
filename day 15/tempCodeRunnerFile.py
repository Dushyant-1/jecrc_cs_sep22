 range(22)]
df1=pd.read_csv('u.item',sep='|',encoding='ISO-8859-1',names=item_cols)
movie=pd.merge(df,df1,on='movie_id')

result = ttk.Variable(app)
box = ttk.Listbox(app,height=10)

for row,val in movie.iterrows():
    print(val['title'])
    box.insert(row+1,val['title'])

box.place(x=10,y=10)

def get_movie():