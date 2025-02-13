# Тестовое техническое задание

Это тестовое техническое задание демонстрирует оптимизированный подход к обработке большого объёма данных (например, миллион строк)

## Описание задачи

- **Разбиение DataFrame на чанки:**  
  Необходимо разбить DataFrame на части (чанки) с учетом минимального (`size_from`) и максимального (`size_to`) размера чанков, при этом не разрывая группы строк с одинаковыми значениями в столбце.
