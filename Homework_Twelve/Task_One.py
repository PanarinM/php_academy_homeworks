# С помощью Selenium и любого вебдрайвера получить все топики с страницы http: // toster.ru
# (имя топика, ссылка, кол - во ответов, кол - во подписчиков, дата поста, кол - во просмотров),
# желательно с помощью разных спосособ(искать по классу, айди, атрибутам, xpath и т.д.).
# Подумать каким образом можно будет реализовать хождение по ссылкам(пагинация) и собирать все топики.

import os
from selenium import webdriver


class toster_walker_class_based:
    def __init__(self):
        """
        Инициализация класса
        Настройка переменной среды и запуск драйвера.
        """
        chromedrive = 'D:\chromedriver\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = chromedrive
        self.driver = webdriver.Chrome(chromedrive)
        self.driver.get('https://toster.ru')

    def __enter__(self):
        """
        Реализация работы с with as
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Реализация работы с with as
        закрытие драйвера по окончанию действий с экземпляром класса
        """
        self.driver.close()

    def get_quest_params(self):
        """
        собирает вопросы на toster.ru, а так же его параметры:
        тэг, ссылку, дату публикации, кол-во подписчиков и просмотров

        :return: список кортежей под каждый вопрос в формате (тэг, имя, ссылка, подписчики, дата, просмотры)
        """
        quest_lst = []
        questionboxes = self.driver.find_elements_by_class_name('question__content_fluid')
        for questionbox in questionboxes:
            tag = questionbox.find_element_by_class_name('tags-list__item').text.lower()
            name = questionbox.find_element_by_class_name('question__title-link_list').text
            href = questionbox.find_element_by_class_name('question__title-link_list').get_attribute('href')
            pubdate = questionbox.find_element_by_class_name('question__date_publish').get_attribute('title')
            subs = questionbox.find_elements_by_class_name('question__views-count')[0].text
            views = questionbox.find_elements_by_class_name('question__views-count')[1].text
            quest_lst.append((tag, name, href, subs, pubdate, views))
        return quest_lst

    def walk_pages(self, amount):
        """
        перелистывает кол-во страниц amount и вызывает get_quest_params для получения вопросов с нее
        :param amount: количество страниц
        :return: формирует словарь,
                 где ключ это номер страницы, а значение это список кортежей(структура get_quest_params)
        """
        assert isinstance(amount, int), 'incorrect input type'
        pages_dict = {}
        for page in range(1, amount+1):
            page_lst = self.get_quest_params()
            pages_dict[page] = page_lst
            if 'Следующие ' in self.driver.find_elements_by_class_name('paginator__item-link')[-1].text:
                self.driver.find_elements_by_class_name('paginator__item-link')[-1].click()
            else:
                break
        return pages_dict

    def walk_range(self, page_range):
        """
        перелистывает страницы из page_range и вызывает get_quest_params для получения вопросов с нее
        :param page_range: список страниц
        :return: формирует словарь,
                 где ключ это номер страницы, а значение это список кортежей(структура get_quest_params)
        """
        assert isinstance(page_range, list) or isinstance(page_range, range), 'incorrect input type: '+str(type(page_range))
        pages_dict = {}
        for page in page_range:
            url = 'https://toster.ru/questions/interesting?page={}'.format(page)
            self.driver.get(url)
            page_lst = self.get_quest_params()
            if len(page_lst) == 0:
                continue
            pages_dict[page] = page_lst
        return pages_dict

if __name__ == '__main__':
    with toster_walker_class_based() as a:
        # questions = a.get_quest_params()
        # for question in questions:
        #     output = "tag: {}, name: {}, link: {}, subscribers: {}, publication date: {}, views: {}".format(
        #         question[0], question[1], question[2], question[3], question[4], question[5])
        #     print(output)
        pages = a.walk_range(range(1, 3))
        for page, lst in pages.items():
            print(page, lst)

