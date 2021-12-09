Веб-сервис similar-texts-recognition
====================================

Работаем с библиотеками FastAPI, pydantic, sentence_transformers, sklearn.metrics.pairwise

Используется предобученная модель RuBERT (Russian, cased, 12-layer, 768-hidden, 12-heads, 180M parameters)

https://huggingface.co/DeepPavlov/rubert-base-cased-sentence

1. Запускаем сервер.
  Инициализируется модель, создается SentenceTransformer.
  Запускается application FastAPI.

2. POST-запрос принимает на вход словарь типа {"text1": "Первый текст", "text2": "Второй текст"}.

3. При передаче POST-запроса /similar-recognition создается класс Text в виде словаря. После чего значения словаря передаются модели в виде списка.

4. Создаем эмбеддинги с помощью нашего трансформера. 

6. Используем cosine_similarity из sklearn.metrics для определения схожести векторов на основе косинусового расстояния.

5. Получаем округленное до 4 знаков значение сходства от 0 до 1.

6. **Потрясающе! Все получилось**  **😊**
