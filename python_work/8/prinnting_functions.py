# coding: utf-8
# prinnting_functions.py

def print_models(unprinted_designs, completed_models):
	""" 打印模型的过程 """
        while unprinted_designs:
            current_models = unprinted_designs.pop()

            print("Printing model:" + current_models)
            completed_models.append(current_models)


def show_completeds(completed_models):
	""" 显示打印设计完的模型 """
        print('\nThe following models have been printed')
        for completed_model in completed_models:
            print completed_model

