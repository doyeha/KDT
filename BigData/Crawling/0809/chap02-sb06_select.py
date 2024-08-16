
from bs4	import BeautifulSoup

html_example = '''
<!DOCTYPE html>
<html lang ="en">
<head>
    <meta	charset="UTF-8">
	<meta	name="viewport"	content="width=device-width,	initial-scale=1.0">
	<title>BeautifulSoup 활용</title>
</head>
<body>
	<h1	id="heading">Heading	1</h1>
	<p>Paragraph</p>
	span	class="red">BeautifulSoup Library	Examples!</span>
	<div	id="link">
		<a	class="external_link"	href="www.google.com">google</a>
		<div	id="class1">
            <p	id="first">class1's	first	paragraph</p>
            <a	class="external_link"	href="www.naver.com">naver</a>
            <p	id="second">class1's	second	paragraph</p>
            <a	class="internal_link"	href="/pages/page1.html">Page1</a>
            <p	id="third">class1's	third	paragraph</p>
        </div>
    </div>
    <div	id="text_id2">
                        Example	page
                        <p>g</p>
    </div>
    <h1	id="footer">Footer</h1>
</body>
</html>
'''


soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text :', head.text.strip())

footer = soup.select_one('h1#footer')
print(footer)

class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])

link1 = soup.select_one('div#link > a.external_link')
print(link1)

link_find = soup.find('div', {'id' : 'link'})

external_link =link_find.find('a', {'class' : 'external_link'})
print('find external link : ', external_link)

link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)

third_tag = soup.select_one('div#link a.internal_link')
print(third_tag['href'])
print(third_tag.text)


h1_all = soup.select('h1')
print('h1_all : ', h1_all)

url_links = soup.select('a')
for link in url_links:
    print(link['href'])


div_urls = soup.select('div#class1 > a')

print(div_urls)
print(div_urls[0]['href'])

div_urls2 = soup.select('div#class1 a')
print(div_urls2)

h1 = soup.select('#heading, #footer')
print(h1)

url_links = soup.select('a.external_link, a.internal_link')
print(url_links)
