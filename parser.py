import requests
from bs4 import BeautifulSoup as bs


url_plus = 'https://www.chitai-gorod.ru'
categorys = {}


def get_categorys(url_plus: str = url_plus, categorys: dict = categorys) -> dict:
	'''
	Получение категорий с сайта "Читай город" и запись их в файл .txt построчно
	Возвращает словарь с названием категории и ссылкой на нее
	'''

	url = 'https://www.chitai-gorod.ru/catalog/books-18030'
	request = requests.get(url)
	soup = bs(request.text, 'html.parser')
	categorys_list = soup.find('div', class_='catalog-menu').find('div', class_='catalog-menu__parent').find_all('a', class_='catalog-menu__parent--children')
	for category in categorys_list:
			categorys[category.text] = url_plus + category.get('href')

	with open('category.txt', 'w')  as cat:
		for k, v in categorys.items():
			cat.write(f'{k}\t{v}\n')

	return categorys


def get_books(url_plus: str = url_plus, category_link: str = 'https://www.chitai-gorod.ru/catalog/books/khudozhestvennaya_literatura-9657/') -> list:
	'''
	Получение книгсо страницы категории, выбранной пользователем
	Возвращает список в формате [название, ссылка, цена, название файла с картинкой]
	'''
	book_list = []
	k = 0
	for page in range(1, 4):

		url = f'{category_link}?page={page}'
		request = requests.get(url)
		soup = bs(request.text, 'html.parser')

		books = soup.find_all('div', class_='product-card js_product js__product_card js__slider_item')

		for book in books:

			name = book.get('data-chg-book-name')
			link = url_plus + book.find('a', class_='product-card__img js-analytic-productlink').get('href')
			img = book.find('a', class_='product-card__img js-analytic-productlink').find('img').get('data-src')
			price = book.find('span', class_='product-price__value').text
			
			with open(f'./img/{k}.jpg', 'wb') as img_new:
				request_img = requests.get(img)
				img_new.write(request_img.content)
			
			book_list.append([name, link, price, f'./img/{k}.jpg'])
			k += 1

	return book_list
