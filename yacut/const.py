import re
from string import ascii_letters, digits

# views
PATTERN_FOR_SHORT = ascii_letters + digits
REGEX_FOR_SHORT = r"^[{}]+$".format(re.escape(PATTERN_FOR_SHORT))
LEN_OF_SHORT = 6
ORIGINAL_LENGTH = 3000
SHORT_LENGTH = 16
REDIRECT_VIEW = 'redirect_view'
UNIQUE_SHORT_MASSAGE = 'Предложенный вариант короткой ссылки уже существует.'

# models
ID_ERROR_MESSAGE = 'Указанный id не найден'
ITERATIONS = 10
WRONG_SHORT = 'Указано недопустимое имя для короткой ссылки'
SHORT_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
TOO_LONG_ORIGINAL = 'Слишком длинная ссылка'

# forms
LONG_LINK = 'Длинная ссылка'
OBLIGATORY_FIELD = 'Обязательное поле'
LINK_IS_NOT_VALID = 'Ссылка не валидна'
YOUR_SHORT_LINK = 'Ваш вариант короткой ссылки'
CREATE = 'Создать'
REGEX_MESSAGE = 'Используйте буквы латинского алфавита и цифры'
