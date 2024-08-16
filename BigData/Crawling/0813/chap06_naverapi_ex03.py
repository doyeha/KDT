def get_post_data(post, json_result_listm cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')

    print(f'[{cnt}]', end=' ')
    print(title, end=": ")
    print(pdate, end=' ')
    print(link)


    json_result_list.append([cnt,pdate,title, desc])