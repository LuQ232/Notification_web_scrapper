import scrapper as scrap



for elem in scrap.list_of_last_posts():
    print("_______________________TITLE_________________________")
    print(scrap.title_of_post(elem))
    print("_____________________________________________________")


    print("_______________________DESCRIBTION_________________________")
    print(scrap.describtion_of_post(elem))
    print("_____________________________________________________")


    print("_______________________TIME_OF_EXIST_________________________")
    print(scrap.time_of_post_exist(elem))
    print("_____________________________________________________")


    print("_______________________AUTHOR_________________________")
    print(scrap.author_of_post(elem))
    print("_____________________________________________________")


    print("_______________________VIEWS_________________________")
    print(scrap.number_of_views(elem))
    print("_____________________________________________________")


    print("_______________________ANSWEARS_________________________")
    print(scrap.number_of_answears(elem))
    print("_____________________________________________________")
    print()
    print()
    print()
    print()
    print()
    print()