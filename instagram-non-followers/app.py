import csv

# Takip edilmeyen kullanıcıları tutmak için bir liste oluştur
not_following_back = []

# following.csv dosyasını aç ve takip edilmeyen kullanıcıları bul
with open('following.csv', 'r', encoding="utf8") as following_file:
    following_reader = csv.reader(following_file)
    for following_row in following_reader:
        is_followed = False # Bu kullanıcı seni takip ediyor mu?
        with open('followers.csv', 'r', encoding="utf8") as followers_file:
            followers_reader = csv.reader(followers_file)
            for followers_row in followers_reader:
                if following_row[1] == followers_row[1]:
                    is_followed = True # Bu kullanıcı seni takip ediyor
                    break
        if not is_followed:
            not_following_back.append(following_row[1])

# Takip edilmeyen kullanıcıları print et
if len(not_following_back) == 0:
    print("Tebrikler! Tüm takipçilerin seni takip ediyor.")
else:
    print("Aşağıdaki kullanıcılar seni takip etmiyor:")
    for username in not_following_back:
        print(username)