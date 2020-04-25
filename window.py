import list_of_post as list
import keyboard


list = list.List_of_posts()
list.print_all_data()


while True:
    if(list.is_new_post()):
        print("THERE IS NEW POST!")
    elif (list.is_changes_in_list()):
        print("YOU SHOULD UPDATE!")
        list.update_list()
        list.print_all_data()
    elif (keyboard.is_pressed('q')):  ##HIT 'Q' TO BREAK LOOP
        break