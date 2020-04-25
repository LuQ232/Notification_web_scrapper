import list_of_post as list
import keyboard


list = list.List_of_posts()



while True:
    print(list.is_new_post())
    if (keyboard.is_pressed('q')):  ##HIT 'Q' TO BREAK LOOP
        break