# from multiprocessing.managers import Value
#
# with open('top_50_2023.csv', 'r') as csvfile:
#     header = next(csvfile)
#     print(header)
#     data = []
#     for line in csvfile:
#         line = line[:-1].split(',')
#         data.append(line)
# print(data)
#
import csv
import ast
with open('top_50_2023.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    rows = []
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

GENRE = header.index('genres')
for row in rows:
    row[GENRE] = ast.literal_eval(row[GENRE])
print(rows[0])

def is_valid(num:str)->bool:
    try:
        num = float(num)
        if 0<num<1:
            return True
        return False
    except ValueError:
        return False

#average danceability
DANCEABILITY= header.index('danceability')
sum_dance = 0
counter = 0
for row in rows:
    if is_valid(row[DANCEABILITY]):
        sum_dance += float(row[DANCEABILITY])
        counter+=1
print(f'Average is {sum_dance/counter}')
print('')

EXPLICIT = header.index('is_explicit')
counter_explicit=0
for row in rows:
    if row[EXPLICIT] == 'True':
        counter_explicit+=1
print(f'There are {counter_explicit} explicit songs')
print('')

DATE = header.index('album_release_date')
years_dict={}
for row in rows:
    year = row[DATE].split('-')[0]
    if year in years_dict:
        years_dict[year]+=1
    else:
        years_dict[year] = 1
popular_year = sorted(years_dict.items(),key = lambda x: x[1], reverse=True)[0]
print('The most popular year is', popular_year[0])
print('')

GENRES = header.index('genres')
genres_dict={}
for row in rows:
    for genre in row[GENRES]:
        if genre in genres_dict:
            genres_dict[genre]+=1
        else:
            genres_dict[genre] = 1
top_3_genre = sorted(genres_dict.items(),key = lambda x: x[1], reverse=True)[:3]
top=1
print("TOP 3 POPULAR GENRES")
for genres in top_3_genre:
    print(f'{top}. {genres[0].capitalize()}')
    top+=1
