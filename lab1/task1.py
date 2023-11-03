def replace_missing_element(nums):
    # Находим сумму всех элементов списка
    total_sum = sum(num for num in nums if num is not None)

    # Находим количество элементов списка
    total_count = len(nums)

    # Находим среднее арифметическое всех элементов
    average = total_sum / total_count

    # Ищем пропущенный элемент
    missing_element = average * (total_count + 1) - total_sum

    # Заменяем пропущенный элемент средним арифметическим
    nums[nums.index(None)] = missing_element

    return nums



numbers = [1, 2, 3, None, 5, 6]
updated_numbers = replace_missing_element(numbers)
print(updated_numbers)