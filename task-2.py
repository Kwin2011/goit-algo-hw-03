import turtle

def draw_koch_segment(turtle_obj, level, length):
    """Рекурсивно малюємо сегмент кривої Коха"""
    if level == 0:
        turtle_obj.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(turtle_obj, level - 1, length)
        turtle_obj.left(60)
        draw_koch_segment(turtle_obj, level - 1, length)
        turtle_obj.right(120)
        draw_koch_segment(turtle_obj, level - 1, length)
        turtle_obj.left(60)
        draw_koch_segment(turtle_obj, level - 1, length)

def draw_koch_snowflake(turtle_obj, level, length):
    """Малюємо сніжинку Коха"""
    for _ in range(3):
        draw_koch_segment(turtle_obj, level, length)
        turtle_obj.right(120)

def main():
    # Вводимо рівень рекурсії
    try:
        recursion_level = int(input("Введіть рівень рекурсії (ціле число): "))
        flake_size = 300  # Розмір сніжинки
    except ValueError:
        print("Помилка: введіть ціле число для рівня рекурсії.")
        return

    # Налаштовуємо екран
    window = turtle.Screen()
    window.bgcolor("white")

    # Налаштовуємо черепаху
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)  # Максимальна швидкість

    # Початкове положення для красивого зображення
    snowflake_turtle.penup()
    snowflake_turtle.goto(-flake_size / 2, flake_size / 3)
    snowflake_turtle.pendown()

    # Малюємо сніжинку Коха
    draw_koch_snowflake(snowflake_turtle, recursion_level, flake_size)

    # Завершуємо роботу з turtle
    turtle.done()




if __name__ == "__main__":
    main()