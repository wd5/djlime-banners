djlime-banners
==============

djlime-banners — это простое django-приложение, которое,
предоставляет интерфейс для добавления и отображения баннеров
на сайте и реализует механизм учета переходов(кликов).

Установка
---------

Из pypi::

    $ pip install djlime-banners

или::

    $ easy_install djlime-banners

или склонировать репозитарий с github::

    $ git clone git://github.com/whitespy/djlime-banners.git

и выполнить следующие действия::

    $ cd djlime-banners
    $ sudo python setup.py install

Настройка
---------

- Добавьте приложение banners в кортеж INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'banners',
    )

- Выполните команду python manage.py migrate banners

- Также необходимо добавить следующую строчку в корневой URLconf::

    url('go$', include('banners.urls')),

Опции
-----

**BANNER_CITY_MODEL** - Модель города в формате:
*имя_приложения.название модели*.
Значение по умолчанию: ``location.City``.

**CITY_CONTEXT_KEY** - Ключ контекста, хранящий текущий объект города.
Значение по умолчанию: ``city``.

**BANNER_IMAGES_DIR** - Директория относительно MEDIA_ROOT, где будут хранится
изображения баннеров.
Значение по умолчанию: ``banners/images``.

**BANNER_THUMBNAIL_SIZE** - Размер миниатюры изображения баннера,
отображаемой в интерфейсе администратора. Значением должен быть кортеж с двумя
положительными, целочисленными элементами, хранящих значения ширины и высоты.
Значение по умолчанию: ``(60, 60)``.

**BANNER_THUMBNAIL_FORMAT** - Формат файла миниатюры изображения баннера.
Значение по умолчанию: ``PNG``.

**BANNER_HEADER_TEMPLATE** - Шаблон используемый при выводе баннера
шаблонным тегом включения *include_header_banner*.
Значение по умолчанию: ``banners/includes/single_banner.html``.

**BANNER_CONTENT_TEMPLATE** - Шаблон используемый при выводе баннера
шаблонным тегом включения *include_content_banner*.
Значение по умолчанию: ``banners/includes/single_banner.html``.

**BANNER_SIDEBAR_TEMPLATE** - Шаблон используемый при выводе баннеров
шаблонным тегом включения *include_sidebar_banners*.
Значение по умолчанию: ``banners/includes/banners_block.html``.

**BANNER_COUNT_PER_SIDEBAR** - Задает количество банеров выводимых
тегом *include_sidebar_banners*. Может быть числом или логическим
значением. Если значением является ``False``, то ограничение на
количество выводимых баннеров будет снято. Иначе значение должно
быть числом, задающим количество выводимых банеров в блоке.
Значение по умолчанию: ``False``.

Шаблонные теги
--------------

- Загрузите библиотеку тегов **{% load banners_tags %}**

*include_header_banner* - тег включения, используемый для вывода баннеров
в заголовке. Тег *include_header_banner* по умолчанию использует шаблон
``banners/includes/single_banner.html``::

    {% if banner %}
        <a href="{{ banner.get_absolute_url }}" target="_blank">
            <img src="{{ banner.image.url }}" />
        </a>
    {% endif %}

В случае необходимости вы можете переопределить этот шаблон.

*include_content_banner* - тег включения, используемый для вывода баннеров
в главной колонке сайта. Тег *include_content_banner* по умолчанию использует
шаблон ``banners/includes/single_banner.html``, В случае необходимости вы
можете переопределить этот шаблон.

*include_sidebar_banners* - тег включения, используемый для вывода баннеров
в боковой панели сайта. Тег *include_sidebar_banners* по умолчанию использует
``banners/includes/banners_block.html``::

    {% if banners.exists %}
        <div id="banners_block">
            {% for banner in banners %}
                <div class="banner">
                    <a href="{{ banner.get_absolute_url }}" target="_blank">
                        <img src="{{ banner.image.url }}" />
                    </a>
                </div>
            {% endfor %}
        </div>
    {% endif %}

В случае необходимости вы можете переопределить этот шаблон.
