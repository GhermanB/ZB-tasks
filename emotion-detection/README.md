Веб-сервис emotion-detection
============================

Работаем с библиотеками FastAPI, pydantic, transformers

Используется предобученная модель ruBERT-tiny, донастроенная на датасете CEDR.

https://huggingface.co/cointegrated/rubert-tiny2-cedr-emotion-detection

1. Запускаем сервер.
  Инициализируется модель распознавания, создается классификатор из объекта pipeline.
  Запускается applicationFastAPI.

2. POST-запрос принимает на вход словарь типа {&quot;text&quot;: &quot;текст для анализа&quot;}.

3. При передаче POST-запроса /emotion-detection создается класс Text и переданное нами значение в виде строки передается модели.

4. Обрабатываем текст с помощью нашего классификатора. Так как требуются все классы и вероятности, выставляем return\_all\_scores=True.

5. Возвращаем список словарей типа:

_[_
  _{_
  _&quot;label&quot;: &quot; __joy__&quot;,_
  _&quot;score&quot;: 0.1640404313802719_
  _},_
    …
  _{_
  _&quot;label&quot;: &quot; __anger__&quot;,_
  _&quot;score&quot;: 0.002997312694787979_
  _}_
_]_

6. **Готово! Задача выполнена, и мы счастливы**  **🥳**
