Пример простого веб сайта, реализованного на html, bootstrap и flask

1. Есть главная страница: index.html
2. Две страницы с фильмами: home-alone.html и knifes-out.html
- home-alone.html обычная страница, которая содержит всю нужную информацию и загружается в виде шаблона
- на странице knifes-out.html сделана попытка изспользования шаблонизатора для вывода ключевой информации о фильме: афиша, название, автор, описание и т.д.
Некая имитация использования данных из БД и их подстановка на html-страницу 
Файл films.db.py создердит один словарь с инфорамацией о фильме
```python
    knifes_out = {
    'user' : 'pnirtep',
    'date' : '10.01.2020',
    'tags': [
        'Семейный',
        'Криминал',
        'Комедия'],
    'film_img' : '/static/assets/knifes.jpg',
    'film_title':'Достать ножи',
    'film_text' :'Когда сразу после празднования 85-летия известного автора криминальных романов Харлана Тромби виновника торжества находят мёртвым, за расследование берётся обаятельный и дотошный частный детектив Бенуа Блан. Ему предстоит распутать тугую сеть уловок и корыстной лжи, которой его опутывают члены неблагополучной семьи Харлана и преданный ему персонал.'}

```
Далее данные из словаря подставляются на соответствующие места в html-странице

```html
    <div class="row post-head">
  			<div class="col-sm-6">
  				<img src="{{ film_img }}" alt="">
  			</div>
  			<div class="col-sm-6 post-head-title">
  				<h2>{{ film_title }}</h2>
  				<hr>
	  				<h4>
	  					<p><span><b>Автор публикации: </span></b><span>{{ user }}</span></p>
	  					<p><span><b>Дата публикации: </span></b><span>{{ date }}</span></p>
	  					<p class = "post_film_tags"><span><b>Теги: </span></b>
                            {% for tag in tags %}
                            <span>{{ tag }},</span>
                        {% endfor %}</p>
	  					<br>
	  					<button><a href="https://yandex.ru/search/?text=один%20дома%20смотреть%20онлайн">Искать в Яндексе</a></button>
	  				</h4>
	  				
  			</div>

		</div>
		<div class="row post-body">
			<div class="col-lg-12">
				<p>{{ film_text }}</p>
			</div>
		</div>
```


4. Base.html - использовал для того, чтобы создать расширение в которое внес мета-теги с CSS, CDN, JS, а так же меню и футер сайта
Правда потом уже прочитал, что есть flask-bootstrap, но уже не стал переделывать

Для верстки использовал Bootstrap 4. Ничего сверхестественного с его использованием не сделал. Разве что адаптивность работает, а так же подглядел вариант Burger меню для маленьких экранов и сделал для себя так же.
