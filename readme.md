Пример простого веб сайта, реализованного на html, bootstrap и flask

1. Есть главная страница: index.html
2. Две страницы с фильмами: home-alone.html и knifes-out.html
- home-alone.html обычная страница, которая содержит всю нужную информацию и загружается в виде шаблона
- на странице knifes-out.html сделана попытка изспользования шаблонизатора для вывода ключевой информации о фильме: афиша, название, автор, описание и т.д.

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

3. Страница add_film.html  с формой, которую в дальнейшем хочу свзяать с БД для добавления новых фильмов. Пока пробовал просто передавать данные, конвертировать их в json формат и выводить обратно на страницу. 
Но почему-то это работает криво: вместо текста обратно выводятся данные вида: 
```json
    {
      "email": "sales@azarenokpro.com", 
      "film_img": "", 
      "film_text": "Высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. ", 
      "film_title": "Достать ножи", 
      "tags": "Comedy"
    }
```
И если в форме отметить три тега, то по идее они все три и должны уходить в словарь tags. На requestbin работает, а тут нет.

4. Base.html - использовал для того, чтобы создать расширение в которое внес мета-теги с CSS, CDN, JS, а так же меню и футер сайта
Правда потом уже прочитал, что есть flask-bootstrap, но уже не стал переделывать

Для верстки использовал Bootstrap 4. Ничего сверхестественного с его использованием не сделал. Разве что адаптивность работает, а так же подглядел вариант Burger меню для маленьких экранов и сделал для себя так же.

В дальнейшем хотелось бы понять, как выводить на страницы все фильмы из БД, как фильтровать их по тегам, пользователям - то есть полноценно связать с той БД, которую мы создавали на прошлом уроке по SQLalchemy