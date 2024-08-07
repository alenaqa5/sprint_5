login_to_account_button = "//button[text()='Войти в аккаунт']"  #кнопка 'Войти в аккаунт' для входа в аккаунт со страницы "Конструктор"
username = "//*[@class='text input__textfield text_type_main-default' and @type='text']"  #поле для ввода имени
email = "//label[text()='Email']/following-sibling::*[@class='text input__textfield text_type_main-default']"  #поле для ввода email
password = "//*[@class='text input__textfield text_type_main-default' and @type='password']"  #поле для ввода пароля
go_to_registration_button = "//*[@class='Auth_link__1fOlj' and @href='/register']"  #кнопка для перехода на форму регистрации
register = "//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']" #кнопка для регистрации на странице регистрации
header_login = "//h2[contains(text(), 'Вход')]" #заголовок "Войти" для проверки редиректа на форму авторизации после регистрации
incorrect_password_error = "//*[@class='input__error text_type_main-default' and contains(text(), 'Некорректный пароль')]" #надпись о некорректном пароле
create_order = "//button[contains(text(),'Оформить заказ')]"  #кнопка для оформления заказа
login_button = "//button[contains(text(),'Войти')]"  #кнопка для входа в аккаунт с формы авторизации
personal_account_button = "//p[text()='Личный Кабинет']" #кнопка "Личный кабинет"
to_login_form = "//a[text()='Войти' and @href='/login']"  #кнопка для перехода на форму авторизации
logout_button = "//button[text()='Выход']"  #кнопка для выхода из профиля
constructor = "//p[text()='Конструктор' and @class='AppHeader_header__linkText__3q_va ml-2']"  #заголовок "конструктор"
collect_burger = "//h1[text()='Соберите бургер' and @class='text text_type_main-large mb-5 mt-10']"  #заголовок "соберите бургер"
logo = "//div[@class='AppHeader_header__logo__2D0X2']"  #логотип сайта
tab_buns = "//*[@class='text text_type_main-default' and contains(text(),'Булки')]"  #таб с булками
bun = "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains(text(),'булка')]"  #заголовок "Булки"
tab_sauces = "//*[@class='text text_type_main-default' and contains(text(),'Соусы')]" #таб с соусами
sauce = "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and starts-with(text(),'Соус')]"  #заголовок "Соусы"
tab_toppings = "//*[@class='text text_type_main-default' and contains(text(),'Начинки')]" #таб с начинками
header_toppings = "//h2[@class='text text_type_main-medium mb-6 mt-10' and contains(text(),'Начинки')]" #начинки